#Spring Break Transportation Calculator
#Calculates the total per person cost of tranpsortation for a spring break trip

class TransportCostCalculator:
    def __init__(self):
        self.num_travelers = 0
        self.plane_ticket_cost = 0.0
        self.rental_car_cost_per_day = 0.0
        self.rental_days = 0

    def get_user_input(self):
        print("Welcome to the Spring Break Trip Cost Calculator!")
        try:
            self.num_travelers = int(input("Enter the number of travelers: "))
            self.plane_ticket_cost = float(input("Enter the cost of the plane ticket (per traveler): $"))
            self.rental_car_cost_per_day = float(input("Enter the daily cost of the car rental: $"))
            self.rental_days = int(input("Enter the number of days the car will be rented: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return False
        return True

    def calculate_costs(self):
        total_plane_ticket_cost = self.num_travelers * self.plane_ticket_cost
        total_car_rental_cost = self.rental_car_cost_per_day * self.rental_days
        total_transportation_cost = total_plane_ticket_cost + total_car_rental_cost

        per_person_car_rental_cost = total_car_rental_cost / self.num_travelers
        per_person_total_cost = total_transportation_cost / self.num_travelers

        return (total_plane_ticket_cost, total_car_rental_cost, per_person_car_rental_cost, per_person_total_cost)

    def display_results(self, costs):
        total_plane_ticket_cost, total_car_rental_cost, per_person_car_rental_cost, per_person_total_cost = costs
        print("\n--- Transportation Cost Summary ---")
        print(f"Total cost for plane tickets: ${total_plane_ticket_cost:.2f}")
        print(f"Total cost for car rental: ${total_car_rental_cost:.2f}")
        print(f"Cost per person for car rental: ${per_person_car_rental_cost:.2f}")
        print(f"Total cost per person: ${per_person_total_cost:.2f}")

    def run(self):
        if self.get_user_input():
            costs = self.calculate_costs()
            self.display_results(costs)


if __name__ == "__main__":
    calculator = TransportCostCalculator()
    calculator.run()
