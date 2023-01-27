from fetch_restapi_json import fetch_restapi_json
from fetch_restapi_csv import fetch_restapi_csv
from fetch_restapi_schema import fetch_restapi_schema
from fetch_restapi_docs import fetch_restapi_docs
from post_data_file import post_file

prod_url = 'https://t-and-s-dp-poc.azurewebsites.net/'
dev_url = 'http://127.0.0.1/'
url = dev_url

#Lets try and login as R2D2 and fetch REST API in JSON format
print("\nLogging in as R2D2 (who isn't allowed to view the dataset)")
username = "R2D2"
password = "tiger"
print("\nFetching continents & countries data from the REST API output data port with an authenticated but unauthorised user")
response = fetch_restapi_json(url+'continents_and_countries',username,password)
print(response)

#Lets try and login as Mary with wrong password and fetch REST API in JSON format
print("\nLogging in as Mary (who is allowed to view the dataset) but with wrong password")
username = "Mary"
password = "tier"
print("\nFetching continents & countries data from the REST API output data port with an unauthenticated user")
response = fetch_restapi_json(url+'continents_and_countries',username,password)
print(response)

#Fetch all continents & countries data from our REST API in JSON format
print("\nLogging in as Mary with correct password")
username = "Mary"
password = "tiger"
print("\nFetching continents & countries data from the REST API output data port with an authenticated and authorised user")
json_data = fetch_restapi_json(url+'continents_and_countries',username,password)
print(json_data)

#Fetch all continents & countries data from our REST API in CSV format into a dataframe
print("\nFetching continents & countries data from the REST API output data port in CSV format")
df = fetch_restapi_csv(url+'continents_and_countries',username,password)
print(df)

print("\nLogging in as R2D2 (who is authorised to upload files)")
#Test pushing countries and continents files to REST API input data port
username = "R2D2"
password = "tiger"
print("\nPushing source countries and continents CSV files to the input data port")
response = post_file(url+'uploadsrcfile', 'countries.csv', username, password)
print(response)
response = post_file(url+'uploadsrcfile', 'continents.csv', username, password)
print(response)

#Test executing a pipeline to create target dataset from source dataset
print("\nExecute the pipeline which will transform source data into an abstraction layer and push to target dataset")
response = post_file(url+'executepipeline', 'pipeline.sql', username, password)
print(response)

#Fetch latest version of continents & countries data from our REST API in JSON format
print("\nLogging back in as Mary")
username = "Mary"
password = "tiger"
print("\nFetch latest version of continents & countries data from our REST API in JSON format")
json_data = fetch_restapi_json(url+'continents_and_countries',username,password)
print(json_data)

#Fetch original version of continents & countries data from our REST API in JSON format
username = "Mary"
password = "tiger"
print("\nFetch original version of continents & countries data from our REST API in JSON format")
json_data = fetch_restapi_json(url+'continents_and_countries/0.1',username,password)
print(json_data)

#Fetch the data dictionary for the continents and countries dataset
print("\nFetching continents & countries data dictionary from the REST API output data port")
json_data = fetch_restapi_schema(url)
print(json_data)

#Test pushing schema file to REST API input data port
print("\nPushing a data dictionary/schema file to the input data port")
response = post_file(url+'uploadschema', 'schema.csv', username, password)
print(response)

#Fetch the revised data dictionary for the continents and countries dataset
print("\nFetching continents & countries data dictionary from the REST API output data port")
json_data = fetch_restapi_schema(url)
print(json_data)

#Fetch the data product docs
print("\nFetching the data product documentation")
response = fetch_restapi_docs(url)
print(response)
