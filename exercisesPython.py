import os
import re
import time
import string
import statistics
import locale
import openpyxl
import math
from random import randint
from datetime import datetime, timedelta
from array import array
from openpyxl.workbook import Workbook

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

### Sum two numbers using a function which use lambda function (MUST LEARN MORE ABOUT IT)

print(sum_values(5, 2))

### working with date ###

print(f"Date two days forward: {(datetime.now() + timedelta(2))}")
print(f"Date with date format: {time.strftime("%Y-%m-%d")}")

### working with dictionary ###
valor = {'m1': {'m2': 'Hi World', 'm3': 'Hello Mickey', "m4": "Hii Mr. Dolittle"}}

print(valor["m1"]["m3"])

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

### Message of gretting someone ###
      
name = input("What is your name? ")
print(f"Hello World {name}")

#### Try to show the name and the last name ####

greeting("Patricia Silva Santos Pereira")

### Figure out the next number and the ancestor number ####

get_latest_behind(99)

### Numbers exercises ###

number = int(input("Write a number (not a float)"))
print(f"The number before is {number-1} and number after is {number+1}")

# Get a float number with 2 decimais houses

print(f"The number with 2 decimals {number:.2f} ") 

### Develop a program to save a median rounded 2 decimal houses #####

array_notas = [55,25,58,88,787,551]

print(f"The avarage is {round(statistics.mean(array_notas),2)}")


### Develop a program that change in real time a word Java for Python in sentence 

phrase = 'Exercises for Java'
print(phrase.replace("Java", "Python"))

### Title a string or full name using a strip command ### 
full_name = ' nuno pereira '
print("Hello, " + full_name.strip() + "!")

### Table number, square and cube ###


print("Number\tSquare\tCube")

print("1\t"+str(square_number(1))+"\t"+str(square_number(1)*1))
print("2\t"+str(square_number(2))+"\t"+str(square_number(2)*2))
print("3\t"+str(square_number(3))+"\t"+str(square_number(3)*3))
print("4\t"+str(square_number(4))+"\t"+str(square_number(4)*4))
print("5\t"+str(square_number(5))+"\t"+str(square_number(5)*5))

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

###############################################################################

x = randint(0,99)
print(x)

y = int(input("Give a number: "))

if y == x:
    print ("Great!! You got it!!")
else:
    print("Try more later...!!")

###############################################################

name = input("What is your name? ")
fav_color = input("What is your favourite color? ")

print(f"{name} likes {fav_color}")
print(name + " likes " + fav_color)

###############################################################
# Convert pounds for Kg
###############################################################

weight = float(input("What is your weight (in pounds)? "))

print(f"{weight*0.45} Kg")
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

##########################################
# Calculate the sum of price of products there in store shop.
#######################################
prices = [22,10,5,5,8,3]
total_prices = 0

for total in prices:
    total_prices += total

print(f"o valor total é {total_prices}")
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

#####################################
# Using emojis
#####################################

message = input("> ")
print(emojis(message))

######################################
# Using class and constructor
#####################################


name_in = str(input("Name: "))
age_in = int(input("Age: "))

john = Person( str(name_in), int(age_in))
john.is_eligible()

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

#### E.2.2.9 Exercise 9, Page 258 ####
### It will be continue
