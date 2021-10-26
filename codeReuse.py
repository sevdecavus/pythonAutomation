'''In this code, identify the repeated pattern and replace it with a function
called month_days, that receives the name of the month and the number of days in that month
as parameters. Adapt the rest of the code so that the result is the same. Confirm your results
by making a function call with the correct parameters for both months listed.'''


def month_days(month, days):
    print(month + " has " + str(days) + " days.")


month_days("June", "30")
month_days("July", "31")

'''This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6?
Tip: a function that calculates the area of a rectangle should probably be called rectangle_area, and if it's receiving base and height, that's what the parameters should be called.
'''


def rectangle_area(base, height):
    area = base * height
    print("The area is " + str(area))


rectangle_area(5, 6)

'''This function converts miles to kilometers (km).

Complete the function to return the result of the conversion

Call the function to convert the trip distance from miles to kilometers

Fill in the blank to print the result of the conversion

Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result


'''


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km


my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))

'''
This function compares two numbers and returns them in increasing order.

Fill in the blanks, so the print statement displays the result of the function call in order.

Hint: if a function returns multiple values, don't forget to store these values in multiple variables'''


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

'''
In math, the factorial of a number is defined as the product of an integer 
and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24. 
Fill in the blanks to make the factorial function return the right number.'''


def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result = result * x
    return result


for n in range(1, 10):
    print(n, factorial(n))
