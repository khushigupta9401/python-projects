try:
    with open("with_statment.py") as file:
        print("file opened")
    age = int(input("age: "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("you didnt enter a valid age")

else:
    print("no exception")
