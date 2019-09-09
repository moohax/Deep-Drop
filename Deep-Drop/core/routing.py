from flask import request
from core.deepdrop import process_callback

def setup_routes(app):
    @app.route('/', methods=['GET'])
    def index():

        return 'Index'

    @app.route('/order', methods=['GET', 'POST'])
    def order():
        # Parse the full process list
        if request.method == 'POST':

            process_list = request.form['product']
            
            return(process_callback(process_list))

        # Inputs were collected client side via get
        if request.method == 'GET':
            
            return 'Hello'
