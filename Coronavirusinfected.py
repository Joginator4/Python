
t= int(input())

for v in range(t):
    n= int(input())
    x = list(map(int,input().split()))
    x.sort()
    mn= 10* 100
    mx = 0
    count = 1
    for i in range(n-1):
        if x[i+1] - x[i]<= 2:
            count +=1
        else:
            mn = min(mn, count)
            mx = max(mx, count)
            count = 1
    mn = min(mn,count)
    mx = max(mx,count)
    print(mn, mx)
        










