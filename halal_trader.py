import alpaca_trade_api as tradeapi
import time

# -------- YOUR API CREDENTIALS --------
API_KEY = 'PKBQ4Q9TTZ8LR5RRPPRC'  # Replace with your actual API key
SECRET_KEY = '79heuzCM7F75JkEDK5yAuJyWOKByAE7aZ2X7JWIX'  # Replace with your actual Secret key
BASE_URL = 'https://paper-api.alpaca.markets'

# -------- INITIAL SETUP --------
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')
budget = 10  # Max total budget in USD
min_profit_percent = 5  # Sell when 5% profit is reached
bought_symbols = {}

# -------- HALAL STOCKS LIST --------
halal_stocks = ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN", "NVDA"]

# -------- BUY FUNCTION --------
def buy_stocks():
    global budget
    per_stock = round(budget / len(halal_stocks), 2)
    for symbol in halal_stocks:
        try:
            api.submit_order(
                symbol=symbol,
                notional=per_stock,
                side='buy',
                type='market',
                time_in_force='day'
            )
            bought_symbols[symbol] = per_stock
            print(f"Buy order placed for {symbol} worth ${per_stock}")
        except Exception as e:
            print(f"Failed to buy {symbol}: {e}")

# -------- SELL FUNCTION --------
def sell_if_profit():
    for symbol in list(bought_symbols.keys()):
        try:
            position = api.get_position(symbol)
            current_price = float(position.current_price)
            avg_price = float(position.avg_entry_price)
            change = ((current_price - avg_price) / avg_price) * 100

            if change >= min_profit_percent:
                api.submit_order(
                    symbol=symbol,
                    qty=position.qty,
                    side='sell',
                    type='market',
                    time_in_force='day'
                )
                print(f"Sold {symbol} for {change:.2f}% profit")
                del bought_symbols[symbol]

        except Exception as e:
            print(f"Error checking/selling {symbol}: {e}")

# -------- RUN --------
print("Running halal intraday trading bot...")
buy_stocks()

while True:
    sell_if_profit()
    time.sleep(60)  # Check every minute
