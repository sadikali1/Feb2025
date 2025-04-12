
try:
    a = int(input("please enter number:"))
except:
    print("Oops you have not entered number")
    raise RuntimeError("Exceptoin throws")