import os
import numpy
import pickle

from core import config
from core import logging

# Neural Network Imports
from keras import models
from keras import layers
from keras.models import load_model
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Decision Tree Imports
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report, confusion_matrix

# Turn Tensor Flow logging down to FATAL
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Create global variables to hold models
decision_tree = None
neural_network = None

# Gets called at start up
def load_models():
    global decision_tree

    global neural_network

    decision_tree = DecisionTree(model_file=config.trained_models['decisiontree'], data_file=config.data_files['decisiontree'])

    decision_tree.load()

    logging.success('DecisionTree loaded')

    neural_network = NeuralNetwork(model_file=config.trained_models['neuralnetwork'], data_file=config.data_files['neuralnetwork'])

    neural_network.load()

    logging.success('Neural Network loaded')

class DecisionTree(object): 
    def __init__(self, training_mode=False, data_file=None,  model_file=None):
        self.training_mode = training_mode
        self.data_file = data_file
        self.model_file = model_file
        self.classifier = DecisionTreeClassifier() # https://stackabuse.com/decision-trees-in-python-with-scikit-learn/

        if self.training_mode == True:
            dataset = numpy.loadtxt(self.data_file, delimiter=",", dtype='float64')
            data = dataset[:,0:3]
            labels = dataset[:,3]
            self.train(data, labels)

    def train(self, data, labels):
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.20)
        self.classifier.fit(X_train, y_train)

        y_pred = self.classifier.predict(X_test)  
        
        print('----Decision Tree Classification----\n')
        print(confusion_matrix(y_test, y_pred))  
        print(classification_report(y_test, y_pred))

        self.save(self.model_file)
        
    def predict(self, features):
        predicton = self.classifier.predict(features)
        return predicton

    def save(self):
        with open(self.model_file, 'wb') as f:
            pickle.dump(self.classifier, f)

    def load(self):
        with open(self.model_file, 'rb') as f:
            self.classifier = pickle.load(f)

    def visualize(self, filename):
        dot_data = export_graphviz(self.classifier, filled=True, rounded=True, special_characters=True, class_names=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_png(filename)


class NeuralNetwork:
    def __init__(self, training_mode=False, data_file=None, model_file=None, epochs=300, batch=250):
        self.epochs = epochs
        self.batch = batch
        self.training_mode = training_mode
        self.model_file = model_file
        self.data_file = data_file
        self.model = models.Sequential()
        self.model.add(layers.Dense(3, input_dim=3)) # Had good results with sigmoid as well
        self.model.add(layers.Dense(3, activation="relu"))
        self.model.add(layers.Dense(3, activation="relu"))
        self.model.add(layers.Dense(1, activation="relu"))
        self.model.compile(loss="binary_crossentropy", optimizer="adam",  metrics=['acc'])

        if self.training_mode == True:
            dataset = numpy.loadtxt(data_file, delimiter=",", dtype='float64')
            data = dataset[:,0:3]
            labels = dataset[:,3]
            self.train(data, labels)

    def train(self, data, labels):

        features = data.astype(numpy.float64)

        labels = labels.astype(numpy.float64).reshape((-1,1))
        
        # Scale the data min max
        min_max = MinMaxScaler(feature_range=(0, 1))

        min_max_data = min_max.fit_transform(features)

        # Scale the data scalar
        #scalar = StandardScaler()
        #scalar.fit(features)
        #std_scalar_data = scalar.transform(features)

        # Train the network
        self.model.fit(min_max_data, labels, epochs=self.epochs, batch_size=self.batch, verbose=False)

        # Get accuracy
        scores = self.model.evaluate(min_max_data, labels)

        print("\n%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100))

        self.save(self.model_file)

    def save(self):
        self.model.save(self.model_file)

    def load(self):
        self.model = models.load_model(self.model_file)

    def predict(self, features):
        # Scale features
        scalar = StandardScaler()

        scalar.fit(features)

        predict_scalar = scalar.transform(features)

        min_max = MinMaxScaler(feature_range=(0, 1))

        min_max_data = min_max.fit_transform(features)

        # Predict
        predict_min_max = min_max.transform(features)

        prediction_prob = self.model.predict(predict_scalar)
        
        prediction_class = self.model.predict_classes(predict_scalar)

        return prediction_prob
