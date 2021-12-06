#N= Jabłka M=Pomarańcze K= coiny

for v in range(int(input())):
    n,m,k = map(int,input().split())
    b=n
    c=m
    l=k
    while l!=0:
        if (b==c):
            break
        elif b < c:
            b+= 1
            l-= 1
        elif c < b:
            c+=1
            l-=1
        print(abs(b-c))

            
        
