# Máquina de Turing

Para que uma máquina realize uma tarefa, precisamentos primeiro encontrar um algoritmo que a realize. Em um esforço para entender tais limitações das máquinas, muitos pesquisadores propuseram e estudaram diversos dispositivos computacionais, como a **Máquina de Turing** (1936).

## Fundamentos da Máquina de Turing

Uma Máquina de Turing consiste em uma unidade de controle, que pode ler e escrever símbolos em uma fita por meio de uma cabeçote de leitura e gravação. A fita estende-se indefinidamente nas duas extremidades e é dividida em células, sendo que cada uma pode conter qualquer elemento de um conjunto finito de símbolos. Este conjunto é chamado de **alfabeto** da máquina.

A qualquer momento durante o seu processamento, uma Máquina de Turing deve estar em uma das condições pertencentes a um conjunto finito chamado de **estados**. O processamento, em uma Máquina de Turing, começa em um estado especial chamado **estado inicial** e cessa quando a máquina atinge outro estado especial, o **estado de parada**.

O processamento de uma Máquina de Turing consiste em uma sequencia de passos executada pela unidade de controle da máquina. Cada passo consiste em observar o símboo da célula corrente da fita, escrever um símbolo na célula, provavelmente movendo o cabeçote de leitura e gravação para célula a esquera ou a direita, e em seguida mudar de estado. A ação exata a ser executada é determinada por um programa que comunica a unidade de controle o que deve ser feito, com base no estado da máquina e no conteúdo da célula corrente.

0**Exemplo:** Calculadora que incrementa uma unidade em um valor binário inserido na Máquina de Turing e separado por *.

## Exercícios

1. Descreva uma máquina de Turing que substitua uma cadeia de 0s e 1s pr um único 0.
2. Descreva uma máquina de Turing que decremente o valor que se encontra na fita se ele for maior que zero, ou o mantenha inalterado se for zero.

### Exercícios propostos pelo professor

Em 27/02/2020

1. Uma máquina de Turing que escreva infinitos X's na fita.
2. Uma máquina de Turing que receba uma sequencia finita de traços (|) e que escreva um traço a mais no final da sequencia.
3. Uma máquina de Turing que receba uma sequencia de traços (|) e que determine se a quantidade de traços é par ou ímpar, escrevendo "p" ou "i", respectivamente.

Em 05/03/2020

1. Escreva uma máquina de Turing que receba como entrada "|||...|||", sendo x > 0 o número de traços, e que reproduza como saída P, se x for par, ou I, se x for ímpar.
2. Escreva uma máquina de Turing que receba como entrada "|||...|||" + "|||...|||" (x, y > 0) e que produza como saída x + y traços.
3. Escreva uma máquina de Turing que receba como entrada "|||...|||" com x > 0 número de traços e que produza como saída 2x traços.

Em 02/08/2020

1. Escreva uma máquina de Turing que receba como entrada uma sequencia não-vazia de A's e B's, e que produza como saída a sequencia inversa. Assim, por exemplo, se a máquina receber como entrada a sequencia AAAABABAAB, então ele deve produzir a saída BAABABAAAA.
2. Escreva uma máquina de Turing que receba como entrada uma sequencia não-vazia de A's e B's e que determine se a sequencia é ou não um palíndromo (uma possibilidade é aceitar as entradas que são palíndromo e rejeitar aquelas que não são). Um palíndromo é uma palavra que é igual a sua inversão, ou seja, que não muda quando lida de trás para a frente. "ARARA", "ATA" e "ABBA" são palíndromos, ao passo que "ABRA" e "ACABA" não o são.
3. Utilizando o simulador em turingmachinesimulator.com, escreva uma máquina de Turing de 1 fita que, recebendo uma entrada na forma X*Y, sendo X e Y números naturais escritos na base 2, produza como saída o resultado da multiplicação entre X e Y, também na base 2.

## [Trabalho Final]()

Elaborar uma máquina de Turing de uma fita que, recebendo uma entrada na forma X*Y, sendo X e Y números naturais escritos na base 2, produza como saída o resultado da multiplicação entre X e Y, também na base 2.

# Referencias Bibliográficas

1. BROOKSHEAR, J. G. Ciencia da Computação: uma visão abrangente. 7. ed. Porto Alegre: Bookman, 2008.
