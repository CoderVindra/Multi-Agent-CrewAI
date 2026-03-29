import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol : str ) -> dict:
    """
    Retrieves the latest stock price and other relevant info for a give stock
    symbol using yahoo finance
    """
    stock = yf.Ticker(ticker=stock_symbol)
    info = stock.info

    if info.get("regularMarketPrice") is None:
        return {
            "result": "Failed",
            "message": f"Could not fetch price for {stock_symbol}. Please check symbol."
        }
    return {
        "result": "success",
        "stock": stock_symbol.upper(),
        "stock_price": info.get("regularMarketPrice"),
        "change": info.get("regularMarketChange"),
        "change_percent": round(info.get("regularMarketChangePercent"), 2)

    }
