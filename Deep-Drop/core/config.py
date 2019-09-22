import os

# domain
domain = 'server.com'

# root dir
basedir = os.path.dirname(os.path.abspath(__file__))

# payloads
payload_files = {
    'vba': os.path.join(basedir, 'macros', 'template.vba'),
    'vbs': os.path.join(basedir, 'macros', 'template.vbs')
}

# data
data_files = {
    'decisiontree': os.path.join(basedir, 'data', 'data_process_count.csv'),
    'neuralnetwork': os.path.join(basedir, 'data', 'data_process_count.csv')
}

# trained mtodels
trained_models = {
    'decisiontree': os.path.join(basedir, 'models', 'DecisionTree.pkl'),
    'neuralnetwork': os.path.join(basedir, 'models', 'NeuralNetwork.h5')
}