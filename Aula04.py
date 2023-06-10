#SOMA
# def soma(a,b):
#     print(f'A = {a} e B = {b}')
#     s=a+b
#     print(f' a soma A + B = {s}\n')
# #Necessário pular duas linhas após definir parâmetros.

# #Programa Principal
# soma(10,20)

# soma(a=10,b=20)

# soma(a=20,b=10)

#CONTADOR
# def contador(*num):
#     tam=len(num)
#     print(f'Recebi valores {num} com o tamanho de {tam}')


# contador(1,2,3)
# contador(3,2,1)
# contador(6,2,6,8,9,2)

#DOBRAR
def dobra(lista):
    pos=0
    while pos<len(lista):
        lista[pos]*=2
        pos +=1


valores= [1,2,3,4,5,6,7,8,9,10]
dobra(valores)
print(valores)