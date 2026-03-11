# SpringBreak Shopping/Souvenirs Calculator
# Calculate Shopping/Souvenirs Budget for SpringBreak Trip using OOP

class ShoppingBudgetCalculator:
    def __init__(self):
        self.total_budget = 0.0
        self.num_categories = 0
        self.category_budgets = []

    def get_total_budget(self):
        # Input Total Budget
        while True:
            try:
                self.total_budget = float(input("Enter your total shopping budget: $"))
                if self.total_budget < 0:
                    print("The total shopping budget must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the total budget.")

    def get_num_categories(self):
        # Input number of shopping categories
        while True:
            try:
                self.num_categories = int(input("Enter the number of shopping categories (e.g., clothes, souvenirs): "))
                if self.num_categories <= 0:
                    print("The number of categories must be a positive integer. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer value for the number of categories.")

    def allocate_budget_per_category(self):
        # Allocate budget per category
        for i in range(self.num_categories):
            while True:
                category_name = input(f"Enter the name of category {i + 1}: ").strip()
                if category_name:
                    break
                else:
                    print("Category name cannot be empty. Please try again.")

            while True:
                try:
                    budget = float(input(f"Enter the allocated budget for {category_name}: $"))
                    if budget < 0:
                        print("The budget must be a positive number. Please try again.")
                    else:
                        self.category_budgets.append((category_name, budget))
                        break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the budget.")

    def calculate_total_allocated_budget(self):
        # Calculate Total Allocated Budget
        return sum(budget for _, budget in self.category_budgets)

    def display_budget_summary(self, total_allocated_budget):
        # Compare Allocated Budget with Total Budget
        if total_allocated_budget <= self.total_budget:
            print("\nShopping/Souvenir Budget Allocation:")
            for category, budget in self.category_budgets:
                print(f"Category: {category}, Budget: ${budget:.2f}")
            print(f"Total Allocated Budget: ${total_allocated_budget:.2f}")
            print(f"Remaining Budget: ${self.total_budget - total_allocated_budget:.2f}")
        else:
            print("\nWarning: You are over budget!")
            print(f"Total Allocated Budget: ${total_allocated_budget:.2f}")
            print(f"Exceeded Budget by: ${total_allocated_budget - self.total_budget:.2f}")

    def run(self):
        print("Welcome to the SpringBreak Shopping/Souvenirs Budget Calculator!")
        self.get_total_budget()
        self.get_num_categories()
        self.allocate_budget_per_category()
        total_allocated_budget = self.calculate_total_allocated_budget()
        self.display_budget_summary(total_allocated_budget)

# Create an instance of the ShoppingBudgetCalculator and run it
if __name__ == "__main__":
    calculator = ShoppingBudgetCalculator()
    calculator.run()
