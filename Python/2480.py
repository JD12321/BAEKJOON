f,s,t = map(int, input().split())
r = 0

if f==s==t:
    r = 10000+f*1000
elif f==s or t==f:
    r = 1000+f*100
elif s==t:
    r = 1000+t*100
else:
    r = max(f,s,t)*100

print(r)
