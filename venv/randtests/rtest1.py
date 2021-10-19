from array import *

vals = array('i', [])
n = int(input("enter the length of array: "))

for i in range(n):
    x = int(input("enter the number: "))
    vals.append(x)

print(vals)

q = int(input("enter the number to search: "))

k = 0
for e in vals:
    if e == q:
        print(k)
        break
    k += 1