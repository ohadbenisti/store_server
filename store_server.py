import httpx2
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("fake-store", version="0.1.0")

API_URL = "https://fakestoreapi.com/products"


@mcp.tool(name="getProducts")
def get_products() -> list[dict]:
    """TODO: this tool shuld fetch a list of products from the an API and rturn it. this is a special tool that will be used in the prompt to get the products and return them to the user."""
    response = httpx2.get("https://fakestoreapi.com/products",timeout = 10)
    response.raise_for_status()  # Raise an error if the request failed
    data = response.json()  # Parse the JSON response
    data_up_to_100 = [product for product in data if product["price"] <= 100]
        
    return data_up_to_100  # Return the list of products

if __name__ == "__main__":
    mcp.run()