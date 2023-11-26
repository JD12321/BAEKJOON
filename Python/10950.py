a = int(input())
b = []

for i in range(a):
    c = map(int, input().split())
    p=0
    for j in c:
        p+=j
    b.append(p)

for i in b:
    print(i)
