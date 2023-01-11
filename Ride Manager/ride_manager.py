class RideManager : 
    def __init__(self) -> None:
        print('Ride manager activated') 
        self.__income = 0
        self.__trip_history = []
        self.__avialable_cars = []
        self.__avialable_cng = []
        self.__avialable_bikes = []

    def add_a_vehicle(self, vehicle_type, vehicle) : 
        if vehicle_type == 'car' : 
            self.__avialable_cars.append(vehicle) 
        elif vehicle_type == 'bike' : 
            self.__avialable_bikes.append(vehicle)
        else : 
            self.__avialable_cng.append(vehicle) 

    def get_avilable_cars(self) : 
        return self.__avialable_cars

    def total_income(self) : 
        return self.__income
    
    def trip_history(self) : 
        return self.__trip_history

    def find_a_vehicle(self, rider, vehicle_type, destination) : 
        if vehicle_type == 'car' : 
            vehicles = self.__avialable_cars
        elif vehicle_type == 'bike' : 
            vehicles = self.__avialable_bikes
        else : 
            vehicles = self.__avialable_cng

            if len(vehicles) == 0 :
                print(f'Sorry, no {vehicle_type} is available')  
                return False 
            for vehicle in vehicles : 
                # print('potential', rider.location, vehicle.driver.location)
                if abs(rider.location - vehicle.driver.location) < 10 : 
                    distance = abs(rider.location - destination)
                    fare = distance * vehicle.rate
                    if rider.balance < fare : 
                        print('You do not have enough money for this trip', fare, rider.balance)
                        return False
                    if vehicle.status == 'available' : 
                        vehicle.status = 'unavailable'
                        trip_info = f'Match {vehicle_type} for {rider.name} for fare :  {fare} with {vehicle.driver.name} started : {rider.location} to : {destination}'
                        print(trip_info)
                        self.__trip_history.append(trip_info)
                        vehicles.remove(vehicle)
                        rider.start_a_trip(fare, trip_info)
                        vehicle.driver.start_a_trip(rider.location, destination, fare * 0.8, trip_info)
                        self.__income += fare * 0.2

                        return True 


    
uber = RideManager()