import json
import requests
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth

env = dotenv_values(".env")
OXY_USERNAME = env["OXY_USERNAME"]
OXY_PASSWORD = env["OXY_PASSWORD"]

if type(OXY_USERNAME) is not str or type(OXY_PASSWORD) is not str:
    raise Exception("Oxylabs credentials not found. Add them to your .env file!")

search_text = "vodka"

url = "https://realtime.oxylabs.io/v1/queries"
headers = {
    "Content-Type": "application/json",
}
payload = {
    "source": "universal_ecommerce",
    "url": f"https://www.klwines.com/Products?searchText={search_text}",
}

response = requests.post(
    url,
    auth=HTTPBasicAuth(OXY_USERNAME, OXY_PASSWORD),
    headers=headers,
    data=json.dumps(payload),
)

print(response.text)
