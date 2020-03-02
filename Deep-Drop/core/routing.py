from flask import request, jsonify
from core import logging
from core import utils
from core import deepdrop

def setup_routes(app):

    @app.route('/api/v1/predict', methods=['GET'])
    def predict():

        process_count = request.args.get('process_count', type=float)
        user_count = request.args.get('user_count', type=float)
        process_user_ratio = request.args.get('process_user_ratio', type=float)

        predictions = deepdrop.predict([process_count, user_count, process_user_ratio])
          
        return str(predictions)
