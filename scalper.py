
import time
import random

# CRYPTO SCALPER 3.0
# DEMO TRADING ONLY

balance = 1000.00
coins = ["BTC", "XRP", "HBAR"]

print("CRYPTO SCALPER 3.0")
print("AI DEMO SYSTEM INITIALISED")
print("Starting balance: $", balance)

while True:
    coin = random.choice(coins)
    price_change = random.uniform(-1, 1)

    print("--------------------")
    print("Scanning:", coin)
    print("Market movement:", round(price_change, 3), "%")

    if price_change > 0.3:
        print("DEMO SIGNAL: BUY", coin)
    elif price_change < -0.3:
        print("DEMO SIGNAL: SELL", coin)
    else:
        print("NO TRADE: Waiting")

    print("Virtual balance: $", round(balance, 2))
    time.sleep(10)

