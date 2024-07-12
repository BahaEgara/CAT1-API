class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"{super().__str__()}, Number of Seats: {self.number_of_seats}"


class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return f"{super().__str__()}, Cargo Capacity: {self.cargo_capacity} kg"


class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def __str__(self):
        return f"{super().__str__()}, Engine Capacity: {self.engine_capacity} cc"


class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.registration_number} added successfully.")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(vehicle)

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number.lower() == registration_number.lower():
                print(f"Vehicle found: {vehicle}")
                return
        print(f"No vehicle found with the registration number {registration_number}.")


def main():
    fleet = Fleet()

    while True:
        print("\nTransport Fleet Management System")
        print("1. Add a new vehicle")
        print("2. Display all vehicles")
        print("3. Search for a vehicle by registration number")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            type_of_vehicle = input("Enter type of vehicle (car/truck/motorcycle): ").lower()
            registration_number = input("Enter registration number: ")
            make = input("Enter make: ")
            model = input("Enter model: ")

            if type_of_vehicle == 'car':
                number_of_seats = int(input("Enter number of seats: "))
                vehicle = Car(registration_number, make, model, number_of_seats)
            elif type_of_vehicle == 'truck':
                cargo_capacity = int(input("Enter cargo capacity in kg: "))
                vehicle = Truck(registration_number, make, model, cargo_capacity)
            elif type_of_vehicle == 'motorcycle':
                engine_capacity = int(input("Enter engine capacity in cc: "))
                vehicle = Motorcycle(registration_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type. Please try again.")
                continue

            fleet.add_vehicle(vehicle)
        elif choice == '2':
            fleet.display_vehicles()
        elif choice == '3':
            registration_number = input("Enter the registration number to search: ")
            fleet.search_vehicle(registration_number)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
