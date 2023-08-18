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

**Variações no triângulo de Pascal**

Para obter o triângulo de Pascal original, fazemos:

```oz
fun {Add X Y} X+Y end
```

Agora podemos fazer `{GenericPascal Add 5}` para retornar a quinta linha do triângulo de Pascal.

Podemos fazer também `{GenericPascal Number.'+' 5}`, uma vez que a operação de adição '+' é parte do módulo `Number`.

Definindo outra função:

```oz
fun {Xor X Y} if X==Y then 0 else 1 end end

{Browse {GenericPascal Xor N}}
```

## Concorrência

A concorrência é a capacidade do programa realizar várias tarefas de forma independente.

Nós introduzimos a concorrência criando threads. Threads são criadas com a instrução `thread`.

```oz
thread P in
    P={Pascal 30}
    {Browse P}
end
{Browse 99*99}
```
Isso cria uma nova thread. Dentro da nova thread, nós chamamos {Pascal 30} e depois chamamos `Browse` para mostrar o resultado. Enquanto a nova thread está executando os cálculos, o sistema prossegue e mostra o resultado de 99*99.

## Dataflow

```oz
declare X in
thread {Delay 10000} X=99 end
{Browse start} {Browse X*X}
```

A multiplicação X*X espera até que X esteja ligado. O primeiro `Browse` mostra "start". O segundo `Browse` espera pela multicação, então não faz nada ainda. O {Delay 10000} faz o sistema esperar 10 segundos. X é ligado é conectado depois que o delay terminar. Quando X é ligada, então a multiplicação continua e o segundo browse mostra 9801.

```oz
declare X in
thread {Browse start} {Browse X*X} end
{Delay 10000} X=99
```

O trecho de código acima se comporta exatamente como o código anterior.

## Estado

Memória é necessária para funções que mudam seu comportamento e aprendem com seu passado. Esse tipo de memória é chamada *estado explícito* .

**A memory cell**

Há várias formas de definir estado explícito. A maneira mais simples é definir uma única célula de memória. A célula é um tipo de caixa na qual você pode colocar qualquer conteúdo dentro dela. Muitas linguagens de programação chamam isso de "variável". Nós chamamos isso de `célula` para evitar confusão com as variáveis definidas anteriormente, que possuem uma noção parecida com as variáveis matemáticas, isto é, atalhos para valores. Há três funções para células: `NewCell` cria uma nova célula, `:=` (atribuição) coloca um novo valor em uma célula, e `@` (access) obtém o atual valor armazenado na célula.

```oz
declare
C={NewCell 0}
C:=@C+1
{Browse @C}
```

Isso cria uma célula C com conteúdo inicial 0, adiciona um ao conteúdo, e então a mostra.

## Objetos

Funções com memória interna são normalmente chamadas `objetos`.

```oz
declare
local C in
    C={NewCell 0}
    fun {Bump}
        C:=@C+1
        @C
    end
    fun {Read}
        @C
    end
end
```

A célula é referenciada por uma variável local, então ela é completamente invisível do lado de fora. Essa propriedade é chamada de `encapsulamento`.

```oz
{Browse {Bump}}
{Browse {Bump}}

{Browse {Read}}
```

## Classes

```oz
declare
fun {NewCounter}
C Bump Read in
    C={NewCell 0}
    fun {Bump}
        C:=@C+1
        @C
    end
    fun {Read}
        @C
    end
    counter(bump:Bump read:Read)
end
```

`NewCounter` é uma função que cria uma nova célula e retorna novas funções Bump e Read. Retornar funções como resultado de funções é outra forma de programação de alta ordem.

Nós agrupamos Bump e Read juntos em uma estrutura de dados composta chamada registro. O registro counter(bump:Bump read:Read) é caracterizado por seu rótulo *counter* e por seus dois campos chamado bump e read.

```oz
declare
Ctr1={NewCounter}
Ctr2={NewCounter}


{Browse {Ctr1.bump}}
```

Cada contador tem sua própria memória interna e suas próprias funções Bump e Read. Nós podemos acessar essas funções usando o operador "." (dot).

**Em direção à programação orientada a objetos**

Operações definidas dentro de classes são normalmente chamadas *métodos*. A classe pode ser usada para fazer muitos outros objetos counters. Todos esses objetos compartilham os mesmos métodos, mas cada um tem sua própria memória interna separada. Programação com classes e objetos são chamadas *object-based programming*.

Adicionar o conceido de herança à *object-based programming* nos dá *object-based programming*. Herança significa que uma nova classe pode ser definida em termos de classes existentes, especificando como a nova classe é diferente da classe herdada.

## Nondeterminism and time

```oz
declare
C={NewCell 0}
thread
    C:=1
end
thread
    C:=2
end
```
O exemplo acima é um exemplo simpes de nondeterminism.

```oz
declare
C={NewCell 0}
thread I in
    I=@C
    C:=I+1
end
thread J in
    J=@C
    C:=J+1
end
```

## Atomicidade

Para resolver o problema de sobreposição de resultados usamos operações atômicas. 

```oz
declare
C={NewCell 0}
L={NewLock}
thread
    lock L then I in
        I=@C
        C:=I+1
    end
end
thread
    lock L then J in
        J=@C
        C:=J+1
    end
end
```

Um *lock* tem a propriedade de apenas uma única thread execute os seus comandos por vez. Se a segunda thread tenta entrar, então esperará até que a primeira termine.