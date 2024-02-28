import os
# restaurantes = ['Pizza','Sushi']
restaurantes = [{'nome':'Cantina','categoria': 'Italiano','Ativo': False}, {'nome':'Sushi','categoria': 'Japones','Ativo': True}, {'nome':'Torta','categoria': 'Massa','Ativo': False}]

def exibir_nome():
    '''Esta funçao é responsável por apresentar o nome do restaurante.'''
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)
    
def exibir_menu():
    '''Esta funçao é responsável por listar o meni principal.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurantes')
    print('4. Sair\n')

def voltar_menu_principal():
    '''Esta funçao é responsável por voltar  voltar para o menu principal.'''
    input('\nPressione qualquer tecla para voltar ao menu...')
    main()

def exibir_subtitulo(texto):
    '''Esta funçao é responsável por mostrar os subtítulos.'''
    os.system('clear')
    linha = '*' * len(texto)
    print(f'\n{linha}\n')
    print(f'{texto}\n')
    print(f'{linha}\n')

def cadastrar_novo_restaurante():
    '''Esta funçao é responsável por cadastrar novos restaurantes.
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona o nome e a categoria do restaurante na lista de restaurantes.
    - Exibe uma mensagem de sucesso.
    - Volta para o menu principal.
    
    '''
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'Ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    '''Esta funçao é responsável por listar todos os restaurantes.'''
    exibir_subtitulo('Listando restaurantes...')
    print('Nome do restaurante'.ljust(23) + ' | Categoria'.ljust(23) + ' | Status\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_menu_principal()

def ativa_desativa_restaurantes():
    '''Esta funçao é responsável por alterar o status dos restaurantes.'''
    exibir_subtitulo('Ativar/Desativar restaurantes...')
    
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if (nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            if (restaurante['Ativo']):
                restaurante['Ativo'] = False
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso!')
            else:
                restaurante['Ativo'] = True
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso!')
    voltar_menu_principal()

def selecionar_opcao():
    '''Esta funçao é responsável por selecionar a opçao desejada do menu principal.'''
    try:
        opcao = int(input('Digite a opção desejada: '))
        match opcao:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativa_desativa_restaurantes()
            case 4:
                finalizar_app()
            case _:
                print('Opção inválida\n')
                selecionar_opcao()
    except ValueError:
        print('Opção inválida\n')
        selecionar_opcao()
    # if (opcao == 1):
    #     print('Cadastrar restaurante')
    # elif (opcao == 2):
    #     print('Listar restaurantes')
    # elif (opcao == 3):
    #     print('Ativar restaurante')
    # elif (opcao == 4):
    #     finalizar_app()
    # else:
    #     print('Opção inválida\n')
    #     selecionar_opcao()

def finalizar_app():
    '''Esta funçao é responsável por finalizar o programa.'''
    exibir_subtitulo('Finalizando o programa...')
    exit()

def main():
    '''Esta funçao é responsável por iniciar o programa.'''
    os.system('clear')
    exibir_nome()
    exibir_menu()
    selecionar_opcao()

if __name__ == '__main__':
    '''Esta funçao é responsável por chamar a funçao principal.'''
    main()