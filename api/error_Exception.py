from math import trunc

a = 20
b =2

try:
    result = a/b
    print(result)
    sum = 10 + 'spam' * 2
except ZeroDivisionError:
    print("Error handled")
except TypeError:
    print("TypeError handled")

print("first exception done")
try:
    sum = 10 + 'spam'*2
except:
    print("second exception handled")

print("second exception done")
