def can_access_library(age):
    if age>=18:
        return True 
    else:
        return False 

print(can_access_library(17))  # Output: False
print(can_access_library(19))  # Output: True


#A city is hosting a car race. However, only cars that have a maximum speed of exactly 200 km/h are allowed to participate. 
#You need to create a function is_eligible_for_race(max_speed) to return if a car is eligible to participate.

def is_eligible_for_race(max_speed):
    return max_speed==200

print(is_eligible_for_race(150))  # Output: False
print(is_eligible_for_race(200))  # Output: True

#In this exercise, your task is to create a Python function named is_valid_triangle that returns if the three given angles can 
#form a valid triangle. An angle cannot be less than or equal to 0.

def is_valid_triangle (angle1, angle2, angel3):
    if angle1<=0 and angle2<=0 and angel3<=0:
        return angle1+angle2+angel3<=180
    else:
        return angle1+angle2+angel3==180

print(is_valid_triangle(30, 60, 90))  # Return True

# In this exercise, calculate of the sum of all divisors of a given integer number

def calculate_sum_of_divisors(number):
    sum_of_divisors = 0

    if number<=0:
        return sum_of_divisors
    
    for divisor in range(1,number+1):
        if number % divisor == 0:
            sum_of_divisors+=divisor
    return sum_of_divisors
    
print(calculate_sum_of_divisors(0))   # Output: 0
print(calculate_sum_of_divisors(6))   # Output: 12
print(calculate_sum_of_divisors(15))  # Output: 24

#In this exercise, your task is to create a Python function named is_perfect_number that checks whether a given integer 
#is a perfect number or not. A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding itself.
#A classic example of a perfect number is 6. Let's break it down:
#Positive divisors of 6 are 1, 2, 3, and 6. 
#However, when checking if a number is perfect, we exclude the number itself. So, for our purposes, the divisors are 1, 2, and 3.
#When you sum these divisors, you get 1 + 2 + 3 = 6, which is the original number. Therefore, 6 is a perfect number.

def is_perfect_number(number):
    
    if number <= 0:
        return False
    
    divisor_sum = 0

    for i in range(1,number):
        if number % i == 0:
            divisor_sum += i
    
    return divisor_sum == number
          
print(is_perfect_number(6))  # Output: True
print(is_perfect_number(28))  # Output: True
print(is_perfect_number(5))  # Output: False

#In this exercise, your task is to create a Python function named get_last_digit that finds 
#the last digit of a given integer.

def get_last_digit(number):
    last_digit = number%10
    return last_digit
    
print(get_last_digit(123))  # Output: 3
print(get_last_digit(9087))  # Output: 7
print(get_last_digit(6))  # Output: 6

#In this exercise, your task is to create a Python function named are_both_even that checks if both 
#input integers are even. The function should return True if both i and j are even, and False otherwise.

def are_both_even(i,j):
    return i%2==0 and j%2==0

print(are_both_even(4, 2))  # Output: True
print(are_both_even(3, 4))  # Output: False

#Your task is to complete the implementation of the method is_leap_year to determine if a given year is a leap year.
#The rules are a little tricky. Read them carefully.
#A year is a leap year in the Gregorian calendar if:
# -> It is divisible by 4 (AND)
# -> It is NOT divisible by 100 (except when it is divisible by 400)
# -> Not Divisible by 4 - NOT Leap Year (2041)
# -> Divisible by 4 and NOT divisible by 100 - Leap Year (2048)
# -> Divisible by 4 and divisible by 100 - Additional check needed
# -> Divisible by 4, divisible by 100, divisible by 400 - Leap Year (2000, 2400)
# -> Divisible by 4, divisible by 100, NOT divisible by 400 - NOT Leap Year (2100, 2200, 2300)

def is_leap_year(year):
    if year <=0:
        return False
    
    return year%4==0 and year%100!=0 and year%400!=0 or year%4==0 and year%100==0 and year%400==0
    
print(is_leap_year(2024))    
print(is_leap_year(2200))
print(is_leap_year(2000))

#In this exercise, your task is to create a Python function named is_right_angled_triangle that determines 
#whether the given lengths of three sides form a right-angled triangle or not.
# As per the Pythagorean theorem, in a right-angled triangle, the square of the length of the hypotenuse 
#(the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.
#If any side has a non-positive length, it's not considered a valid triangle.

def is_right_angled_triangle(side1,side2,side3):
    if side1<=0 or side2<=0 or side3<=0:
        return False

    if side1**2 + side2**2 == side3**2:
        return True
        
    if side3**2 + side2**2 == side1**2:
        return True
    
    if side2**2 + side1**2 == side3**2:
        return True
    
    return False

print(is_right_angled_triangle(3, 4, 5))  # Output: True
print(is_right_angled_triangle(5, 3, 4))  # Output: False


#In this exercise, your task is to create a Python function named assign_grade 
#that assigns a grade (A to F) to a student based on the marks they received.
#
#Here is the grade assignment criteria:
#
#   -> If marks are 90 or more, grade is 'A'
#   -> If marks are 80 or more but less than 90, grade is 'B'
#   -> If marks are 70 or more but less than 80, grade is 'C'
#   -> If marks are 60 or more but less than 70, grade is 'D'
#   -> If marks are 50 or more but less than 60, grade is 'E'
#   -> If marks are less than 50, grade is 'F'

def assign_grade(marks):
    if marks < 50:
        return "F"
    elif marks >= 50 and marks < 60:
        return "E"
    elif marks >= 60 and marks < 70:
        return "D"
    if marks >= 70 and marks < 80:
        return "C"
    elif marks >= 80 and marks < 90:
        return "B"
    if marks >= 90:
        return "A"
        
print(assign_grade(85))  # Output: 'B'

#In this exercise, your task is to create a Python function named 
#provide_weather_advisory that provides a weather advisory message based on the current temperature.
#
#Here is the advisory message criteria:
#
#   -> If the temperature is below 0, return "It's freezing! Wear a heavy coat."
#   -> If the temperature is between 0 and 10 (inclusive), return "It's cold! Bundle up."
#   -> If the temperature is between 11 and 20 (inclusive), return "It's cool! A light jacket will do."
#   -> If the temperature is above 20, return "It's warm! Enjoy the day."
#

def provide_weather_advisory(temperature):
    if temperature < 0:
        return "It's freezing! Wear a heavy coat."
    elif temperature <=10:
         return "It's cold! Bundle up." 
    elif temperature <=20:
        return "It's cool! A light jacket will do."
    if temperature > 20:
        return "It's warm! Enjoy the day."
    
print(provide_weather_advisory(15))  # Output: "It's cool! A light jacket will do."

#### TABUADA MATEMATICA ######

from colorama import Fore

print(f"{Fore.LIGHTRED_EX}")

estrutura = {}
print ('TABUADA MATEMATICA 😊'.center(500,' '))

for i in range(1,11): ## FAZ AS COLUNAS
    chave = f"{Fore.LIGHTMAGENTA_EX}Tabuada do {i}"
    estrutura[chave] = []

for t in estrutura:  ## FAZ AS COLUNAS
    print(f"{t:<15}\t", end='')
print()

for i in range(1,11):
    for tabuada in range(1,11):
        print(f"{Fore.WHITE}{tabuada:>1} * {i:>2} = {Fore.GREEN}{tabuada*i:>3}\t", end='')
    print()
print()
 