from prac_08.taxi import Taxi

taxi = Taxi("Prius 1", 100, 1.23)
taxi.drive(40)
print(f"{taxi}, current fare: {taxi.get_fare()}")
taxi.start_fare()
taxi.drive(100)
print(f"{taxi}, current fare: {taxi.get_fare()}")




