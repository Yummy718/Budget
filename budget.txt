from datetime import datetime

# -------------------------------------------------
# 1. Determine the current day of the week
# -------------------------------------------------

def get_current_day():
    """
    Returns the current day of the week as a string.
    """
    return datetime.now().strftime("%A")


# -------------------------------------------------
# 2. Calculate total price per item and subtotal
# -------------------------------------------------

def calculate_item_totals(items):
    """
    items: list of dictionaries
           each item has 'price' and 'quantity'

    Returns:
    - updated items with 'total_price'
    - subtotal of all items
    """
    subtotal = 0

    for item in items:
        item["total_price"] = item["price"] * item["quantity"]
        subtotal += item["total_price"]

    return items, subtotal


# -------------------------------------------------
# 3. Determine if weekly allowance should be added
# -------------------------------------------------

def apply_weekly_allowance(budget, allowance_amount, allowance_day, current_day):
    """
    Adds weekly allowance to budget if today is allowance day.
    """
    if allowance_day == current_day:
        return budget + allowance_amount
    return budget


# -------------------------------------------------
# 4. Calculate tax and final total cost
# -------------------------------------------------

def calculate_total_with_tax(subtotal, tax_rate):
    """
    Calculates tax amount and total cost.
    """
    tax_amount = subtotal * tax_rate
    total_cost = subtotal + tax_amount
    return tax_amount, total_cost


# -------------------------------------------------
# 5. Calculate remaining money and budget status
# -------------------------------------------------

def calculate_remaining_budget(budget, total_cost):
    """
    Determines remaining money and whether user is within budget.
    """
    remaining_money = budget - total_cost
    within_budget = remaining_money >= 0
    return remaining_money, within_budget


# -------------------------------------------------
# 6. Carry leftover money forward
# -------------------------------------------------

def calculate_carry_over(remaining_money):
    """
    Only positive money is carried over to next week.
    """
    return max(0, remaining_money)


# -------------------------------------------------
# 7. Maintain chronological order of purchases
# -------------------------------------------------

def record_transaction(items, item_name, price, quantity, day):
    """
    Adds an item purchase in chronological order.
    """
    items.append({
        "name": item_name,
        "price": price,
        "quantity": quantity,
        "day": day
    })
    return items
