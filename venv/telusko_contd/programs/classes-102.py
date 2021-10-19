# Inheritance

class A:

    def __init__(self) -> None:
        print("in A init")

    def feature1():
        print("feature 1 working")

    def feature2():
        print("feature 2 working")


class B(A): #class B inheriting from class A - Single Level

    def __init__(self) -> None:
        super().__init__()
        print("in B init")

    def feature3():
        print("feature 3 working")

    def feature4():
        print("feature 4 working")


class C(B): # class is grandchild, inheriting both A and B - Multi Level

    def __init__(self) -> None:
        super().__init__()
        print("in C init")
    def feature5():
        print("feature 5 working")

c1 = C()

a = 6
b = 3

print(int.__add__(a,b))