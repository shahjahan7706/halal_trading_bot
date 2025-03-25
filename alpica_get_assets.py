import requests

# Your Alpaca Paper Trading API credentials
API_KEY = 'PKA5A3J2WH4DZL1HYNBC0'
SECRET_KEY = 'hwa9Uqvvv9qHqJe0Lf1jjPiKjdsYGPbVRknz2WY'
BASE_URL = 'https://paper-api.alpaca.markets'

# Endpoint to get assets
endpoint = f'{BASE_URL}/v2/assets'

# Set headers
headers = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': SECRET_KEY
}

# Make GET request
response = requests.get(endpoint, headers=headers)

# Check and print the result
if response.status_code == 200:
    assets = response.json()
    print("Assets fetched successfully:")
    for asset in assets[:5]:  # Displaying only first 5 assets
        print(f"{asset['symbol']}: {asset['name']} - {asset['status']}")
else:
    print(f"Failed to fetch assets: {response.status_code}")
    print(response.text)
