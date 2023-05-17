a = '              Hello World                '
print(len(a)) #len conta os caracteres, mas precisa usar o print para mostra

txt = "Macarrão é bom."
b= "Amanhã vai ser treino de costas"
texto= 'O abacate, também conhecido como "a manteiga verde", é uma fruta tropical versátil e deliciosa. Sua casca áspera e esverdeada esconde uma polpa cremosa e rica em nutrientes, que oferece uma infinidade de benefícios para a saúde. Com seu sabor suave e textura aveludada, o abacate é frequentemente utilizado em pratos salgados e doces ao redor do mundo. Desde guacamoles picantes até smoothies refrescantes, essa fruta é verdadeiramente um curinga culinário. Além disso, o abacate é um ingrediente popular em dietas saudáveis, pois é uma excelente fonte de gorduras saudáveis, fibras, vitaminas e minerais essenciais.'
lista= b.split("vai")
print(len(txt))
print(txt.find('bom')) #Find busca na string

print(txt.upper()) # CAIXA ALTA
print(txt)
print(txt.lower()) # CAIXA BAIXA
print(a)
print(a.strip()) # REMOVE ESPAÇOS EM BRANCO
print(txt.replace("ã" , "a")) #TROCA DE LETRAS, PALAVRAS, NUMEROS, FODA-SE
print(b.split(" ")) # QUEBRA STRING E TRANSFORMA EM LISTA
print(lista[2])
print(len(texto.split(" ")))