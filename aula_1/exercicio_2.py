import banco

"""
Exercicio 2
Dada uma lista de numeros
escrever um algoritimo que calcula
a media dos numeros nesta lista
salvar em uma variavel e imprimir
"""

lista_de_numero = [1,2,3,4,5,6]
soma = 0
total_da_lista  = len(lista_de_numero)
total=0

for numero in lista_de_numero:
	soma  += numero
	total += 1 

media = soma/total
print('A Media',media)