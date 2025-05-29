from Biblioetca import *

biblioteca = []

while True:
    print('========== Menu ==========\n')
    print('1 - Cadastrar Livro')
    print('2 - Listar livros')
    print('3 - Procurar Livro')
    print('\n============================\n')
    
    opcao = int(input('Escolha uma opção: '))
    
    match opcao:

        case 1:
            cadastraLivros(biblioteca)    
        case 2:
            listarLivros(biblioteca)
        case 3:
            livro = input('Qual livro deseja consultar? ')
            consulta = buscaLivro(livro, biblioteca)
            
            if not consulta:
                print('\nLivro indisponível na nossa biblioteca!\n')
            else:
                print('\nLivros disponíveis:')
                listarLivros(consulta)
                print()