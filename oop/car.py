from vehicle import Vehicle


class Car(Vehicle):
    def brag(self):
        print('Look how cool my car is!')


car1 = Car()
car1.drive()
print(car1)
car1.add_warning('New warning')
car1.get_warnings()

car2 = Car(200)
car2.drive()
car2.get_warnings()

car3 = Car(300)
car3.drive()
car2.get_warnings()
