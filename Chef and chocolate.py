


t=int(input())
while(t>0):
    n,m=map(int,input().split())
    if((n*m)%2==0):
        print('Yes')
    else:
        print('No')
    t-=1


