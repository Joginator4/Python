# 0 programował , 1 nie programował jesli programował więcęj niż 5 dni pod rząd to jest zmęczony
t= int(input())
for v in range(t):
    x = input().split()
    c=0
    z=0
    for i in (x):
        if i=="1":
            c+=1
            if c==6:
                z=1
                print("#codelifematters")
                break
        else:
            c =0
    if z!= 1:
        print("#allcodersarefun")


    
















