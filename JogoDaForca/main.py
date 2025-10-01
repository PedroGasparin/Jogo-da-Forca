from forca import forca

secreta = "PYTHON"

tentativas = []
while True: 
    letra = input("Digite uma letra (ou 0 para sair): ").upper()
    if letra == "0":
        break
    tentativas.append(letra)

forca(secreta, tentativas)