﻿Exercício 1 


vetor = [1, 2, 3, 4, 5]
soma = sum(vetor)
print(soma)


Exercício 2 


vetor = [1, 2, 3, 4, 5]
maior = max(vetor)
menor = min(vetor)


print("Maior elemento da lista:", maior)
print("Menor elemento da lista:", menor)


Exercício 3 


vetor = [1, 2, 3, 4, 5]
media = sum(vetor) / len(vetor or [0])
print("A média dos elementos é:", media)


Exercício 4 


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0


for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1


print('Quantidade de números pares:', pares)
print('Quantidade de números ímpares:', impares)


Exercício 5 


lista = [1, 2, 3, 4, 5]
lista_invertida = sorted(lista, reverse=True)


print(lista_invertida)


Exercício 6 


lista = [1, 2, 3, 4, 2, 5, 6, 3, 4]


nova_lista = list(set(lista))


print(nova_lista)


Exercício 7 


pessoas = [('Maria', 25), ('João', 30), ('Ana', 20)]


ordenada_por_nome = sorted(pessoas, key=lambda x: x[0])


print("Ordenado por nome:", ordenada_por_nome)


Exercício 8 


lista1 = [3, 1, 5]
lista2 = [2, 4, 6]


listacomb = lista1 + lista2


listacomb.sort()


print(listacomb)


Exercício 9 


lista = [1, 2, 3, 4, 1, 5, 1]
vlrnovo = 1
vlrantigo = 6


for i in range(len(lista)):
    if lista[i] == vlrantigo:
        lista[i] = vlrnovo


print(lista)


Exercício 10 


lista = [1, 2, 3, 4, 5]
valor = 3


if valor in lista:
    posicao = lista.index(valor)
    print((True, posicao))
else:
    print((False, None))

