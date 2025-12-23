import tkinter as tk
from budgeting_helper_app import InputGUI
from output_for_project import display_results

def main():
    root = tk.Tk()
    app = InputGUI(root)
    root.mainloop()

    if not app.finished:
        return

    display_root = tk.Tk()
    display_root.withdraw()

    budget, tax, items, day = app.collect_user_data()
    display_results(display_root, budget, tax, items, day)

    display_root.mainloop()

if __name__ == "__main__":
    main()
