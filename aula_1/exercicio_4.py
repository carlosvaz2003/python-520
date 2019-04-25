"""

"""
import banco

 

acertos = 0

while acertos < 3:
	for usuario in banco.lista_de_usuarios:
		idade =  usuario['idade']
		idade_entrada  = input('Digite sua idade :')

		if int(idade_entrada) in range(idade - 15 , idade + 15):
			acertos +=1
			print('Acertou !!!',acertos)
			if acertos > 3:
				break
		else:
			print('Errou !!!',idade)



