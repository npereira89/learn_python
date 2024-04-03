import os
import re
import time
import statistics
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

