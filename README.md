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
* Exemplos:
     - print("Hello World!")
     - print(f"Nome: {nome}")

## Função range()
Produz uma sequência de números inteiros
* Recebe um argumento obrigatório e 2 opcionais
     - stop é o obrigatório - indica o fim da sequência com exclusão do valorde stop
     - start opcional - indica o início da sequência, incluído o valor de start
     - step opcional - indica o passo entre os elementos da sequencia
* Exemplos
     - **range(4)** - retorna range(0,4) que é um range object, não a sequencia. Para gerar a sequencia é preciso usar list
                    **list(range(4))** -> retorna [0, 1, 2, 3]
     - **range(2,7)** - retorna range(2,7) que é um range object, não a sequencia. Para gerar a sequencia é preciso usar list
                       **list(range(2,7))** -> retorna [2, 3, 4, 5, 6]
     - **range(5,11,2)** -  retorna range(5,11,2) que é um range object, não a sequencia. Para gerar a sequencia é preciso usar list
                       **list(range(5,11,2))** -> retorna [5, 7, 9]

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

# Precedência de operadores aritméticos
* Parêntesis
* Expoentes (**)
* Multiplicação e divisão (da esquerda para a direita)
* Somas e subtrações (da esquerda para a direita)

# Operadores de comparação (número, string, etc.)
== verifica se valores são iguais
!= diferetes
/>= maior ou igual
/<= menor ou igual

# Operadores de atribuição
a = b  -> a recebe o valor de b
a += b  -> a recebe a soma do valor b ao valor atual de a (ou seja, a = a+b)
a -= b  -> a recebe a subtração do valor atual de a por b (ou seja, a = a-b)
a *= b  -> a recebe a multiplicação do valor b pelo valor atual de a (ou seja, a = a*b)
a /= b  -> a recebe a divisão(float) do valor atual de a pelo valor atual de b (ou seja, a = a/b)
a //= b  -> a recebe a divisão(inteira) do valor atual de a pelo valor atual de b (ou seja, a = a//b)
a %= b  -> a recebe o resto da divisão(inteira) do valor atual de a pelo valor atual de b (ou seja, a = a%b)
a/**= b  -> a recebe o resultado do valor atual de a elevado ao valor de b (ou seja, a = a/**b)

# Operadores de idantidade
is  -> verifica se a variável ocupa a mesma posição de memória
is not

# Operadores de associação
Verificam de um item está presente em uma sequência
Ex: curso = "Curso de Python"
    frutas = [maçã, uva, banana]
    saque = [1500, 100]

in  -->          "Python" on curso --> True
                 300 in saque  --> False
not in  -->      "limão" not in frutas --> True

# Estruturas condicionais
**if _condição1_:**
  _código do if_
**elif _condição2_:**
  _código do elif_
**else:**
  _código do else_

## if ternário
(_sucesso_) **if** (_condição_) **else** (_falha_)
Ex: "Saque permitido" **if** saldo >= saque **else** "Falha! Não há fundos."

# Estruturas de repetição
## **FOR**
**for** (_índice da iteração_) **in** (_elemento a ser iterado_)
* Exemplos:
     - **for** letra **in** texto
     - **for** indice **in** array
## **FOR/ELSE**
**for** (_índice da iteração_) **in** (_elemento a ser iterado_)
**else** _ação de fim de laço_
* Exemplo:
     - **for** letra **in** texto
         print(letra)
       **else** print("Fim do laço for!")
       
## **FOR RANGE**
**for** (_índice da iteração_) **range(start, stop, step)**
**else** _ação de fim de laço_
* Exemplo:
     - **for** numero **range(1,21,3)**
         print(numero)
       **else** print("Fim do laço for!")
       
## **WHILE**
**while** (_condição de parada da iteração_)**:**
* Exemplo:
     - **while** True:
           input("numero: ", numero)
           if (numero = 10):
               break
           if (numero = 15):
               continue
           print(numero)
       
       **else** print("Fim do laço while!")
