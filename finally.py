try:
    file = open("finally.py")
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError,ZeroDivisionError):
    print("you did not enter a valid age:")

else:
    print("no exception were thrown ")

finally:
    print("always executed")

