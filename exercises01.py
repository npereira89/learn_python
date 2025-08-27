#####################################
##				   ##
##  EXERCICIOS GERADOS POR CHATGPT ##
##				   ##
#####################################

from datetime import datetime, timedelta
import random
from colorama import Fore

class Person:
    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age

def greeting_funct(person):
    now = datetime.datetime.now()
    mood = "Morning" if now.hour < 12 else "Afternoon"
    return print(f"Good {mood}, {person}!! Have a nice day!")

def calculator(numb1, number2):
    return print(f"""\nSum: {numb1}+{number2}={int(numb1 + number2)}
Subtract: {numb1}-{number2}={int(numb1 - number2)}
Multiply: {numb1}*{number2}={int(numb1 * number2)}
Division: {numb1}/{number2}={float(numb1 / number2)}
""")

def is_pair(number):
    if number % 2 == 0:
        return print("The number is pair")
    else:
        return print("The number isn't pair")

def double_numb(num):
    return num * 2

def celsius_para_fahrenheit(celsius_temp):
    return (celsius_temp * 9 / 5) + 32

def revert_phrase(string):
    return string[::-1]

def get_vowel(string):
    vowel = "aeiouAEIOU"
    count = 0
    for letra in string:
        if letra in vowel:
            count += 1
    return count

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return factorial(n - 1) * n


###### BASICO ######


##################################
## EXERCICIO 1
## Crie um programa que solicite ao usuário o nome 
## e imprima uma saudação personalizada. 
##################################

name = input("Name? ")
greeting_funct(name)

#################################
## EXERCICIO 2
## Faça um programa que receba dois números e exiba 
## a soma, subtração, multiplicação e divisão entre eles.
#################################

value1 = int(input("Number 1: "))
value2 = int(input("Number 2: "))
calculator(value1, value2)

#################################
## EXERCICIO 3
## Escreva um programa que verifique se um número fornecido 
## pelo usuário é par ou ímpar.
#################################

value = int(input("Number: "))
is_pair(value)

#################################
## EXERCICIO 4
## Crie uma função que receba um número e retorne o dobro desse número.
#################################

number = int(input("Number to double: "))
print(f"The double is {double_numb(number)}")

#################################
## EXERCICIO 5
## Faça um programa que converta uma temperatura de Celsius para Fahrenheit.
#################################

value_celsius = int(input("Temperature Celsius: "))
print(f"The double is {celsius_para_fahrenheit(value_celsius)}")


###### INTERMEDIO ######

##################################
## EXERCICIO 1
## Desenvolva um programa que leia uma lista de números inteiros e exiba 
## apenas os números pares.
## Nota: ordenado do menor para o maior (desafio meu).
##################################

numeros_aleatorios = set()

while len(numeros_aleatorios) < 10:
    numero = randint(1, 50)
    if numero % 2 == 0:
        numeros_aleatorios.add(numero)

print(sorted(numeros_aleatorios))

##################################
## EXERCICIO 2
## Crie uma função que receba uma string e retorne a string invertida.
##################################

phrase = input("Input the phrase: ")
print(revert_phrase(phrase))

##################################
## EXERCICIO 3
## Escreva um programa que conte quantas vogais existem em uma frase fornecida pelo usuário.
##################################

phrase = input("Input the phrase: ")
print(get_vowel(phrase))

##################################
## EXERCICIO 4
## Faça um programa que calcule o fatorial de um número utilizando uma função recursiva.
##################################

num = int(input("Number: "))
print(factorial(num))

##################################
## EXERCICIO 5
## Crie um programa que leia uma lista de números e exiba o maior e o menor número da lista.
##################################

listnum = []
for _ in range(10):
    numero = randint(1, 40)
    listnum.append(numero)

print(listnum)
print(f"Da lista gerada o valor minimo é {min(listnum)} e o máximo {max(listnum)}")


###### AVANÇADO ######

##################################
## EXERCICIO 1
## Implemente um algoritmo para ordenar uma lista de números utilizando o método Bubble Sort
##################################

listnum = []
for _ in range(10):
    numero = randint(1, 40)
    listnum.append(numero)

print(sorted(listnum))

##################################
## EXERCICIO 2
## Crie um programa que leia um arquivo de texto e conte o número de palavras que ele contém.
##################################

with open('words_to_cv.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(len(words))

##################################
## EXERCICIO 3
## Escreva um programa que implemente um jogo de adivinhação em que o 
## usuário deve adivinhar um número aleatório
##################################

tries, x = 3, 0
sort_numb = randint(1, 40)

while x != tries:
    guess_n = int(input("Guess number between 1 and 40: "))
    if guess_n <= 40:
        x += 1
        if x <= tries:
            if guess_n == sort_numb:
                print(Fore.GREEN, "Get it!! Congrats 🍀")
                exit(1)
            if guess_n != sort_numb and x == tries:
                print(Fore.MAGENTA, "Game over 😔")
    else:
        print(Fore.MAGENTA, "The value isn't between the range")

##################################
## EXERCICIO 4
## Desenvolva uma classe chamada 'Pessoa' com atributos como nome e idade, 
## e métodos para exibir essas informações.
##################################

# Create instances of the Person class
your_person = Person("Hector", 12)
your_person1 = Person("Delson", 25)
your_person2 = Person("Nuno", 35)

print(f"Hello, {your_person.name}. I'm {your_person.age} yo.")  # Output: Buddy
print(f"Hello, {your_person1.name}. I'm {your_person1.age} yo.")  # Output: Buddy
print(f"Hello, {your_person2.name}. I'm {your_person2.age} yo.")  # Output: Buddy

##################################
## EXERCICIO 5
## Crie uma função que resolva o problema da 'Torre de Hanói' para 
## um número de discos fornecido pelo usuário.
##################################

def torre_hanoi(n, orig, dest, aux):
    if n == 1:
        print(f"Move disco 1 from {orig} to {dest}")
        return
    torre_hanoi(n - 1, orig, aux, dest)
    print(f"Move disco {n} from {orig} to {dest}")
    torre_hanoi(n - 1, aux, dest, orig)


discos = int(input("Give number of disco: "))
torre_hanoi(discos, 'A', 'C', 'B')

