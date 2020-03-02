import re
import base64
import numpy
import uuid
from collections import namedtuple

from core import config
from core import logging
from core import utils

Models = None

def load_models(config):
    global Models
    Models = utils.Models()
    Models.NeuralNetworkClassifier(config.trained_models['neuralnetwork'], config.trained_models['nn_scaler'])
    Models.DecisionTreeClassifier(config.trained_models['decisiontree'])

def predict(features):
    if len(features) < 3:
        return 'Not enough features'
    
    ProcessList = utils.ProcessList(features)
    Models.predict(ProcessList)

    return ProcessList.predictions