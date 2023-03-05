from authentication import basic_auth
import requests, json

def execute_pipeline(url, username, password):
    headers = {'Authorization': basic_auth(username, password)}
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        if response and response.status_code == 200:
            return {'Details':'pipeline.sql has been successfully executed'}
    except requests.exceptions.HTTPError as e:
        response_text = json.loads(e.response.text)
        return {'Error':str(response.status_code)+' '+response.reason+' - '+response_text['detail']}
