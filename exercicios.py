# # 1 - Faça um programa que solicite um número do usuário e apresente a seguinte mensagem na tela:
# # "O número digitado foi [número]"
numero_usuario= input('Digite um número: ')
print(f"O número digitado foi {numero_usuario}")

# # 2 - Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome completo do usuário na tela.
nome=input('Qual seu nome?\n')
sobrenome=input('Qual seu sobrenome?\n')
print(f'Seu nome completo é {nome} {sobrenome}')

# # 3 - Faça um programa que solicite três números inteiros do usuário e imprima a soma destes.
numero1=int(input('Escreva o primeiro número: '))
numero2=int(input('Escreva o segundo número: '))
numero3=int(input('Escreva o terceiro número: '))
print(f'A soma dos três números inseridos é: {numero1+numero2+numero3}')

# # 4 - Escreva um programa que solicite duas notas do usuário e apresente a média na tela da seguinte forma:
# # "A média das notas [nota1] e [nota2] é [média]".
nota1=float(input('Insira sua primeira nota: '))
nota2=float(input('Agora, insira a sua segunda nota: '))
media=float(nota1+nota2/2)
print(f'A media das notas {nota1 } e {nota2} é {media}')

# # 5 - Faça um programa que calcule a raiz quadrada de um número. O usuário deve inserir um número e o programa deve mostrar na tela o resultado da raiz quadrada do número inserido.
# numero=float(input('Insira um número para calcular sua raiz: '))
raiz=(numero)**1/2
print(f'A raiz quadrada do número {numero} é {raiz}')

# # 6 - Escreva um programa que faça a conversão de um dado valor de metro para quilômetro. 
metro=float(input('Insira o valor de metro: '))
km=metro/1000
print(f'Resultado é: {km}KM')

# # 7 - Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela a área da circunferência.
# # Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.
# # Dica: você pode usar a biblioteca math para pegar a constante pi.
pi=float(3.14)
raio=float(input(f'Insira o valor do raio: '))
raiopotencia=raio**2
area=pi*raiopotencia
print(f'Valor da área é: {area}')

# # 8 - Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela:
# "Seja bem-vindo [nome] [sobrenome]."
# "Você possui [idade] anos de idade."
# # No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e depois da string, enquanto que o último permite colocar a string no formato Title(). (capitaliza a string).
nome= input('Escreva seu nome: ').strip()
sobrenome=input('Agora seu sobrenome: ').strip()
idade=int(input('Informe sua idade: ').strip())
print(f'Seu nome é {nome} {sobrenome} e sua idade {idade}')

# # 9 - Elabore um programa para calcular a hipotenusa de um triângulo.
cateto1 = float(input('Me informe o cateto1= '))
cateto2 = float(input('E o cateto2= '))
print(f'Valor da hipotenusa: {(cateto1**2+cateto2**2)**(1/2)}')

# # 10 - Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.
numero=int(input('Informe o número da tabuada: '))
print(f'{numero} X 1= {numero*1}')
print(f'{numero} X 2= {numero*2}')
print(f'{numero} X 3= {numero*3}')
print(f'{numero} X 4= {numero*4}')
print(f'{numero} X 5= {numero*5}')
print(f'{numero} X 6= {numero*6}')
print(f'{numero} X 7= {numero*7}')
print(f'{numero} X 8= {numero*8}')
print(f'{numero} X 9= {numero*9}')
print(f'{numero} X 10= {numero*10}')