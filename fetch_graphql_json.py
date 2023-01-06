from python_graphql_client import GraphqlClient

def fetch_graphql_json(variables):
    # Instantiate the client with an endpoint.
    client = GraphqlClient(endpoint="http://127.0.0.1/graphql")

    # Create the query string and variables required for the request.
    query = """
query MyQuery($CountryName: String, $ContinentCode: String) {
  countries(ContinentCode: $ContinentCode, CountryName: $CountryName) {
    ContinentCode
    ContinentName
    ThreeLetterCountryCode
    CountryName
  }
}
    """

    # Synchronous request
    data = client.execute(query=query, variables=variables)
    return data