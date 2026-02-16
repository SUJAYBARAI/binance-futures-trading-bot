# Binance Futures Demo Trading Bot (USDT-M)

## Overview

This project is a simplified Python-based trading bot that places MARKET
and LIMIT orders on Binance Futures Demo (USDT-M).

The application is designed with a clean, modular architecture, proper
logging, structured validation, and robust error handling to simulate
production-level backend development practices.

------------------------------------------------------------------------

## Features

-   Place MARKET orders
-   Place LIMIT orders
-   Supports both BUY and SELL
-   CLI-based input using argparse
-   Separate API client layer and CLI layer
-   Structured logging of API requests and responses
-   Proper exception handling for:
    -   Invalid user inputs
    -   API errors
    -   Network failures

------------------------------------------------------------------------

## Tech Stack

-   Python 3.x
-   python-binance
-   python-dotenv
-   argparse

------------------------------------------------------------------------

## Project Structure

trading_bot/ │ ├── bot/ │ ├── **init**.py │ ├── client.py │ ├──
orders.py │ ├── validators.py │ ├── logging_config.py │ ├── cli.py ├──
requirements.txt ├── README.md └── logs/ (auto-generated)

------------------------------------------------------------------------

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/SUJAYBARAI/binance-futures-trading-bot {=html} cd trading_bot

### 2. Create Virtual Environment (Recommended)

Windows: python -m venv venv venv`\Scripts`{=tex}`\activate`{=tex}

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Create a .env File

Create a .env file in the project root and add:

BINANCE_API_KEY=your_api_key BINANCE_SECRET_KEY=your_secret_key

⚠️ Do NOT commit the .env file to GitHub.

------------------------------------------------------------------------

## API Endpoint Used

Binance Futures Demo API Endpoint:

https://demo-fapi.binance.com

------------------------------------------------------------------------

## Usage Examples

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

### LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002
--price 70000

------------------------------------------------------------------------

## CLI Output

The application prints:

-   Order request summary
-   Order ID
-   Order status
-   Executed quantity
-   Average price (if available)
-   Success / Failure message

------------------------------------------------------------------------

## Logging

All API requests, responses, and errors are logged to:

logs/trading.log

The log file includes: - Timestamp - Log level - Order details - Full
API response - Error information (if any)

------------------------------------------------------------------------

## Assumptions

-   USDT-M Futures only
-   Binance Demo environment is used
-   Minimum notional requirement (\~\$100) applies
-   Valid Demo API credentials required

------------------------------------------------------------------------

## Conclusion

This project demonstrates:

-   Clean and modular code structure
-   Proper API abstraction
-   Strong validation and error handling
-   Production-style logging
-   Successful integration with Binance Futures Demo API
