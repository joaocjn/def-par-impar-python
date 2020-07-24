#função: Definir se o número inserido é ímpar ou par
#autor: João Cândido

p = 0
i = 0

numero = int(input("Insira um número: "))

if numero % 2 == 0:
	p = numero
	print (p, "é um número par")
else:
	i = numero
	print (i, "é um número ímpar")