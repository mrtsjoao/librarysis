# Sistema de gerenciamento de biblioteca

A fim de aprimorar e colocar meu aprendizado em Python e Banco de Dados, decidi por criar um sistema de gerenciamento de biblioteca como forma de colocar meus estudos em prática.

Até o momento, a biblioteca funciona a partir de uma lista de dicionários, sendo cada dicionário um livro da biblioteca composto pelo nome do livro, autor e ano em que foi publicado.

## Funções
 O algoritmo conta com as seguintes funções até o monento
#### cadastraLivros
Função responsável pelo cadastro de um novo livro. Recebe a lista 'biblioteca', cria um dicionário 'livro' e solicita ao usuário preencher os dados do livro e adiciona-lo à lista.

#### listarLivros
Função responsável apenas por listar os livros. Recebe uma lista de livros e mostra no terminal da seguinte maneira:

    ---------------------
        Nome: ######
        Autor: ######
        Ano: ######
    ---------------------

#### buscaLivro

A função buscaLivro recebe o nome de um livro e retorna uma lista de livros com o mesmo nome.
