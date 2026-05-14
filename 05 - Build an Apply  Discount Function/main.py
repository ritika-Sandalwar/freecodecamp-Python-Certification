# define a function named apply_discount.
def apply_discount(price, discount):

    # If price is not a number (int or float), the function should return the string The price should be a number.
    if not isinstance(price, (int, float)):
        return 'The price should be a number'
    
    # If discount is not a number (int or float), the function should return the string The discount should be a number.
    if not isinstance(discount, (int, float)):
        return 'The discount should be a number'

    # If price is less than or equal to 0, the function should return the string The price should be greater than 0.
    if price <= 0:
        return 'The price should be greater than 0'

    # If discount is less than 0 or greater than 100, the function should return the string The discount should be between 0 and 100.
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    # calculating the discount as a percentage of the price.
    discount_amount = (price * discount) / 100
    final_price = price - discount_amount
    return final_price  # The function is returning the final price after applying the discount

print(apply_discount(50, 20))


