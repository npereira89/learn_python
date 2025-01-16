import os
import re
import time
import string
import statistics
import ipinfo
import locale
import pytz
import openpyxl
import math
import random
import sys
import textwrap
import numpy as np
from colorama import Fore, Style
from random import randint
from datetime import datetime, timedelta
from array import array
from openpyxl.workbook import Workbook

###############################
### ALL FUNCTIONS AND CLASS ###
###############################

import os, time

def convert_cels_fahre(valor_to_convert):
  fahrenheit = round((valor_to_convert*(9/5)) +32,3)
  print(f"{valor_to_convert} ºC --> {fahrenheit} ºF")
  return fahrenheit

def convert_fahre_cels(valor_to_convert):
  celsius = round((valor_to_convert-32) / 1.79999999,3)
  print(f"{valor_to_convert} ºF --> {celsius} ºC")
  return celsius

def combo_string(a, b):
  
  check_size_a = len(a)
  check_size_b = len(b)
  
  if check_size_a > check_size_b:
      longer = a
      short = b
  else:
      longer = b
      short = a
  
  return short+longer+short

def join_middle(bound_by, tag_name):
  if len(bound_by) % 2 == 0:
    # Even length: Insert between the two middle characters
    mid = len(bound_by) // 2
    return bound_by[:mid] + tag_name + bound_by[mid:]
  else:
    # Odd length: Insert after the middle character
    mid = len(bound_by) // 2
    return bound_by[:mid] + tag_name + string[mid:]

def reverseWords(s):
    words = s.split() 
    reversed_words = words[::-1]
    return " ".join(reversed_words)

def gfg(S):
    b = S.lower()
    if(b.startswith("gfg") or b.endswith('gfg')):  
        print ("Yes")
    else:
        print ("No")

def trim(str):
    str_final = str.strip()
    return str_final
    
def exists(str, x):
    str_final = str.strip()
    return str_final.find(x)
    
def titleIt(str):
    str_final = str.strip()
    return str_final.title()
    
def casesSwap(str):
    str_final = str.strip()
    return str_final.upper()

def intersection(arr1, arr2):
    new_arr = arr1 + arr2
    result = list()

    for value in new_arr:
        if new_arr.count(value) > 1:
            result.append(value)
            new_arr.remove(value)

    return print(result)

def stringJumper(str):
    for i in range(0, len(str), 2): ## from 0 to length of str and skip 2
        print(str[i], end="") ##printing character and separating characters by nothing

def printIncreasingPower(x):
    for num in range(1, x+1):
        result = num ** 2
        if result<=x:
            print(result, end= ' ')
	    
def pos(n):
    for n in range(n-1, -1, -1):
        print(n, end= ' ')
    
def neg(n):
    for n in range(n, 1, 1):
        print(n, end= ' ')

class Solution:
    def checkNumber(a, b):
        if int(a) == int(b):
            flag="True"
        else:
            flag="False"
        return flag
	
    def get_min_max(self, arr):
        return min(arr), max(arr)
    
    def findUnion(self, a, b):
        total_union = a + b
        return len(list(set(total_union)))

class Person:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def is_eligible(self):
        if self.age >= 18:
            print(f"Hi {self.name} \nYou can see pornography!!")
        else:
            print(f"Go away {self.name} \nYou are not allow to see pornography, cuz you're {self.age} yo!")

def round_number(value):
    valor_approach = round(value, 0)
    if valor_approach > value:
        return print(f"The excess approach is {valor_approach:.0f}")
    else:
        return print(f"The default approach is {value:.0f}")

def calc_area(side1, side2, side3):
    if side1 >= 0 and side2 >= 0 and side3 >= 0:
        a = side1 + side2 + side3 / 2
        area = math.sqrt(a * (a - side1) * (a - side2) * (a - side3))
        return print(f"The value of area is {area:.2f} m2")
    else:
        print("Not possible calculate area of triangle, because one of the values are not positive")

def calc_price(qtd_hmb, qtd_ch, qtd_shp, qtd_itea, qtd_shk):
    price = (qtd_hmb * 6.5) + (qtd_ch * 7.5) + (qtd_shp * 3.5) + (qtd_itea * 0.7) + (qtd_shk * 0.8)
    return float(price)

def round_number(value):
    valor_approach = round(value, 0)
    if valor_approach > value:
        return print(f"The excess approach is {valor_approach:.0f}")
    else:
        return print(f"The default approach is {value:.0f}")
	
