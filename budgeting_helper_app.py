import tkinter as tk
from budget import get_current_day, record_transaction

class InputGUI:
    def __init__(self, root):
        self.root = root
        self.items = []
        self.finished = False

        # Stored values (saved before window closes)
        self.budget = None
        self.tax = None
        self.day = get_current_day()

        self.root.title("Budget Input")

        # ===== Budget Inputs =====
        tk.Label(root, text="Weekly Budget").grid(row=0, column=0)
        self.budget_entry = tk.Entry(root)
        self.budget_entry.grid(row=0, column=1)

        tk.Label(root, text="Tax Rate (e.g. 0.07)").grid(row=1, column=0)
        self.tax_entry = tk.Entry(root)
        self.tax_entry.grid(row=1, column=1)

        # ===== Item Inputs =====
        tk.Label(root, text="Item Name").grid(row=2, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=1)

        tk.Label(root, text="Price").grid(row=3, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=3, column=1)

        tk.Label(root, text="Quantity").grid(row=4, column=0)
        self.qty_entry = tk.Entry(root)
        self.qty_entry.grid(row=4, column=1)

        tk.Button(root, text="Add Item", command=self.add_item).grid(
            row=5, column=0, columnspan=2
        )

        tk.Button(root, text="Finish", command=self.finish).grid(
            row=6, column=0, columnspan=2
        )

        # ===== Item List Display =====
        tk.Label(root, text="Items Added").grid(row=7, column=0, columnspan=2)

        self.item_listbox = tk.Listbox(root, width=45)
        self.item_listbox.grid(row=8, column=0, columnspan=2)

    def add_item(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.qty_entry.get())

        record_transaction(
            self.items,
            name,
            price,
            quantity,
            self.day
        )

        # Show item in listbox
        self.item_listbox.insert(
            tk.END,
            f"{name} - ${price:.2f} x {quantity}"
        )

        # Clear inputs
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)

    def finish(self):
        # Save values BEFORE destroying window
        self.budget = float(self.budget_entry.get())
        self.tax = float(self.tax_entry.get())

        self.finished = True
        self.root.destroy()

    def collect_user_data(self):
        return self.budget, self.tax, self.items, self.day
