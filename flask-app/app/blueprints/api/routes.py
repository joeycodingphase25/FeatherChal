import requests
from . import api
response = requests.get("https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers")



@api.route('/test')
def index():
    return str(response.status_code)
