# Sub-programas

## Motivação para modularização

A modularização é recomendada tanto pela eficiência no projeto e desenvolvimento do algoritmo, quanto pela escabilidade, qualidade, confiabilidade, documentação e manutenção do mesmo.

A modularização de algoritmos consiste em dividir um algoritmo maior ou principal em algoritmos menos, também referenciados como subalgoritmos ou sub-rotinas (procedimentos e funções), tornando o principal mais estruturado, organizado e refinado.

A maioria das linguagens de programação permite a utilização da técnica de modularização, através da criação de dois tipos de sub-rotinas: o procedimentos (*procedure*) e a função (*function*). Excetuando a lógica de cada uma, a diferença entre ambas é que o procedimento pode ou não retornar valores (variáveis ou parâmetros) após sua execução, enquanto que a função, após ser executada, sempre irá retornar um valor.

**Observarção**: Algumas linguagens não distinguem um procedimento de uma função, isto é, uma função pode se comportar como um procedimento.

## Vantagens da modularização

A modularização proporciona:

A. Que partes comuns a vários algoritmos, ou que se repetem dentro de um mesmo algoritmo, sejam escritas e testadas em momento único.
B. A reutilização de trechos de algoritmos já desenvolvidos - as sub-rotinas.
C. Bibliotecas de sub-rotinas (procedimentos e funções) que podem ser construídas e disponibilizadas para uso em diferentes algoritmos sem alteração
D. A preservação dos refinamentos obtidos durante o desenvolvimento dos algoritmos
E. Uma melhor estruturação do algoritmo, facilitando a depuração de erros e proporcionando uma melhor documentação.

## Sub-rotinas (programação modularizada)

Dentro das subrotinas pode ocorrer declaração de variáveis, chamadas **variáveis locais**. Elas recebeme sse nome porque podem ser utilizadas apenas dentro da sub-rotina. Quando a execução desta chega ao fim, essas variáveis são destruídas e seus conteúdos são perdidos.

Variáveis declaradas fora de qualquer sub-rotina são chamadass **variáveis globais**. Elas recebem esse nome porque qualquer ponto do programa, incluindo as sub-rotinas, pode utilizá-las. São destruídas quando a execução do programa chega ao fim.

**Observação**: Não se aconselha a utilização excessiva de variáveis globais, por tornar difícil a manutenção e a busca por erros nos programas.

### Parâmetros

A chamada de sub-rotinas (procedimentos ou funções) pode ocorrer com ou sem passagem de parâmetros.

Parâmetros podem ser:

a) Conteúdo de uma variável ou seu endereço;
b) Valores constantes;
c) Resultado de uma expressão aritmética.

Os parâmetros passados para sub-rotinas podem ocorrer de duas formas: por Valor, ou por Referência.

#### Passagem de parâmetros por Valor

**Parâmetros por Valor**, passados do "chamador" para o parâmetro formal correspondente na sub-rotina, tem seu **conteúdo inalterado** quando o parâmetro formal é manipulado dentro da sub-rotina.

#### Passagem de parâmetros por Referência

**Parâmetros por Referência**, passados do "chamador" para o parâmetro formal correspondente na sub-rotina, tem seu **conteúdo alterado** quando esse parâmetro é manipulado dentro da sub-rotina, pois o "chamador" não passa o conteúdo da variável global, mas o endereço ede memória dela para o parâmetro da sub-rotina.

Em resumo quando a passagem de parãmetro para uma sub-rotina é feita por Valor, significa que o parâmetro é de **ENTRADA**, enquanto que a passagem por Referência significa que o parâmetro é de **ENTRADA/SAÍDA**.

## Sub-rotinas em Python

### Procedimentos

```python
def saudar(nome):
	print("Bom dia, %s!" %nome)

saudar("Matheus")
```

### Funções 

```python
def maximo(a, b):
	if a > b
		maxim = a
	else:
		maxim = b
	return maxim

print(maximo(7,2))
```

# Trabalho Prático 8

Questões retiradas do URI/beecrowd. Não encontrei as minhas soluções. Refazer

1. 1929 - triangle
2. 1105 - sub-prime
3. 1541 - building houses
4. 1087 - queen
5. 1930 - electrical outlet
6. 2059 - odd, even or cheating
7. 1847 - welcome to the winter!

# Trabalho Prático 9

Questões retiradas do URI/beecrowd. Não encontrei as minhas soluções. Refazer

1. 1959 - regular simple polygons
2. 1961 - jumping frog
3. 2028 - sequence of sequence
4. 2483 - merry christmaaas!
5. 2727 - secret code

# Referências Bibliográficas

- ASCENCIO, A. F. G. CAMPOS, E. A. V. Fundamentos da programação de computadores: algoritmos, PASCAL C/C++ (padrão ANSI) e JAVA. 3. ed. São Paulo: Pearson Education do Brasil, 2012.
- DOWNEY, A. Think Python: How to think like a computer scientist.
- PIVA, D. [et al]. Algoritmos e programação de computadores. Rio de Janeiro: Elsevier, 2012.
