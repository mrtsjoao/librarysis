from Biblioetca import *

FLAG_TESTES = True
if FLAG_TESTES == True:
    biblioteca = [{'nome': 'Dom Casmurro', 
                'autor': 'Machado de Assis',
                'ano': 1899},
              
              {'nome': 'Memórias do Subsolo', 
                'autor': 'Fiodor Dostoievsk',
                'ano': 1864},
              
              {'nome': 'Crime e castígo', 
                'autor': 'Fiodor Dostoievsk',
                'ano': 1866},
              
              {'nome': 'Memórias Póstumas', 
                'autor': 'Machado de Assis',
                'ano': 1881}]
else:
    biblioteca = []

while True:
    print('========== Menu ==========\n')
    print('1 - Cadastrar Livro')
    print('2 - Listar livros')
    print('3 - Procurar Livro')
    print('4 - Remover livro')
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
        case 4:
            
            livroARemover = input('\nInforme o livro que deseja remover da biblioteca: ')
            removelivro(livroARemover, biblioteca)
            
            if removelivro == True:
                print('\nLivro removido com sucesso!\n')