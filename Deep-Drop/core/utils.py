import base64
import re
from uuid import uuid4
from datetime import date
from collections import namedtuple

from core import logging
import numpy as np
import pickle

from tensorflow.keras.models import load_model
# from sklearn.preprocessing import MinMaxScaler

# Decision Tree Imports
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load

class Models(object):
    def __init__(self):
        self.nn_clf = None
        self.dt_clf = None
        self.minmax_scaler = None

    def DecisionTreeClassifier(self, model_file):
        self.dt_clf = pickle.load(open(model_file, 'rb'))

    def NeuralNetworkClassifier(self, model_file, scaler_file):
        self.nn_clf = load_model(model_file)
        self.minmax_scaler = load(scaler_file)

    def predict(self, ProcessList):
        scaled_features = self.minmax_scaler.transform(ProcessList.features['raw'])
        ProcessList.features['min_max_scaled'].append(scaled_features)
        
        #ProcessList.predictions['neural_network'] = self.nn_clf.predict_classes(ProcessList.features['min_max_scaled'])[0][0]
        ProcessList.predictions['decision_tree'] = self.dt_clf.predict(ProcessList.features['raw'])[0]

class ProcessList(object):
    def __init__(self, features):
        self.uid = uuid4()
        self.date = date.today()
        self.parsed_data = []
        self.features = {'raw': [features], 'min_max_scaled': []}
        self.predictions = {}