def FizzBuzz(x: int):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Buzz"
    elif x % 5 == 0:
        return "Fizz"
    else:
        return "Not match"
