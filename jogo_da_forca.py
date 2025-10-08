chances = 6
adivinhaçoes = []
tentativasErradas = []
letrasUsadas = []

secreta = input("Digite a palavra secreta: ").strip().upper()

print("\nVai começar o jogo!")
print(f"Você tem {chances} chances.")

# Cria os espaços em branco
for i in range(len(secreta)):
    adivinhaçoes.append("_")

print(" ".join(adivinhaçoes))

while True:
    if chances == 0 or "".join(adivinhaçoes) == secreta:
        break  
    
    letra = input("\nDigite uma letra: ").upper()

    if letra in letrasUsadas and letra not in tentativasErradas :
        print(f"A letra '{letra}' já foi usada! Tente outra.")
        continue
    else:
        letrasUsadas.append(letra)

    if letra in secreta:
        print("Você acertou!")
        for i in range(len(secreta)):
            if letra == secreta[i]:
                adivinhaçoes[i] = letra
        print("Como estamos no momento:", " ".join(adivinhaçoes))
    else:
        if letra not in tentativasErradas:
            chances -= 1
            tentativasErradas.append(letra)
            print(f"Letra incorreta! Chances restantes: {chances}")
            print("Tentativas erradas até agora:", ", ".join(tentativasErradas))
        else:
            print("Essa letra ja foi usada!!")

if chances == 0:
    print("\nVocê perdeu! A palavra era:", secreta)
else:
    print("\nParabéns, você venceu! A palavra era:", secreta)