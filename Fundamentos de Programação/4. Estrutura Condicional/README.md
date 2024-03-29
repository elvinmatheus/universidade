# Estrutura Condicional

## Expressões Booleanas

Uma **expressão booleana** é uma expressão que pode ser verdadeira ou falsa. Exemplo:

```
>>> 5 == 5
True
>>> 5 == 6
False
# O operador == compara dois operandos e retorna True se eles são iguais e Falso, caso contrário.
```

`True` e `False` são valores especiais que pertencem ao tipo `bool`. Eles não são strings.

```
>>> type(True)
<type 'bool'>
>>> type(False)
<type 'bool'>
```

O operador == é um dos **operadores** relacionais. Os outros são:

```
	x != y					# x não é igual a y
	x > y					# x é maior que y
	x < y					# x é menor que y
	x >= y					# x é maior ou igual a y
	x <= y					# x é menor ou igual a y
``` 

Observação: o símbolo =  é o operador de atribuição e == é o operador relacional.

## Operadores Lógicos

Existem três **operadores lógicos** em Python: `and`, `or`, e `not`.

Os operandos dos operadores lógicos devem ser expressões booleanas, mas Python não é muito estrito. Qualquer número diferente de 0 é interpretado como `True`

```
>>> 17 and True
True
```

## Execução Condicional

As **sentenças condicionais** nos dão a habilidade de checar condições e mudar o comportamento do programa de acordo com o resultado.

```
if x > 0:
	print("x é positivo")
```

A expressão booleana após o `if` é chamado de **condição**. Se é `True`, então a sentença indentada é executada. Se não, não nada acontece.

Sentenças `if` são chamadas de **sentenças compostas**, pois possuem um header seguido de um corpo indentado.

## Execução Alternativa

A segunda forma de uma sentença `if` é a **execução alternativa**, no qual há duas possibilidades e a condição determina qual delas será executada. Exemplo:

```python
if x % 2 == 0:
	print("x é par")
else:
	print("x é ímpar")
```

As alternativas são chamadas de "ramos" (branches), porque eles são ramos no fluxo de execução.

## Condicionais encadeadas

Quando precisamos de mais do que apenas dois ramos, nós utilizamos **condições encadeadas**

```python
if x < y:
	print("x é menor do que y")
elif x > y:
	print("x é maior do que y")
else:
	print("x e y são iguais")
```

`elif` é uma abreviação de "else if". Não há limite para sentenças `elif`. A cláusula `else` deve vir no final da condição encadeada.

Cada condição é checada em ordem. Se a primeira é falsa, a segunda será checada, e assim por diante. Se uma delas é verdadeira, o ramo correspondente é executado e a sentença termina. Mesmo que ainda haja mais de uma condição verdadeira, apenas o primeiro ramo verdadeiro é executado.

## Condições aninhadas

Uma condicional pode ser aninhada dentro de outra. Exemplo:

```python
if x == y:
	print("x e y são iguais")
else:
	if x < y:
		print("x é menor do que y")
	else:
		print("x é maior do que y")
```

É uma boa ideia evitar condicionais aninhadas, pois se tornam difíceis de ler rapidamente.

Operadores lógicos podem prover uma maneira de simplificar condições aninhadas.
```python
if 0 < x:
	if x < 10:
		print("x é um número positivo de apenas um dígito.")

# Alternativa sem condições aninhadas
if 0 < x and x < 10:
	print("x é um número positivo de apenas um dígito.")
```

# [Trabalho Prático 2](https://github.com/elvinmatheus/universidade/tree/main/Fundamentos%20de%20Programa%C3%A7%C3%A3o/4.%20Estrutura%20Condicional/Trabalho%20Pr%C3%A1tico%202)

1. 1035 - Selection Test 1
2. 1036 - Bhaskara's Formula
3. 1037 - Interval
4. 1038 - Snack
5. 1040 - Average 3
6. 1041 - Coordinates of a Point
7. 1042 - Simple Sort
8. 1043 - Triangle
9. 1044 - Multiples
10. 1045 - Triangle Types
11. 1046 - Game Time
12. 1047 - Game Time with Minutes

# [Trabalho Dirigido 1](https://github.com/elvinmatheus/universidade/tree/main/Fundamentos%20de%20Programa%C3%A7%C3%A3o/4.%20Estrutura%20Condicional/Trabalho%20Dirigido%201)

Questões propostas pelo professor (infelizmente não encontrei o pdf com as orientações para cada questão)

# [Trabalho Prático 3](https://github.com/elvinmatheus/universidade/tree/main/Fundamentos%20de%20Programa%C3%A7%C3%A3o/4.%20Estrutura%20Condicional/Trabalho%20Pr%C3%A1tico%203)

1. 1018 - banknotes
2. 1020 - age in days
3. 1048 - salary increase
4. 1049 - animal
5. 1050 - DDD
6. 1051 - taxes
7. 1061 - event time
8. 1064 - positives and average
# Referencias Bibliográficas
- DOWNEY, A. Think Python: How to Think Like a Computer Scientist.
