# PROGRAMA 1
numero = input("digite um numero inteiro: ")

try:
    numero = int(numero)
    if numero % 2 == 0:
        print("Numero PAR")
    else:
        print("Numero impar")

except:
    print("Voce não digitou um numero inteiro")
