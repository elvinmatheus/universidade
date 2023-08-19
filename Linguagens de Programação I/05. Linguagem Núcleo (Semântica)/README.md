# Linguagem Núcleo (Semântica)

## Identificadores e Escopo Estático

```oz
local A in
    local B in
        local C in
            local D in
                A=11
                B=2
                {`+` A B C}
                {`*` C C D}
            end
        end
    end
end
```

```oz
local X in
    X = 1
    local X in
        X = 2
        {Browse X} /* Exibe 2 */
    end
    {Browse X} /* Exibe 1 */
end
```

## Procedimentos

```oz
Max = proc {$ X Y ?Z}
        if X>=Y then Z=X else Z=Y end
      end
```

- "?": anotação para argumento de saída;
    - Não possui efeito na execução;
    - Trata-se de um comentário (documentação no código);
- {Max 3 5 C}
    - X e Y são ligados aos valores 3 e 5;
    - Z é ligado a variável não-ligada identificada por C;
- Chamada por referência

## Procedimentos com Referências Externas

- if X>=Y then Z=X else Z=Y end
    - X, Y e Z são identificadores livres;
    - Comando não executável;
    - No contexto de Max, torna-se executável

```oz
LB = Proc {$ X ?Z}
    if X>=Y then Z=X else Z=Y end
end
```

- Quem é Y? É aquele existente na declaração;
- Consequência do escopo estático

```oz
local Y LB in
    Y = 10
    LB = proc {$ X ?Z}
            if X>=Y then Z=X else Z=Y end
         end
    local Y=15 Z in
        {LB 5 Z}
    end
end
```

- Saída é 10;
- Y é aquele existente no ambiente na declaração;

## Escopo Dinâmico vs Escopo Estático

```oz
local P Q in
    proc {Q X} {Browse stat(X)} end
    proc {P X} {Q X} end
    local Q in
        proc {Q X} {Browse dyn(x)} end
        {P hello}
    end
end
```

- No escopo estático, retorna-se stat(hello);
- No escopo dinâmico, retorna-se dyn(hello);
- Escopo estático tem mais vantagens;

## Abstração de Procedimento

- Qualquer comando pode ser transformado em uma unidade lógica independente colocando-no em um procedimento;

- Identificador livre em um comando:
    - Não está declarado no comando;
    - Pode estar declarado no comando que o abrange;
- Escopo estático:
    - Referências externas são resolvidas na declaração dos procedimentos;
 
## Comportamento Dataflow

```oz
local X Y Z In
    X = 10
    if X>=Y then Z=X else Z=Y end
end
```

- Y está associado a uma variável não-ligada;
- Qual o comportamento previsto?
    - O programa pára para esperar que um valor seja ligado à variável associada a Y;
 
## Máquina Abstrata

- Armazenamento de atribuição única;
    - sigma = {x1, x3 = nil, x2 = x3, x4 = a | x2}
- Ambiente
    - E = {X -> x, Y -> y}
- Comando semântico
    - (<s>, E);
        - <s> é um comando;
        - E é um ambiente;
- Estado de execução:
    - (ST, sigma)
        - ST é uma pilha de comandos semânticos;
        - sigma é um armazenamento (memória);
- Computação
    - (ST0, sigma0) -> (ST1, sigma1) -> (ST2, sigma2) -> ...
    - Uma transição é um passo de computação;
    - Um passo de computação é atômico;
    - No momento, computações são sequenciais;
 
## Execução de Programas

- Estado inicial
    - ([(<s>, ø)], ø)
        - Ambiente e armazenamento vazios;
        - <s> é o programa a ser executado;
- Passo de execução
    - Estado atual: (ST, sigma);
    - Primeiro elemento de ST é desempilhado e executado, de acordo com a semântica do comando;
- Estado final de execução;
    - Se houver, é o estado onde a pilha encontra-se vazia.
- Estados possíveis de ST
    - Executável: ST pode executar um passo;
    - Terminado: ST está vazia;
    - Suspenso: ST não está vazia, mas não pode realizar um passo de execução.
        - No modelo sequencial, uma vez suspenso não pode voltar a ser executável.
     
## Cálculo com Ambientes

- E' = E + {<x> -> x}
    - Acrescenta um novo mapeamento do identificado <x> para a variável x;
     - E' é um novo ambiente obtido a partir de E acrescentando o novo mapeamento;
     - Mapeamentos de <x> em E são sobrescritos em E';
- E' = E + {<x1> -> x1, <x2> -> x2, ..., <xn> -> xn}
    - Abreviação para introduzir novos mapeamentos;
- E' = E | {<x>1, <x>2, ..., <x>n}
    - E' é obtido de E considerando-se somento os identificadores de variáveis da lista;

## Semântica de comandos

- Skip
    - ((skip, E) | ST', sigma) -> (ST', sigma)
- Composição sequencial
    - ((<s>1 <s>2, E) | ST', sigma) -> ((<s>1, E) | (<s>2, E) | ST', sigma)
- Declaração de variável local
    - ((local <x> in <s> end, E) | ST', sigma) -> ((<s>, E + {<x> -> x}) | ST', sigma + {x})
- Ligação Variável-Variável
    - ((<x>1 = <x>2, E) | ST', sigma) -> (ST', sigma + {E(<x>1) = E(<X>2)})
- Criação de valor
    - ((<x>=<v>, E) | ST', sigma) -> (ST', sigma + {E(<x>)=x, x=v})
    - Todos os identificadores em <v> são substituídos por seus conteúdos no armazenamento determinados por E;