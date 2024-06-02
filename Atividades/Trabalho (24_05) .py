forca = "churrasco"
letras_corretas = set(forca)
letras_descobertas = set()
erros = 0

print("Bem-vindo ao Jogo de Adivinhar Palavras!")

while True:
    letra = input("Digite uma letra: ").lower()

    if letra in letras_corretas:
        letras_descobertas.add(letra)
        print("Correto!")
    else:
        erros += 1
        print("Errado! Você tem", 3 - erros, "tentativas restantes.")

    print("Palavra:", ''.join(l if l in letras_descobertas else '_' for l in forca))

    if letras_corretas == letras_descobertas:
        print("Parabéns! Você acertou a palavra secreta:", forca)
        break

    if erros == 3:
        print("Você errou 3 vezes! A palavra secreta era:", forca)
        break
