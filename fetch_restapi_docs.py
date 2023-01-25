#Retrieve the continents & countries data from the REST API
import requests, json

def fetch_restapi_docs(url):
    try:
        response = requests.get(url+'openapi.json')
        response.raise_for_status()
        if response and response.status_code == 200:
            html_data = response.text
            return html_data
    except requests.exceptions.HTTPError as e:
        response_text = json.loads(e.response.text)
        return {'Error':str(response.status_code)+' '+response.reason+' - '+response_text['detail']}
