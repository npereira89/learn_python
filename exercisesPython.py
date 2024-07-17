import os
import re
import time
import statistics
from random import randint
from datetime import datetime, timedelta
from array import array
import locale

### working with date ###

print(f"Date two days forward: {(datetime.now() + timedelta(2))}")
print(f"Date with date format: {time.strftime("%Y-%m-%d")}")

### working with dictionary ###
valor = {'m1': {'m2': 'Hi World', 'm3': 'Hello Mickey', "m4": "Hii Mr. Dolittle"}}

print(valor["m1"]["m3"])

### check number is pair or unpair ###

def is_pair(number):
    return number % 2 == 0

number = int(input("Input the number to check the number is pair or unpair: "))

if is_pair(number):
  print(f"{number} is pair.")
else:
  print(f"{number} is unpair.")

### Develop a program to store 4 notes on list and get avarage, max and minimun note ###

array_notas = []

for i in range(1,5):
    nota = int(input(f"Input the note {i}: "))
    array_notas.append(nota)
    i += 1

print(f"The avarage is {statistics.median(array_notas)}")
print(f"The maximun is {max(array_notas)}")
print(f"The minimun is {min(array_notas)}")

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

### Message ###
      
message = "Hello World"
print(message)

name_greet = input("Name: ")
print(f"Hello {name_greet}")

### Numbers ###

number = int(input("Write a number (not a float)"))
print(f"The number before is {number-1} and number after is {number+1}")

print(f"The number with 2 decimals {number:.2f} ")


### Develop a program to save a median

array_notas = [55,25,58,88,787,551]

print(f"The avarage is {round(statistics.mean(array_notas),2)}")


### Develop a program that change in real time a word Java for Python in sentence 

phrase = 'Exercises for Java'
print(phrase.replace("Java", "Python"))

### Title a string or full name ### 
full_name = ' nuno pereira '
print("Hello, " + full_name.strip() + "!")

### Table number, square and cube

def square_number(number):
    number *= number
    return number

print("Number\tSquare\tCube")

print("1\t"+str(square_number(1))+"\t"+str(square_number(1)*1))
print("2\t"+str(square_number(2))+"\t"+str(square_number(2)*2))
print("3\t"+str(square_number(3))+"\t"+str(square_number(3)*3))
print("4\t"+str(square_number(4))+"\t"+str(square_number(4)*4))
print("5\t"+str(square_number(5))+"\t"+str(square_number(5)*5))

## String module

import string
 
print(string.ascii_letters)  # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)   # Output: abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)   # Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)            # Output: 0123456789
print(string.hexdigits)         # Output: 0123456789abcdefABCDEF
print(string.punctuation)       # Output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.ascii_letters)     # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

def find_right_most_digit(text):
    count=0
    
    for ch in text:
        if ch.isdigit() == True:
            count += 1

    return count
         
            
print(find_right_most_digit('The value is 42 dsds2323'))  # Output: 2
print(find_right_most_digit('No digits heredssd34'))  # Output: -1

###############################################################################

x = randint(0,99)
print(x)

y = int(input("Give a number: "))

if y == x:
    print (f"Great!! You got it!!")
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
path = "C://Users/Nuno/Downloads"
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


message = input("> ")
print(emojis(message))

######################################
# Using class and constructor
#####################################

class Person:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def is_eligible(self):
        if self.age >= 18:
            print(f"Hi {self.name} \nYou can see pornography!!")
        else:
            print(f"Go away {self.name} \nYou are not allow to see pornography, cuz you're {self.age} yo!")


name_in = str(input("Name: "))
age_in = int(input("Age: "))

john = Person( str(name_in), int(age_in))
john.is_eligible()

########################################################
# Create a file excel with some columns and values
# using the module openpyxl to built the file
########################################################
import openpyxl
from openpyxl.workbook import Workbook

# wb = xl.load_workbook(filename='testes_afr.xlsx',read_only=False)
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
