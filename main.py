from fetch_restapi_json import fetch_restapi_json
from fetch_restapi_csv import fetch_restapi_csv
from fetch_restapi_schema import fetch_restapi_schema
from fetch_graphql_json import fetch_graphql_json
from post_data_file import post_file

prod_url = 'https://t-and-s-dp-poc.azurewebsites.net/'
dev_url = 'http://127.0.0.1/'
url = dev_url



#Fetch continent & country data from our GraphQL API for a specific country
#print("Fetching continents & countries data from the GraphQL output data port where CountryName = 'Martinique'")
#json_data = fetch_graphql_json(url, {"ContinentCode":"AF", "CountryName": "Martinique"})
#print(json_data)

#Lets try and login as R2D2 and fetch REST API in JSON format
username = "R2D2"
password = "tiger"
print("Fetching continents & countries data from the REST API output data port with an authenticated but unauthorised user")
response = fetch_restapi_json(url,username,password)
print(response)

#Lets try and login as Mary with wrong password and fetch REST API in JSON format
username = "Mary"
password = "tier"
print("\nFetching continents & countries data from the REST API output data port with an unauthenticated user")
response = fetch_restapi_json(url,username,password)
print(response)

#Fetch all continents & countries data from our REST API in JSON format
username = "Mary"
password = "tiger"
print("\nFetching continents & countries data from the REST API output data port with an authenticated and authorised user")
json_data = fetch_restapi_json(url,username,password)
print(json_data)

#Fetch all continents & countries data from our REST API in CSV format into a dataframe
print("\nFetching continents & countries data from the REST API output data port")
df = fetch_restapi_csv(url,username,password)
print(df)

#Fetch the data dictionary for the continents and countries dataset
print("\nFetching continents & countries data dictionary from the REST API output data port")
json_data = fetch_restapi_schema(url)
print(json_data)

#Test pushing schema file to REST API input data port
print("\nPushing a data dictionary/schema file to the input data port")
response = post_file(url+'uploadschema', 'schema.csv')
print(response)

#Fetch the revised data dictionary for the continents and countries dataset
print("\nFetching continents & countries data dictionary from the REST API output data port")
json_data = fetch_restapi_schema(url)
print(json_data)

#Test pushing countries and continents files to REST API input data port
print("\nPushing source countries and continents CSV files to the input data port")
response = post_file(url+'uploadsrcfile', 'countries.csv')
print(response)
response = post_file(url+'uploadsrcfile', 'continents.csv')
print(response)

#Test executing a pipeline to create target dataset from source dataset
print("\nExecute the pipeline which will transform source data into an abstraction layer and push to target dataset")
response = post_file(url+'executepipeline', 'pipeline.sql')
print(response)
