import time
import requests

TELEGRAM_TOKEN = "8788812870:AAHYLCYEO7U9IjAjfk0NV9Ne0lOQYDDuPoU"
CHAT_ID = "7831099760"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

def check_market_pumps():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    try:
        response = requests.get(url)
        data = response.json()
        for coin in data:
            symbol = coin['symbol']
            if symbol.endswith('USDT'):
                price_change_percent = float(coin['priceChangePercent'])
                volume = float(coin['quoteVolume'])
                if price_change_percent >= 7.0 and volume > 50000:
                    alert_msg = f"🚀 **Pump Alert!**\n\nCoin: `{symbol}`\nPrice Change: `+{price_change_percent}%`\nVolume: `{volume:,.2f} USDT`"
                    send_telegram_message(alert_msg)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        check_market_pumps()
        time.sleep(180)