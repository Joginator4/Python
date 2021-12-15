

T=int(input())
for v in range(0,T):
    x,y = map(int,input().split())
    sum = x + y
    if sum % 2 == 0:
        print('YES')
    else:
        print('NO')
    

