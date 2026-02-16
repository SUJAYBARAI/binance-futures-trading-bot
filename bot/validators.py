def validate_side(side: str):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(quantity: float):
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")
    return float(quantity)


def validate_price(price: float):
    if price is not None and float(price) <= 0:
        raise ValueError("Price must be greater than 0")
    return float(price) if price else None
