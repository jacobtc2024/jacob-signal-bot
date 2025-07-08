import requests
import time

TELEGRAM_TOKEN = "7964495690:AAHKkTLvcRtxadqk_lP3L8K5NTHAr0WhnKs"
CHAT_ID = "169908910"

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd']

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

def check_and_send_signal():
    btc_price = get_price("bitcoin")
    eth_price = get_price("ethereum")

    if btc_price < 60000:
        send_telegram_message(f"🚨 قیمت بیت‌کوین پایین‌تر از 60K شد: {btc_price} دلار")
    if eth_price < 3500:
        send_telegram_message(f"🚨 قیمت اتریوم پایین‌تر از 3500 شد: {eth_price} دلار")

while True:
    try:
        check_and_send_signal()
        print("✅ بررسی انجام شد.")
    except Exception as e:
        print(f"❌ خطا: {e}")

    time.sleep(900)  # هر ۱۵ دقیقه
