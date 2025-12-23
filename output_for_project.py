import datetime

def run_budget_helper():
    print("--- Budgeting Helper Application ---")
    
    # 1. User Inputs (Design Spec 5)
    try:
        weekly_budget = float(input("Enter your weekly allowance/budget: $"))
        tax_rate = float(input("Enter your local tax rate (e.g., 0.07 for 7%): "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    transactions = []
    total_spent = 0.0
    
    while True:
        print(f"\nCurrent Balance: ${weekly_budget - total_spent:.2f}")
        action = input("\nAdd item (a) or View Summary (s) or Quit (q): ").lower()
        
        if action == 'a':
            # 2. Tracking items and quantities
            item_name = input("Item name: ")
            try:
                price = float(input("Price per item: $"))
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Invalid price or quantity.")
                continue

            # 3. Calculate sum with tax (Functional Req)
            subtotal = price * quantity
            tax_amount = subtotal * tax_rate
            item_total = subtotal + tax_amount
            
            # Check if within budget
            if total_spent + item_total > weekly_budget:
                print(f"!!! ALERT: This exceeds your budget by ${(total_spent + item_total) - weekly_budget:.2f}")
                proceed = input("Do you still want to add it? (y/n): ")
                if proceed.lower() != 'y':
                    continue

            # Store transaction with timestamp (Functional Req)
            transactions.append({
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "item": item_name,
                "total": item_total
            })
            total_spent += item_total
            print(f"Added {item_name}. Total for this item: ${item_total:.2f}")

        elif action == 's':
            # 4. Show chronological order (Functional Req)
            print("\n--- Weekly Transaction Log ---")
            if not transactions:
                print("No transactions yet.")
            for t in transactions:
                print(f"[{t['time']}] {t['item']}: ${t['total']:.2f}")
            
            # Summary stats
            remaining = weekly_budget - total_spent
            print("-" * 30)
            print(f"Total Spent: ${total_spent:.2f}")
            if remaining < 0:
                print(f"DEFICIT: -${abs(remaining):.2f}")
            else:
                print(f"REMAINING BUDGET: ${remaining:.2f}")
                
        elif action == 'q':
            print("Closing Budgeting Helper. Goodbye!")
            break

if __name__ == "__main__":
    run_budget_helper()