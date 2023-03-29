# Introdução ao Python

## Variáveis, expressões e sentenças

### Valores e tipos
Um **valor** é uma das unidades básicas no qual um programa trabalha, como uma letra ou um número. Alguns exemplos são: 1, 5 e 'Olá, Mundo!'.

Estes valores são de **tipos** diferentes: 1 e 5 são inteiros e 'Olá, Mundo!' é uma string.

A função `type` informa qual tipo um valor é:
```
>>> type(3.2)
<type 'float'>
```

#### Conversão (casting)

Podemos converter o tipo de um valor para outro tipo. Exemplo: float -> int, string -> int, etc...

### Variáveis

Uma **variável** é um nome que se refere a um valor.

Um **comando de atribuição** cria uma nova variável e lhes atribui valores.

Criamos uma variável digitando um nome, seguido do símbolo = e depois o valor da variável.
```
nome = 'Elvin'
dia = 29
distancia = 5.7
mes = 'Outubro'
```

### Nomes de variáveis e palavras-chave

**Nomes de variáveis** precisam começar com uma letra.

É permitido começar com letras maiúsculas e com sublinhado, mas é ideal começar com letras minúsculas.

O sublinhado pode aparecer em um nome. É comumente usado em nomes com múltiplas palavras, como *my_name*.

O interpretador usa **palavras-chave** para reconhecer a estrutura do programa, e eles não podem ser usadas como nomes de variáveis. Exemplo: and, del, from, not,....

### Operadores e operandos

**Operadores** são símbolos especiais que representam computações como adição e multiplicação. Os valores no qual o operador são aplicados são chamados de **operandos**

### Expressões e Sentenças

Uma **expressão** é uma combinação de valores, variáveis e operadores. Um valor sozinho é considerado uma expressão, assim como uma variável. Exemplo
```
13
x
x + 13
```

Uma **sentença** é uma unidade de código que o interpretador Python pode executar. O comando de atribuição é um tipo de sentença.

### Ordem das Operações

Quando mais de um operador aparecem em uma expressão, a ordem de avaliação dependem das **regras de precedência**. Para os operadores matemáticos, Python segue a convenção matemática:
- Parênteses;
- Exponenciação;
- Produto;
- Operadores com a mesma precedência são avaliados da esquerda para a direita (exceto exponenciação). 
-
### Operador de módulo

O **operador de módulo** funciona em números inteiros e produz o resto da divisão do primeiro operando divido pelo segundo. Em Python, o operador de módulo é representado pelo símbolo de porcentagem (%).
```
>>> resto = 7 % 3
>>> print(resto)
1
```
### Operações com strings

O operador + entre strings realiza uma concatenação.
```
>>> primeiro = 'para'
>>> segundo = 'lelo'
>>> print(primeiro + segundo)
paralelo
``` 

O operador * entre string e inteiro realiza repetição.
```
>>> 'Spam' * 3
SpamSpamSpam
```

### Comentários

Para adicionar **comentários** em um programa em Python, utilizamos o símbolo #.
```
# Comentário de uma linha
print('Hello, world!')
# Comentário
# em mais de uma
# linha
```

Para adicionar comentários em múltiplas linhas, utilizamos o símbolo """
```
"""
This is a comment
written in
more than just one line
"""
```

### Entrada de Dados

A função `input` obtém o valor do teclado.
```
>>> nome = input("Qual o seu nome?")
```

### Saída de Dados

A função `print` imprime na tela o conteúdo passado como argumento.
```
>>> print("Olá, mundo!")
Olá, mundo!
```

### Blocos ou Escopo

Conjunto de ações com uma função definida.
Um algoritmo pode ser visto como um bloco.
Define os limites nos quais as variáveis declaradas em seu interior são conhecidas.
Em Python:
	- O número de espaços (tab) no começo da linha indica o bloco;
	- Os blocos são construídos adicionando-se tab's no começo de cada linha.

## Estrutura Sequencial

Instruções são executadas linearmente na ordem em que foram escritas:
	- de cima para baixo;
	- da esquerda para direita.
Em Python, cada instrução ocupa uma linha.

# [Trabalho Prático 1](https://github.com/elvinmatheus/universidade/tree/main/Fundamentos%20de%20Programa%C3%A7%C3%A3o/3.%20Introdu%C3%A7%C3%A3o%20ao%20Python/Trabalho%20Pr%C3%A1tico%201)

Questões tiradas do URI (Atualmente BeeCrowd)

1. 1001 - Extremely Basic
2. 1002 - Area of a Circle
3. 1005 - Average 1
4. 1006 - Average 2
5. 1011 - Sphere
6. 1013 - The Greatest
7. 1014 - Consuption
8. 1015 - Distance between two points
9. 1017 - Fuel Spent

# Referencias Bibliográficas

- DOWNEY, A. Think Python: How to Think Like a Computer Scientist.
