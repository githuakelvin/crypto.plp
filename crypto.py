# CryptoBuddy - Your Friendly Crypto Advisor
#Id prefer to print a name of our group instead of CRUB BUBLIS
print("""
   ____            _       ____        _     _ _     
  / ___|_ __ _   _| |__   | __ ) _   _| |__ | (_)___ 
 | |   | '__| | | | '_ \  |  _ \| | | | '_ \| | / __|
 | |___| |  | |_| | |_) | | |_) | |_| | |_) | | \__ \\
  \____|_|   \__,_|_.__/  |____/ \__,_|_.__/|_|_|___/
""")
print("Hey there! I'm CryptoBuddy! Let's find you a green and growing crypto! 🌱🚀\n")

# Crypto database
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    }, 
    "Solana": {
        "price_trend": "rising",  
        "market_cap": "medium-high",  
        "energy_use": "low",  
        "sustainability_score": 7/10,  
        "use_case": "High-Speed Transactions, NFTs",  
        "risk_level": "Medium",  
        "community_sentiment": "Growing"  
    }, 
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    } ,
    "avalanche": {  
        "price_trend": "rising",  
        "market_cap": "medium-low",  
        "energy_use": "low",  
        "sustainability_score": 6,  
        "use_case": "Fast Transactions, Smart Contracts",  
        "risk_level": "High",  
        "community_sentiment": "Mixed"  
    } ,
     "polkadot": {  
        "price_trend": "stable",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 7,  
        "use_case": "Cross-Chain Interoperability",  
        "risk_level": "Medium",  
        "community_sentiment": "Positive"  
    }, 
    "Litecoin": {  
        "price_trend": "stable",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 5/10  
    }, 
}

def recommend_crypto(user_query):
    user_query = user_query.lower()
    
    # Initialize profitable_coins
    profitable_coins = []
    # Check if user is looking for trending coins
    if "trend" in user_query or "rising" in user_query or "growing" in user_query or "popular" in user_query or "grow" in user_query:
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if trending_coins:
            return f"Here are some trending coins: {', '.join(trending_coins)}! 🚀"
    
    # Profitability recommendation
    if "profit" in user_query or "grow" in user_query or "trend" in user_query:
        profitable_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if profitable_coins:
          best_profit = max(profitable_coins, key=lambda x: crypto_db[x]["market_cap"])
          return f"{best_profit} is trending up with a strong market cap! Good for growth potential! 📈"

    #risk assessment #added Max
    elif "risk" in user_query or "safe" in user_query or "stable" in user_query:
        stable_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "stable"]
        if stable_coins:
            best_stable = max(stable_coins, key=lambda x: crypto_db[x]["sustainability_score"])
            return f"{best_stable} is a stable choice with a sustainability score of {crypto_db[best_stable]['sustainability_score']*10}/10! 🛡️"    
    
    # Sustainability recommendation
    elif "sustain" in user_query or "eco" in user_query or "green" in user_query:
        sustainable_coins = [coin for coin in crypto_db if crypto_db[coin]["sustainability_score"] >= 7/10]
        if sustainable_coins:
            best_eco = max(sustainable_coins, key=lambda x: crypto_db[x]["sustainability_score"])
            return f"Invest in {best_eco}! 🌱 It's eco-friendly with a sustainability score of {crypto_db[best_eco]['sustainability_score']*10}/10!"
    
    # General recommendation
    elif "buy" in user_query or "invest" in user_query or "recommend" in user_query:
        balanced_choice = max(crypto_db, key=lambda x: (
            crypto_db[x]["sustainability_score"] * 0.6 + 
            (1 if crypto_db[x]["price_trend"] == "rising" else 0) * 0.4
        ))
        return f"For a balanced choice, consider {balanced_choice}! It has good sustainability and {'is rising' if crypto_db[balanced_choice]['price_trend'] == 'rising' else 'stable'} trends."
    
    # Default response
    return "I'm not sure I understand. Try asking about profitable cryptos or sustainable investments!"

def main():
    print("I can help you with:")
    print("- Trending cryptocurrencies 📈")
    print("- Eco-friendly crypto options 🌱")
    print("- General investment advice 💰")
    print("Type 'quit' to exit.\n")
    
    
    disclaimer = "\n⚠️ Remember: Crypto is risky—always do your own research! This is not financial advice. ⚠️"
    print(disclaimer)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye", "enough", "stop", "kwaheri", "baadae", "see ya", "arios", "KWENDA!!!"]:
            # If user types 'exit' or 'quit', end the chatbot session
            print("\nCryptoBuddy: Goodbye! Stay informed and invest wisely. 🚀\n")
            break
        
        
        response = recommend_crypto(user_input)
        print(f"CryptoBuddy: {response}")
        print(disclaimer)

if __name__ == "__main__":
    main()