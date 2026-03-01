class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    name: str
    age: int
    sex: str

    def speak(self):
        print(f"{self.name} is speaking")


person_1 = Human("John", 33, "male")
# person_1.speak()


class Child(Human):
    is_schooler: bool


child_1 = Child("Bobby", 12, "male")
child_2 = Child("Mary", 8, "female")
child_3 = Child("Peter", 10, "male")
child_1.seat = 4

# child_1.speak()


class Bus:
    def __init__(self):
        self.passengers = []

    def add_passengers(self, passenger):
        self.passengers.append(passenger)

    def del_passengers(self, pas_name):

        for i in range(len(self.passengers)):
            if self.passengers[i].name == pas_name:
                self.passengers.pop(i)
                return

    def change_seat(self, name, seat_number):
        for passenger in self.passengers:
            if passenger.name == name and hasattr(passenger, "seat"):
                passenger.seat = seat_number

    def get_passengers_count(self):
        return len(self.passengers)


big_yellow_bus = Bus()
big_yellow_bus.add_passengers(child_2)
big_yellow_bus.add_passengers(child_1)
big_yellow_bus.add_passengers(child_3)

# for passenger in big_yellow_bus.passengers:
#     print(passenger.name)

print(big_yellow_bus.get_passengers_count())
big_yellow_bus.del_passengers("Peter")

# for passenger in big_yellow_bus.passengers:
#     print(passenger.name)

# print(vars(child_1))

# print(child_1.__dict__)
big_yellow_bus.change_seat(child_1.name, 7)
# print(child_1.__dict__)
print(big_yellow_bus.get_passengers_count())