def consumer_price(farmer_cost):
    if farmer_cost <= 10000:
        rate_distribution = 0.08
    elif farmer_cost > 10000:
        rate_distribution = 0.06

    if rate_distribution <= 0.06:
        rate_taxes = 0.35
    if rate_distribution > 0.06:
        rate_taxes = 0.45

    total = farmer_cost + (farmer_cost * rate_distribution) + (farmer_cost * rate_taxes)
    return print(f"The consumer price is {total:2f} €")

def formula_delta(value_a, value_b, value_c):
    delta = value_b**2 - (4 * value_a * value_c)
    if delta == 0:
        return print(f"The delta value is {delta}.\nThe discriminante is null")
    if delta > 0:
        return print(f"The delta value is {delta}.\nThe discriminante is positive")
    if delta < 0:
        return print("Not possible calculate the quadratic equation")

def thought_exame(exam1, exam2, work):
    total = (exam1 * 0.3) + (exam2 * 0.3) + (work * 0.4)
    if total < 50:
        return print("Scale 5. You repproved this year 😔😢")
    elif  59 <= float(total) >= 50:
        return print("Scale 4. You need to improve 😐")
    elif  60 <= total >= 69:
        return print("Scale 3. It's enought but you can do better!! 😉")
    elif  70 <= total >= 79:
        return print("Scale 2. You make a good job this year!! 😍")
    elif  80 <= total >= 100:
        return print("Scale 2. Fantastic!! You're master this year! 💖")

def calc_area(ba, alt):
    area = (ba * alt) / 2
    return print(f"The area of triangle is {area:.2f}")

def emojis(message):
    words = message.split(" ")
    emojis = {

        ":)": "🙂",
        ":(": "😔",
        "*_*": "😍"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output

def find_right_most_digit(text):
    count=0
    
    for ch in text:
        if ch.isdigit() == True:
            count += 1

    return count

def square_number(number):
    number *= number
    return number
    
def greeting(name):
    first_name = lambda nome: nome.split()[0]
    last_name = lambda nome: nome.split()[-1]

    return print(f'Seu primeiro nome é {first_name(name)} '
                 f'e o seu último nome é {last_name(name)}')

def sum_values(a, b):
    multwo = lambda c, d: c + d
    return multwo(a, b)


def is_pair_or_not(value):
    if value % 2 == 0:
        return print(f"The number {value} is pair")
    else:
        return print(f"The number {value} is not pair")


def get_latest_behind(num):
    ant = num - 1
    last = num + 1
    return print(f"The number is {num}. The next one is {last} and the ancestor is {ant}")

def remove_data(list_num):
    i = 0
    while i< len(list_num):
       if list_num[i] > 50:
           list_num.remove(list_num[i])
           i -= 1
       else:
           i += 1
    return print(list_num)
    
def greeting_out_func(x, y):
    def inner_greeting(x,y):
        return x + y

    greet = inner_greeting(x,y)
    return greet + 'Developers'

def is_leap(year):
    leap = False
    
    if (year%4==0 and year%100!=0) or year%400==0:
        leap = True 
            
    return leap
    
def mutate_string(string, position, character):
    text = string[:position] + character + string[position+1:]
    return text

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

def solve(meal_cost, tip_percent, tax_percent):
    tip = float((meal_cost * tip_percent)/100)
    tax = float((meal_cost * tax_percent)/100)
    total_cost = meal_cost + tip + tax
    return print(round(total_cost))

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result = string[i:max_width+i]
        if len(result) == max_width:
            print(result)
        else:
            return(result)

def swap_case(s):
    num = ""
    for let in s:
        if let.isupper() == True:
            num+=(let.lower())
        else:
            num+=(let.upper())
    return num

##################################
### STRINGS AND CHAR EXERCISES ###
##################################

##################################
## Given two strings a and b. The task is to make a new string where the string with longer length should 
## be in between and the one with shorter length should be outside on front and end. New string should be like 
## shorter+longer+shorter.
##################################

a = Hi
b = There
combo_string(a, b)

##################################
## Given a string of braces named bound_by, and a string named tag_name. 
## The task is to print a new string such that tag_name is in the middle of bound_by.
##################################

bound = "[[[]]]"
tag = "nuno"
print(join_middle(bound, tag))

##################################
## Given a string s, reverse the string without reversing its individual words. 
## Words are separated by spaces.
##################################

string='O meu nome é Nuno'
print(reverseWords(string))

##################################
## You are given a string, 'S'. You need to write a function called 'gfg' that takes 'S' as input and 
## checks if the string starts and ends with the substring 'gfg'
##################################

gfg("DXvBFJkfndGfg")

##################################
## Using the built-in commands title, trim, uppercase and title string to show in output
##################################

text = "nuno"
chars = "no"

print(trim(text))
print(exists(text, chars))
print(titleIt(text))
print(casesSwap(text))


##################################
## Showing Code ASCII between 33 and 126
##################################
for i in range(33,127):
    print(f"{i} -> {chr(i)}")
    
##################################
## Print the alphabetic with ASCII code with upper and lower case
##################################

for i in range(65,91):
    print(chr(i),end=' ')
print("\n")
for x in range(65,91):
    print(chr(x).lower(), end=' ')

##################################
## Manipulate the string with some characters
##################################

string='The life is beautiful'
print(string.replace(' ','-'))

string1='The'
string2='life'
string3='is'
string4='beautiful'
print(string1+'-'+string2+'-'+string3+'-'+string4)

##################################
## Break line each word in a string
##################################

print('\n')
string='Python is an awesome programming language to learn for beginners'
print(string.replace(' ','\n'))

##################################
## You are given a string and your task is to swap cases. 
## In other words, convert all lowercase letters to uppercase letters and vice versa.
##################################
s = input()
result = swap_case(s)
print(result)

##################################
## Your task is to find the first occurrence of an alphanumeric character in  
## (read from left to right) that has consecutive repetitions. 
##################################

string = input()
ans = re.search(r'([^\W_])\1+', string)
print(ans.group(1) if ans else -1)

##################################
### Your task is to complete the regex_pattern defined below, 
##  which will be used to re.split() all of the , and . symbols
##################################

regex_pattern = r"[.,]" # Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))

##################################
##   Complete the code in the editor below. The variables are already declared and initialized for you. You must:
##    - Declare  variables: one of type int, one of type double, and one of type String.
##    - Read  lines of input from stdin (according to the sequence given in the Input Format section below) 
## and initialize your  variables.
##    - Use the  operator to perform the following operations:
##    - Print the sum of  plus your int variable on a new line.
##    - Print the sum of  plus your double variable to a scale of one decimal place on a new line.
##    - Concatenate the string you read as input str and print the result on a new line.
##################################

i = 4
d = 4.0
s = 'HackerRank '

i += int(input())
d += float(input())
s = 'HackerRank ' + str(input())

print(i)
print(d)
print(s)

##################################
You are given a string and width
Your task is to wrap the string into a paragraph of width .
##################################

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result, end='\n')

