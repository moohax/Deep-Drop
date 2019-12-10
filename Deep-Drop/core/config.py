import os

# domain
domain = 'localhost'

# root dir
basedir = os.path.dirname(os.path.abspath(__file__))

# payloads
payload_files = {
    'vba': os.path.join(basedir, 'payloads', 'template.vba')
}

# trained models
trained_models = {
    'decisiontree': os.path.join(basedir, 'models', 'decisiontree.pkl'),
    'neuralnetwork': os.path.join(basedir, 'models', 'neuralnetwork'),
    'nn_scaler': os.path.join(basedir, 'models', 'minmax_scaler.bin')
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