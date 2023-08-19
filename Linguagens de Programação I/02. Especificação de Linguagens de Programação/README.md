# Modelo Declarativo de Computação

## Introdução

Elementos de uma linguagem de programação:

- Modelo de computação, ou **paradigma**
    - Sistema formal que define como são as sentenças da linguagem e como devem ser executadas em termos de uma máquina abstrata;
 
- Modelo de programação
    - Conjunto de técnicas para construção de programas na linguagem associada ao modelo de computação;
 
- Técnicas de raciocínio sobre programas
    - Avaliação da corretude e do desempenho de programas
 

## Modelos de Computação

- Modelo declarativo
    - Linguagens funcionais e lógicas
- Modelo declarativo concorrente
- Modelo imperativo (estado explícito)
    - Linguagens imperativas
- Modelo orientado a objetos

## Especificação de Linguagens de Programação

- Sintaxe
    - Como construir sentenças corretas em uma linguagem?
    - Gramáticas;
- Semântica
    - Qual o significado de um programa?
    - Como um programa executa sobre uma máquina abstrata?
    - Abordagem da linguagem núcleo (kernel language);
 
## Sintaxe - Gramáticas

- Linguagens Naturais:
    - Conjunto de regras que definem como formar **sentenças** de uma linguagem a partir de um conjunto de **palavras**;
        - **Sentenças** são sequências de palavras;
        - **Palavras** são sequências de símbolos;
- Linguagens de Programação:
    - Sentenças -> Declarações (statements)
    - Palavras -> Lexemas (tokens)
    - Símbolos -> Caracteres
    - Teoria de linguagens formais e autômatos
    - Construção de compiladores;
        - Reconhecimento de tokens: análise léxica;
        - Reconhecimento de sentenças: análise sintática ou parsing.
     
### Análise Léxica e Sintática

```oz
fun {Fact N}
    if N == 0 then 1
        else N * {Fact N - 1}
    end
end
```

**Análise léxica**

"fun\b{Fact N}\n\b\bif N == 0 then 1\n\b\b\b else\bN*{Fact N-1}\bend\bend"

["fun", "{", "Fact", "N", "}", "if", "N", "==", "0", "then", "1", "else", "N", "*", "{", "Fact", "N", "-", "1", "}", "end", "end"];


**Análise sintática**

Forma uma árvore sintática de execução (?)

### EBNF - Extended Backus-Naur Form

- Representação de gramáticas de Linguagens de Programação
- Principais elementos conceituais:
    - Símbolos terminais (tokens);
    - Símbolos não-terminais (variáveis);
    - Produções (regras para construir sentenças);
    - Derivações (como gerar sentenças a partir das produções);
- Gramáticas livres-do-contexto:
    - Na derivação de uma sentença, a decisão de qual produção de um símbolo não terminal aplicar idepende do contexto;
- Ambiguidade

### Notação de Sintaxe Adotada

<digit>      ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<int>        ::= <digit> { <digit> }
<exp>        ::= <int> | <exp> <op> <exp>
<op>         ::= + | *
<statement>  ::= skip | <expression> '=' <expression> | ...
<expression> ::= <variable> | <int> | ...
<statement>  ::= if <expression> then <statement>
                 {elseif <expression> then <statement>}
                 [else <statement>] end | ...
<expression> ::= '['{<expression>}'] | ...
<label>      ::= unit | true | false | <variable> | <atom> 

### Gramáticas Livres de Contexto vs Gramáticas Sensíveis ao Contexto

- Gramáticas livres de contexto não são capazes de expressar todos os detalhes sintáticos de linguagens
    - Porém, são mais eficientes
 
### Ambiguidade

- Considere a seguinte sentença: 2 * 3 + 4;
- Há duas árvores sintáticas possíveis
- Para retirar a ambiguidade (alternativas):
    - Reescrever a gramática (nem sempre é possível);
    - Usar condições extras;

- Reescrever a gramática:

  <exp>    ::= <exp> + <term> | <term>
  <term>   ::= <term> * <factor> | <factor>
  <factor> ::= <int>

- Condições extras

    - Precedência de operadores:
        - Operadores com maior precedência (e.g. *) são posicionados em profundidades maiores na árvore sintática sempre que possível;
        - Associatividade de operadores:
            - 2-3-4
            - Associatividade à esquerda: (2-3)-4
            - Associatividade à direita 2-(3-4)
    
## Semântica

- Abordagem da linguagem núcleo;
- Características da Linguagem Núcleo:
    - Fácil leitura e intepretação por um programador
    - Concentra-se em elementos de abstração essenciais;
    - Tratabilidade de raciocínio sobre corretude de programas;
    - Fidelidade em relação ao desempenho de tempo e espaço da implementação sobre máquinas reais;
    - Fácil extensão para introduzir novas abstrações linguísticas e "açúcar sintático".
- Para cada modelo de computação, uma linguagem núcleo apropriada

### Abordagem Semântica Baseada em Linguagem Núcleo

- Linguagem prática
    - Provê abstrações úteis ao programador
    - Pode ser extendida com abstrações linguísticas

    ```oz
    fun (Sqr X) X*X end
    B = (Sqr (Sqr A))
    ```

- Linguagem núcleo (Kernel language)
    - Contém um conjunto mínimo de conceitos intuitivos
    - É fácil para o programador entender e raciocinar
    - Tem uma semântica formal
 
### Semântica formal

- Operacional
    - Máquina abstrata
- Axiomática
    - Relações entre entradas e saídas
    - Assertivas lógicas
    - Adequado para modelos com estado (prog. imperativa)
- Denotacional
    - Funções sobre um domínio abstrato
    - Adequado para models declarativos (prog. funcional)
- Lógica
    - Modelo de uma teoria lógica
 
### Extensões sobre a Linguagem Núcleo

- Abstrações Linguísticas
    - Novas abstrações
    - Definição em termos dos construtos da linguagem núcleo;
    - Ex: laços de controle (for), funções, classes, funções lazy, travas, funtores, etc;
- Açúcares Sintáticos
    - Atalhos sintáticos, formas mais simplificadas de expressar elementos sintáticos;
    - Não introduzem novas abstrações
    - Definição em termos dos construtores da linguagem núcleeo;
    - Ex: várias abreviações para definir variáveis locais
 
```oz
if N == 1 then [1]
else
    local L in
        ...
    end
end

if N==1 then [1]
else L in
    ...
end
```

## Abordagens baseadas em traduções

- Linguagem de Programação
    - Linguagem Núcleo: Auxilia o programador a raciocinar a entender uma linguagem - Programador
    - Cálculo: Estudo matemático da programação - Matemático/Teórico de computação
    - Máquina virtual: Execução eficiente em uma máquina virtual - Desenvolvedor de compiladores
