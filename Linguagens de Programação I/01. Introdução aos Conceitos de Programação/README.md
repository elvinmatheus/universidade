# Introdução aos conceitos de Programação

## Uma calculadora

Inicie o sistema Mozart clicando duas vezes no ícone do Mozart ou escrevendo `oz` no terminal.

Com o editor aberto, selecione o frame de cima e escreva 

```oz
{Browse 9999*9999}
```

Use o mouse para selecionar essa linha. Agora vá ao menu Oz e selecione `Feed Region`. O sistema então fará o cálculo.

As chaves {...} são usados para chamadas de procedimento ou funções.

`Browse` é um procedimento com um argumento, isto é: `{Browse X}`. Esta sentença abre a janela browser e mostra o conteúdo de X.

## Variáveis

Para declarar uma variável, use:

```oz
declare
V=9999*9999
```

Podemos usar a variável depois:

```
{Browse V*V}
```

Variáveis são atalhos para valores. Elas não podem ser atribuídas mais de uma vez. Mas podemos declarar outra variável com o mesmo nome da anterior. Isso implica que o valor anterior não será mais acessível. Mas cálculos realizados usando a variável antiga não são alterados. Isso é devido a dois conceitos:

- O identificador: é o nome da variável. Exemplo: a letra "V".
- A store variable: é parte da memória do sistema.

A sentença `declare` cria uma nova store variable e faz o identificador da variável "apontar" para ela.

## Funções

**Fatorial**

```oz
declare
fun {Fact N}
    if N==0 then 1 else N*{Fact N-1} end
end
```

A palavra-chave `declare` diz que queremos definir algo novo. A palavra-chave `fun` inicia uma nova função. A função é chamada Fact e tem um argumento N. O argumento é uma variável local, i.e., é conhecida apenas dentro do corpo da função. Cada vez que a função é chamada uma nova variável é declarada.

Podemos testar a função fazendo

{Browse {Fact 10}}

**Combinação**

```oz
declare
fun {Comb N R}
    {Fact N} div ({Fact R} * {Fact N-R})
end
```

**Abstração funcional**

A função `Comb` chama a função `Fact` três vezes. É sempre possível para usar funções existentes para ajudar a definir novas funções. Esse princípio é chamado *abstração funcional* porque usa funções para construir abstrações. 

## Listas

Uma lista é apenas uma sequência de elementos, com colchetes na esquerda e direita, como [5 6 7 8]. A lsita vazia é escrita `nil`. Listas podem ser mostradas como números:

```oz
{Browse [5 6 7 8]}
```

A notação [5 6 7 8] um atalho. Uma lista é atualmente uma cadeia de linkes, onde cada link contém duas coisas: um elemento da lista e uma referência para o resto da cadeia. Listas são sempre criadas um elemento por vez, começando com `nil` e adicionando-se links um por um. Um novo link é escrito como `H|T`, onde H é o novo elemento e T é a antiga parte da cadeia.

O link `H|T` é frequentemente chamado *cons*.

```oz
declare
H=5
T=[6 7 8]
{Browse H|T}
```

A lista `H|T` pode ser escrita [5 6 7 8]. Ela tem cabeça 5 e cauda [6 7 8]. O cons `H|T` pode ser separado, para obter a cabeça e cauda:

```oz
declare
L=[5 6 7 8]
{Browse L.1}
{Browse L.2}
```

Isso usa o dot operator ".", que é usado para selectionar o primeiro ou segundo argumento de uma lista. Fazer L.1 retorna a cabeça 5 e L.2 retorna a cauda [6 7 8]

**Pattern matching**

Uma forma mais compacta de separar uma lista é usando a instrução `case`, o qual obtém ambas cabeça e cauda em um só passo:

```oz
declare 
L=[5 6 7 8]
case L of H|T then {Browse H} {Browset T} end
```

Isso mostra 5 e [6 7 8]. A instrução case declara duas variáveis locais, H e T, e conecta elas à cabeça e cauda da lista L. Dizemos que a instrução case faz *pattern matching* (casamento de padrão), porque decompõe L de acordo com o "padrão" H|T. Variáveis locais declaradas com `case` são como variáveis declaradas com `declare`, exceto que as variáveis existem apenas no corpo da sentença `case`, isto é, entre `then` e `end`.

## Funções sobre listas

Vamos construiir uma função para calcular a enésima linha do triângulo de Pascal.

**A função principal**

```oz
declare Pascal AddList ShiftLeft ShiftRight
fun {Pascal N}
    if N==1 then [1]
    else
        {AddList {ShiftLeft {Pascal N-1}}
                 {ShiftLeft {Pascal N-1}}}
    end
end
```

**As funções auxiliares**

```oz
fun {ShiftLeft L}
    case L of H|T then
        H|{ShiftLeft T}
    else [0] end
end

fun {ShiftRight L}
    0|L
end

fun AddList L1 L2
    case L1 of H1|T1 then
        case L2 Of H2|T2 then
            H1 + H2|{AddList T1 T2}
        end
    else nil end
end
```

## Complexidade 

A função Pascal fica muito lenta se tentarmos calcular linhas de numeraçao alta. Para melhorar isso, vamos definir a função `FastPascal`:

```oz
fun {FastPascal N}
    if N==1 then [1]
    else L in
        L={FastPascal N-1}
        {AddList {ShiftLeft L} {ShiftRight L}}
    end
end
```

A complexidade de tempo da função {Pascal N} é proporcional a 2^N. A {FastPascal N}, por sua vez, tem complexidade de tempo n^2.

## Lazy evaluation

As funções que definimos até aqui utilizam a eager evaluation. Outra forma de calcular o resultado de funções é chamado *lazy evaluation*.

```oz
fun lazy {Ints N}
    N|{Ints N+1}
end
```

A palavra-chave *lazy* fatante que a função só será calculada quando for necessário. Essa é uma das vantagens da *lazy evaluation*: podemos calcular infinitas estruturas de dados sem usar loops.

Para mostrar os valores da função, nós temos que fazer algo que precise da lista. Por exemplo:

```
L = {Ints 0}
{Browse L} */ Não mostra nada /*

{Browse L.1}

case L of A|B|C|_ then {Browse A+B+C} end
```
**Lazy calculation do triângulo de Pascal**

```oz
fun lazy {PascalList Row}
    Row|{PascalList
            {AddList {ShiftLeft Row}
                     {ShiftRight Row}}}
end

declare
L={PascalList [1]}
{Browse L} /* Não mostra nada */

{Browse L.1} /* Mostra a primeira linha */
{Browse L.2.1} /* Mostra a segunda linha
```

Vantagem da *lazy evaluation*: evita retrabalho/recálculo.

## Programação de alta ordem

A habilidade de passar funções como argumentos é conhecida como *programação de alta ordem*

```oz
fun {GenericPascal Op N}
    if N==1 then [1]
    else L in
        L={GenericPascal Op N-1}
        {OpList Op {ShiftLeft L} {ShiftLeft Right}}
    end
end
```

`AddList` é substituída por `OpList`. O argumento extra `Op` é passado para OpList. Usamos as versões antigas de ShiftLeft e ShiftRight, pois eles não precisam de Op. Definimos `OpList` a seguir:

```oz
fun {OpList Op L1 L2}
    case L1 of H1|T1 then
        case L2 of H2|T2 then
            {Op H1 H2}|{OpList Op T1 T2}
        end
    else nil end
end
```

Em vez de fazer uma adição H1+H2, essa versão faz {op H1 H2}