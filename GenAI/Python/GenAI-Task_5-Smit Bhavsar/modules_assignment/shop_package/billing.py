#Task 3: Billing Module

def calculate_total(prices):
    total = sum(prices)
    return total

def apply_tax(total):
    tax_amount = total * (5 / 100)
    total_with_tax = total + tax_amount
    return total_with_tax