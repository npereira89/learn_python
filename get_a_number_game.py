## This application is built to get the number the machine get.
## The goal is catch the number between 1 and 100

import random
import os

def sorted_number():
    numbers = random.randrange(1, 100)
    return numbers

def check_if_is_got(get_number, get_number_sorted):

    if get_number < get_number_sorted:
        print("Above!!👆")
    elif get_number > get_number_sorted:
        print("Easy, not too high!! 😄")

get_number_sorted = sorted_number()
get_number = 0

for attemps in range(2, -1, -1):
                
    get_number = int(input("Figured out the number sorted!!: "))
    check_if_is_got(get_number, get_number_sorted)
    
    if get_number != get_number_sorted and attemps !=0:
        #attemps -=1
        print(f"You have {attemps} attemps")
    elif get_number == get_number_sorted:
        print("You get it!! You're the master!😊")
        os.sys.exit(0) 
    if attemps == 0:
        print(f"Game over!! The number was {get_number_sorted}")
        os.sys.exit(0)


