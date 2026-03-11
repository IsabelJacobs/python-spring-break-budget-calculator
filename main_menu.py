from hotel_calculator import HotelCostCalculator
from food_calculator import FoodBudgetCalculator
from shopping_calculator import ShoppingBudgetCalculator
from transport_calculator import TransportCostCalculator
from fuel_calculator import FuelCostCalculator
from activity_calculator import ActivityBudgetCalculator

class Menu:

    def display_menu(self):
        menu = 0

        while menu < 7:  # Change to 7 since you're checking for this option
            print("Welcome to the Spring Break Calculator!")
            print("---------MAIN MENU--------")
            print("1. Hotel Calculator\n2. Food Budget Calculator\n3. Shopping Budget Calculator\n4. Transportation Calculator\n5. Fuel Cost Calculator\n6. Activity Budget Calculator\n7. Quit")
        
            try:
                menu = int(input("Select a menu option: "))
                
                # Create instances of each calculator class
                if menu == 1:
                    hotel_calculator = HotelCostCalculator()
                    hotel_calculator.run()  
                elif menu == 2:
                    food_calculator = FoodBudgetCalculator()
                    food_calculator.run()  
                elif menu == 3:
                    shopping_calculator = ShoppingBudgetCalculator()
                    shopping_calculator.run()  
                elif menu == 4:
                    transport_calculator = TransportCostCalculator()
                    transport_calculator.run()  
                elif menu == 5:
                    fuel_calculator = FuelCostCalculator()
                    fuel_calculator.run()  
                elif menu == 6:
                    activity_calculator = ActivityBudgetCalculator()
                    activity_calculator.run()  
                elif menu == 7:
                    print("Thank you for using Spring Break Calculator")
                else:
                    print("Invalid input, please enter a number from 1-7")
                    menu = 0

            except ValueError:
                print("Invalid input. Please enter a valid integer menu selection.\n")

if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()  # Call the display_menu method to start the menu