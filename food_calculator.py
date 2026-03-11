#Spring Break FoodBudgetCalculator
#Calculate budget per meal based on number of days

class FoodBudgetCalculator:  
    def __init__(self, total_budget=0, days=0):  # Provide default values
        self.total_budget = total_budget
        self.days = days
        self.meals_per_day = 3
        self.total_meals = days * self.meals_per_day if days > 0 else 0  # Avoid division by zero

    def budget_per_meal(self):
        if self.total_meals > 0:
            return self.total_budget / self.total_meals
        return 0  # Return 0 if no meals to avoid division by zero

    def display_summary(self):
        print("\nFood Budget Summary:")
        print(f"Total Budget: ${self.total_budget:.2f}")
        print(f"Budget per Meal: ${self.budget_per_meal():.2f}")

    def run(self):
        try:
            total_budget = float(input("Enter your total food budget for the trip: "))
            days = int(input("Enter the number of days: "))
            
            # Re-initialize with user input
            self.total_budget = total_budget
            self.days = days
            self.total_meals = days * self.meals_per_day if days > 0 else 0  # Update total meals

            self.display_summary()

        except ValueError:
            print("Invalid input. Please enter numeric values for budget and days.")


if __name__ == "__main__":
    calculator = FoodBudgetCalculator()  # No arguments needed now
    calculator.run()  # Call the run method