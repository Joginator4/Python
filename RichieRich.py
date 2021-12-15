

T = int(input())
for v in range(0,T):
    A, B, X=map(int,input().split())
    NeededToBeRich = B-A
    YearsToBeRich = NeededToBeRich // X
    print(YearsToBeRich)





