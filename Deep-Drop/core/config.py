import os

# domain
domain = 'localhost'

# root dir
basedir = os.path.dirname(os.path.abspath(__file__))

# payloads
payload_files = {
    'vba': os.path.join(basedir, 'payloads', 'template.vba')
}

# data
data_files = {
    'decisiontree': os.path.join(basedir, 'data','data_process_count.csv'),
    'neuralnetwork': os.path.join(basedir, 'data', 'data_process_count.csv')
}

# trained models
trained_models = {
    'decisiontree': os.path.join(basedir, 'models', 'DecisionTree.pkl'),
    'neuralnetwork': os.path.join(basedir, 'models', 'NeuralNetwork.h5')
}

# stagers
stagers = {
    'shellcode_stager': os.path.join(basedir, 'stagers', 'Invoke-Shellcode.ps1')
}

# dlls
dlls = {
    'test_x64': os.path.join(basedir, 'bin', 'test_x64.dll'),
    'test_x86': os.path.join(basedir, 'bin', 'test_x86.dll')
}