Exercício 1

 valor1 = float(input("Digite o primeiro valor: "))
 valor2 = float(input("Digite o segundo valor: "))
 if valor1 > valor2:
 maior = valor1
 else:
 maior = valor2
 print("O maior número é:", maior)

 Exercício 2

 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 if num1 < num2:
 print("O menor número é:", num1)
 else:
 print("O menor número é:", num2)

 Exercício 3

 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 if num1 < num2:
 print("O menor número é:", num1)
 elif num2 < num1:
 print("O menor número é:", num2)
 else:
 print("Ambos os números são iguais.")

 Exercício 4

 nome1 = input("Digite o nome do primeiro funcionário: ")
 salario1 = float(input("Digite o salário do primeiro funcionário: "))
 nome2 = input("Digite o nome do segundo funcionário: ")
 salario2 = float(input("Digite o salário do segundo funcionário: "))
 if salario1 > salario2:
 print(nome1, "ganha mais que", nome2, "e a diferença é de R$", salario1- salario2)
 elif salario2 > salario1:
 print(nome2, "ganha mais que", nome1, "e a diferença é de R$", salario2- salario1)
 else:
 print("Os funcionários ganham o mesmo salário.")

Exercício 5

 peso = float(input("Digite o seu peso: "))
 altura = float(input("Digite sua altura: "))
 imc = peso / (altura ** 2)
 classificacao = ""
 if imc < 18.5:
 classificacao = "Abaixo do peso"
 elif 18.5 <= imc <= 24.9:
 classificacao = "Peso ideal"
 else:
 classificacao = "Acima do peso"
 print("Seu IMC é:", imc)
 print("Classificação:", classificacao)

 Exercício 6

 idade = int(input("Digite a sua idade: "))
 sexo = input("Digite o seu sexo (M para masculino ou F para feminino): ")
 if idade >= 18 and sexo == 'F':
 print("Você é maior de idade e do sexo feminino.")
 else:
 print("Você não atende aos critérios de ser maior de idade e do sexo feminino.")

 Exercício 7

 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 num3 = float(input("Digite o terceiro número: "))
 maior = num1
 medio = num2
 menor = num3
 if medio > maior:
 maior, medio = medio, maior
 if menor > medio:
 medio, menor = menor, medio
 if medio > maior:
 maior, medio = medio, maior
 print("Os números ordenados do maior para o menor são:", maior, medio, menor)

Exercício 8

 num1 = int(input("Digite o primeiro número: "))
 num2 = int(input("Digite o segundo número: "))
 resultado = num1 + num2
 if resultado > 0:
 if resultado % 2 == 0:
 print("+par")
 else:
 print("+ímpar")
 elif resultado < 0:
 if resultado % 2 == 0:
 print("-par")
 else:
 print("-ímpar")
 else:
 print("zero")

 Exercício 9

 valor1 = float(input("Digite o primeiro valor: "))
 valor2 = float(input("Digite o segundo valor: "))
 soma = valor1 + valor2
 if soma == 40 or (25 <= soma <= 33):
 print("É isso aí")
 else:
 print("A soma não atende às condições especificadas")

 Exercício 10

 idade = int(input("Digite a idade da pessoa: "))
 if idade >= 18:
 print("Pode entrar no bar no Brasil (maior de 18 anos)")
 if idade >= 21:
 print("Pode entrar no bar nos Estados Unidos (maior de 21 anos)")
 if idade < 18:
 print("A pessoa não é maior de idade para entrar no bar")

Exercício 11

 idade = float(input("Digite sua idade: "))
 altura = float(input("Digite sua altura: "))
 acomp = float(input("Se estiver acompanhado digite 1 se não 2: "))
 if(idade >= 16 and altura >= 1.60):
 print("Pode ir para os brinquedos")
 elif(idade >= 16 and altura >= 1.50 and acomp == 1):
 print("Pode ir para os brinquedos pois está acompanhado")
 elif(idade >= 16 and altura >= 1.50 and acomp == 2):
 print("Você não pode ir para os brinquedos pois não está acompanhado")
 elif(idade >= 18 and altura < 1.50):
 print("Você precisa assinar um termo para usar os brinquedos")
 elif(idade < 18 and altura < 1.50):
 print("Desculpe, você não pode usar os brinquedos vá para um passeio menor perigoso")
 else:
 print("Desculpe, você não pode usar os brinquedos vá para um passeio menos perigoso")