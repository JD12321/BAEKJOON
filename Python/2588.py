a = list(map(int,''.join(input())))
b = list(map(int,''.join(input())))
total = 0

for i in [2, 1, 0]: 
    c = ((a[0]*100)+(a[1]*10)+a[2])*b[i]
    if(i==1): total += c * 10
    elif(i==0): total += c * 100
    else: total += c
    print(c)
print(total)
