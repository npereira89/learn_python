import os, time

def convert_cels_fahre(valor_to_convert):

    fahrenheit = round((valor_to_convert*(9/5)) +32,3)

    print(f"{valor_to_convert} ºC --> {fahrenheit} ºF")
    return fahrenheit

def convert_fahre_cels(valor_to_convert):
    
    celsius = round((valor_to_convert-32) / 1.79999999,3)

    print(f"{valor_to_convert} ºF --> {celsius} ºC")
    return celsius

valor_to_convert = int(input("Input the Fahrenheit temperatures: "))

convert_fahre_cels(valor_to_convert)
convert_cels_fahre(valor_to_convert)

time.sleep(20)
