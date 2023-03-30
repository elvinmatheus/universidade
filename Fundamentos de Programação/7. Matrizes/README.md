# Matrizes

## Matriz em algoritmos

### Definição de matriz

Uma matriz é formada por uma sequência de variáveis, todas do mesmo tipo, com o mesmo identificador (mesmo nome), e alocadas sequencialemente na memória. Como as variáveis têm o mesmo nome, o que as distingue são os índices que referenciam sua localização dentro da estrutura.

Uma variável do tipo matriz precisa de um índice para cada uma de suas dimensões.

### Declaração de matriz

```
DECLARE nome[dimensao1, dimensao2, dimensao3, ..., dimensaoN] tipo
```
onde:
- `nome`: é o nome da variável do tipo matriz;
- `dimensao1`: é a quantidade de elementos da 1ª dimensão (linhas)
- `dimensao2`: é a quantidade de elementos da 2ª dimensão (coluna)
- `dimensao3`: é a quantidade de elementos da 3ª dimensão (profundidade)
- `dimensaoN`: é a quantidade de elementos da enésima dimensão
- `tipo`: é o tipo de dados dos elementos da matriz

Exemplo:

```
DECLARE X[5,3] NUMÉRICO
```

### Atribuidno valores a uma matriz

```
DECLARE mat[5, 4] NUMÉRICO
mat[2, 4] <- 45
mat[3, 1] <- -8
mat[1, 3] <- 10
```

### Preenchendo uma matriz

```
PARA i <- 1 ATÉ 3 FAÇA
INÍCIO
	PARA j <- 1 ATÉ 5 FAÇA
	INÍCIO
		ESCREVA "Digite o número da linha ", i, " e coluna ", j, " : " 
		LEIA X[i, j]
	FIM
FIM
```

### Percorrendo uma matriz

#### Linha a linha

```
PARA i <- 1 ATÉ 3 FAÇA
INÍCIO
	ESCREVA "Elementos da linha ", i
	PARA j <- 1 ATÉ 4 FAÇA
	INÍCIO
		ESCREVA x[i, j]
	FIM
FIM
```

#### Coluna a Coluna

```
PARA i <- 1 ATÉ 4 FAÇA
INÍCIO
	ESCREVA "Elementos da coluna ", i
	PARA J <- 1 ATÉ 3 FAÇA
	INÍCIO
		ESCREVA X[j, i]
	FIM
FIM
```

## Matrizes em Python

- Assim como nos vetores, os índices se iniciam no zero
- Não há declaração, apenas inicialização
- As matrizes não existem no Python básico, mas pode-se "improvisar" uma lista de listas
- Há várias bibliotecas no Python para manipulação de matrizes (ex.: Numpy)

``` python
...
m = [[0] * 3 for i in range(3)] # inicialização de matrizes
...

soma  = m[0][0] + m[1][1] + m[2][2] # manipulação de elementos da matriz
w[2][2] = 435 # atribuição de valores em elementos da matriz
```

### Função para criar matrizes 2x2

``` python
def matriz(lins, cols, val_inic):
	m = [[val_inic] * cols for _ in range(lins)]
	return m

mat = matriz(4, 5, 1.0) # Cria uma matriz de 4 linhas e 5 colunas
```

Outra função (sintaxe mais simplificada):
``` python
def matriz (linhas, colunas, valorInicial):
	m = [[valorInicial] * colunas] * linhas
	return m

mat = matriz(3, 2, 0.0)
```

# [Trabalho Prático 7](https://github.com/elvinmatheus/universidade/tree/main/Fundamentos%20de%20Programa%C3%A7%C3%A3o/7.%20Matrizes/Trabalho%20Pr%C3%A1tico%207)

1. 1181 - line in array
2. 1182 - column in array
3. 1183 - above the main diagonal
4. 1184 - below the main diagonal
5. 1185 - above the secundary diagonal
6. 1186 - below the secundary diagonal
7. 1190 - right area
8. 1435 - square matrix I
9. 1478 - square matrix II
10. 1557 - square matrix III

# Referências Bibliográficas

- ASCENCIO, A. F. G.; CAMPOS, E. A. V. Fundamentos da programação de computadores: algoritmos, PASCAL, C/C++ (padrão ANSI) e JAVA. 3. ed. São Paulo: Pearson Education do Brasil, 2012.
- PIVA, D. [et al]. Algoritmos e programação de computadores. Rio de Janeiro: Elsevier,2012.
