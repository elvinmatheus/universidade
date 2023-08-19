# Armazenamento de Atribuição Única

## Armazenamento de Atribuição Única (sigma)

Exemplo:

- sigma = {x1, x2, x3}

    - variáveis x1, x2 e x3 não ligadas

- sigma = {x1 = 314, x2 = [1 2 3], x3}

    - variáveis x1 e x2 ligadas
 
## Variáveis declarativas

- Variáveis no sentido matemático;

- Inicialmente, valor indefinido (variável não-ligada);

- Uma vez atribuído um valor, não pode ser modificada;

- Variável se confunde com o valor que armazena.

Exemplo: x + y == 11 + 22 (no armazenamento {x = 11, y = 22})

## Armazenamento de Valor (Value Store)

- Armazenamento no qual não há variável não-ligada;

- Mapeamento persistente de variáveis a valores;

- Haskell, ML, Scheme suportam **armazenamento de valor**;

- Java, C++, Smalltalk suportam **armazenamento de células**.

## Criação de Valor

Ligando uma variável a um valor criado:

    - x1 = 314
    - x2 = [1 2 3]

## Identificadores de Variáveis

- Variáveis são inacessíveis diretamente em programas;
- Como então referenciar as variáveis que estão no armazenamento?
    - Identificadores de variáveis
    - Introduzidos através de comandos **declare** e **local**;
- Ambiente:
    - Mapeamento de identificadores a variáveis:
    - {X -> x1}
 
## Criação de Valores com Identificadores

- Comando de ligação (binding) aplicado a variáveis em programas
    - X = [1 2 3]
 
## Valores Parciais

- Valor estruturado que contém partes não-ligadas

Exemplo: 
```oz
X = person(name:"George", age:x2)
    Y = x2  
```

- Armazenamento após executar um dos comandos de ligação a seguir:

```oz
Y=25
X=person(name:"George", age:25)
```

## Ligação Variável-Variável

- X = Y
    - X e Y são variáveis compatíveis
- As variáveis identificadas por X e Y agora são indistinguíveis;
    - Conjunto de equivalência;
    - x1 = x2, onde x1 e x2 são respectivamente as variáveis identificadas por X e Y;
 
## Variáveis Dataflow

O que acontece ao acessar uma variável não-ligada?

    - Execução continua e nenhum erro ocorre
        - O valor da variável é indefinido (lixo) - C++
        - O valor é inicializado a um valor default - Java;
    - Execução para com uma mensagem de erro ou uma exceção é levantada;
        - Prolog
        - Não-determinismo potencial em execução concorrente
    - Execução não é possível pois a não-inicialização é detectada pelo compilador, estaticamente;
        - Java, com variáveis locais.
    - Execução espera até que a variável seja ligada - Oz
        - Semântica dataflow;
        - Não funciona em execução serial;