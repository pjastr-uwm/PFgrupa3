def calculate_discounted_price(price, discount):
    """
    Calculate price after applying discount.

    Args:
        price (float): Base price
        discount (float): Discount as percentage (0-100)

    Returns:
        float: Price after discount
    """
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Price must be a non-negative number")

    if not isinstance(discount, (int, float)) or discount < 0 or discount > 100:
        raise ValueError("Discount must be a number between 0 and 100")

    discounted_price = price * (1 - discount / 100)
    return round(discounted_price, 2)