#Spring Break Trip Hotel Cost Calculator
#Calculate the total tranpsortation cost per perosn 

class HotelCostCalculator:
    def __init__(self):
        self.num_travelers = 0
        self.rental_cost = 0.0
        self.rental_nights = 0

    def get_user_input(self):
        print("Welcome to the Spring Break Trip Hotel Cost Calculator!")
        try:
            self.num_travelers = int(input("Enter the number of travelers: "))
            self.rental_cost = float(input("Enter the cost of the hotel or house rental per night: $"))
            self.rental_nights = int(input("Enter the number of nights of the stay: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return False
        return True

    def calculate_costs(self):
        total_hotel_cost = self.rental_cost * self.rental_nights
        per_person_hotel_cost = total_hotel_cost / self.num_travelers
        return total_hotel_cost, per_person_hotel_cost

    def display_results(self, costs):
        total_hotel_cost, per_person_hotel_cost = costs
        print("\n--- Accommodation Cost Summary ---")
        print(f"Total accommodation cost for the trip: ${total_hotel_cost:.2f}")
        print(f"Total cost per person: ${per_person_hotel_cost:.2f}")

    def run(self):
        if self.get_user_input():
            costs = self.calculate_costs()
            self.display_results(costs)


if __name__ == "__main__":
    calculator = HotelCostCalculator()
    calculator.run()

