def FruitList():
    fruits = ["apple", "peach", "pear"]
    for fruit in fruits:
        print(fruit)


FruitList()

student_heights = [120, 300, 200, 220, 990, 180]


def AverageHeight():
    total_height = 0
    student = 0
    for height in student_heights:
        total_height += height
        student += 1
    average = round(total_height/student)
    print(average)


AverageHeight()


def HighestHeight():
    highest_height = 0
    for height in student_heights:
        if height > highest_height:
            highest_height = height
    print("highest height: {}".format(highest_height))


HighestHeight()


def SumOfEvenNumbers():
    total_sum = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total_sum += number
    print(total_sum)


SumOfEvenNumbers()


def fizzBuzz():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


fizzBuzz()
