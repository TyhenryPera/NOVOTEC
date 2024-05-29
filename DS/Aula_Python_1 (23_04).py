Exercício 1

 numero1 = float(input("Digite o primeiro número: "))
 numero2 = float(input("Digite o segundo número: "))
 numero3 = float(input("Digite o terceiro número: "))
 media = (numero1+numero2+numero3)/3
 print("A média é:", media)

 Exercício 2

 numero1 = float(input("Digite o primeiro número: "))
 numero2 = float(input("Digite o segundo número: "))
 soma = (numero1+numero2)
 print("A média é:", soma)

 Exercício 3

 idadeAnos = float(input("Digite sua idade:"))
 idadeDias = idadeAnos *365
 print("Seus dias de vida são: ",idadeDias)

 Exercício 4

 numero = float(input("Digite o primeiro número: "))
 quadrado = (numero*numero)
 print("O quadrado do seu número é:", quadrado)

 Exercício 5

 numero = int(input("Insira um número: "))
 if numero % 2 == 0:
 print(f"O número é par.", numero)
 else:
 print("O número é ímpar.", numero)

 Exercício 6

 metros = float(input("Digite a quantidade de metros: "))
 centimetros = metros * 100
 print ("A quatidade de metros é:",centimetros,metros)

 Exercício 7

 gph = float(input("Quanto você ganha por hora? "))
 hpm =float(input("Quantas horas você trabalhou no mês? "))
salariomensal = gph * hpm
 salario3meses = salariomensal * 3
 print("Seu salário em 3 meses seria de:", salario3meses)

 Exercício 8

 raio = float(input("Digite o raio do círculo: "))
 area = 3.14 * raio ** 2
 print("A área do círculo é:", area)

 Exercício 9

 lado = float(input("Insira o valor do lado do quadrado: "))
 area = lado * lado
 print("A área do quadrado é:", area)

 Exercício 10

 salario = float(input("Digite o salário total: R$"))
 print("Salário com aumento de 5%: R$",salario * 1.05)
 print("Salário com aumento de 15%: R$",salario * 1.15)
 print("Salário com aumento de 30%: R$",salario * 1.30)

 Exercício 11

 nome = input("Digite seu nome: ")
 idade = input("Digite sua idade: ")
 apelido = input("Digite seu apelido: ")
 print("Olá! Seja bem-vindo(a).Você tem", idade, "anos e seu apelido é", apelido