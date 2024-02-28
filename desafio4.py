# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
cadastro = {'nome': 'Maria', 'idade': 30, 'cidade': 'São Paulo'}

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
cadastro['idade'] = 31
# Adicione um campo de profissão para essa pessoa;
cadastro['profissao'] = 'Programadora'
# Remova um item do dicionário.
del cadastro['cidade']

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
# numeros = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dicionario = {'a': 1, 'b': 2, 'c': 3}
if 'a' in dicionario:
    print('A chave "a" existe no dicionário.')

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = 'Olá, meu nome é Danilo e sou aprendiz de programador e pretendo me tornar mais uma pessoa de nome chamado Danilo que tem otimo still de programador'
frequencia = {}  # Cria um dicionário vazio
palavras = frase.split()  # Divide a frase em palavras

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1  # Incrementa a frequência da palavra
print (frequencia)