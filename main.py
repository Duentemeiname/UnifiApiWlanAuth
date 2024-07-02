from flask import Flask, request, jsonify
from unifiapi import *
from keycloakapi import *
import os
from dotenv import load_dotenv
from pyunifi.controller import Controller

load_dotenv()

app = Flask(__name__)

UNIFI_API_ENDPOINT = os.getenv('UNIFI_API_ENDPOINT')
UNIFI_API_USERNAME = os.getenv('UNIFI_API_USERNAME')
UNIFI_API_PASSWORD = os.getenv('UNIFI_API_PASSWORD')
UNFIF_API_SITE = os.getenv('UNFIF_API_SITE')

UnifiEndpoint = Controller(UNIFI_API_ENDPOINT, UNIFI_API_USERNAME, UNIFI_API_PASSWORD, 8443, "UDMP-unifiOS", "default", True)

@app.route('/')
def get_default():
    return jsonify({'message': 'This is the default route', 'status': 'success'}), 200

# Beispiel für einen GET-Endpunkt
@app.route('/api/wlansso', methods=['GET'])
def wlanlogin():
    mac_address = request.args.get('mac')
    minutes = request.args.get('minutes')
    response = userlogin(UnifiEndpoint, mac_address, minutes)

    if response:
        return jsonify({'message': 'User successfully logged in', 'status': 'success', 'unificode': 'reponse'}), 200
    else:
        return jsonify({'message': 'User login failed', 'status': 'failure', 'unificode': 'reponse'}), 400






# Beispiel für einen POST-Endpunkt
# @app.route('/api/post', methods=['POST'])
# def post_example():
#     if request.is_json:
#         req_data = request.get_json()
#         response_data = {
#             'message': 'This is a POST request',
#             'received': req_data,
#             'status': 'success'
#         }
#         return jsonify(response_data), 200
#     else:
#         return jsonify({'message': 'Request must be JSON', 'status': 'failure'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)