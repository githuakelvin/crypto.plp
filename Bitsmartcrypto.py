import requests  # To fetch real-time prices
import spacy  # For NLP query understanding

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Real-time crypto API (CoinGecko)
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano,solana,polkadot,avalanche,litecoin&vs_currencies=usd"

# Function to fetch real-time prices
def get_crypto_prices():
    try:
        response = requests.get(API_URL)
        prices = response.json()
        return prices
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return {}

# Crypto database with real-time price fetching
crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high"},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium"},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low"},
    "Solana": {"price_trend": "rising", "market_cap": "medium-high", "energy_use": "low"},
    "Polkadot": {"price_trend": "stable", "market_cap": "medium", "energy_use": "low"},
    "Avalanche": {"price_trend": "rising", "market_cap": "medium-low", "energy_use": "low"},
    "Litecoin": {"price_trend": "stable", "market_cap": "medium", "energy_use": "low"},
}

# NLP-powered recommendation function
def recommend_crypto(user_query):
    doc = nlp(user_query.lower())  # Process query with NLP

    # Get real-time prices
    prices = get_crypto_prices()

    # Check if user asked about real-time price
    if "price" in user_query or "current value" in user_query:
        response = [f"{coin}: ${prices[coin.lower()]['usd']}" for coin in crypto_db if coin.lower() in prices]
        return "\n".join(response) if response else "Sorry, couldn't fetch real-time prices."

    # Profitability recommendation
    if "profit" in user_query or "grow" in user_query or "trend" in user_query:
        profitable_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if profitable_coins:
            best_profit = max(profitable_coins, key=lambda x: crypto_db[x]["market_cap"])
            return f"{best_profit} is trending up! Current price: ${prices.get(best_profit.lower(), {}).get('usd', 'N/A')}. 📈"

    # Sustainability recommendation
    elif "sustain" in user_query or "eco" in user_query or "green" in user_query:
        sustainable_coins = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        return f"Eco-friendly choices: {', '.join(sustainable_coins)} 🌱"

    return "I didn't quite get that. Try asking about profitable cryptos or sustainable investments!"

# Main chatbot function
#we need to choose a name for our chatbot

def main():
    print("Welcome to **CRUB BUBLIS** - Your Crypto Advisor!")
    disclaimer = "\n⚠️ Remember: Crypto is volatile—always do research! ⚠️"
    print(disclaimer)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye", "stop","baadae","goodbye","see you later"]:
            # Exit the chatbot
            print("\nCRUB BUBLIS: Goodbye! Stay informed and invest wisely. 🚀\n")
            break

        response = recommend_crypto(user_input)
        print(f"CRUB BUBLIS: {response}")
        print(disclaimer)

if __name__ == "__main__":
    main()
