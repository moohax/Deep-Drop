import pickle
import numpy
from core import config

# Neural Network Imports
# from tensorflow.keras import models
# from tensorflow.keras import layers
from tensorflow.keras.models import load_model
# from sklearn.preprocessing import MinMaxScaler

# Decision Tree Imports
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load

# Create global variables to hold models
decision_tree_clf = None
neural_network_clf = None

# Gets called at start up
def load_models():
    global decision_tree_clf
    global neural_network_clf

    decision_tree_clf = DecisionTree(config.trained_models['decisiontree'])
    neural_network_clf = NeuralNetwork(config.trained_models['neuralnetwork'], config.trained_models['nn_scaler'])

class DecisionTree(object): 
    def __init__(self, model_file=None):
        self.model_file = model_file
        self.clf = pickle.load(open(self.model_file, 'rb'))
        self.prediction = None

    def predict(self, features):
        return self.clf.predict(features)

class NeuralNetwork(object):
    def __init__(self, model_file=None, scaler_file=None):
        self.model_file = model_file
        self.clf = load_model(self.model_file)
        self.scaler = load(scaler_file)
        
    def predict(self, features, verbose=True):
        # test = numpy.array([[131, 65.5, 2]])
        # test1 = numpy.array([[36, 18.0, 2]])

        features = features.astype(numpy.float64) 
        min_max_data = self.scaler.transform(features)

        if verbose:
            print(f'Predicted Class: {self.clf.predict_classes(min_max_data)[0][0]}')
            print(f'Class Probability: {self.clf.predict(min_max_data)[0][0]}')