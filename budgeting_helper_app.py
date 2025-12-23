from budget import get_current_day, apply_weekly_allowance, record_transaction

def collect_user_data():
    """Handles all user input and returns structured data."""

    weekly_budget = float(input("Enter your weekly budget: $"))
    weekly_allowance = float(input("Enter weekly allowance amount: $"))
    allowance_day = input("What day do you receive your allowance? ").strip().title()
    tax_rate = float(input("Enter tax rate (example: 0.07): "))

    current_day = get_current_day()
    weekly_budget = apply_weekly_allowance(
        weekly_budget, weekly_allowance, allowance_day, current_day
    )

    items = []
    num_items = int(input("How many items do you want to buy? "))

    for i in range(num_items):
        print(f"\nItem {i + 1}")
        name = input("Item name: ")
        price = float(input("Item price: $"))
        quantity = int(input("Quantity: "))

        record_transaction(items, name, price, quantity, current_day)

    return weekly_budget, tax_rate, items, current_day
