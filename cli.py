import argparse
import logging
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price required for LIMIT order")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        if order_type == "LIMIT" and price is None:
            raise ValueError("LIMIT order requires --price")

        print("\n===== ORDER REQUEST SUMMARY =====")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")
        if price:
            print(f"Price       : {price}")

        client = get_client()

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n===== ORDER RESPONSE =====")
        print("Order ID    :", response.get("orderId"))
        print("Status      :", response.get("status"))
        print("ExecutedQty :", response.get("executedQty"))
        print("Avg Price   :", response.get("avgPrice", "N/A"))
        print("\n✅ Order placed successfully!")

    except Exception as e:
        logging.error(str(e))
        print(f"\n❌ Order Failed: {str(e)}")


if __name__ == "__main__":
    main()
