import banco


"""
exercicio 1:
Imprima somente os usuarios
Cuja emails contenham as letras:
'a' ou 'k' 'm' ou 'l'
cujas idades sejam Maior que 30
menor qu 40
""" 

for usuario in banco.lista_de_usuarios:
	email = usuario['email'].lower()
	idade = usuario['idade']

	condicao_1 = 'a' in email
	condicao_1 = condicao_1 or 'k' in email
	condicao_1 = condicao_1 or 'm' in email
	condicao_1 = condicao_1 or 'l' in email
	condicao_2 = idade > 30 and idade < 40
	
	if condicao_1 and condicao_2:
		print(usuario)
