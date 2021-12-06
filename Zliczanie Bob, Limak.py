for x in range(int(input())):
    a,b=map(int,input().split())
    a1=1
    b1=2
    count=1
    while (True):
        if(count%2!=0 and a1<=a):
            a=a-a1
            a1+=2
            count+=1
        elif(count%2==0 and b1<=b):
            b=b-b1
            b1+=2
            count+=1
        else:
            break  
    if(count%2==1):
        print("Bob")
    if(count%2==0):
        print("Limak")
        



