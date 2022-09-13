from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():

    current_bill = 0
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ") .lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            show_taxi(TAXIS)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice > len(TAXIS) - 1:
                print("Invalid choice!")
            else:
                current_taxi = TAXIS[taxi_choice]

        elif choice == "d":
            if current_taxi == None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} cost you {cost}")
                total_bill += cost

        else:
            print("Invalid option!")
        print(f"Bill to date: {total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    show_taxi(TAXIS)



def show_taxi(TAXIS):
    for i, taxi in enumerate(TAXIS):
        print(f"{i} - {taxi}")

main()