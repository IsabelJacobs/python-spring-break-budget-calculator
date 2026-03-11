# SpringBreak Shopping/Souvenirs Calculator
# Fuel Cost Calculator for a Spring Break Trip using OOP

class FuelCostCalculator:
    def __init__(self):
        self.destination_mileage = 0.0
        self.fuel_efficiency = 0.0
        self.fuel_price_per_gallon = 0.0
        self.total_fuel_needed = 0.0
        self.total_fuel_cost = 0.0

    def get_destination_mileage(self):
        # Input destination mileage
        while True:
            try:
                self.destination_mileage = float(input("Enter your destination mileage (in miles): "))
                if self.destination_mileage <= 0:
                    print("Mileage must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the mileage.")

    def get_fuel_efficiency(self):
        # Input fuel efficiency
        while True:
            try:
                self.fuel_efficiency = float(input("Enter your vehicle's fuel efficiency (mpg): "))
                if self.fuel_efficiency <= 0:
                    print("Fuel efficiency must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for fuel efficiency.")

    def get_fuel_price_per_gallon(self):
        # Input fuel price per gallon
        while True:
            try:
                self.fuel_price_per_gallon = float(input("Enter the fuel price per gallon: $"))
                if self.fuel_price_per_gallon <= 0:
                    print("Fuel price must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the fuel price.")

    def calculate_total_fuel_needed(self):
        # Calculate total fuel needed for the trip
        if self.destination_mileage > 0 and self.fuel_efficiency > 0:
            self.total_fuel_needed = self.destination_mileage / self.fuel_efficiency
            print(f"Total fuel needed for the trip: {self.total_fuel_needed:.2f} gallons")
        else:
            print("Invalid input data for calculation.")

    def calculate_total_fuel_cost(self):
        # Calculate total fuel cost
        if self.total_fuel_needed > 0 and self.fuel_price_per_gallon > 0:
            self.total_fuel_cost = self.total_fuel_needed * self.fuel_price_per_gallon
            print(f"Total fuel cost for the trip: ${self.total_fuel_cost:.2f}")
        else:
            print("Invalid input data for calculation.")

    def display_fuel_cost_summary(self):
        # Display the fuel cost summary
        print("\nFuel Cost Summary:")
        print(f"Destination Mileage: {self.destination_mileage} miles")
        print(f"Fuel Efficiency: {self.fuel_efficiency} mpg")
        print(f"Fuel Price per Gallon: ${self.fuel_price_per_gallon:.2f}")
        print(f"Total Fuel Needed: {self.total_fuel_needed:.2f} gallons")
        print(f"Total Fuel Cost: ${self.total_fuel_cost:.2f}")

    def run(self):
        print("Welcome to the Spring Break Trip Fuel Cost Calculator!")
        self.get_destination_mileage()
        self.get_fuel_efficiency()
        self.get_fuel_price_per_gallon()
        self.calculate_total_fuel_needed()
        self.calculate_total_fuel_cost()
        self.display_fuel_cost_summary()


# Create an instance of the FuelCostCalculator and run it
if __name__ == "__main__":
    calculator = FuelCostCalculator()
    calculator.run()
