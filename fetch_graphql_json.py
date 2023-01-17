from python_graphql_client import GraphqlClient

def fetch_graphql_json(url, variables):
    # Instantiate the client with an endpoint.
    endpoint=url+'graphql'
    client = GraphqlClient(endpoint=endpoint)

    # Create the query string and variables required for the request.
    query = """
query MyQuery ($ContinentCode: String, $CountryName:String) {
  countries(ContinentCode: $ContinentCode, CountryName: $CountryName) {
    ContinentName
    CountryName
  }
}
    """

    # Synchronous request
    data = client.execute(query=query, variables=variables)
    return data