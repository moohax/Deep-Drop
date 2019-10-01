import argparse

from flask import Flask
from core import config
from core import routing
from core import logging
from core import ddmodels
from core import payloads

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Intelligent Droppers")

    args = parser.parse_args(sys.argv[1:])

    logging.print('''                   
 ____              ____              
|    \ ___ ___ ___|    \ ___ ___ ___ 
|  |  | -_| -_| . |  |  |  _| . | . |
|____/|___|___|  _|____/|_| |___|  _|
              |_|               |_|  
    ''')

    app = Flask(__name__, template_folder="core/templates", static_folder="core/static")
    
    try: 
        ddmodels.load_models()

        routing.setup_routes(app)

        logging.success('Routes loaded')

        payloads.patch_payloads(config.payload_files, config.domain)

        logging.success(f'Payloads patched. Callback info {config.domain}')

    except Exception as e:
        logging.error(str(e))

    logging.success("Starting HTTP Server")

    app.run('0.0.0.0', 80, threaded=False, use_reloader=False) # No threading because https://github.com/keras-team/keras/issues/2397
