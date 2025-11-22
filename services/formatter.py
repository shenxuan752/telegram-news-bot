from datetime import datetime

def format_digest(news_data):
    """Format news data into a nice Telegram message."""
    today = datetime.now().strftime("%b %d, %Y")
    
    message = f"📰 **Daily News Digest** - {today}\n\n"
    
    # Tech News
    if news_data.get("tech"):
        message += "🔧 **TECH NEWS**\n"
        for article in news_data["tech"]:
            title = article["title"][:80] + "..." if len(article["title"]) > 80 else article["title"]
            message += f"• [{title}]({article['url']})\n"
        message += "\n"
    
    # Financial News
    if news_data.get("financial"):
        message += "💰 **FINANCIAL & ECONOMIC NEWS**\n"
        for article in news_data["financial"]:
            title = article["title"][:80] + "..." if len(article["title"]) > 80 else article["title"]
            message += f"• [{title}]({article['url']})\n"
        message += "\n"
    
    # Stock News
    if news_data.get("stock"):
        message += "📈 **STOCK MARKET NEWS**\n"
        for article in news_data["stock"]:
            title = article["title"][:80] + "..." if len(article["title"]) > 80 else article["title"]
            symbol = f" ({article.get('symbol', '')})" if article.get('symbol') else ""
            message += f"• [{title}]({article['url']}){symbol}\n"
        message += "\n"
    
    message += "_Powered by NewsAPI, Alpha Vantage, FMP_"
    
    return message

if __name__ == "__main__":
    # Test formatting
    test_data = {
        "tech": [{"title": "OpenAI Releases GPT-5", "url": "https://example.com/1"}],
        "financial": [{"title": "Fed Holds Rates Steady", "url": "https://example.com/2"}],
        "stock": [{"title": "Tesla Stock Soars", "url": "https://example.com/3", "symbol": "TSLA"}]
    }
    print(format_digest(test_data))
