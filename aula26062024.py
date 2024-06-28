# Teste simples de loop com lista
nome = ['teste']
for i in nome:
    print(i)
    
# Soma dos elementos de uma lista de números
numero = [0, 10, 100, 1000, 100023, 121432]
total = 0
for i in numero:
    total += i
print(total)

# Dicionário de cores e busca de uma cor
cores = {'branco': 'white', 'azul': 'blue', 'preto': 'black', 'verde': 'green'}
cor = input('Digite uma cor: ')
print(cores.get(cor, 'cor não cadastrada'))

# Loop de 0 a 9
for i in range(0, 10):
    print(i)

# Divisão inteira e resto
a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = 0
while a >= b:
    a = a - b
    c += 1
print(c, a)

# Loop entre dois números fornecidos
numI = int(input('Digite um número inicial: '))
numF = int(input('Digite o número final: '))
for i in range(numI, numF):
    print(i)

# Impressão de números ímpares entre 100 e 200
for i in range(100, 200):
    if i % 2 != 0:
        print(i)

# Leitura de 10 números e soma
nume = []
soma = 0
for i in range(10):
    numero = int(input('Digite um número: '))
    nume.append(numero)
    soma += numero

print('Os números digitados foram:', nume)
print('A soma dos números é:', soma)

# Cálculo da média de números pares
opcao = 1
x = 0
vetor = []
total = 0
while opcao == 1:
    numero = int(input('Digite um número: '))
    vetor.append(numero)
    x += 1
    if numero % 2 == 0:
        total += numero
    opcao = int(input('Digite 1 para continuar digitando e 0 para sair: '))
if x > 0:
    media = total / x
else:
    media = 0
print('A média dos valores digitados é:', media)

# Encontrar o menor valor digitado
pergunta = 1
leitura = []
#coloquei um try po que estava travando nessa parte e não entendi o porquê
try:
    while pergunta == 1:
        valor = int(input('Digite um número: '))
        leitura.append(valor)
        pergunta = int(input('Digite 1 para continuar e 0 para sair: '))
    if leitura:
        menorValor = min(leitura)
        print('O menor valor digitado foi', menorValor)
    else:
        print('Nenhum valor foi digitado.')
except:
    print('Erro em entender o numero digitado.')
# Validação de entrada para sexo
sexo = ''
while sexo.lower() not in ('m', 'f'):
    sexo = input('Digite seu sexo (M ou F): ').lower()
    
# Verificação de palíndromo
def verificaLetraInicialDaPalavra(pal):  
    if len(pal) == 0:
        return False
    else:
        return pal[0] == pal[-1]

pal = input('Digite uma palavra: ')
if verificaLetraInicialDaPalavra(pal):
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
