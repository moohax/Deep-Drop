import os
import uuid
import argparse

from flask import Flask
from core import config
from core import routing
from core import logging
from core import ddmodels
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
        ddmodels.load_models()
        logging.warn('All models loaded')

        # Patch our payloads - will be moved.
        deepdrop.patch_payloads(config.payload_files, config.domain)
        logging.warn(f'Payloads patched for {config.domain}')

        if args.debug:
            captains_key = str(uuid.uuid4())
            app.config['CAPTAINS_KEY'] = captains_key
            app.debug = True

            logging.debug(captains_key)

        # Setup our routes
        routing.setup_routes(app)

    except Exception as e:
        logging.error(str(e))

    app.run('0.0.0.0', 80, threaded=False, use_reloader=False) # No threading because https://github.com/keras-team/keras/issues/2397
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Math enabled dropper for fun and safety')
    parser.add_argument('-d', '--debug', default=False, required=False, action='store_true', help='for testing payloads with master key')
    args = parser.parse_args()
    main(args)