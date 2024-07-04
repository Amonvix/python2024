# Programa 2

hora = input("Que horas são? : ")

try:
    horario = int(hora)

    if horario >= 0 and horario <= 11:
        print("Bom dia")
    elif horario >= 12 and horario <= 17:
        print("Boa tarde")
    elif horario >= 18 and horario <= 23:
        print("Boa noite")

    else:
        print("Não conheço essa hora")

except:
    print("Por favor digite numeros inteiros")

print(horario)
