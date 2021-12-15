
T = int(input())
for v in range(0,T):
    xa ,xb ,Xa, Xb = map(int,input().split())
    coconutsA = Xa//xa
    coconutsB = Xb//xb
    result = coconutsA +coconutsB
    print(result)



