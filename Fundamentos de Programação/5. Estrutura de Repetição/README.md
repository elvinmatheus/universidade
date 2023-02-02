# Estrutura de Repetição

## Atualizando variáveis

Uma das formas mais comuns de atribuição é uma atualização de variáveis, onde o novo valor da variável depende do valor anterior.

```python
x = x + 1 #Esta atribuição significa "pegue o valor atual de x, adicione um, e então atualize o valor de x com o novo valor."
```

Antes de atualizar uma variável, você precisa inicialiá-la, normalmente com uma simples atribuição:

```python
x = 0
x = x+1
```

Atualizar uma variável adicionando 1 é chamada de **incremento**; subtraindo de 1 é chamada de **decremento**.

## Estrutura de Repetição em algoritmo

Uma estrutura de repetição é utilizada quando um trecho do algoritmo, ou até mesmo o algoritmo inteiro, precisa ser repetido. O número de repetições pode ser fixo ou estar atrelado a uma condição.

### Estrutura de repetição para número definido de repetições (estrutura PARA)
Essa estrutura de repetição é utilizada quando se sabe o número de vezes que um trecho do algoritmo deve ser repetido.

```
PARA I <- valor_inicial ATÉ valor_final FAÇA [PASSO n]
INÍCIO
	comando1
	comando2
	...
	comandom
FIM
```

O comando1, comando2, ..., e comandom serão executados utilizando a variável I como controle, e seu conteúdo vai variar do valor_inicial até o valor_final. A informação do PASSO está entre colchetes porque é opcional. O PASSO indica como será a variação da variável de controle. Por exemplo, quando for indicado PASSO 2, a variável de controle será aumentada em 2 unidades a cada iteração até atingir o valor_final. Quando a informação do PASSO for suprimida, isso significa que o incremento ou o decremento da variável de controle será de 1 unidade.

### Estrutura de repetição para número indefinido de repetições e teste no início (estrutura ENQUANTO)

Essa estrutura de repetição é utilizada quando não se sabe o número de vezes que um trecho do algoritmo deve ser repetido, embora também possa ser utilizada quando se conhece esse número.

Essa estrutura baseia-se na análise de uma condição. A repetição será feita enquanto a condição se mostrar verdadeira.

Existem situações em que o teste condicional da estrutura de repetição, que fica no início, resulta em um valor falso logo na primeira comparação. Nesses casos, os comandos escritos dentro da esrtutura de repetição não serão executados.

```
ENQUANDO condição FAÇA
INÍCIO
	comando1
	comando2
	...
	comandom
FIM
```

### Estrutura de repetição para número indefinido de repetições e teste no final (estrutura REPITA)

Essa estrutura de repetição é utilizada quando *não* se sabe o número de vezes que um trecho do algoritmo deve ser repetido, embora também pode ser utilizada quando se conhece esse número.

Essa estrutura baseia-se na análise de uma condição. A repetiçao será feita até a condição se tornar verdadeira.

A diferença entre a estrutura ENQUANTO e a estrutura REPITA é que, nessa última, os comandos serão repetidos pelo menos uma vez, já que a condição se encontra no final.

```
REPITA
comandos
ATÉ condição
```

Repita os comandos até a condição se tornar verdadeira.

## Estruturas de repetição em Python

### `for` (PARA) em Python

O laço `for`, em Python, é executado sobre um conjunto conhecido de itens. Assim, são executadas tantas iterações quantos forem os itens no conjunto. Exemplos de conjunto de elementos são listas de palavras, linhas em um arquivo ou uma lista de números.

```python
friends = ['Fulano', 'Ciclano', 'Beltrano']
for friend in friends:
	print("Feliz ano novo, ", friend)
print("Feito!")
```

### A sentença `while` (ENQUANTO) em Python

O funcionamento da sentença `while` é semelhante ao encontrado em outras linguagens de programação.

Podemos usar `while`, em Python, para substituir a sentença `for`.

```python
n = 5
while n > 0:
	print(n)
	n = n - 1
print("Feito!)
```

Este tipo de fluxo é chamados de **loop**. O corpo do **loop** deve conter uma ou mais variáveis de controle, de modo que o loop possa ter um fim. Caso não haja, teremos um loop infinito.

#### Loops infinitos

Quando não há nenhuma variável de iteração para indicar quantas vezes executar o loop, temos um loop infinito.

```python
n = 10
while True:
	print(n)
	n = n - 1
print("Feito!")
```

O loop acima é um loop infinito porque a expressão lógica na sentença `while` é simplesmente a constante lógica `True`.

##### O comando `break`

Para sair de um loop infinito, devemos inserir no corpo da sentença `while` o comando `break`:

```python
while True:
	line = input('> ')
	if line == 'done':
		break
	print(line)
print("Done!)
```

##### O comando `continue`

Para saltar da iteração atual e saltar imediatamente para a próxima iteração, nós utilizamos o comando `continue`.

```python
while True:
	line = input("> ")
	if line [0] == '#':
		continue
	if line == 'done':
		break
	print(line)
print("Done!")
```
Exemplo de execução do programa:

```
> olá
olá
> # Não imprima isso
> imprima isso
imprima isso
> done
Done!
```

### A sentença do-while (REPITA-ENQUANTO) em Python

Python não possui um comando explícito para criar um laço do-while como em outras linguagens. Mas é possível emular o loop em Python.

```python
secret_word = "python"
counter = 0

while True:
	word = input("Enter the secret word: ").lower()
	counter = counter + 1
	if word == secret_word:
		break
	if word != secret_word and counter > 7:
		break
```

O código irá rodar pelo menos uma vez, perguntando pela entrada do usuário.

# Referência Bibliográfica
- ASCENCIO, A. F. G.; CAMPOS, E. A. V. Fundamentos da programação de computadores: algoritmos, PASCAL, C/C++ (padrão ANSI) e JAVA. 3. ed. São Paulo: Pearson Education do Brasil, 2012.
- DOWNEY, A. Think Python: How to Think Like a Computer Scientist.
- PIVA, D... [et al.] Algoritmos e programação de computadores. Rio de Janeiro: Elsevier, 2012.
