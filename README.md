# DIO_Bootcamp_Backend_Python
Domine a sintaxe e fundamentos do Python, trabalhe com estruturas de dados, listas e dicionários, manipule strings e crie sistemas interativos, utilize Git e GitHub para versionamento de código e criar APIs com FastAPI e banco de dados SQL.

# Introdução ao Python
* Multiplataforma (Windows, MAC, Linux)
* Tipologia dinâmica e forte
* Multiparadigma (Orientado a objeto, Procedural, etc.)
* Código aberto com grande comunidade que colabora para desenvolvimento

# Para Executar código Python
É necessário um interpretador que vem junto ao instalar o Python3

## É possível executar direto no terminal
* Digitar python no terminal
* Realizar as operações que quiser

## Em modo interativo 
* Digitar o comando:  python -i script.py
* Permite interagir com o script.py

# Boas Práticas em Python
* O padrão de nomes (métodos e variáveis) deve ser _snake case_. 
* Escolher nomes sugestivos.
* Não existe uma palavra para indicar o valor de uma constante, há apenas a convenção a seguir:  
  Constantes são escritas com letras maiúsculas

# Dicas práticas
## Função dir()
Retorna lista de atributos do objeto
## Função help()
Apresenta documentação módulos, métodos, etc. de um elemento (objeto, atributo, etc.)
## Função input()
Lê dados da entrada padrão (teclado) e exibe na saída padrão (console). Lê o teclado, cnverte o dado lido em string e retorna o valor convertido na tela.  
nome = input("Informe o seu nome: ")
## Função print()
Exibe dados na saída padrão (console).  
* Recebe um argumento obrigatório e 4 opcionais
     - string inicial a ser processada e exibida é o obrigatória
     - sep imprime os objetos com o sep entre eles
     - end termina os objetos
     - Todos os objetos são convertidos para string


# Tipos de variáveis em Python
* Numéricos: int, float, complex
     - Complex é pouco usado  
* String: Sequencia de caracteres
     - Podem ser declarados como "string", 'string', "'string'", """string"""
* Sequência: list, tuple, range
* Mapa: dictionary
     - Conjunto de chave e conteúdo
* Coleção: set, fronzenset
     - Se difere de sequência por não permitir repetir itens
* Booleano: bool
     - É o tipo int em que zero é falso e o resto é true
* Binário: bytes, bytearray, memoryview

# Converter tipos
## Numéricos
preco = 10   ->   inteiro  
preco/2      ->   a divisão gera um float 5.0  
preço//2     ->   duas barras faz manter o inteiro no resultado da divisão  
float(preço) ->  converte o inteiro preço em float 10.0

## Numérico para string
texto = fpreço = {preco}"  -> converte a variável preco em string para compor a variável texto

## String para Numérico
preco_str = "10.50"           -> preco_str é uma string  
preco_flt = float(preco_str)  -> converte a string preco_str em float para compor a variável preco_flt  







