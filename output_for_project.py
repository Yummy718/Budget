import tkinter as tk
from budget import (
    calculate_item_totals,
    calculate_total_with_tax,
    calculate_remaining_budget,
    calculate_carry_over
)

def display_results(parent, budget, tax_rate, items, day):
    window = tk.Toplevel(parent)
    window.title("Budget Summary")

    items, subtotal = calculate_item_totals(items)
    tax, total = calculate_total_with_tax(subtotal, tax_rate)
    remaining, within = calculate_remaining_budget(budget, total)
    carry = calculate_carry_over(remaining)

    # ===== Summary =====
    summary_text = (
        f"Day: {day}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"Tax: ${tax:.2f}\n"
        f"Total: ${total:.2f}\n"
        f"Remaining: ${remaining:.2f}\n"
        f"Carry Over: ${carry:.2f}\n"
        f"Status: {'Within Budget' if within else 'Over Budget'}"
    )

    tk.Label(window, text=summary_text, justify="left").pack(pady=5)

    # ===== Item List =====
    tk.Label(window, text="Items Purchased").pack()

    listbox = tk.Listbox(window, width=55)
    listbox.pack(padx=10, pady=5)

    for item in items:
        listbox.insert(
            tk.END,
            f"{item['name']} - ${item['price']:.2f} x {item['quantity']} "
            f"= ${item['total_price']:.2f}"
        )
