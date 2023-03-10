#Retrieve the continents & countries data from the REST API
import requests, pandas as pd, json
from io import StringIO
from authentication import basic_auth

def fetch_restapi_csv(url, username, password):
    headers = {'Authorization': basic_auth(username, password)}
    try:
        response = requests.get(url, headers=headers, params={'format':'csv'})
        response.raise_for_status()
        if response and response.status_code == 200:
            df = pd.read_csv(StringIO(response.text))
            return df
    except requests.exceptions.HTTPError as e:
        response_text = json.loads(e.response.text)
        return {'Error':str(response.status_code)+' '+response.reason+' - '+response_text['detail']}
