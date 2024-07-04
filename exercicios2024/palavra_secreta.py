import os
palavra_secreta = "avaliador"
palavra_exibida = "*" * len(palavra_secreta)
palavra_exibida_nova = ''
i = 0


while True:
    letra_digitada = input("Tente adivinhar a palavra digitando uma letra: ").lower()
    i += 1
    

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra de cada vez! ")        
        i += 1
        continue


    if letra_digitada in palavra_secreta:
        palavra_exibida_nova += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_exibida_nova:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print('Palavra formada',palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("PARABENS!!! VOCE ACERTOU")
        print('A palavra secreta era, ', palavra_secreta)
        print(f'Foram usadas {i} tentativas para achar a palavra!')
        break
    