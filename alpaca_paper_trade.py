import alpaca_trade_api as tradeapi

# Alpaca API credentials
API_KEY = 'PKBQ4Q9TTZ8LR5RRPPRC'
SECRET_KEY = '79heuzCM7F75JkEDK5yAuJyWOKByAE7aZ2X7JWIX'
BASE_URL = 'https://paper-api.alpaca.markets/v2'

# Initialize API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Example: Get account info
account = api.get_account()
print("Account Info:")
print(f"ID: {account.id}")
print(f"Status: {account.status}")
print(f"Cash: ${account.cash}")
print(f"Portfolio Value: ${account.portfolio_value}")
