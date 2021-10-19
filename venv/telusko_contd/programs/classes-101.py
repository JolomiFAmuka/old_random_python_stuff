
# INNER Class tutorial

class Student:
    def __init__(self, name, matno) -> None:
        self.name = name
        self.matno = matno
        self.lap = self.Laptop()

    def show(self):
        return f"{self.name}; {self.matno}"

    class Laptop: #create an inner class
        def __init__(self) -> None:
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16

jim = Student("Jimmi Jatt", 9002021) # instantiate outer class

print(jim.show()) # call method in outer class

print(jim.lap.brand) # call the inner class

print()

lap1 = jim.lap # alternate call to the inner class object
lap2 = jim.Laptop()


print(lap1)
print(lap1.cpu)

print('lap2',lap2)
print(lap2.cpu)