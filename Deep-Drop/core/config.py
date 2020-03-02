import os

# domain
domain = 'localhost'

# root dir
basedir = os.path.dirname(os.path.abspath(__file__))

# trained models
trained_models = {
    'decisiontree': os.path.join(basedir, 'models', 'decisiontree.pkl'),
    'neuralnetwork': os.path.join(basedir, 'models', 'neuralnetwork'),
    'nn_scaler': os.path.join(basedir, 'models', 'minmax_scaler.bin')
}