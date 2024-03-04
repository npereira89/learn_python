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