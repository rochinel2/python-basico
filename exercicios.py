import math
import random as rd

# # # 1 - Faça um programa que solicite um número do usuário e apresente a seguinte mensagem na tela:
# # # "O número digitado foi [número]"
# numero_usuario= int(input('Digite um número: '))
# print(f"O número digitado foi {numero_usuario}")

# # # 2 - Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome completo do usuário na tela.
# nome=input('Qual seu nome?\n')
# sobrenome=input('Qual seu sobrenome?\n')
# print(f'Seu nome completo é {nome} {sobrenome}')

# # # 3 - Faça um programa que solicite três números inteiros do usuário e imprima a soma destes.
# numero1=int(input('Escreva o primeiro número: '))
# numero2=int(input('Escreva o segundo número: '))
# numero3=int(input('Escreva o terceiro número: '))
# print(f'A soma dos três números inseridos é: {numero1+numero2+numero3}')

# # # 4 - Escreva um programa que solicite duas notas do usuário e apresente a média na tela da seguinte forma:
# # # "A média das notas [nota1] e [nota2] é [média]".
# nota1=float(input('Insira sua primeira nota: '))
# nota2=float(input('Agora, insira a sua segunda nota: '))
# media=float((nota1+nota2)/2)
# print(f'A media das notas {nota1 } e {nota2} é {media}')

# # # 5 - Faça um programa que calcule a raiz quadrada de um número. O usuário deve inserir um número e o programa deve mostrar na tela o resultado da raiz quadrada do número inserido.
# novaraiz=math.sqrt(10) #UTILIZANDO A BIBLIOTECA MATH
# print(novaraiz)

# numero=float(input('Insira um número para calcular sua raiz: '))
# raiz=(numero)**(1/2)
# print(f'A raiz quadrada do número {numero} é {raiz}')

# # # 6 - Escreva um programa que faça a conversão de um dado valor de metro para quilômetro. 
# metro=float(input('Insira o valor de metro: '))
# km=metro/1000
# print(f'Resultado é: {km}KM')

# # # 7 - Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela a área da circunferência.
# # # Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.
# # # Dica: você pode usar a biblioteca math para pegar a constante pi.
# pi=(3.14)
# raio=float(input(f'Insira o valor do raio: '))
# raiopotencia=raio**2
# area=pi*raiopotencia
# print(f'Valor da área é: {area}')

# # # 8 - Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela:
# # "Seja bem-vindo [nome] [sobrenome]."
# # "Você possui [idade] anos de idade."
# # # No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e depois da string, enquanto que o último permite colocar a string no formato Title(). (capitaliza a string).
# nome= input('Escreva seu nome: ').strip().title()
# sobrenome=input('Agora seu sobrenome: ').strip().title()
# idade=int(input('Informe sua idade: '))
# print(f'Seu nome é {nome} {sobrenome} e sua idade {idade}')

# # # 9 - Elabore um programa para calcular a hipotenusa de um triângulo.
# cateto1 = (float(input('Me informe o cateto1= ')))
# cateto2 = (float(input('E o cateto2= ')))

# print(f'Valor da hipotenusa: {round((cateto1**2+cateto2**2)**(1/2),2)}')

# # # 10 - Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.
# numero=int(input('Informe o número da tabuada: '))
# print(f'{numero} X 1= {numero*1}')
# print(f'{numero} X 2= {numero*2}')
# print(f'{numero} X 3= {numero*3}')
# print(f'{numero} X 4= {numero*4}')
# print(f'{numero} X 5= {numero*5}')
# print(f'{numero} X 6= {numero*6}')
# print(f'{numero} X 7= {numero*7}')
# print(f'{numero} X 8= {numero*8}')
# print(f'{numero} X 9= {numero*9}')
# print(f'{numero} X 10= {numero*10}')

# Exercicio 11 - Ler duas notas, calcular a média e informar se foi reprovado, aprovado ou se foi para recuperação. Aprovado > 7, Reprovado < 5, Recuperação >= 5.
# nota1=float(input('Informe a sua primeira nota: '))
# nota2=float(input('E a segunda nota: '))
# media= (nota1+nota2)/2
# print(f'Sua média foi: {media}')
# if media>7:
#     print('Parabéns! Você foi aprovado.')
# elif media>=5:
#     print('Você está de recuperação')
# else:
#     print('Você foi reprovado.')

# Exercicio 12 - Criar um pedra, papel ou tesoura.
# opcoes=['pedra', 'papel', 'tesoura']
# escolha1= input('Escolha entre pedra, papel ou tesoura: ').strip().lower()
# escolha2= rd.choice(opcoes)
# print(escolha2)
# if escolha1 in opcoes:
#     if escolha1=='pedra' and escolha2=='tesoura':
#         print('Parabéns! Você ganhou.')
#     if escolha1=='papel'  and escolha2=='pedra':
#         print('Parabéns! Você ganhou.')
#     if escolha1=='tesoura' and escolha2=='papel':
#         print('Parabéns! Você ganhou.')
#     if escolha1=='tesoura' and escolha2=='tesoura':
#         print('Empate. Tente novamente')
#     if escolha1=='papel' and escolha2=='papel':
#         print('Empate. Tente novamente')
#     if escolha1=='pedra' and escolha2=='pedra':
#         print('Empate. Tente novamente')
#     if escolha1=='tesoura' and escolha2=='pedra':
#         print('Você perdeu!')
#     if escolha1=='pedra'  and escolha2=='papel':
#         print('Você perdeu!')
#     if escolha1=='papel' and escolha2=='tesoura':
#         print('Você perdeu!')
# else:
#     print('Escolha uma das opções informadas.')

