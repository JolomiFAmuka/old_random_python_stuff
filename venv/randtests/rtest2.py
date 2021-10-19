from numpy import *

# arr = array([1,2,3,4,5])

# arr = linspace(0,16,10)
 
# arr = array([1,2,3,4,5])
# arr2 = array([9,3,6,5,2])

# arr += 5
# arr3 = arr + arr2

# print(arr)
# print(arr3)

# arr1 = array([5,2,6,9,7])

# arr2 = array([2,6,3,5,9])

# arr3 = ([])

# arr2 = arr3

# print(arr2)
# print(arr3)

# arr3 = array([2,6,3,5,9])

# print(arr2)
# print(arr3)

# print(id(arr2))
# print(id(arr3))

class Student:
    def __init__(self, name, matno):
        self.name = name
        self.matno = matno
        self.lap = self.Laptop()

    def show(self):
        return f"{self.name}: {self.matno}"

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16


jim = Student("Jimmi Jat", 9002021)

print(jim.show())


print(jim.lap.ram)