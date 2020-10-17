import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    f=0
    l=[]
    for i in range(2,int((n+1)/2)):
        if n%i==0:
            for j in range(2,i//2):
                if i%j==0:
                    f=1
                    break

            if f==0:
                l.append(i)

    print(l)