# Linguagem Núcleo (Sintaxe)

## Gramática

<s> ::=
    skip                                                         Empty statement
    | <s>1 <s>2                                                  Statement sequence
    | local <x> in <s> end                                       Variable creation
    | <x>1 = <x>2                                                Variable-variable binding
    | <x> = <v>                                                  Value creation
    | if <x> then <s>1 else <s>2 end                             Conditional
    | case <x> of <pattern> then <s>1 else <s>2 end              Pattern matching
    | {<x> <y>1 ... <y>n}                                        Procedure application


<v>                 ::= <number> | <record> | <procedure>
<number>            ::= <int> | <float>
<record>, <pattern> ::= <literal>
                       | <literal>(<feature>1: <x>1 ... <feature>n: <x>n)
<procedure>         ::= proc { $ <x>1 ... <x>n} <s> end
<literal>           ::= <atom> | <bool>
<feature>           ::= <atom> | <bool> | <int>
<bool>              ::= true | false

## Identificadores de Variáveis

- Um identificador de variáveis pode ser escrito de duas formas alternativas:
    - Uma letra maiúscula seguida de uma sequência de um ou mais caracteres alfanuméricos (letras, dígitos ou underscore);
        - e.g. X, Y, Var, Counter1, etc ...
    - de caracteres "imprimíveis" cercados por um símbolo da crase (`) (backquote)

## Tipos

- Um tipo é um conjunto de valores associados a operações que podem ser aplicados sobre eles:
- Modelo tipado:
    - Qualquer tentativa de executar uma operação não referente ao tipo causa erro (ou exceção)
- Tipos básicos:
    - Numéricos (inteiro e ponto flutuante), registros (átomo, lógico, tupla, lista e string), procedimentos;
- Tipagem dinâmica vs tipagem estática;
- Hierarquia de tipos
- Tipos definidos pelos usuários (e.g. ADTs, ...).

## Registros

- Registros são blocos de construção básicos para definição de muitas estruturas de dados compostas:
    - Listas, árvores, filas, grafos, etc.
- Significado formal: produto de tipos;
- Orientação a registros oferece expressividade para definição de abstrações de mais alto nível

## Procedimentos

- Por que não objetos ou funções?
- Procedimentos são mais simples que objetos
- Funções são casos especiais de procedimentos
    - Procedimentos permitem descrever entidades que não necessariamente se comportam como funções matemáticas;
    - Procedimento pode causar efeitos colaterais e retornar mais de um resultado através de parâmetros de saída
- Programação de alta ordem

## Operações básicas

- Aritmética
    - +, -, *, /, div, mod, ... 
- Registros
    - X = person(name:"Elvin", age: 23)
    - {Arity X} = [age name]
    - {Label X} = person
    - X.age = 25
- Comparações
    - ==, \=, =<, <, >=, >
- Procedimentos
    - IsProcedure