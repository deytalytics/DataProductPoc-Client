#Retrieve the continents & countries data from the REST API
import requests

def fetch_restapi_json():
    response = requests.get('https://dp-poc.azurewebsites.net/REST/0.1/countries')
    json_data = response.json() if response and response.status_code == 200 else {"Error": "REST API did not return any data"}
    return json_data