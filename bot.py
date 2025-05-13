import requests
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN
import time
from datetime import datetime

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def get_nifty_oi():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/option-chain"
    }
    
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)  # Establish session
    
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()["records"]["data"][0]  # Get first strike data
    except Exception as e:
        print(f"[{datetime.now()}] API Error: {str(e)}")
        return None

def send_alert(chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print(f"[{datetime.now()}] Alert sent: {message}")
    except Exception as e:
        print(f"[{datetime.now()}] Telegram Error: {str(e)}")

def main():
    chat_id = "7623496477"  # Your chat ID
    while True:
        oi_data = get_nifty_oi()
        if oi_data:
            ce_oi = oi_data.get("CE", {}).get("openInterest", 0)
            pe_oi = oi_data.get("PE", {}).get("openInterest", 0)
            
            if ce_oi > pe_oi:
                send_alert(chat_id, "📈 BUY NIFTY CE (OI Rising)")
            else:
                send_alert(chat_id, "📉 BUY NIFTY PE (OI Rising)")
        
        time.sleep(300)  # 5 minute delay

if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting Profitsphere Bot...")
    main()