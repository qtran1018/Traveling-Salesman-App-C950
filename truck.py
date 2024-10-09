class truck:
    def __init__(self, truck_number, miles_traveled, departure_time, current_address, package_list):
        self.truck_number = truck_number
        self.miles_traveled = miles_traveled
        self.departure_time = departure_time
        self.current_address = current_address
        self.package_list = package_list
        self.return_time = None

    #TODO - maybe don't need a setter, change the var directly.
    def set_departure_time(self, value):
        if isinstance(value, int):
            self.departure_time = value
        else:
            raise ValueError("Value must be an integer.")