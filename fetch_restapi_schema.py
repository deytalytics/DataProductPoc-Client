#Retrieve the continents & countries data from the REST API
import requests, json

def fetch_restapi_schema(url):
    try:
        response = requests.get(url+'REST/0.1/dictionary/continents_and_countries')
        response.raise_for_status()
        if response and response.status_code == 200:
            json_data = response.json()
            return json_data
    except requests.exceptions.HTTPError as e:
        response_text = json.loads(e.response.text)
        return {'Error':str(response.status_code)+' '+response.reason+' - '+response_text['detail']}
