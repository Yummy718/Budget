import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class BudgetAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Budgeting Helper Application")
        self.root.geometry("500x600")

        # --- Data State ---
        self.weekly_budget = 0.0
        self.tax_rate = 0.0
        self.total_spent = 0.0
        self.transactions = []

        self.setup_ui()

    def setup_ui(self):
        """Creates the layout of the application."""
        
        # 1. Setup Section (Budget & Tax)
        setup_frame = ttk.LabelFrame(self.root, text="Initial Setup", padding=10)
        setup_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(setup_frame, text="Weekly Budget: $").grid(row=0, column=0, sticky="w")
        self.budget_entry = ttk.Entry(setup_frame)
        self.budget_entry.grid(row=0, column=1, pady=2)

        ttk.Label(setup_frame, text="Tax Rate (e.g. 0.07):").grid(row=1, column=0, sticky="w")
        self.tax_entry = ttk.Entry(setup_frame)
        self.tax_entry.grid(row=1, column=1, pady=2)

        self.set_btn = ttk.Button(setup_frame, text="Initialize Budget", command=self.initialize_budget)
        self.set_btn.grid(row=2, column=0, columnspan=2, pady=5)

        # 2. Add Item Section
        item_frame = ttk.LabelFrame(self.root, text="Add Transaction", padding=10)
        item_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(item_frame, text="Item Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(item_frame)
        self.name_entry.grid(row=0, column=1, pady=2)

        ttk.Label(item_frame, text="Price per Item: $").grid(row=1, column=0, sticky="w")
        self.price_entry = ttk.Entry(item_frame)
        self.price_entry.grid(row=1, column=1, pady=2)

        ttk.Label(item_frame, text="Quantity:").grid(row=2, column=0, sticky="w")
        self.qty_entry = ttk.Entry(item_frame)
        self.qty_entry.grid(row=2, column=1, pady=2)

        self.add_btn = ttk.Button(item_frame, text="Add Item", command=self.add_item, state="disabled")
        self.add_btn.grid(row=3, column=0, columnspan=2, pady=5)

        # 3. Summary Section (Display Area)
        summary_frame = ttk.LabelFrame(self.root, text="Weekly Transaction Log", padding=10)
        summary_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log_display = tk.Text(summary_frame, height=10, state="disabled", font=("Courier", 9))
        self.log_display.pack(fill="both", expand=True)

        # 4. Status Bar
        self.status_var = tk.StringVar(value="Please initialize budget to start.")
        self.status_label = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        self.status_label.pack(side="bottom", fill="x")

    def initialize_budget(self):
        try:
            self.weekly_budget = float(self.budget_entry.get())
            self.tax_rate = float(self.tax_entry.get())
            self.add_btn.config(state="normal")
            self.update_status()
            messagebox.showinfo("Success", "Budget values set successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for budget and tax.")

    def add_item(self):
        try:
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.qty_entry.get())
            
            if not name:
                raise ValueError("Name cannot be empty")

            # Calculations
            subtotal = price * quantity
            tax_amount = subtotal * self.tax_rate
            item_total = subtotal + tax_amount

            # Budget Check
            if (self.total_spent + item_total) > self.weekly_budget:
                over_by = (self.total_spent + item_total) - self.weekly_budget
                proceed = messagebox.askyesno("Alert", f"This exceeds budget by ${over_by:.2f}. Proceed?")
                if not proceed:
                    return

            # Store Transaction
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.transactions.append(f"[{timestamp}] {name}: ${item_total:.2f}")
            self.total_spent += item_total
            
            self.update_log()
            self.update_status()
            self.clear_item_entries()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Check price, quantity, and item name.")

    def update_log(self):
        self.log_display.config(state="normal")
        self.log_display.delete('1.0', tk.END)
        for t in self.transactions:
            self.log_display.insert(tk.END, t + "\n")
        self.log_display.config(state="disabled")

    def update_status(self):
        remaining = self.weekly_budget - self.total_spent
        status_text = f"Total Spent: ${self.total_spent:.2f} | Remaining: ${remaining:.2f}"
        self.status_var.set(status_text)

    def clear_item_entries(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)

def display_results(weekly_budget=None, tax_rate=None, items=None, current_day=None):
    """
    This keeps compatibility with your main.py file. 
    It launches the GUI.
    """
    root = tk.Tk()
    app = BudgetAppGUI(root)
    
    # If data is passed from collect_user_data, pre-fill it
    if weekly_budget is not None:
        app.budget_entry.insert(0, str(weekly_budget))
        app.tax_entry.insert(0, str(tax_rate))
        app.initialize_budget()
    
    root.mainloop()

if __name__ == "__main__":
    display_results()
