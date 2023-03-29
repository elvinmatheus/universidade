# Vetores

## Vetor em algoritmos

### Definição de Vetor

Um Vetor é um conjunto de variáveis do mesmo tipo, que possuem o mesmo identificador (nome) e são alocadas sequencialmente na memória. Como as variáveis têm o mesmo nome, o que as distingue é um índice que referencia sua localização dentro da estrutura.

### Declaração de Vetor

```
DECLARE nome[tamanho] tipo
```

onde:
- `nome` é o nome da variável do tipo vetor;
- `tamanho` é a quantidade de variáveis que vão compor o vetor;
- `tipo` é o tipo básico dos dados que serão armazenados ao vetor.

Exemplo:

```
DECLARE X[5] NUMÉRICO
```

Observações:

- Dimensão é definida no momento da declaração
- Dimensão imutável em tempo de execução
- Possui mesma necessidade de inicialização
- Não é possível acessar o valor de um vetor como um todo, mas suas posições individualmente.

### Manipulação de vetor

Para o computador acessar um vetor é preciso que ele conheça o nome do vetor, e o valor do índice que irá apontar para o elemento do vetor, cujo conteúdo será acessado.

### Atribuindo valores ao vetor

As atribuições exigem que seja informada em qual de suas posições o valor ficará armazenado.

```
X[1] <- 45
X[4] <- 0
```

### Preenchendo um vetor

Preencher um vetor significa atribuir valores a todas as suas posições.

```
PARA i <- 1 ATÉ 5 FAÇA
INÍCIO
	ESCREVA "Digite o ", i, "º número"
	LEIA X[i]
FIM
```

### Mostrando os elementos do vetor

Mostrar os valores contidos em um vetor também implica na utilização do índice.

```
PARA i <- 1 ATÉ 5 FAÇA
INÍCIO
	ESCREVA "Este é o ", i, "º número do vetor"
	ESCREVA X[i]
FIM
```

## Vetor em Python

- Python não oferece variável indexada homogênea. Apenas heterogênea, mas que pode ser usada como homogênea.
- Índices se iniciam no zero
- Não há declaração, apenas inicialização.

```python
...
# Para criar vetores em Python
v = [4, 22, 7] 
w = list(range(6))
...
# Para acessar e atribuir valores
media = (v[0] + v[1] + v[2])/3.0
w[5] = 435
...
```

### Criando um "vetor" em Python

```python
v = [None] * 15

# Povoando o vetor
v[4] = 4.55
v[8] = 3.14

# Em Python, é possível que "vetor" armazene tipos distintos
```

# [Trabalho Prático 5](https://github.com/elvinmatheus/universidade/tree/main/Fundamentos%20de%20Programa%C3%A7%C3%A3o/6.%20Vetores/Trabalho%20Pr%C3%A1tico%205)

Questões retiradas do URI (atualmente beecrowd)

1. 1080 - highest and position
2. 1134 - type of fuel
3. 1174 - array selection I
4. 1175 - array change I
5. 1176 - fibonacci array
6. 1177 - array fill II
7. 1178 - array fill III
8. 1179 - array fill IV (não encontrei nos meus documentos)
9. 1180 - lowest number and position

# [Trabalho Dirigido 3](https://github.com/elvinmatheus/universidade/tree/main/Fundamentos%20de%20Programa%C3%A7%C3%A3o/6.%20Vetores/Trabalho%20Dirigido%203)

Questões elaboradas pelo professor

# Referências Bibliográficas
- ASCENCIO, A. F. G.; CAMPOS, E. A. V. Fundamentos da programação de computadores: algoritmos, PASCAL, C/C++ (padrão ANSI) e JAVA. 3. ed. São Paulo: Pearson Education do Brasil, 2012.
- DOWNEY, A. Think Python: How to Think Like a Computer Scientist.
- PIVA, D... [et al.]. Algoritmos e programação de computadores. Rio de Janeiro: Elsevier, 2012.
