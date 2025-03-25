import alpaca_trade_api as tradeapi

API_KEY = 'PKBQ4Q9TTZ8LR5RRPPRC'
SECRET_KEY = '79heuzCM7F75JkEDK5yAuJyWOKByAE7aZ2X7JWIX'
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Check if the market is open
clock = api.get_clock()
if clock.is_open:
    # Place a market order to buy 1 share of AAPL
    order = api.submit_order(
        symbol='AAPL',
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print("Order submitted successfully!")
else:
    print("Market is closed right now.")
