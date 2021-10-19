# overload method

class Teams:

    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def __add__(self, other):
        point1 = self.point1
        point2 = self.point2
        s3 = point1 + point2
        return s3

    
t1 = Teams(20, 2)
t2 = Teams(10, 1)

print(t1 + t1)