# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
def par_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
def classificacao_idade():
    idade = int(input("Digite sua idade: "))
    if idade >= 0 and idade <= 12:
        print("Você é uma criança")
    elif idade >= 13 and idade <= 18:
        print("Você é um adolescente")
    elif idade > 18:
        print("Você é um adulto")
    else:
        print("Idade inválida")
        classificacao_idade()

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
def autenticacao():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == "admin" and senha == "admin":
        print("Autenticação realizada com sucesso!")
    else:
        print("Usuário ou senha inválidos")
        autenticacao()

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# # Caso contrário: o ponto está localizado no eixo ou origem.

def quadrante():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante")
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante")
    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante")
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante")
    else:
        print("O ponto está no eixo ou origem")