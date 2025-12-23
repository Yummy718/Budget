from budget import (
    calculate_item_totals,
    calculate_total_with_tax,
    calculate_remaining_budget,
    calculate_carry_over
)

def display_results(weekly_budget, tax_rate, items, current_day):
    """Handles all output and reporting."""

    items, subtotal = calculate_item_totals(items)
    tax_amount, total_cost = calculate_total_with_tax(subtotal, tax_rate)
    remaining_money, within_budget = calculate_remaining_budget(
        weekly_budget, total_cost
    )
    carry_over = calculate_carry_over(remaining_money)

    print("\n=== Weekly Budget Summary ===")
    print(f"Day of Week: {current_day}")
    print(f"Budget: ${weekly_budget:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

    print("\nItems Purchased (Chronological Order):")
    for item in items:
        print(
            f"- {item['day']} | {item['name']} | "
            f"${item['price']} x {item['quantity']} "
            f"= ${item['total_price']:.2f}"
        )

    if within_budget:
        print(f"\nMoney Left: ${remaining_money:.2f}")
    else:
        print(f"\nOver Budget By: ${abs(remaining_money):.2f}")

    print(f"Money Carried Over: ${carry_over:.2f}")
    print("\n=== End of Report ===")