### Read a given string, change the character at a given index and then print the modified string.

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#########################################
# Making a Christmas Tree with date
#########################################

now = datetime.now()
x = np.arange(7, 16)
y = np.arange(1, 18, 2)
z = np.column_stack((x[::-1], y))

print('')

for i, j in z:
    if j == 1:
        print(Style.BRIGHT + Fore.YELLOW + ' ' * i + '*' * j)
    else:
        print(Style.BRIGHT + Fore.GREEN + ' ' * i + '*' * j)
for r in range(4):
    print('\x1b[38;2;139;69;19m' + ' ' * 13, '**')

print(Style.RESET_ALL)
print(Style.NORMAL + Fore.LIGHTRED_EX + ' ' * 7, end='Merry Christmas!! 🎅\n')
print(Style.NORMAL + Fore.LIGHTRED_EX + ' ' * 7, end=now.strftime("%d/%m/%Y %H:%M:%S"))
print('')

######## Verificador de Palíndromos 							       #################
######## Crie um programa que verifique se uma palavra fornecida pelo usuário é um palíndromo. #################

string = input("Diz-me qual é a palavra ou frase: ")
texto_invertido = string[::-1]

if string.lower() == texto_invertido.lower() and len(string.split()) == 1:
    print("É uma palavra palíndromo!!")
elif string.lower() != texto_invertido.lower() and len(string.split()) == 1:
    print("Não é uma palavra palíndromo!!")

####### IP LOCATION GIVEN #########

access_token = 'ACCESS_TOKEN_IPINFO'
handler = ipinfo.getHandler(access_token)
ip_address = 'IP_PC'
details = handler.getDetails()
print(details.country_name + " -> " + details.city)
print("Hostname: " + details.hostname)

#########################################
# Making a "F" and "L" with a nested loop
#########################################
number_xs = [5,2,5,2,2]
number_ls = [2,2,2,2,5,5]

size_xs = len(number_xs)
size_ls = len(number_ls)

for i in range(0,size_xs,1):
    for xs in range(number_xs[i]):
        print("X",end="")
    print("",end="\n")
