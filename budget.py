from datetime import datetime

def get_current_day():
    """Returns the current day of the week."""
    return datetime.now().strftime("%A")


def calculate_item_totals(items):
    """Calculates total price per item and subtotal."""
    subtotal = 0
    for item in items:
        item["total_price"] = item["price"] * item["quantity"]
        subtotal += item["total_price"]
    return items, subtotal


def apply_weekly_allowance(budget, allowance_amount, allowance_day, current_day):
    """Adds weekly allowance if today is allowance day."""
    if allowance_day == current_day:
        return budget + allowance_amount
    return budget


def calculate_total_with_tax(subtotal, tax_rate):
    """Calculates tax and final total."""
    tax_amount = subtotal * tax_rate
    total_cost = subtotal + tax_amount
    return tax_amount, total_cost


def calculate_remaining_budget(budget, total_cost):
    """Calculates remaining money and budget status."""
    remaining_money = budget - total_cost
    within_budget = remaining_money >= 0
    return remaining_money, within_budget


def calculate_carry_over(remaining_money):
    """Carries leftover money forward."""
    return max(0, remaining_money)


def record_transaction(items, name, price, quantity, day):
    """Stores items in chronological order."""
    items.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "day": day
    })
