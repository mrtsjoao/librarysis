
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
        
#A função removelivro recebe um livro e uma lista. Remove o livro recebido da biblioteca, caso o item seja removido retorna Tru, se não, retorna False

def removelivro(nomeLivro,biblioteca):
    
    for livro in biblioteca:
        
        if nomeLivro.lower().replace(' ', '') == livro['nome'].lower().replace(' ', ''):
            print('------------------------------')
            print(f'    Nome: {livro["nome"]}')
            print(f'    Autor: {livro["autor"]}')
            print(f'    Ano: {livro["ano"]}')
            print('------------------------------')
            confirma = input('\nDeseja exluir esse livro da biblioteca? [S]SIM [N]NÃO\n').capitalize().startswith('S')
            if confirma is True:
                biblioteca.remove(livro)
                return True
            else:
                return False
        else:
            print('O livro informado não foi encontrado ou já foi removido!\n')
            return False