print("\n")
for ls_count in range(0,size_ls,1):
    for ls in range(number_ls[ls_count]):
        print("X",end="")
    print("", end="\n")

##########################################
# Program to open images files in Python
##########################################
import os.path
from PIL import Image

images = []
path = "path_folder_images"
valid_files = [".jpg", ".gif", ".png"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_files:
        continue
    image_path = os.path.join(path, f)
    with Image.open(image_path) as img:
        img.show()

### String module ###
 
print(string.ascii_letters)  # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)   # Output: abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)   # Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)            # Output: 0123456789
print(string.hexdigits)         # Output: 0123456789abcdefABCDEF
print(string.punctuation)       # Output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.ascii_letters)     # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
         
print(find_right_most_digit('The value is 42 dsds2323'))  # Output: 2
print(find_right_most_digit('No digits heredssd34'))  # Output: -1

#####################################
# Write a program where you describe the number in text
#####################################
phone_number = input("Phone: ")

phone =  {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

for numbers in phone_number:
    print(phone[numbers], end=" ")

### working with date ###

print(f"Date two days forward: {(datetime.now() + timedelta(2))}")
print(f"Date with date format: {time.strftime("%Y-%m-%d")}")

### Create an inner function to concat two string. ###

print(greeting_out_func('Nuno', 'Pereira'))


### working with dictionary ###
valor = {'m1': {'m2': 'Hi World', 'm3': 'Hello Mickey', "m4": "Hii Mr. Dolittle"}}

print(valor["m1"]["m3"])

### Reverting dictionary values ###

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

reverse_dict = {value: key for key, value in ascii_dict.items()}
print(reverse_dict)

### Working with dict using json string ###

import json

emp_dict = {
    "company": {
        "employee": {
            "professional": {
                "id": "001",
                "name": "Jess",
                "payable": {
                    "salary": 9000,
                    "increment": 1,
                    "method": 'diary'
                },
            }
        }
    }
}

formatted_json_data = json.dumps(emp_dict['company']['employee']['professional'], indent=2, separators=(",", ": ")).encode("ascii")

# Output the JSON string
print(formatted_json_data)

### Message of gretting someone ###
      
name = input("What is your name? ")
print(f"Hello World {name}")

#### Try to show the name and the last name ####

greeting("Patricia Silva Santos Pereira")

### Develop a program that change in real time a word Java for Python in sentence 

phrase = 'Exercises for Java'
print(phrase.replace("Java", "Python"))

### Title a string or full name using a strip command ### 
full_name = ' nuno pereira '
print("Hello, " + full_name.strip() + "!")

##############################################################
# Check the name has between 3 and 50 characters. If the name
# is above 50 characters the name is wrong but it's minor
# 3 chars must be at least 3 chars too
##############################################################
name = input("What's your name? ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be 50 characters")
else:
    print("name looks good")

##############################################################

name = input("What is your name? ")
fav_color = input("What is your favourite color? ")

print(f"{name} likes {fav_color}")
print(name + " likes " + fav_color)

##############################################################
# Program to read a keyboard value and show last input value,
# through a array variable with 3 values.
##############################################################
valor = ["text_write"]
size_array = int(len(valor))

while size_array < 3:
    text = input("Put a value: ")
    valor.append(text)
    print(valor[size_array-1])
    size_array += 1

##################################
# Using class and constructor
##################################


name_in = str(input("Name: "))
age_in = int(input("Age: "))

john = Person( str(name_in), int(age_in))
john.is_eligible()


##################################
### 	NUMBER EXERCISES       ###
##################################

##################################
### Convert celsius to fahrent and vice versa
##################################

valor_to_convert = int(input("Input the Fahrenheit temperatures: "))

convert_fahre_cels(valor_to_convert)
convert_cels_fahre(valor_to_convert)

time.sleep(20)

##################################
### Intersection two list variables and check which values is repeated in that intersection
##################################

arr_a = [1, 2, 3, 4]
arr_b = [2, 4, 6, 7, 8]
intersection(arr_a, arr_b)

##################################
### You are given two array with various numbers and union them
### Task: Get the lenght of the new array (union of array A with B)
##################################

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

##################################
### You are given a array with various numbers and get the min and max value
##################################

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1
        print("~")

##################################
### You are given a string str, you need to print its 
### characters at even indices(index starts at 0).
##################################

stringJumper("DoctorPhenomenal")

##################################
### Given a positive integer x, the task is to print the numbers from 1 to x in the order 
### as 12, 22, 32, 42, 52, ... (in increasing order).
##################################

def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n = int(input())
        if(n > 0):
            pos(n)
        elif(n < 0):
            neg(n)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()

##################################
### Check if the value is equal or not for other 
##################################

print(Solution.checkNumber("18","155"))

##################################
### Power build-in maths library
##################################

for x in range(2, 11):
    for y in range(1, 11):
        print(f"{x} elevado a {y} = {float(math.pow(x,y)):.0f}")
    print("\n")

##################################
### Write a program calculating the sum of all numbers raised to a specific power. 
### Input format: First line contains two integers: n, e separated by a comma. Each of the next 
### n lines contains an integer.
##################################

values = input("Sample Input: ")
n, e = map(int, values.split(','))
total = 0

for numb in range (1, n+1):
    total += numb**e
    
print(total)

######## Sum two numbers ########

print('\n')
x = int(input("Enter the number 1: "))
y = int(input("Enter the number 2: "))
print(f"Sum of two number is {x+y}")

##################################
### Get three numbers in one line from STDIN, separated by a space
### then print their product using python code
##################################

values = input(f"Enter three numbers:")
listNumbr = list(map(int, values.split())) 
total = 1

for x in listNumbr:
    total *= x

print(total)

######## Date format ########

time = datetime.now()
print(time.strftime("%Y-%m-%d"))

######## GIVE THE HOUR AT THE MOMENT FROM A TIMEZONE ########

# Set the timezone
timezone = pytz.timezone(input('Give the timezone: '))
# Get the current time in Brazil
brazil_time = datetime.datetime.now(timezone)
print(f"Current hour in {timezone}:", brazil_time.strftime("%H:%M:%S"))

######## TABUADA ATE AOS 10 ########

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x*y}')
    print("\n")

######## Jogo de Adivinhação	 							 #################
######## Escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. 	 #################

number_sorted = random.randint(1, 100)
tries, x = 3, 0
print(number_sorted)

while x != tries:
    value = int(input("Guess number between 1 and 100: "))
    if value <= 100:
        x += 1
        if x <= tries:
            if value == number_sorted:
                print("Get it!! Congrats 🍀")
                exit(1)
            elif value != number_sorted and x < 3:
                print(f"No, try again. You have more {tries - x} tries")
            elif value != number_sorted and x == tries:
                print("Game over 😔")
    else:
        print("The value isn't between the range")

##################################
## Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
## You are given  scores. Store them in a list and find the score of the runner-up.
##################################

n = int(input())    
arr = map(int, input().split())
arr2 = list(set(arr))
arr2.sort()
print(arr2[-2])   

##################################
## Given an integer, , perform the following conditional actions:
##  - If is odd, print Weird
##  - If is even and in the inclusive range of  to , print Not Weird
##  - If is even and in the inclusive range of  to , print Weird
##  - If is even and greater than , print Not Weird
## Complete the stub code provided in your editor to print whether or not  is weird.
##################################

if __name__ == '__main__':
    N = int(input().strip())
    
    if N % 2 == 0 and N<=5:
        print("Not Weird")
    elif N % 2 != 0 and N >= 6 or N<=20:
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")       

##################################
##   Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
##   and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. 
##   Round the result to the nearest integer.
##################################

meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())
solve(meal_cost, tip_percent, tax_percent)


