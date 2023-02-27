from ksql import KSQLAPI
import json
with open("ksql.json", "r") as file:
    credentials = json.load(file)
print(credentials)
client = KSQLAPI(credentials['CCLOUD_KSQL_ENDPOINT'], api_key=credentials['CCLOUD_KSQL_API_KEY'], secret=credentials['CCLOUD_KSQL_API_SECRET'], verify=False)