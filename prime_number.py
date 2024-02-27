def eh_primo(numero):

  if numero <= 1:
    return False
  elif numero <= 3:
    return True
  elif numero % 2 == 0 or numero % 3 == 0:
    return False
  
  i = 5

  while i * i <= numero:

    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6

  return True

numero = int(input("Input a number "))

if eh_primo(numero):
  print(f"The number {numero} is prime number!! :)")
else:
  print(f"The number {numero} isn't prime number!! :)")