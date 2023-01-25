import requests
from authentication import basic_auth
def post_file(url, filename, username, password ):
    headers = {'Authorization': basic_auth(username, password)}
    file = {'file': open(filename, 'rb')}
    resp = requests.post(url=url, files=file, headers=headers)
    return (resp.json())

