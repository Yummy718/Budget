import tkinter as tk
from datetime import datetime
from tkinter import messagebox

# ---------------- LOGIC ----------------

def get_current_day():
    return datetime.now().strftime("%A")

def apply_weekly_allowance(budget, allowance, allowance_day, current_day):
    if allowance_day.lower() == current_day.lower():
        return budget + allowance
    return budget

# ---------------- GUI FUNCTIONS ----------------

items = []

def add_item():
    try:
        name = entry_item_name.get().strip()
        price_val = float(entry_item_price.get())
        qty_val = int(entry_item_quantity.get())

        if not name:
            messagebox.showwarning("Input Error", "Please name the item.")
            return

        cost = price_val * qty_val
        items.append({"name": name, "qty": qty_val, "total": cost})
        
        # Receipt-style alignment in listbox
        listbox_items.insert(tk.END, f" {qty_val:02d}x  {name.upper():<15} ${cost:>8.2f}")

        # Clear entries
        entry_item_name.delete(0, tk.END)
        entry_item_price.delete(0, tk.END)
        entry_item_quantity.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers for Price and Quantity.")

def update_ui():
    try:
        budget = float(entry_budget.get() or 0)
        allowance = float(entry_allowance.get() or 0)
        day = entry_allowance_day.get().strip()
        tax_rate = float(entry_tax.get() or 0)

        total_budget = apply_weekly_allowance(budget, allowance, day, get_current_day())
        
        subtotal = sum(i['total'] for i in items)
        calculated_tax = subtotal * tax_rate
        final_total = subtotal + calculated_tax
        remaining = total_budget - final_total

        lbl_tax_amt.config(text=f"Tax Amount: ${calculated_tax:.2f}")
        lbl_spent.config(text=f"Total Expenses: ${final_total:.2f}")
        lbl_bal.config(text=f"Balance: ${remaining:.2f}")

        if remaining >= 0:
            lbl_status.config(text="✅ ON TRACK", fg="#27AE60")
            lbl_bal.config(fg="#27AE60")
        else:
            lbl_status.config(text="❌ LIMIT EXCEEDED", fg="#E74C3C")
            lbl_bal.config(fg="#E74C3C")

    except ValueError:
        messagebox.showerror("Math Error", "Check your budget and tax settings.")

def reset():
    items.clear()
    listbox_items.delete(0, tk.END)
    lbl_tax_amt.config(text="Tax Amount: $0.00")
    lbl_spent.config(text="Total Expenses: $0.00")
    lbl_bal.config(text="Balance: $0.00", fg="#95A5A6")
    lbl_status.config(text="READY", fg="#95A5A6")

# ---------------- STYLING ----------------

CLR_BG = "#FDFEFE"
CLR_SIDEBAR = "#F2F4F4"
CLR_PRIMARY = "#5D6D7E"
CLR_ACCENT = "#58D68D"
CLR_TEXT = "#2E4053"
CLR_CORAL = "#F1948A"

root = tk.Tk()
root.title("Designer Budget Tracker")
root.geometry("720x480") 
root.configure(bg=CLR_BG)

FONT_BOLD = ("Verdana", 9, "bold")
FONT_MAIN = ("Verdana", 10)
FONT_LARGE = ("Verdana", 13, "bold")
FONT_LIST = ("Consolas", 10)

# LEFT PANEL
left_p = tk.Frame(root, bg=CLR_SIDEBAR, padx=25, pady=20)
left_p.pack(side="left", fill="both", expand=True)

def draw_input(label, default=""):
    tk.Label(left_p, text=label, font=FONT_BOLD, bg=CLR_SIDEBAR, fg=CLR_PRIMARY).pack(anchor="w")
    e = tk.Entry(left_p, font=FONT_MAIN, bg="white", fg=CLR_TEXT, bd=0, highlightthickness=1, highlightbackground="#D5DBDB")
    e.insert(0, default)
    e.pack(fill="x", pady=(0, 10), ipady=4)
    return e

