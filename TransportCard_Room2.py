#The transport system card class where user can top up and get card information
from turtle import distance
from abc import ABC, abstractmethod

class Transport_Card(ABC):
    def __init__(self, passenger_name, card_id, current_balance):
        self.passenger_name = passenger_name
        self.card_id = card_id
        self.__current_balance = current_balance
    def top_up(self,amount):
        #adding money to the transport card
        if amount > 0:
            self.__current_balance += amount
            print(f"top up {amount}, new balance = {self.__current_balance}")
        else:
            print("top up must be positive")
    def deduct(self, amount):
        if amount <= self.__current_balance:
            self.__current_balance -= amount
            return True
        else:
            return False
    def get_balance(self):
        return self.__current_balance
    def get_card_info(self):
        #returning the card information
        return f"Passenger Name: {self.passenger_name}, Card ID: {self.card_id}, Current Balance: {self.__current_balance}"
class Passenger:
    def __init__(self, passenger_name, passenger_id, passenger_type):
        self.passenger_name = passenger_name
        self.passenger_id = passenger_id
        self.passenger_type = passenger_type
        self.transport_card = None
    
    def assign_transport_card(self, card):
        #assigning a transport card to the passenger
        self.transport_card = card

    def travel(self, fare_calculator, distance, transport_type):
        # we determine what happens to passenger without a transport card
        if self.transport_card is None:
            print(f"{self.passenger_name} does not have a transport card and cannot travel.")
            return
        fare = fare_calculator.calculate_fare(self.passenger_type, distance, transport_type)
        #deduct fare from the transport card balance if passenger has a transport card
        if fare <= self.transport_card.__current_balance:
            self.transport_card.__current_balance -= fare #fare is deducted from the card balance
            print(f"{self.passenger_name} traveled {distance} km by {transport_type}. Fare: {fare}. Remaining Balance: {self.transport_card._Transport_Card__current_balance}")
        else:
            print(f"{self.passenger_name} has insufficient balance to travel {distance} km by {transport_type}. Fare: {fare}")

class FareCalculator(ABC):
    def calculate_fare(self, distance, passenger_type):
        pass
class busfare(FareCalculator):
    def calculate_fare(self, passenger_type, distance):
        base_fare_per_km = 40 # base fare per km for bus
        if passenger_type == "student":
            discount = 0.1 # 10% discount for students
        elif passenger_type == "senior":
            discount = 0.2 # 20% discount for seniors
        else:
            discount = 0.0 # no discount for regular passengers
        fare = base_fare_per_km * distance
        fare -= fare * discount
        return fare
class trainfare(FareCalculator):
    def calculate_fare(self, passenger_type, distance):
        basefare_per_km = 50 # base fare per km for train
        if passenger_type == "student":
            discount = 0.10 # 10% discount for students
        elif passenger_type == "senior":
            discount = 0.20 # 20% discount for seniors
        else:
            discount = 0.0 # no discount for regular passengers
        fare = basefare_per_km * distance
        fare -= fare * discount
        return fare 

from datetime import datetime, time
class FerryFare(FareCalculator):
    def is_peak_time(self, travel_time: datetime) -> bool:
        #Check if travel time falls within peak hours this supports the surcharge calculation
        morning_start = time(6, 0)
        morning_end   = time(9, 0)
        evening_start = time(16, 45)
        evening_end   = time(19, 30)

        current = travel_time.time()
        return (morning_start <= current <= morning_end) or (evening_start <= current <= evening_end)

    def frequent_traveler_discount(self, rides_count: int) -> float:
        """Return discount rate if passenger has more than 100 ferry rides."""
        return self.frequent_discount_rate if rides_count > 100 else 0.0

    def calculate_fare(self, passenger_type, rides_count=0, travel_time=None):
        basefare_for_ferry = 80 # base fare for ferry
        surcharge = 1.3 if travel_time and self.is_peak_time(travel_time) else 1.0 # 30% surcharge during peak hours
        if passenger_type == "student":
            discount = 0.10 # 10% discount for students
        elif passenger_type == "senior":
            discount = 0.20 # 20% discount for seniors
        elif passenger_type == "frequent":
            discount = 0.15 # 15% discount for frequent travelers
        else:
            discount = 0.0 # no discount for regular passengers
        fare: float = basefare_for_ferry * surcharge
        fare -= fare * discount
        return fare

#create transport cards
Taofikat_card = Transport_Card("TC100", "Taofikat", current_balance=500)
Lovelyn_card   = Transport_Card("TC200", "Lovelyn", current_balance=450)
Conny_card = Transport_Card("TC300", "Conny", current_balance=500)

# create passengers
Taofikat = Passenger("Taofikat", "P001", "student")
Lovelyn  = Passenger("Lovelyn", "P002", "senior")
Conny = Passenger("Conny", "P003", "frequent")

# Assign cards
Taofikat.assign_transport_card(Taofikat_card)
Lovelyn.assign_transport_card(Lovelyn_card)
Conny.assign_transport_card(Conny_card)

bus_fare = busfare()
train_fare = trainfare()
ferry_fare = FerryFare()

#Passengers traveling
fare1 = ferry_fare.calculate_fare("student", rides_count=20, travel_time=datetime(2026, 1, 20, 8, 0))
print(f"Taofikat fare (student, peak): {fare1}")
Taofikat_card.deduct(fare1)
print(Taofikat_card.get_card_info())

#fare2 = bus_fare.calculate_fare("student", distance=4)
#print(f"Taofikat fare (student, bus, 4 stops): {fare2}")
#Taofikat_card.deduct(fare2)
#print(Taofikat_card.get_card_info())








    
    