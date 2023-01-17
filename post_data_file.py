import requests

def post_file(url, filename):
    file = {'file': open(filename, 'rb')}
    resp = requests.post(url=url, files=file)
    return (resp.json())

