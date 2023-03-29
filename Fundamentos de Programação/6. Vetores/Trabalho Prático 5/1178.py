X = float(input())

N = [None] * 100
N[0] = X

print("N[0] = ", X)

for i in range(1, 100):
    N[i] = N[i-1] / 2
    print("N[{0}] = {1}".format(i, N[i]))
