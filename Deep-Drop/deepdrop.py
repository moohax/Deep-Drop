import os
import uuid
import argparse

from flask import Flask
from core import config
from core import routing
from core import logging
from core import deepdrop


def main(args):
    logging.print('''                   
 ____              ____              
|    \ ___ ___ ___|    \ ___ ___ ___ 
|  |  | -_| -_| . |  |  |  _| . | . |
|____/|___|___|  _|____/|_| |___|  _|
              |_|               |_|  
    ''')

    app = Flask(__name__)
    
    try: 
        # Load the models
        deepdrop.load_models(config)
        logging.success('All models loaded')

        # Setup our routes
        routing.setup_routes(app)

    except Exception as e:
        logging.error(str(e))

    app.run('0.0.0.0', 80, threaded=False, use_reloader=False) # No threading because https://github.com/keras-team/keras/issues/2397
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Math enabled dropper for fun and safety')
    parser.add_argument('-d', '--debug', default=False, required=False, action='store_true', help='Will return the entire process list object for examination')
    args = parser.parse_args()
    main(args)