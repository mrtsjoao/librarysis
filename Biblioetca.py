
#Função cadastraLivro apenas solicita os dados do livro ao usuário
def cadastraLivros(biblioteca):
    livro= {
        'nome' : input('Informe o nome do livro que deseja cadastrar: '),
        'autor' : input('Informe o nome do autor: '),
        'ano' : int(input('Informe o ano de lançamento: '))
    }
    biblioteca.append(livro)

#Função listarLivros responsável por listar os livros cadastrados em uma biblioteca
def listarLivros(biblioteca):

    for livro in biblioteca:
        print('------------------------------')
        print(f'    Nome: {livro["nome"]}')
        print(f'    Autor: {livro["autor"]}')
        print(f'    Ano: {livro["ano"]}')
        print('------------------------------')

#A função buscaLivro recebe um nome, percorre a lista "biblioteca" e retorna os livros com mesmo nome
def buscaLivro(nomeLivro, biblioteca):
    
    retornaLivros = []
    
    for livro in biblioteca:
        if nomeLivro.lower().replace(' ', '') == livro['nome'].lower().replace(' ',''):
            retornaLivros.append(livro)
        return retornaLivros
        

