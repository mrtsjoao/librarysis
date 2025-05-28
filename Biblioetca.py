estruturalivro = {
    'nome' : '',
    'autor' : '',
    'ano' : ''
    }

biblioteca = []

#Função cadastraLivro apenas solicita os dados do livro ao usuário
def cadastraLivros(livro, biblioteca):
    
    livro['nome'] = input('Informe o nome do livro que deseja cadastrar: ')
    livro['autor'] = input('Informe o nome do autor: ')
    livro['ano'] = int(input('Informe o ano de lançamento: '))
    
    biblioteca.append(livro)

#Auto explicativo
def listarLivros(listaLivros):

    for livro in listaLivros:
        print(f'    Nome: {livro['nome']}')
        print(f'    Autor: {livro['autor']}')
        print(f'        Ano: {livro['ano']}')
        print('---------------------')

#A função buscaLivro recebe um nome (do livro ou autor), percorre a lista "biblioteca" e retorna os livros com mesmo nome ou livros do mesmo autor

def buscaLivro(nomeLivro):
    
    retornaLivros = []
    
    for livro in biblioteca:
        if livro['nome'] == nomeLivro:
            retornaLivros.append(livro)
            
    return retornaLivros
