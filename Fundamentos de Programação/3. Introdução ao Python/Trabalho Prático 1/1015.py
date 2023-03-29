p1 = input().split()
p2 = input().split()

x = (float(p2[0]) - float(p1[0])) ** 2
y = (float(p2[1]) - float(p1[1])) ** 2

distance = (x + y) ** 0.5
                       
print("%.4f" %distance)