# Exercicio 13 - Ilha do tesouro
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# Introdução ao jogo
# print("Bem vindo a Ilha do Tesouro")
# print("Sua missão é achar e capturar o tesouro") 
# #Jogo
# escolha=input('Você encontrou dois caminhos. Escolha entre a esquerda ou a direita: ').lower()
# if escolha== "esquerda":
#     escolha2= input('Você chegou a um lago. Deseja esperar ou nadar? \n').lower()
#     if escolha2 == "esperar":
#         escolha3 = input("Como você esperou, agora há um barco na beira do lago. Agora tem uma casa com três portas: vermelha, amarela e azul. Qual você deseja escolher?\n").lower()
#         if escolha3 == "vermelha":
#             print("Uma sala pegando fogo. Fim do jogo")
#         elif escolha3 == "amarela":
#             print("Achou o tesouro. Você venceu!")
#         elif escolha3 == "azul":
#             print("Entrou em uma sala cheio de pragas malignas. Fim do jogo")
        
#         else:
#             print("Essa porta explodiu. Fim do jogo.")
#     else:
#         print('Você foi morto por um jacaré. Fim do jogo.')        
# else:
#       print('Você caiu em um buraco. Fim do jogo.')

# Exercicio 14: Escreva um programa que receba uma lista de 10 números. O programa deve retornar para o usuário duas novas listas, uma com os números pares e outra com os números ímpares. 
# Por exemplo, se a lista for [1, 2, 3, 4, 5, 6]:
# Lista Pares: = [2,4,6]
# Lista Impares: = [1,3,5]
# numero = [1,2,3,4,5,6,7,8,9,10]
# lista_par = []
# lista_impar = []
# for item in numero:
#     # se os itens(da lista de numeros) divididos por 2 tiverem resto 0,
#     if item%2==0:
#         # coloque este item dentro da variavel lista_par
#         lista_par.append(item)
        
#     # se não, 
#     #     coloque dentro da lista_impar
#     else:
#         lista_impar.append(item)
# print(lista_par)
# print(lista_impar)
        
# # Exercicio 15: Escreva uma programa que receba uma lista de números e retorne a soma de todos os elementos da lista. Por exemplo, se a lista for [1, 2, 3, 4], a função deve retornar 10.
# lista = []
# soma= 0
# for x in range(1,6):
#     numeros_usuario=int(input("Informe os números: "))
#     lista.append(numeros_usuario)

# for numero in lista:
#     soma=soma+numero
# print(soma)

# # Exercicio 16: Escreva uma função que receba uma lista de strings e retorne uma nova lista com as strings da lista original em maiúsculas. Por exemplo, se a lista for [“a”, “b”, “c”, “d”], a função deve retornar [“A”, “B”, “C”, “D”].
# lista = []

# for x in range(0,8):
#     x=input('Letra: ').upper()
#     lista.append(x)
# print(lista)

# # Exercicio 17: Escreva uma função que receba uma lista de números e retorne uma nova lista com os elementos da lista original multiplicados por 2. Por exemplo, se a lista for [1, 2, 3, 4], a função deve retornar [2, 4, 6, 8].
# lista = []
# multiplicar = int(input('Número: '))


# for numero in range(1,11):
#     informe=int(input('Lista: '))
#     lista.append(informe*multiplicar)

# print(lista)

# # Exercicio 18: Escreva uma função que receba uma lista de números e retorne uma nova lista com os números pares na ordem inversa e os números ímpares na ordem original. 
# # Por exemplo, se a lista for [1, 2, 3, 4, 5, 6], a função deve retornar [1, 3, 5, 6, 4, 2].
# lista_par = []
# lista_impar = []

# for x in range(1,11):
#     numeros=int(input('Números: '))
#     if numeros%2==0:
#         lista_par.append(numeros)

#     else:
#         lista_impar.append(numeros)

# lista_par.reverse()

# lista_par.extend(lista_impar)
# print(lista_par)

# Exercicio 19: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# letra=input('Digite uma letra: ').upper()

# if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
#     print('É uma vogal.')
# else:
#     print('Consoante.')

# Exercicio 20: Faça um Programa que leia três números inteiros e mostre o maior deles.
# lista=[]

# for x in range(1,4):
#     numeros=input('Número: ')
#     lista.append(numeros)
# print(lista)
# print(max(lista))

# Exercicio 21: Faça um Programa que leia três números e mostre-os em ordem decrescente. 
# lista = []

