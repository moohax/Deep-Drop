import re
import base64
from collections import namedtuple
import numpy

from core import config
from core import logging
from core import ddmodels

def process_callback(callback):
    # Parse the process list
    parsed_process_list = parse_process_list(callback)

    # Extract features
    collected_features = gather_features(parsed_process_list)

    # Make a prediction
    decision_tree_prediction, neural_network_prediction = make_prediction(collected_features)

    # Make the drop decision
    if decision_tree_prediction < 1 or neural_network_prediction < 0.50:
        logging.success(f'Dropping payload.\nDecision Tree: {decision_tree_prediction}\n Neural Network: {neural_network_prediction}\n')

        return 'Payload'

    else:
        logging.warn(f'Not dropping payload.\nDecision Tree: {decision_tree_prediction}\n Neural Network: {neural_network_prediction}\n')
        
        return 'Safety first'

def parse_process_list(process_list):
    parsed = {}

    processes = namedtuple('process', 'pid, owner, name')

    try:
        task_result = base64.b64decode(process_list).decode().split('\r\n')

        hostname = task_result[0].split('=')[1]

    except Exception as e:
        print(e)

        pass

    if task_result[1] == '':
        logging.error('Process list is empty')

        return 'Hello'
        
    for process in task_result[1:]:
        full_result = re.findall(r'^([0-9]+)\s+(\S+)\s+(.+)$', process)

        if full_result:
            (pid, owner, name) = full_result[0]
            
            if hostname not in parsed.keys():
                parsed[hostname] = []
            
            parsed[hostname].append(processes(int(pid), owner, name))
            continue

        else:
            #logging.error(f'No process to parse\n')
            continue

    return parsed

def gather_features(parsed_process_list):
    features = []

    for host in parsed_process_list:

        users = []

        process_count = len(parsed_process_list[host])

        user_count = len([users.append(process.owner) for process in parsed_process_list[host][0:] if process.owner not in users])

        process_user_ratio = process_count/user_count

        features.append([process_count, user_count, process_user_ratio])

    return features

        # More Features
        # highest_pid = max(process_list, key=lambda k: k.pid).pid
        # average_pid = highest_pid/process_count

def make_prediction(features):

    decision_tree_prediction = ddmodels.decision_tree.predict(numpy.asarray(features))[0]

    neural_network_prediction = ddmodels.neural_network.predict(features)[0]

    return decision_tree_prediction, neural_network_prediction

def patch_payloads(payload_files, domain):
    server = '**server**'
    
    for pfile in payload_files:
        new_payload = open(payload_files[pfile], 'r').read().replace(server, config.domain)

        new_payload_file = f'{config.basedir}\\macros\\{config.domain}.{pfile}'
        
        with open(new_payload_file, 'w') as f:
            f.write(new_payload)