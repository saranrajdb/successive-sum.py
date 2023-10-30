l=list(map(int,input().split()))
s=0
n=int(input())
for i in range(n-1,len(l),n):
    s+=l[i]
print(s)