# for x in range(1,4):
#     numero=int(input('Número: '))
#     lista.append(numero)
# lista.sort(reverse=True)
# print(lista)

# Exercicio 22: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
# nota=int(input('Nota: '))

# while nota<11:
#     print(f'Sua nota é: {nota}')
#     break
# else:
#     print('Favor informar um número até 10')

# Exercicio 23: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 
# usuario=input('Usuário: ')
# senha=input('Senha: ')

# while usuario==senha:
#     print('Sua senha deverá ser diferente do usuário.')
#     senha = input('Senha: ')

# else:
#     print('Login feito com sucesso.')

# Exercicio 24: .Faça um programa que leia e valide as seguintes informações:
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';
# nome=input('Digite seu nome: ')
# while len(nome) <=3:
#     nome=input('Seu nome precisar ser maior que 3 caracteres. Digite novamente: ')

# idade=int(input('Idade: '))
# while (idade<1) and (idade>150):
#     idade=input('Sua idade precisa ter de 1 até 150 caracteres. Digite novamente: ')

# salario=float(input('Salário: R$'))
# while (salario==0):
#     salario=input('Seu salario informado precisa ser maior que 0. Digite novamente: ')

# sexo=input('Sexo(f ou m): ')
# while (sexo !="f") and (sexo !="m"):
#     sexo=input('Escolha entre "m" ou "f". Tente novamente: ').lower()

# civil=input('Estado civil(s,c,v,d): ').lower()
# while (civil!='s') and (civil!='c') and (civil!='v') and (civil!='d'):
#     civil=input('Opção incorreta. Escolha entre "s" de solteiro, "c" de casado, "v" viúvo ou "d" divorciado: ')

# else:
#     print('Cadastro feito com sucesso')

# Exercico 25: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
# numero=int(input('Insira um número:\n'))

# while (numero<1) or (numero>10):
#     numero=int(input('Escolha um número de 1 a 10:\n'))

# for x in range(1,11):
#     print(f'{x}x{numero}={x*numero}')

# Exercicio 26: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares:
# impares=int()
# pares=int()

# for x in range(1,11):
#     int(input('Insira 10 números: \n'))

# Não sei como vou fazer para separar os números impares e os pares.
# impares=(x%2!=0)
# pares=(x%2==0)

# Exercício 27: Jogo de Palavras

# Neste exercício, você deve criar um jogo de palavras em que o jogador deve adivinhar a palavra correta com base em uma dica. Use um dicionário para armazenar as palavras e suas respectivas dicas.

# Passo 1: Crie o dicionário de palavras e dicas  ex:
# palavras = {
#     "python": "Uma linguagem de programação popular.",
#     "banana": "Uma fruta amarela e doce.",
#     "abacaxi": "Uma fruta tropical com casca dura e espinhosa.",
#     "computador": "Uma máquina eletrônica que processa dados.",
#     "aviao": "Meio de transporte que voa pelos céus."
# }

# Passo 2: Escolha uma palavra aleatória para o jogador adivinhar

# Passo 3: Apresente a dica ao jogador e peça a resposta

# Passo 4: Verifique se a resposta está correta e informe o jogador
# ex:
# Parabéns! Você acertou a palavra!
# Infelizmente, você errou. A palavra correta era ...
# import random
# palavras={
# 'relógio': 'Este objeto tem ponteiros e é usado para medir o tempo.',
# 'espremedor de limão': 'Este objeto é usado na cozinha para extrair o suco cítrico de uma fruta.',
# 'binóculos': 'Este objeto é usado para ampliar a visão e observar objetos distantes.',
# 'chapéu de palha': 'Este objeto é usado na cabeça para proteger do sol e é comumente associado a ambientes tropicais.',
# 'abajur': 'Este objeto é usado como fonte de iluminação e geralmente é colocado em mesas ou criados-mudos.',
# 'martelo': 'Este objeto é uma ferramenta manual usada para bater em pregos ou quebrar coisas.',
# 'bola de futebol': 'Este objeto é redondo e usado em um esporte em que os jogadores chutam a bola para marcar gols.',
# 'binóculo astronômico': 'Este objeto é usado para observar o céu noturno e ampliar a visão de estrelas, planetas e outros corpos celestes.',
# 'mala': 'Este objeto é usado para armazenar roupas e outros itens pessoais durante viagens.',
# 'fone de ouvido': 'Este objeto é usado para ouvir música.'
# }
# objeto = random.choice(list(palavras.keys()))
# dica = palavras[objeto]

# print("Jogo de Palavras")
# print("Dica: " + dica)
# resposta = input("Digite a palavra: \n")
# if resposta.lower() == objeto:
#     print("Parabéns! Você acertou a palavra!")
# else:
#     print("Infelizmente, você errou. A palavra correta era", objeto + ".")

# Exercicio 28: Faça um programa que tenha uma função chama área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
# def área(b,h):
#     A=b*h
#     print(f'O valor da área é: {A}m²')


# b=float(input('Insira o valor da base: \n'))
# h=float(input('Insira o valor da altura: \n'))
# área(b,h)





    
