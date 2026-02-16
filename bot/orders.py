import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(
            f"Placing order | Symbol: {symbol} | Side: {side} | "
            f"Type: {order_type} | Qty: {quantity} | Price: {price}"
        )

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order Response: {response}")
        return response

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise
