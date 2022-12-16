from fetch_restapi_json import fetch_restapi_json
from fetch_graphql_json import fetch_graphql_json

#Fetch all continents & countries data from our REST API
json_data = fetch_restapi_json()
print(json_data)

#Fetch continent & country data from our GraphQL API for a specific country
json_data = fetch_graphql_json({"CountryName": "Martinique"})
print(json_data)