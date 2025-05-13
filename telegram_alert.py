from telegram import Bot

def send_telegram_alert(signal):
    bot = Bot(token="@Anilstockalert")
    message = (
        f"🚀 *Profitsphere Signal* 🚀\n"
        f"Symbol: {signal['symbol']}\n"
        f"Trend: {signal['trend']}\n"
        f"Action: {signal['strategy']}\n"
        f"Strike: {signal['strike']}\n"
        f"Reason: {signal['reason']}"
    )
    bot.send_message(chat_id="7623496477", text=message, parse_mode="Markdown")

# Example signal
signal = {
    "symbol": "NIFTY",
    "trend": "BULLISH",
    "strategy": "BUY 22800 CE",
    "strike": 22800,
    "reason": "OI buildup + IV spike"
}
send_telegram_alert(signal)