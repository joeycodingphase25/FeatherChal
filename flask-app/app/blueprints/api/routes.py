from . import api
import requests
import json
from flask import jsonify, request
from app.blueprints.api.models import Supervisors
from app.blueprints.user.models import User

# THIS IS THE REQUIRED RESPONSE OBJECT
@api.route('/supervisors', methods=['GET'])
def index():
    response = requests.get("https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers")
    # get response turned into a readable json
    response = response.json()
    # create the Supervisor*s* object with list response
    supervisors = Supervisors(response)
    # sort the supervisor self.list
    supervisors.sorter()
    # grab the list of *Superisor* objects
    super_list = supervisors.listing
    return jsonify([x.to_dict() for x in super_list])

# Make a Submit Route that will interact With React Front End VIA request package
@api.route('/submit', methods=['GET', 'POST'])
def submit():
    ##### Create the recieve request from REACT forms ########
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400
    # Get data from request body
    data = request.json
    # Check to make sure all required fields are present
    for field in ['firstName', 'lastName', 'Supervisor']: # per requirements
        if field not in data:
            # if not return a 400 response with error
            return jsonify({'error': f'{field} must be in request body'}), 400
    # Get fields from data dict
    firstName = data['firstName']
    lastName = data['lastName']
    Supervisor = data['Supervisor']
    email = False
    phoneNumber = False
    # non-required values, boolean checker to avoid error
    if data['email'] in data:
        email = data['email']
    if data['phoneNumber'] in data:
        phoneNumber = data['phoneNumber']    
    user = User(firstName=firstName, lastName=lastName, Supervisor=Supervisor, email=email, phoneNumber=phoneNumber)
    ########## Query the Actual API ############
    url = "https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/submit"

    # use to_dict() to return a DYNAMIC json object
    payload = json.dumps(user.to_dict())
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    ##############################################
    return jsonify(response.json())


