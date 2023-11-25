h,m = map(int, input().split())
r = int(input())

if (m+r<60): m+=r
else:
    h+=((m+r)//60)
    m=((m+r)%60)
    if (h>23): h-=24

print(h,m)
