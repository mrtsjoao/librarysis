# Sistema de gerenciamento de biblioteca

A fim de aprimorar e colocar meu aprendizado em Python em prática, decidi criar um sistema simples de gerenciamento de biblioteca.

Até o momento, a biblioteca funciona a partir de uma lista de dicionários, sendo cada dicionário um livro da biblioteca, composto pelo nome do livro, autor e ano de publicação. O algoritmo roda no terminal, com um menu de opções digitadas pelo usuário.

Ainda pretendo aprimorar bastante, como salvar os livros em um arquivo .txt ou até mesmo utilizar um banco de dados com MySQL.



## Funções

O algoritmo conta com as seguintes funções até o momento:

#### cadastraLivros
Função responsável pelo cadastro de um novo livro.
Recebe a lista biblioteca, cria um dicionário livro e solicita ao usuário preencher os dados do livro, adicionando-o à lista.

#### listarLivros

Função responsável por listar os livros.
Recebe uma lista de livros e exibe no terminal da seguinte maneira:

    ---------------------
        Nome: ######
        Autor: ######
        Ano: ######
    ---------------------

#### buscaLivro

A função buscaLivro recebe o nome de um livro e uma biblioteca.
Retorna uma lista de livros com o mesmo nome. Caso o livro desejado não esteja na biblioteca, retorna uma lista vazia.

#### removelivro

A função removelivro é responsável por remover um livro da biblioteca.
Ela recebe o nome do livro que o usuário deseja remover, juntamente com a lista onde ele se encontra.

Se o livro estiver presente na lista, a função exibe os dados do livro e confirma com o usuário se está correto.
Caso sim, o livro é removido da lista e a função retorna True.

Se não, ou caso o livro não esteja presente na lista, a função retorna False.


## Como rodar o sistema

**1.** Clone ou baixe este repositório na sua máquina.

**2.** Certifique-se de ter o Python instalado (versão 3.x).

**3.** No terminal ou prompt de comando, navegue até a pasta do projeto.

Execute o comando:

    python main.py

O menu será exibido e você poderá interagir digitando os números correspondentes às opções desejadas.

## Futuras implementações

- Salvar os livros em um arquivo .txt.

- Criar um sistema de persistência com banco de dados MySQL.

- Adicionar mais campos ao livro, como editora e gênero.

- Criar uma interface gráfica com Tkinter ou Flet.

- Melhorar a validação de entradas do usuário.