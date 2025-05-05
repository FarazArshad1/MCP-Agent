from fastmcp import FastMCP
from pandas import DataFrame
import yfinance as yf

mcp = FastMCP("stocks")


@mcp.tool()
def fetch_stock_info(symbol: str) -> dict:
    """Get the general information of comapny"""
    stock = yf.Ticker(symbol)
    return stock.info


@mcp.tool()
def fetch_quarterly_financials(symbol: str) -> DataFrame:
    """Get the quarterly report of stocks"""
    stock = yf.Ticker(symbol)
    return stock.quarterly_financials.T

@mcp.tool()
def fecth_annual_financials(symbol: str) -> DataFrame:
    """Get the annual report of stocks"""
    stock = yf.Ticker(symbol)
    return stock.financials.T

if __name__ == "__main__":
    mcp.run(transport="stdio")