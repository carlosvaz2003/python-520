#!/usr/bin/python3
print('Hello, World')

#Interpolacao

lista_de_usuarios = [
  {
    "nome": "qMHHOwoAaYECgB",
    "idade": 49,
    "email": "yMEpqGsegWXw@4linux.com",
    "sexo": "?",
    "endereco": "Rua NIbCtFYJpZtRJg"
  },
  {
    "nome": "GJBxVjGYtVEqmRasx",
    "idade": 23,
    "email": "mBZWAcaUDCVioOQEdIu@4linux.com",
    "sexo": "?",
    "endereco": "Rua VFJGPBuNRnz"
  },
  {
    "nome": "TFeiNzjMuAfyYHksx",
    "idade": 39,
    "email": "BEjDyrdxPJoniHIDFgZ@4linux.com",
    "sexo": "?",
    "endereco": "Rua AEhMBiFAuGgSAiuIyx"
  },
  {
    "nome": "EguHnoFTrUAuUUoery",
    "idade": 37,
    "email": "QzqgJRboorIzKjKp@4linux.com",
    "sexo": "?",
    "endereco": "Rua LgktJSYDjo"
  },
  {
    "nome": "zDjQIfYyTwtzetXMJvDs",
    "idade": 25,
    "email": "CZBArUyyMa@4linux.com",
    "sexo": "F",
    "endereco": "Rua DEPwqBeLgyylX"
  },
  {
    "nome": "FDLtOesbqzdqzGe",
    "idade": 47,
    "email": "MakWfrgesmuBb@4linux.com",
    "sexo": "F",
    "endereco": "Rua qVLKGbVYOPRNTdrRYA"
  },
  {
    "nome": "xrffFndgNldHhb",
    "idade": 20,
    "email": "MUvdkHayaYULCTkSDH@4linux.com",
    "sexo": "F",
    "endereco": "Rua ZwkeJCYdeZgEcX"
  },
  {
    "nome": "RyfOocoNhyuEDSN",
    "idade": 50,
    "email": "ggQNSQvIOmDqZj@4linux.com",
    "sexo": "M",
    "endereco": "Rua kvvnDojQEMsHMXzc"
  },
  {
    "nome": "GAXCbICkOjzNZxU",
    "idade": 31,
    "email": "ClNJyJMhNfmTvyQxxYvQ@4linux.com",
    "sexo": "?",
    "endereco": "Rua yIParNvhlayIcGup"
  },
  {
    "nome": "wvaTNhfqPOlnt",
    "idade": 29,
    "email": "EwTJHbRTCrfYF@4linux.com",
    "sexo": "F",
    "endereco": "Rua bGCVdBFXSzcVBeLvKYUZ"
  },
  {
    "nome": "qhDBAYlbwaSMar",
    "idade": 27,
    "email": "AwDWEkwtZcGgaHlsaW@4linux.com",
    "sexo": "M",
    "endereco": "Rua hVYSkEHTmaBIJG"
  },
  {
    "nome": "fAZzfzvEySnSei",
    "idade": 44,
    "email": "wrzgKwORTAnliywEq@4linux.com",
    "sexo": "M",
    "endereco": "Rua cSdMqmMvebnTd"
  },
  {
    "nome": "HJBLhUuMHeAogrtbeq",
    "idade": 47,
    "email": "akKkICosKJbUdVcLTCnQ@4linux.com",
    "sexo": "F",
    "endereco": "Rua IhyoOwKTUCQlBvDuVVYS"
  },
  {
    "nome": "vEeSluRuOmIJTFrgNA",
    "idade": 35,
    "email": "wrCGKAsQRlWLKUSH@4linux.com",
    "sexo": "?",
    "endereco": "Rua ZRfcRxPsJPO"
  },
  {
    "nome": "OyehQbxCsnSGPBLcviBs",
    "idade": 23,
    "email": "fnndYbeFLPmhB@4linux.com",
    "sexo": "?",
    "endereco": "Rua cnquXCCUji"
  },
  {
    "nome": "JDZdCgzulyGWW",
    "idade": 30,
    "email": "brPbOrQBWfIBikDA@4linux.com",
    "sexo": "M",
    "endereco": "Rua HgtuwqKeMin"
  },
  {
    "nome": "MoinSGxEySEgrb",
    "idade": 36,
    "email": "qolygpBXCKEeur@4linux.com",
    "sexo": "?",
    "endereco": "Rua xoVGMdTrFKHboQRzFd"
  },
  {
    "nome": "XStrcVVPyieJJznYZ",
    "idade": 49,
    "email": "doKMuRYdKwolzgkq@4linux.com",
    "sexo": "M",
    "endereco": "Rua jeTpYoJAHnSeWAUWG"
  },
  {
    "nome": "uWVZbFSfdE",
    "idade": 30,
    "email": "WpRAukMAAygh@4linux.com",
    "sexo": "?",
    "endereco": "Rua QQvsljaHXnhqjHlg"
  },
  {
    "nome": "jgVjBVFVVKui",
    "idade": 43,
    "email": "SCUVGmVBRpREfAMIleo@4linux.com",
    "sexo": "?",
    "endereco": "Rua ioMdZJPBgdMUzWsDg"
  }
]

TEMPLATE = '{nome};{idade};{email};{sexo};{endereco};'

for usuario in lista_de_usuarios :
	if usuario['idade'] > 30:
		arquivo = TEMPLATE.format(nome=usuario['nome'],
								  idade=usuario['idade'],
								  email=usuario['email'],
								  sexo=usuario['sexo'],
								  endereco=usuario['endereco'])
		print(arquivo)

exit()
mensagem = 'Olá {nome} , seja bem vindo ao mundo do Python'
mensagem = mensagem.format(nome='Carlos Alberto Vaz da Silva')
print(mensagem)




exit()
n = 10
i = 0
j = 1

for x in range(n):
	j, i  = i + j, j

	print('Interacao :',x ,'Resultado :',j)



exit()
for letra in 'Carlos Alberto Vaz Da Silva':
	print(letra)

print('')
lista_de_numeros = [0,1,2,3,4,5,6,7,8,9]
for numero in lista_de_numeros:
	print(numero)
exit()
nome = input('Qual é a melhor liguagem de programação:')

if nome == 'python':
	print('Você acertou')
else:
	print('Errou :(')

