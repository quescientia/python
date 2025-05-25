
# this file will have helper functions
# for finding the characteristics of a number

# 1. odd or even
# 2. positive, negative, zero
# 3. factors
# 4. prime or not

#from number_helper import odd_or_even 

# 
# I want to find out whether the number is positive or negative
# Check if the number is greater than 0
# If yes, it's positive
# If not, check if it is zero
# if it is not zero, it is negative
# 

# factors
# example: 10
# factors will belong in this list( 1.... 10 ) 
# start a loop from 1 to 10 i.e. the given number
# check if 10 is divisible by each number through the loop
# 10%1 = 0.. so 1 is a factor
# 10%2 = 0.. so 2 is also a factor
# 10%3 = 1.. so 3 is not a factor
# if we found a factor, add it to a list
# a python list, comes with a function called "append"
# at the end of the loop, the list should contain all the factors


def odd_or_even(number) -> str:
    if (number % 2 == 0):
        return "even"
    else:
        return "odd"


def pos_neg_zero(number) -> str:
    if (number > 2):
        return "p"
    elif (number == 0):
        return "z"
    else:
        return "n"


def factors(number) -> list:
    factors_list = []
    for i in range(1, number+1):
        if (number % i == 0):
            factors_list.append(i)
    return factors_list


def prime_or_not(factor_list) -> bool:
    if (len(factor_list) == 2):
        return True
    else:
        return False