tk.Label(left_p, text="PLANNER", font=FONT_LARGE, bg=CLR_SIDEBAR, fg=CLR_PRIMARY).pack(anchor="w", pady=(0,10))
entry_budget = draw_input("WEEKLY BUDGET ($)")
entry_allowance = draw_input("WEEKLY ALLOWANCE ($)")
entry_allowance_day = draw_input("ALLOWANCE DAY")
entry_tax = draw_input("TAX RATE (e.g. 0.07)", "0.00")

tk.Frame(left_p, height=2, bg="#D5DBDB").pack(fill="x", pady=10)

# ITEM SECTION
tk.Label(left_p, text="NEW ITEM NAME", font=FONT_BOLD, bg=CLR_SIDEBAR, fg=CLR_PRIMARY).pack(anchor="w")
entry_item_name = tk.Entry(left_p, font=FONT_MAIN, bd=0, highlightthickness=1, highlightbackground="#D5DBDB")
entry_item_name.pack(fill="x", pady=(2, 10), ipady=4)

# Multi-column frame for Price and Qty labels + boxes
item_details_frame = tk.Frame(left_p, bg=CLR_SIDEBAR)
item_details_frame.pack(fill="x")

# Price Column
tk.Label(item_details_frame, text="PRICE ($)", font=FONT_BOLD, bg=CLR_SIDEBAR, fg=CLR_PRIMARY).grid(row=0, column=0, sticky="w")
entry_item_price = tk.Entry(item_details_frame, width=12, font=FONT_MAIN, bd=0, highlightthickness=1, highlightbackground="#D5DBDB")
entry_item_price.grid(row=1, column=0, pady=(2, 0), ipady=4)

# Quantity Column
tk.Label(item_details_frame, text="QUANTITY", font=FONT_BOLD, bg=CLR_SIDEBAR, fg=CLR_PRIMARY).grid(row=0, column=1, sticky="w", padx=(15, 0))
entry_item_quantity = tk.Entry(item_details_frame, width=12, font=FONT_MAIN, bd=0, highlightthickness=1, highlightbackground="#D5DBDB")
entry_item_quantity.grid(row=1, column=1, padx=(15, 0), pady=(2, 0), ipady=4)

# RIGHT PANEL
right_p = tk.Frame(root, bg=CLR_BG, padx=20, pady=20)
right_p.pack(side="right", fill="both", expand=True)

tk.Button(right_p, text="ADD ITEM", bg=CLR_ACCENT, fg="white", font=FONT_BOLD, bd=0, cursor="hand2", command=add_item).pack(fill="x", ipady=6)

listbox_items = tk.Listbox(right_p, bg="#FBFCFC", fg=CLR_TEXT, borderwidth=0, font=FONT_LIST, height=6, highlightthickness=1, highlightbackground="#EBEDEF")
listbox_items.pack(fill="x", pady=15)

tk.Button(right_p, text="CALCULATE", bg=CLR_PRIMARY, fg="white", font=FONT_BOLD, bd=0, cursor="hand2", command=update_ui).pack(fill="x", ipady=8)

# SUMMARY AREA
summary_f = tk.Frame(right_p, bg=CLR_SIDEBAR, pady=12)
summary_f.pack(fill="x", pady=10)

lbl_status = tk.Label(summary_f, text="READY", font=FONT_LARGE, bg=CLR_SIDEBAR, fg="#95A5A6")
lbl_status.pack()

lbl_tax_amt = tk.Label(summary_f, text="Tax Amount: $0.00", font=FONT_MAIN, bg=CLR_SIDEBAR, fg=CLR_TEXT)
lbl_tax_amt.pack()

lbl_spent = tk.Label(summary_f, text="Total Expenses: $0.00", font=FONT_MAIN, bg=CLR_SIDEBAR, fg=CLR_TEXT)
lbl_spent.pack()

lbl_bal = tk.Label(summary_f, text="Balance: $0.00", font=FONT_LARGE, bg=CLR_SIDEBAR, fg=CLR_TEXT)
lbl_bal.pack()

tk.Button(right_p, text="RESET ALL DATA", bg=CLR_BG, fg=CLR_CORAL, font=FONT_BOLD, bd=0, command=reset).pack(pady=5)

root.mainloop()