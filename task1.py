class Person:
    def __init__(self, fullname, age, city, plane, sit_number) -> None:
        self.fullname = fullname
        self.age = age
        self.city = city
        self.plane = plane
        self.sit_number = sit_number

class Airport:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
    @staticmethod
    def check(person : Person):
        if person.fullname == input("Your fullname: "):
            if person.age == int(input("Your age: ")):
                if person.city == input("Your destination: "):
                    if person.plane == input("Plane: "):
                        if person.sit_number == int(input("Sit number: ")):
                            return 'Enjoy your flight'
                        else:
                            return "Mistake (sit number)"
                    else:
                        return "Mistake (plane)"
                else: 
                    return "Mistake (destination)"
            else:
                return "Mistake (age)"
        else:
            return "Mistake (fullname)"        

a1 = Airport("Turkish airlines", "Istanbul")
p1 = Person("Yunusjonov Shavkatjon", 16, "Amsterdam", "AS528", 25)
print(a1.check(p1))