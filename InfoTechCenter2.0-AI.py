import random
from time import sleep


def gas_level_alert():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    gas_level = random.choice(gas_level_list)

    gas_stations = ["Shell", "Speedway", "Kum And Go", "Circle K", "Mobil", "Costco", "Meijer", "7Eleven"]
    nearest_gas_station = random.choice(gas_stations)

    miles_to_gas_station_low = round(random.uniform(1, 25), 1)
    miles_to_gas_station_quarter_tank = round(random.uniform(25.1, 50), 1)

    if gas_level == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY ***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gas_level in ("Low", "Quarter Tank"):
        print(f"Your gas tank is {gas_level.lower()}, checking Google Maps for the nearest gas station.")
        sleep(2.5)
        print(f"The closest gas station is {nearest_gas_station}, which is {miles_to_gas_station_low} miles away.")
    elif gas_level == "Half Tank":
        print("Your gas tank is halfway full, which is plenty to get where you need to go.")
    elif gas_level == "Three Quarter Tank":
        print("Your gas tank is three quarters full.")
    else:
        print("Full tank, nice.")


gas_level_alert()
