import os
import re
import time
import string
import statistics
import locale
import openpyxl
import math
import numpy as np
from colorama import Fore, Style
from random import randint
from datetime import datetime, timedelta
from array import array
from openpyxl.workbook import Workbook

###############################
### ALL FUNCTIONS AND CLASS ###
###############################

class Person:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def is_eligible(self):
        if self.age >= 18:
            print(f"Hi {self.name} \nYou can see pornography!!")
        else:
            print(f"Go away {self.name} \nYou are not allow to see pornography, cuz you're {self.age} yo!")

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

def is_capt(s):
    chars = str.split(s, ' ')
    for i in chars:
        result = ''.join(i.capitalize())
    return print(result, end = ' ')

def split_and_join(line):
    text = line.split()
    return "-".join(text)
    
def mutate_string(string, position, character):
    text = string[:position] + character + string[position+1:]
    return text

##################################
### STRINGS AND CHAR EXERCISES ###
##################################

### Read a given string, change the character at a given index and then print the modified string.

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

### You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
#########################################
# Captalize the firts letter of the name
#########################################

name = input()
is_capt(name)

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

################################################################
# Program to open images files in Python
################################################################
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
####################################
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

###############################################################
# Check the name has between 3 and 50 characters. If the name
# is above 50 characters the name is wrong but it's minor
# 3 chars must be at least 3 chars too
###############################################################
name = input("What's your name? ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be 50 characters")
else:
    print("name looks good")

###############################################################

name = input("What is your name? ")
fav_color = input("What is your favourite color? ")

print(f"{name} likes {fav_color}")
print(name + " likes " + fav_color)

###############################################################
# Program to read a keyboard value and show last input value,
# through a array variable with 3 values.
###############################################################
valor = ["text_write"]
size_array = int(len(valor))

while size_array < 3:
    text = input("Put a value: ")
    valor.append(text)
    print(valor[size_array-1])
    size_array += 1

######################################
# Using class and constructor
#####################################


name_in = str(input("Name: "))
age_in = int(input("Age: "))

john = Person( str(name_in), int(age_in))
john.is_eligible()


##################################
### 	NUMBER EXERCISES       ###
##################################

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
## 	An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
## 	It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. 
## 	A leap year contains a leap day.
##
##	In the Gregorian calendar, three conditions are used to identify leap years:
##
##	The year can be evenly divided by 4, is a leap year, unless:
##	The year can be evenly divided by 100, it is NOT a leap year, unless:
##	The year is also evenly divisible by 400. Then it is a leap year.
##	This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
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



###############################################################################

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
########################################
# Remove the duplicates
########################################
number_list = [10,10,20,20,2,7,7,5]

check = number_list[0]
number = 0

for number in number_list:
    if number_list.count(number) > 1:
        number_list.remove(number)

print(number_list)
######### other example ###############
number_list = [10,10,20,20,2,7,7,5]
numbers_list = []

for number in number_list:
    if number not in numbers_list:
        numbers_list.append(number)

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

align_a = a/b + 1
print(f"The result of the first operation is {align_a}")
align_b = (a + b) / (c-d)
print(f"The result of the second operation is {align_b}")
align_c = a + (b/c) / d + (e/f)
print(f"The result of the third operation is {align_c}")
align_d = a + (b / (c - d))
print(f"The result of the fourth operation is {align_d}")
align_e = (a+b) * b/d
print(f"The result of the fifth operation is {align_e}")
align_f = ((a+b) ** c)**d
print(f"The result of the sixth operation is {align_f}")
align_g = math.sin(a) + math.cos(a)/math.tan(a)
print(f"The result of the seventh operation is {align_g:2f}")
align_h = -b + math.sqrt(b**2 - 4*a*c)/2*a
print(f"The result of the eight operation is {float(align_h):2f}")

#### E.2.1.4 Exercise 4, Page 257 ####

def calc_price(qtd_hmb, qtd_ch, qtd_shp, qtd_itea, qtd_shk):
    price = (qtd_hmb * 6.5) + (qtd_ch * 7.5) + (qtd_shp * 3.5) + (qtd_itea * 0.7) + (qtd_shk * 0.8)
    return float(price)


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


def formula_delta(value_a, value_b, value_c):
    delta = value_b**2 - (4 * value_a * value_c)
    if delta == 0:
        return print(f"The delta value is {delta}.\nThe discriminante is null")
    if delta > 0:
        return print(f"The delta value is {delta}.\nThe discriminante is positive")
    if delta < 0:
        return print("Not possible calculate the quadratic equation")


print("Let's calculate the quadratic equation:")
A = int(input("Define the value of coefficient a: "))
B = int(input("Define the value of coefficient b: "))
C = int(input("Define the value of coefficient c: "))
formula_delta(A, B, C)

#### E.2.2.2 Exercise 6, Page 257 ####

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


cost_factory = int(input("What's factory cost for a new car??\n"))
consumer_price(cost_factory)


#### E.2.2.3 Exercise 7, Page 258 ####

def calc_area(side1, side2, side3):
    if side1 >= 0 and side2 >= 0 and side3 >= 0:
        a = side1 + side2 + side3 / 2
        area = math.sqrt(a * (a - side1) * (a - side2) * (a - side3))
        return print(f"The value of area is {area:.2f} m2")
    else:
        print("Not possible calculate area of triangle, because one of the values are not positive")


s1 = int(input("Measure 1: "))
s2 = int(input("Measure 2: "))
s3 = int(input("Measure 3: "))

calc_area(s1, s2, s3)


#### E.2.2.4 Exercise 8, Page 258 ####

def round_number(value):
    valor_approach = round(value, 0)
    if valor_approach > value:
        return print(f"The excess approach is {valor_approach:.0f}")
    else:
        return print(f"The default approach is {value:.0f}")


number = float(input("Input the number float: "))
round_number(number)


#### E.2.2.4 Exercise 8, Page 258 ####

def round_number(value):
    valor_approach = round(value, 0)
    if valor_approach > value:
        return print(f"The excess approach is {valor_approach:.0f}")
    else:
        return print(f"The default approach is {value:.0f}")


round_number(float(input("Input the number float: ")))

#### E.2.2.5 Exercise 9, Page 258 ####

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

name = input("What's your name? ")
first_exam = int(input("What's first exame note? (%) "))
second_exam = int(input("What's second exame note? (%) "))
work_exam = int(input("What's work exame note? (%) "))

thought_exame(first_exam, second_exam, work_exam)

#### E.2.2.6 Exercise 10, Page 258 ####

def calc_area(ba, alt):
    area = (ba * alt) / 2
    return print(f"The area of triangle is {area:.2f}")

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
