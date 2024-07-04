while True:
    numero_1 = input("Digite o primeiro numero: ")
    numero_2 = input("Digite o outro numero: ")
    operador = input("Digite o operador a ser usado '+-*/': ")

    numeros_validos = None
    num1_float = 0
    num2_float = 0
    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os numeros digitados são invalidos")
        continue

    operadores_permitidos = '+-*/'
    if len(operador) > 1:
        print("Digite apenas um Operador aceito")
        continue

    if operador not in operadores_permitidos:
        print("Operador não aceito")
        continue

    match operador:
        case '+':
            resposta = num1_float + num2_float
            print(resposta)
        case '-':
            resposta = num1_float - num2_float
            print(resposta)
        case '/':
            resposta = num1_float / num2_float
            print(resposta)
        case '*':
            resposta = num1_float * num2_float
            print(resposta)

    sair = input('Quer [S]air? ').lower().startswith('s')
    if sair is True:
        break
