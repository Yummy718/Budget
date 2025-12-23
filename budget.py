from datetime import datetime

def get_current_day():
    return datetime.now().strftime("%A")


def record_transaction(items, name, price, quantity, day):
    items.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "day": day
    })


def calculate_item_totals(items):
    subtotal = 0
    for item in items:
        item["total_price"] = item["price"] * item["quantity"]
        subtotal += item["total_price"]
    return items, subtotal


def calculate_total_with_tax(subtotal, tax_rate):
    tax = subtotal * tax_rate
    return tax, subtotal + tax


def calculate_remaining_budget(budget, total_cost):
    remaining = budget - total_cost
    return remaining, remaining >= 0


def calculate_carry_over(remaining):
    return max(0, remaining)
