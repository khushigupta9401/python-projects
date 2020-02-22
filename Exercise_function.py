def fizz_buzz(input):
    if input % 3 == 0:
        print("fizz")

    elif input % 5 == 0:
        print("buzz")

    elif input % 7 == 0:
        print("fizz buzz")

    else:
        print(input)


fizz_buzz(5)