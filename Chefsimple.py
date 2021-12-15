T = int(input())

for v in range(0,T):
    A,B,C = map(int,input().split())
    if A > B > C :
        print(B)
    elif B > A > C:
        print(A)
    elif C > B > A:
        print(B)
    elif A > C > B:
        print(C)
    elif B > C > A:
        print(C)
    elif C > A > B:
        print(A)
