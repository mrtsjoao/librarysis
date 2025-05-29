from Biblioetca import *
import os

#FLAG_TESTES apenas usa uma lista já preenchida com uns livros que eu coloquei, caso queira iniciar uma lista "biblioteca" do zero, basta mudar o valor para False

FLAG_TESTES = True
if FLAG_TESTES == True:
    biblioteca = [{'nome': 'Dom Casmurro', 
                'autor': 'Machado de Assis',
                'ano': 1899},
              
              {'nome': 'Memórias do Subsolo', 
                'autor': 'Fiodor Dostoievsk',
                'ano': 1864},
              
              {'nome': 'Crime e castigo', 
                'autor': 'Fiodor Dostoievsk',
                'ano': 1866},
              
              {'nome': 'Memórias Póstumas', 
                'autor': 'Machado de Assis',
                'ano': 1881}]
else:
    biblioteca = []


while True:
    print('\n========== Menu ==========\n')
    print('1 - Cadastrar Livro')
    print('2 - Listar livros')
    print('3 - Procurar Livro')
    print('4 - Remover livro')
    print('0 - Sair')
    print('\n============================\n')
    
    opcao = int(input('Escolha uma opção: '))
    
    limparTela()
    
    match opcao:

        case 1:
            cadastraLivros(biblioteca)   
            limparTela() 
        case 2:
            listarLivros(biblioteca)
        case 3:
            livro = input('Qual livro deseja consultar? ')
            consulta = buscaLivro(livro, biblioteca)
            
            if not consulta:
                print('\nLivro indisponível na nossa biblioteca!\n')
            else:
                print('\nLivros disponíveis:\n')
                listarLivros(consulta)
                print()
        case 4:
            
            livroARemover = input('\nInforme o livro que deseja remover da biblioteca: ')
            resultado = removerlivro(livroARemover, biblioteca)
            
            if resultado is True:
                print('\nLivro removido com sucesso!\n')
                input('\nPressione Enter para continuar...')
                limparTela()
        case 0:
            
            sair = input('\nDeseja sair? [S]SIM [N]NÃO\n').capitalize().startswith('S')
            
            if sair is True:
                break