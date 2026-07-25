#Task 3: Dicount Modul

def apply_discount(price, percentage):
    discount_amount = price * (percentage / 100)
    discounted_price = price - discount_amount
    return discounted_price

def flat_discount(price, discount_amount):
    discounted_price = price - discount_amount
    return discounted_price