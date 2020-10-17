import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    i=0
    j=1
    k=0
    total=0
    while j<=n:
        k=i+j
        if k>n:
            break
        i=j
        j=k
        
        if k%2==0:
            total+=k
    print(total)