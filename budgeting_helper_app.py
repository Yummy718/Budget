print("=== Budgeting Helper Application ===")

# Weekly budget
weekly_budget = float(input("Enter your budget for the week: $"))

# Tax rate
tax_rate = float(input("Enter the tax rate (example: enter 8 for 8%): ")) / 100

# How much the user plans to spend
planned_spending = float(input("How much do you want to spend this week? $"))

items = []
total_cost = 0

# Number of items
num_items = int(input("How many different items do you want to buy? "))

# Item input loop
for i in range(num_items):
    print(f"\nItem {i + 1}")
    item_name = input("Item name: ")
    price = float(input("Price of the item: $"))
    quantity = int(input("Quantity: "))

    item_total = price * quantity
    total_cost += item_total

    items.append({
        "name": item_name,
        "price": price,
        "quantity": quantity,
        "total": item_total
    })

# Tax calculation
tax_amount = total_cost * tax_rate
final_total = total_cost + tax_amount

# Money left or deficit
money_left = weekly_budget - final_total

# Output summary
print("\n=== Weekly Budget Summary ===")
print(f"Weekly Budget: ${weekly_budget:.2f}")
print(f"Planned Spending: ${planned_spending:.2f}")
print(f"Subtotal (before tax): ${total_cost:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total Cost (after tax): ${final_total:.2f}")

print("\nItems Purchased (Chronological Order):")
for item in items:
    print(
        f"- {item['name']} | "
        f"${item['price']} x {item['quantity']} = ${item['total']:.2f}"
    )

# Budget result
if money_left >= 0:
    print(f"\nMoney Left: ${money_left:.2f}")
    print("You are within your budget!")
else:
    print(f"\nDeficit: ${abs(money_left):.2f}")
    print("You exceeded your budget!")

print("\n=== End of Report ===")
