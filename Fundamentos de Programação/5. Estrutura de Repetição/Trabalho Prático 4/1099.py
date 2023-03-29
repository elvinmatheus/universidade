N = int(input())

for i in range(N):
    entrada = [int(num) for num in input().split()]
    X = min(entrada)
    Y = max(entrada)
    soma = 0
    for j in range(X + 1, Y):
        if j % 2 != 0:
            soma = soma + j
    print(soma)
