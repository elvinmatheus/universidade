x = input().split()
x = list(map(int, x))

def maior(x, y):
    return ((x+y+abs(x-y))/ 2)

maior2 = maior(x[0], x[1])
maior1 = int(maior(x[2], maior2))

print("{} eh o maior".format(maior1))