from number_helper import *

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


number = int(input("Enter a number: "))

# odd or even
result = odd_or_even(number)
if (result == "even"):
    print(f"{number} is even")
else:
    print(f"{number} is odd")


result = pos_neg_zero(number)
if (result == "p"):
    print(f"{number} is positive")
elif (result == "z"):
    print(f"{number} is zero")
else:
    print(f"{number} is negative")


factor_list = factors(number)
print(f"The factors of {number} are {factor_list}")

result = prime_or_not(factor_list)
if (result == True):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

# postive, negative, zero
#if (number > 0):
#    print(f"{number} is positive")
#elif (number == 0):
#    print(f"{number} is zero")
#else:
#    print(f"{number} is negative")

# prime or not

# what are the factors