##################################
## Given an array, , of size  distinct elements, sort the array in ascending order 
## using the Bubble Sort algorithm above. 
## Once sorted, print the following lines: array sorted, first and last element
##################################

n = int(input())
a = [int(x) for x in input().split(" ")]
numberOfSwaps = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            tmp = arr[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp
            num_swaps += 1
    if num_swaps == 0:
        break
   
print(f'Array is sorted in {numberOfSwaps} swaps.')
print(f'First Element: {min(a)}')
print(f'Last Element: {max(a)}')

##################################
##  Read in two integers, A and B, and print three lines.
##  The first line is the integer division
##  The second line is the result of the modulo operator moddivisor (%)
##  The third line prints the divmod of A and B.
##################################

a = int(input())
b = int(input())
div = a/b
module = a%b
result = (int(div), module)

print(int(div))
print(module)
print(result)

##################################
##	Given an integer, n, print the following values for each integer i from 1 to n: Decimal, Octal, Hexa and Binary. 
##	The four values must be printed on a single line in the order specified above for each i from 1 to n. 
##	Each value should be space-padded to match the width of the binary value of n.
##################################       
n = int(input())
print_formatted(n)

##################################
##  Rupal has a huge collection of country stamps. She decided to count the total number of distinct 
##  country stamps in her collection. She asked for your help. You pick the stamps one by one from a 
##  stack of  country stamps. Find the total number of distinct country stamps.
##################################

N = int(input())
conta, total = N, 0
list_country = set('')

for put in range(N):
    country = input()
    
    if country not in list_country:
        list_country.add(country)
        total += 1

print(total)


##################################
##  The provided code stub will read in a dictionary 
##  containing key/value pairs of name:[marks] for a list of students. 
##  Print the average of the marks array for the student name provided, 
##  showing 2 places after the decimal.
##################################

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    subtotal, total = 0, 0
    
    for rate in student_marks[query_name]:
        subtotal += rate
        
    total = float(subtotal/len(student_marks[query_name]))
    print("%.2f" % total)

##################################
## An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
## It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. 
## A leap year contains a leap day.
##
## In the Gregorian calendar, three conditions are used to identify leap years:
##
## The year can be evenly divided by 4, is a leap year, unless:
## The year can be evenly divided by 100, it is NOT a leap year, unless:
## The year is also evenly divisible by 400. Then it is a leap year.
## This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
## while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
###################################
    
year = int(input())
print(is_leap(year))

### Sum two numbers using a function which use lambda function (MUST LEARN MORE ABOUT IT) ####

print(sum_values(5, 2))

### Develop a program to store 4 notes on list and get avarage, max and minimun note ###

array_notas = []

for i in range(1,5):
    nota = int(input(f"Input the note {i}: "))
    array_notas.append(nota)
    i += 1

if statistics.mean(array_notas) >= 7:
   print("APPROVED")
else:
   store_final_prove=int(input("Should study more :(\nStore final exam score: "))
   array_notas.append(store_final_prove)

   if statistics.mean(array_notas) >= 5:
      print("APPROVED!!")
   else:
      print("REPROVED!!")

### Figure out the next number and the ancestor number ####

get_latest_behind(99)

### Removing numbers above 50 ###

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
remove_data(number_list)

### Get the number before and the after number ###

number = int(input("Write a number (not a float)"))
print(f"The number before is {number-1} and number after is {number+1}")

### Get a float number with 2 decimais houses ####

print(f"The number with 2 decimals {number:.2f} ") 

### Develop a program to save a median rounded 2 decimal houses #####

array_notas = [55,25,58,88,787,551]

print(f"The avarage is {round(statistics.mean(array_notas),2)}")

### Display all duplicate items from a list ### 

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

list_number_dupl = []
for i in range (0, len(sample_list)):
    if int(sample_list.count(sample_list[i])) >= 2:
        if sample_list[i] not in (list_number_dupl):
            list_number_dupl.append(sample_list[i])

print(list_number_dupl)

### Filter dictionary to contain keys present in the given list ###

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']

filtered_d1 = {key: d1[key] for key in l1}
print(filtered_d1)

### check number is pair or unpair ###

is_pair_or_not(15)

### Develop a program to store 4 notes on list and get avarage, max and minimun note ###

array_notas = []

for i in range(1,5):
    nota = int(input(f"Input the note {i}: "))
    array_notas.append(nota)
    i += 1

print(f"A nota mais baixa é {min(array_notas)}")
print(f"A nota mais alta é {max(array_notas)}")
print(f"A média de todas as notas é {(sum(array_notas) / len(array_notas))}")

### Table number, square and cube ###


print("Number\tSquare\tCube")

print("1\t"+str(square_number(1))+"\t"+str(square_number(1)*1))
print("2\t"+str(square_number(2))+"\t"+str(square_number(2)*2))
print("3\t"+str(square_number(3))+"\t"+str(square_number(3)*3))
print("4\t"+str(square_number(4))+"\t"+str(square_number(4)*4))
print("5\t"+str(square_number(5))+"\t"+str(square_number(5)*5))

###############################################################

x = randint(0,99)
print(x)

y = int(input("Give a number: "))

if y == x:
    print ("Great!! You got it!!")
else:
    print("Try more later...!!")

###############################################################
# Convert pounds for Kg
###############################################################

weight = float(input("What is your weight (in pounds)? "))

print(f"{weight*0.45} Kg")

###############################################################
# THE PROGRAMMER IS BUILT FOR CAR RUN ON THE STREET
###############################################################
command = ""
tries_car_run = 0
tries_car_stop = 0

while command.lower() != "quit":
    command = input("> ").lower()

    if command == "help":
        print('''start - to start the car\nstop - to stop the car\nquit - to exit''')
    elif command == "start" and tries_car_run == 0:
        tries_car_stop = 0
        print("Car started... Ready to go!")
        tries_car_run += 1
    elif command == "start" and tries_car_run >= 1:
        print("Car is already run")
    elif command == "stop" and tries_car_stop == 0 and tries_car_run == 1:
        tries_car_run = 0
        print("Car stopped.")
        tries_car_stop += 1
    elif command == "stop" and tries_car_stop >= 1:
        print("Car is already stopped")
    elif command == "stop" and tries_car_run == 0 and tries_car_stop == 0:
        print("Car isn't run")
    elif command == "quit":
        exit(0)
    else:
        print("I don't understand that...")

###############################################################
# Write a program to read the dimensions of rectangle
# (base and height) calculate and showing the total area.
###############################################################
base = float(input("Input the value of base: "))
height = float(input("Input the value of height: "))

area_rect = base * height
print (f"The area of rectangle is {area_rect}")

###############################################################
# Escreva um programa para ler o número total de eleitores de um município, o
# numero de votos brancos, nulos e válidos. Apresente a percentagem que cada
# um representa em relação ao total de eleitores.
###############################################################
city = input("Where do you vote? ")
votes = int(input("How many votes? "))
blank_votes = int(input("How many blank votes do you have? "))
null_votes = int(input("How many null votes do you have? "))
valid_votes = votes - blank_votes - null_votes
people = 15325

# Use f-string formatting to control decimal places for percentages
percentage_blank_votes = (blank_votes / votes) * 100 if valid_votes > 0 else 0  # Handle zero division
percentage_null_votes = (null_votes / votes) * 100 if valid_votes > 0 else 0
percentage_votes = (votes / people) * 100 if valid_votes > 0 else 0

print (f'''
There are {percentage_votes:.2f}% votes in {city}, which {valid_votes} votes are valid.
At last elections, there was {percentage_blank_votes:.2f} % of electors did a blank vote and {percentage_null_votes:.2f}% for null votes.
''')


##########################################
# Print the following number pattern
##########################################

rows = 5
line = 0
for num in range(rows, 0, -1):
    line += 1
    for time in range(1, num + 1):
        print(line, end=' ')
    print('\r')

#######################################
# Calculate the sum of price of products there in store shop.
#######################################
prices = [22,10,5,5,8,3]
total_prices = 0

for total in prices:
    total_prices += total

print(f"o valor total é {total_prices}")

#########################################
# Get a largest number in a list variable
#########################################
number_list = [10,2,20,14,3,7,1,4,5]

size = number_list[0]

for number in number_list:
    if number > size:
        size = number

print(size)

######### other example ###############

number_list = [10,10,20,20,2,7,7,5]
check = number_list[0]
number = 0
numbers_list = []

for number in number_list:
    if number not in numbers_list:
        numbers_list.append(number)

for number in number_list:
    if number_list.count(number) > 1:
        number_list.remove(number)

print(number_list)
print(numbers_list)

#####################################
# Using emojis
#####################################

message = input("> ")
print(emojis(message))

########################################################
# Create a file excel with some columns and values
# using the module openpyxl to built the file
########################################################


wb = Workbook()
ws = wb.active
data = [
    ["Data Subscribe","Value Subscribe","Data Renew","Debs Tax","Recover"],
    ["28/12/2022",100, '28/03/2023', "284%","TRUE" ],
    ["06/01/2023",4000, '06/04/2023', "3,09%","TRUE" ],
    ["23/01/2023",1100, '23/04/2023', "3,09%","TRUE" ],
    ["06/03/2023",2000, '06/06/2023', "3,50%","TRUE" ],
    ["22/05/2023",2000, '22/08/2023', "3,50%","TRUE" ],
    ["31/07/2023",3000, '31/10/2023', "2,75%","TRUE" ],
    ["25/09/2023",2500, '25/12/2023', "2,75%","TRUE" ],
    ["01/02/2024",3000, '01/05/2024', "2,75%","FALSE" ],
    ["27/03/2024",1500, '27/06/2024', "2,75%","FALSE" ],
   ]

for r in data:
    ws.append(r)

wb.save(filename='teste_file.xlsx')

################################################################							
## Livro de Introduçcao a Algoritmia e Programação com Python ##
################################################################
	
#### E.2.1.1 Exercise 1, Page 256 ####

A, B = 4.0, 6.0
I = 3

C = A * B - I
print(f"The result of the first operation is {C}")
K = I / 4 * 6
print(f"The result of the second operation is {K}")
C = B / A + 1.5
print(f"The result of the third operation is {C}")
K = math.trunc(B / A + 4.7)
print(f"The result of the fourth operation is {K}")
J = round(A / (5 / I))
print(f"The result of the fifth operation is {J}")
K = abs(A - B) * 2 + I
print(f"The result of the sixth operation is {K}")

#### E.2.1.1 Exercise 2, Page 256 ####

a, b, c, d, e, f = 1, 5, 3, 6, 5, 4

print(f"The result of the first operation is {a/b + 1}") 
print(f"The result of the second operation is {(a + b) / (c-d)}")
print(f"The result of the third operation is {a + (b/c) / d + (e/f)}")
print(f"The result of the fourth operation is {a + (b / (c - d))}")
print(f"The result of the fifth operation is {(a+b) * b/d}")
print(f"The result of the sixth operation is {((a+b) ** c)**d}")
print(f"The result of the seventh operation is {math.sin(a) + math.cos(a)/math.tan(a):2f}")
print(f"The result of the eight operation is {float(-b + math.sqrt(b**2 - 4*a*c)/2*a):2f}")

#### E.2.1.4 Exercise 4, Page 257 ####




print("""##### MENU #####\n(1) Hamburger -> 6,50€\n(2) Cheeseburger -> 7,50€\n(3) Sheep -> 3, 50€\n(4) Ice Tea -> 0,70€
(5) Shake milk -> 0,80€\n""")

qtd_hamb = int(input("quantity of Hamburger: "))
qtd_cheese = int(input("quantity of Cheeseburger: "))
qtd_sheep = int(input("quantity of Sheep: "))
qtd_tea = int(input("quantity of Ice Tea: "))
qtd_shake = int(input("quantity of Shake milk: "))
subtotal = calc_price(qtd_hamb, qtd_cheese, qtd_sheep, qtd_tea, qtd_shake)

total = subtotal * 0.23
print(f"The total of the shop is {total:.2f} €.\nThanks for your visit!! See you soon!!\n")


#### E.2.2.1 Exercise 5, Page 257 ####

print("Let's calculate the quadratic equation:")
A = int(input("Define the value of coefficient a: "))
B = int(input("Define the value of coefficient b: "))
C = int(input("Define the value of coefficient c: "))
formula_delta(A, B, C)

#### E.2.2.2 Exercise 6, Page 257 ####




cost_factory = int(input("What's factory cost for a new car??\n"))
consumer_price(cost_factory)


#### E.2.2.3 Exercise 7, Page 258 ####




s1 = int(input("Measure 1: "))
s2 = int(input("Measure 2: "))
s3 = int(input("Measure 3: "))

calc_area(s1, s2, s3)


#### E.2.2.4 Exercise 8, Page 258 ####



number = float(input("Input the number float: "))
round_number(number)


#### E.2.2.4 Exercise 8, Page 258 ####




round_number(float(input("Input the number float: ")))

#### E.2.2.5 Exercise 9, Page 258 ####


name = input("What's your name? ")
first_exam = int(input("What's first exame note? (%) "))
second_exam = int(input("What's second exame note? (%) "))
work_exam = int(input("What's work exame note? (%) "))

thought_exame(first_exam, second_exam, work_exam)

#### E.2.2.6 Exercise 10, Page 258 ####



base = float(input("What's the measure of base of triangle? "))
hight = float(input("What's the measure of hight of triangle? "))
calc_area(base, hight)

#### E.2.2.7 Exercise 11, Page 259 ####

import colorama
from colorama import Style, Fore
listA = ['Vista Alegre', 'Quinta Nova','Magres']
listB = ['Teka', 'MarketShop','Porcel']
listC = ['Cimpor', 'AEK','Mitsub']

value_pol = float(input("What's rate of polution? "))

if  value_pol >= 0.05 and value_pol <= 0.29:
    print(Fore.GREEN + Style.BRIGHT + "Good!! You contribute for a greeen environment!! 🍀")
if value_pol >= 0.30 and value_pol <= 0.39:
    print(Fore.YELLOW + Style.BRIGHT + f"{listA} should suspend operations until values will be normal!!")
if value_pol >= 0.40 and value_pol <= 0.49:
    print(Fore.YELLOW + Style.BRIGHT +f"{listA + listB} should suspend operations until values will be normal!!")
if value_pol >= 0.50:
    print(Fore.RED + Style.BRIGHT + f"{listA + listB + listC} all activities should be suspended!! ")

#### E.2.2.8 Exercise 12, Page 259 ####

number = int(input("Type an integer value: "))

if number % 2 == 0:
    print(f"The number {number} is pair")
else:
    print(f"The number {number} is not pair")

#### E.2.2.8 Exercise 12, Page 259 ####
