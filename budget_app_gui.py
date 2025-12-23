import tkinter as tk
from datetime import datetime

# ---------------- LOGIC FUNCTIONS ----------------

def get_current_day():
    return datetime.now().strftime("%A")

def apply_weekly_allowance(budget, allowance, allowance_day, current_day):
    if allowance_day == current_day:
        return budget + allowance
    return budget

def record_transaction(items, name, price, quantity, day):
    total = price * quantity
    items.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total,
        "day": day
    })

# ---------------- GUI FUNCTIONS ----------------

items = []

def add_item():
    try:
        name = entry_item_name.get()
        price = float(entry_item_price.get())
        quantity = int(entry_item_quantity.get())

        if not name:
            raise ValueError

        current_day = get_current_day()
        record_transaction(items, name, price, quantity, current_day)

        # Show in listbox only
        listbox_items.insert(
            tk.END, f"{name} | ${price:.2f} x {quantity}"
        )

        # Clear entries
        entry_item_name.delete(0, tk.END)
        entry_item_price.delete(0, tk.END)
        entry_item_quantity.delete(0, tk.END)

    except ValueError:
        # Only clear invalid entries, no output
        entry_item_name.delete(0, tk.END)
        entry_item_price.delete(0, tk.END)
        entry_item_quantity.delete(0, tk.END)

def collect_input_only():
    """Function to collect all user input without output."""
    try:
        weekly_budget = float(entry_budget.get())
        weekly_allowance = float(entry_allowance.get())
        allowance_day = entry_allowance_day.get().strip().title()
        tax_rate = float(entry_tax.get())

        current_day = get_current_day()
        updated_budget = apply_weekly_allowance(
            weekly_budget, weekly_allowance, allowance_day, current_day
        )

        # Return all collected input
        return updated_budget, tax_rate, items, current_day

    except ValueError:
        # Return None if input is invalid
        return None, None, items, get_current_day()

# ---------------- GUI SETUP ----------------

root = tk.Tk()
root.title("Budgeting Helper App (Input Only)")
root.configure(bg="#F2F6FC")

FONT_TITLE = ("Helvetica", 16, "bold")
FONT_LABEL = ("Helvetica", 10)
FONT_BUTTON = ("Helvetica", 10, "bold")

# Title
tk.Label(root, text="💰 Budgeting Helper App (Input Only)",
         font=FONT_TITLE, bg="#F2F6FC", fg="#2C3E50")\
    .grid(row=0, column=0, columnspan=2, pady=10)

# Budget section
tk.Label(root, text="Weekly Budget", bg="#F2F6FC", font=FONT_LABEL).grid(row=1, column=0, sticky="e")
entry_budget = tk.Entry(root)
entry_budget.grid(row=1, column=1, pady=2)

tk.Label(root, text="Weekly Allowance", bg="#F2F6FC", font=FONT_LABEL).grid(row=2, column=0, sticky="e")
entry_allowance = tk.Entry(root)
entry_allowance.grid(row=2, column=1, pady=2)

tk.Label(root, text="Allowance Day", bg="#F2F6FC", font=FONT_LABEL).grid(row=3, column=0, sticky="e")
entry_allowance_day = tk.Entry(root)
entry_allowance_day.grid(row=3, column=1, pady=2)

tk.Label(root, text="Tax Rate (e.g. 0.07)", bg="#F2F6FC", font=FONT_LABEL).grid(row=4, column=0, sticky="e")
entry_tax = tk.Entry(root)
entry_tax.grid(row=4, column=1, pady=2)

# Item section
tk.Label(root, text="Items", font=("Helvetica", 12, "bold"),
         bg="#F2F6FC", fg="#34495E").grid(row=5, column=0, columnspan=2, pady=(10, 5))

tk.Label(root, text="Item Name", bg="#F2F6FC").grid(row=6, column=0, sticky="e")
entry_item_name = tk.Entry(root)
entry_item_name.grid(row=6, column=1)

tk.Label(root, text="Price", bg="#F2F6FC").grid(row=7, column=0, sticky="e")
entry_item_price = tk.Entry(root)
entry_item_price.grid(row=7, column=1)

tk.Label(root, text="Quantity", bg="#F2F6FC").grid(row=8, column=0, sticky="e")
entry_item_quantity = tk.Entry(root)
entry_item_quantity.grid(row=8, column=1)

tk.Button(root, text="➕ Add Item", bg="#3498DB", fg="white",
          font=FONT_BUTTON, command=add_item).grid(row=9, column=0, columnspan=2, pady=6)

listbox_items = tk.Listbox(root, width=40, height=5)
listbox_items.grid(row=10, column=0, columnspan=2, pady=5)

# Dummy calculate button for later use
tk.Button(root, text="📥 Collect Input (No Output)", bg="#F39C12", fg="white",
          font=FONT_BUTTON, command=collect_input_only).grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()
