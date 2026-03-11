class ActivityBudgetCalculator:
    def __init__(self):
        self.sightseeing_budget = 0.0
        self.culinary_budget = 0.0
        self.adventurous_budget = 0.0
        self.sightseeing_activities = 0
        self.culinary_activities = 0
        self.adventurous_activities = 0

    def get_user_input(self):
        print("Welcome to the Activity Budget Calculator!")
        try:
            self.sightseeing_budget = float(input("Enter your total budget for Sightseeing activities: $"))
            self.sightseeing_activities = int(input("Enter the number of Sightseeing activities planned: "))
                         

            self.culinary_budget = float(input("Enter your total budget for Culinary activities: $"))
            self.culinary_activities = int(input("Enter the number of Culinary activities planned: "))
                            

            self.adventurous_budget = float(input("Enter your total budget for Adventurous activities: $"))
            self.adventurous_activities = int(input("Enter the number of Adventurous activities planned: "))
                            
        except ValueError as e:
            print(f"Invalid input: {e}")
            return False
        return True

    def calculate_budget_per_activity(self):
        budget_per_activity = {
            "Sightseeing": self.sightseeing_budget / self.sightseeing_activities,
            "Culinary": self.culinary_budget / self.culinary_activities,
            "Adventurous": self.adventurous_budget / self.adventurous_activities
        }
        return budget_per_activity

    def display_summary(self):
        budget_per_activity = self.calculate_budget_per_activity()
        print("\n--- Activity Budget Summary ---")
        print(f"Sightseeing: Total Budget: ${self.sightseeing_budget:.2f}, Budget per Activity: ${budget_per_activity['Sightseeing']:.2f}")
        print(f"Culinary: Total Budget: ${self.culinary_budget:.2f}, Budget per Activity: ${budget_per_activity['Culinary']:.2f}")
        print(f"Adventurous: Total Budget: ${self.adventurous_budget:.2f}, Budget per Activity: ${budget_per_activity['Adventurous']:.2f}")

    def run(self):
        if self.get_user_input():
            self.display_summary()


if __name__ == "__main__":
    calculator = ActivityBudgetCalculator()
    calculator.run()