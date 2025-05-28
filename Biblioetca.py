biblioteca = []

#Função cadastraLivro apenas solicita os dados do livro ao usuário
def cadastraLivros(biblioteca):
    livro= {
        'nome' : input('Informe o nome do livro que deseja cadastrar: '),
        'autor' : input('Informe o nome do autor: '),
        'ano' : int(input('Informe o ano de lançamento: '))
    }
    biblioteca.append(livro)

#Auto explicativo
def listarLivros(listaLivros):

    for livro in listaLivros:
        print('------------------------------')
        print(f'    Nome: {livro["nome"]}')
        print(f'    Autor: {livro["autor"]}')
        print(f'        Ano: {livro["ano"]}')
        print('------------------------------')

#A função buscaLivro recebe um nome, percorre a lista "biblioteca" e retorna os livros com mesmo nome
def buscaLivro(nomeLivro):
    
    retornaLivros = []
    
    for livro in biblioteca:
        if nomeLivro.lower().replace(' ', '') == livro['nome'].lower().replace(' ',''):
            retornaLivros.append(livro)
            
    return retornaLivros

while True:
    print('========== Menu ==========\n')
    print('1 - Cadastrar Livro')
    print('2 - Listar livros')
    print('3 - Procurar Livro')
    print('============================\n')
    
    
    opcao = int(input('Escolha uma opção: '))
    
    match opcao:

        case 1:
            cadastraLivros(biblioteca)    
        case 2:
            listarLivros(biblioteca)
        case 3:
            print('Qual livro deseja consultar?')
            livro = input()
            listarLivros(buscaLivro(livro))