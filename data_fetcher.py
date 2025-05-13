import requests
from config import PROFMART_API_KEY, PROFMART_BASE_URL

def fetch_option_chain(symbol="NIFTY"):
    url = f"{PROFMART_BASE_URL}/option-chain"
    headers = {
        "Authorization": f"Bearer {PROFMART_API_KEY}",
        "Content-Type": "application/json"
    }
    params = {"symbol": symbol}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise error for HTTP failures
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage
nifty_chain = fetch_option_chain("NIFTY")
print(nifty_chain)