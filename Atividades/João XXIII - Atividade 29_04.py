Exercício 1

 def multiplicacao():
 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 resultado = num1 * num2
 return resultado
 print("Resultado da multiplicação: ", multiplicacao())

Exercício 2

 def addSobrenome(nome):
 sobrenome = "Silva"
 nome_completo = nome + " " + sobrenome
 return nome_completo
 nome_inserido = input("Insira o nome: ")
 print("Nome completo com sobrenome Silva:", addSobrenome(nome_inserido))