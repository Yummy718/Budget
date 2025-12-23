from budgeting_helper_app import collect_user_data
from output_for_project import display_results

def main():
    weekly_budget, tax_rate, items, current_day = collect_user_data()
    display_results(weekly_budget, tax_rate, items, current_day)

if __name__ == "__main__":
    main()
