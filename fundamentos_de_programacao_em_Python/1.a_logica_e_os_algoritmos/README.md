# Introdução aos algoritmos

## Conceitos básicos

A finalidade de um computador é receber, manipular e armazenar dados.
Sua finalidade principal é realizar a tarefa de processamento de dados.

As etapas para o desenvolvimento de um programa são:
- **Análise**: estuda-se o enunciado do problema para definir os dados de entrada, o processamento e os dados de saída.
- **Algoritmo**: ferramentas do tipo descrição narrativa, fluxograma ou português estruturado são utilizadas para descrever o problema com suas soluções.
- **Codificação**: o algoritmos é transformado em códigos da linguagem de programação escolhida para se trabalhar.

Portanto, um programa é a codificação de um algoritmo em uma linguagem de programação.

### Conceito de algoritmo

Um algoritmo é uma sequência lógica de passos, com começo, meio e fim. Cada passo desse algoritmo deve ser expresso de forma clara, utilizando, muitas vezes, um formalismo específico, justamente para que não deixe qualquer dúvida, ou seja, ambiguidade na sua interpretação. Essa sequência de passos tem um objetivo específico, que geralmente é a resolução de um problema. Para tanto, esse algoritmo pode receber dados de entrada, muitas vezes chamados de variáveis, e como visa a resolução de um problema, essa resposta do algoritmo visando a solução do problema gera dados de saída.

### Método para a construção de algoritmos

Passos para construção de qualquer tipo de algoritmos:
1. Compreender o problema;
2. Identificar as entradas do problema, ou seja, as informações necessárias ou fornecidas para resolver o problema;
3. Identificar os dados de saída, ou as informações que respondem ou resolvem o problema;
4. Determinar o que é preciso para transfomar dados de entrada em dados de saída;
5. Construir o algoritmo ou a sequência de passos possibilita a transformação do passo 4;
6. Testar o algoritmo em várias situações.

### Tipos de algoritmos

Os três tipos mais utilizados de algoritmos são: *descrição narratica, fluxograma* e *pseudocódigo* ou *portugol*

#### Descrição narrativa

Consiste em analisar o enunciado do problema e escrever, utilizando uma linguagem natural, os passos a serem seguidos para sua resolução.

#### Fluxograma

Consiste em analisar o enunciado do problema e escrever, utilizando símbolos gráficos predefinidos, os passos a serem seguidos para sua resolução.

#### Pseudocódigo ou portugol

Consiste em analisar o enunciado do problema e escrever, por meio de regras predefinidas, os passos a serem seguidos para sua resolução.

## Linguagens de Programação

Linguagem de Programação é uma linguagem artificial desenvolvida para expressar sequências de ações que podem ser executadas por uma máquina, em particular um computador. Linguagens de programação podem ser usadas para criar programas que controlam o comportamento de uma máquina e/ou para expressar algoritmos com precisão.

### Baixo Nível vs. Alto Nível

Uma linguagem de alto nível se aproxima mais da linguagem humana.

Uma linguagem de baixo nível se aproxima mais da linguagem de máquina.

### Linguagem Compilada vs. Linguagem Interpretada

Linguagens de programação são traduzidas em linguagem de máquina (compostas por 0s e 1s), que podem ser processadas pelo computador

Linguagem de Alto Nível (Python, C/C++, Java, ...) -> Tradutor (Compilador ou Interpretador) -> Linguagem de Baixo Nível (Linguagem de Máquina) 

#### Tradutores

Processam linguagens de alto nível, traduzindo-as em linguagens de baixo nível

##### Interpretadores

No interpretador, as instruções definidas na linguagem de alto nível (código fonte) são executadas diretamente. Ele traduz o comando de um programa de cada vez e então chama uma rotina para completar a execução do comando. Mais precisamente, o interpretador é um programa que executa repetidamente a seguinte sequência: pega a próxima instrução -> determina as ações a serem executadas -> executa estas ações.

##### Compilador

Um compilador produz a partir do arquivo de entrada, outro arquivo que é equivalente ao arquivo original, porém em uma linguagem que é executável. Este arquivo resultante pode ser em uma linguagem que é diretamente executável, tal como linguagem de máquina, ou indiretamente executável, tal como outra linguagem para a qual já existe um tradutor. O objetivo de um compilador é traduzir um programa escrito em uma linguagem (código fonte) em um programa equivalente expresso em uma linguagem que é executável diretamente pela máquina (código objeto) 

Nota: O tempo durante o qual o compilador está "trabalhando", isto é, realizando a conversão do código fonte em código objeto é chamado de tempo de compilação.

### Paradigmas de Programação

Um paradigma de programação está intimamente relacionado à forma de pensar do programador e como ele busca a solução para os problemas. É o paradigma que permite ou proíbe a utilização de algumas técnicas de programação. Ele é capaz, ainda, de mostrar como o programador analisou e abstraiu o problema a resolver. Existem vários paradigmas de programação: estruturado, orientado a objetos, lógico, funcional, dentre outros.

Na maioria das vezes, uma determinada linguagem apresenta características de diferentes Paradigmas de Programação.

A escolha do Paradigma de Programação se dá pela adequação à aplicação pretendida.

#### Imperativo
- Expressa a sequência de comandos que manipulam os dados (mudanças de estado)
- Detalhamento passo a passo do que precisa ser feito (receita de bolo)
- Máquina de Von Neumann
	- Orientado a procedimentos
	- Orientado a objetos

#### Declarativo
- Não há conceitos como sequência de comandos e atribuição
- Foco no "o que fazer" em detrimento ao "como fazer"

#### Alguns exemplos
- Estruturado (C, Fortran, Pascal, PHP)
- Orientado a Objetos (C++, Java, Smalltalk, ...)
- Funcional (JavaScript, ...)
- Lógico (Prolog, ...)
- Distribuído (ADA,...)

## BIBLIOGRAFIA BÁSICA

- ASCENCIO, A. F. G.; CAMPOS, E. A. V. Fundamentos da Programação de Computadores: algoritmos, PASCAL, C/C++ (padrão ANSI) e JAVA. São Paulo: Pearson Education do Brasil, 2012

- PIVA JR, D.; NAKAMITI, G. S.; ENGELBRECHT, A. M.; BIANCHI, F. Algoritmos e programação de computadores. Rio de Janeiro: Elsevier, 2012.
