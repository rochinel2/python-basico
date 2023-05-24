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

#Exercicio 11 - Ler duas notas, calcular a média e informar se foi reprovado, aprovado ou se foi para recuperação. Aprovado > 7, Reprovado < 5, Recuperação >= 5.
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

#Exercicio 12 - Criar um pedra, papel ou tesoura.
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

#Exercicio 13 - Ilha do tesouro
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
# #Introdução ao jogo
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
