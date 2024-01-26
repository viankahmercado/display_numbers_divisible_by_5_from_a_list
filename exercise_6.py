# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 6:
# Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# create a function to print divisible by 5
def check_divisible_by_5(numbers):
    print("Given list:", numbers)
    print('\nNumbers divisible by 5:')
    for num in numbers:
        if num % 5 == 0:
            print(num)

# make the list as variable
given_list = [10, 20, 33, 46, 55]
# check the logic by print
