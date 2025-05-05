# MCP Agent - Stock Analysis Tool

A Python-based agent that leverages LangChain and MCP (Machine Control Protocol) to analyze stock market data using natural language queries.

## Features

- Real-time stock data analysis using yfinance
- Natural language processing with GPT-4
- Support for both quarterly and annual financial analysis
- Easy-to-use command-line interface

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/FarazArshad1/MCP-Agent.git
cd MCP-Agent
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the application:

```bash
python mcp_client.py
```

2. The agent can perform the following analyses:

- Fetch general company information
- Analyze quarterly financial reports
- Review annual financial statements
- Track revenue changes over time

## Project Structure

- `mcp_client.py` - Main client application using LangChain and OpenAI
- `mcp_server.py` - Server implementing stock analysis tools
- `requirements.txt` - Project dependencies

## Tools Available

- `fetch_stock_info`: Get general company information
- `fetch_quarterly_financials`: Retrieve quarterly financial reports
- `fetch_annual_financials`: Access annual financial statements
