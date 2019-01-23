from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.__passengers = []

    def get_passengers(self):
        print(self.__passengers)

    def add_passengers(self, passengers):
        self.__passengers.extend(passengers)


bus1 = Bus(150)
bus1.add_warning('Bus Warning')
bus1.add_passengers(['Calvin', 'Max', 'Kevin'])
bus1.get_passengers()
bus1.drive()
