# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
numeros = list(range(1, 11))
for numero in numeros:
    print(numero)
nomes = ["João", "Maria", "Pedro", "Ana"]
anos = [1973, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for nome in nomes:
    print(nome)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for numero in numeros:
    if numero % 2 != 0:
        soma_impares += numero
print(soma_impares)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for numero in reversed(numeros):
    print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
tabuada = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
novos_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
try:
    for numero in novos_numeros:
        soma += numero
    print(f'A soma dos elementos é {soma}')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_valores = [1, 2, 3, 4, 5]

try:
    media = sum(lista_valores) / len(lista_valores)
    print(f'A media dos valores é {media}')
except Exception as e:
    print("A lista está vazia")