from fetch_restapi_json import fetch_restapi_json
from fetch_graphql_json import fetch_graphql_json
from post_data_file import post_file

prod_url = 'http://tands-dp-poc.azurewebsites.net/'
dev_url = 'http://127.0.0.1/'
url = dev_url

#Fetch all continents & countries data from our REST API
json_data = fetch_restapi_json(url)
print(json_data)

#Fetch continent & country data from our GraphQL API for a specific country
json_data = fetch_graphql_json(url, {"ContinentCode":"AF", "CountryName": "Martinique"})
print(json_data)

#Test pushing countries and continents files to REST API
response = post_file(url+'uploadsrcfile', 'countries.csv')
print(response)
response = post_file(url+'uploadsrcfile', 'continents.csv')
print(response)