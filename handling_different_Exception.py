try:
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you did  not enter a vslid age.")

else:
    print("no exception were throw")