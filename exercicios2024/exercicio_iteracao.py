frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum'
i = 0
vezes = 0
letra = ""

while i < len(frase):
    letra_atual = frase[i]

    numero_vezes = frase.count(letra_atual)

    i += 1
    if letra_atual == " ":
        i += 1
        continue
    
    if vezes <= numero_vezes:
        vezes = numero_vezes
        letra = letra_atual
    
print(f'A letra que apareceu mais vezes foi {letra}, aparecendo {vezes}x')