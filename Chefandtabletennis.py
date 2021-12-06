# t= int(input())

# for v in range(t):
    # s=str(input())
    # chefpoints=0
    # enemypoints=0
    # for i in s:
    #     if i == "1":
    #         chefpoints+=1
    #     elif i =="0":
    #         enemypoints+=1
    # if chefpoints > enemypoints:
    #     print("WIN")
    # else:
    #     print("LOSE")
        
        
t= int(input())
for v in range(t):       
    s=str(input())
    chef=s.count('1')
    enemy=s.count('0')
    if(chef>enemy) and chef-enemy > 1:
        print("WIN")
    elif(enemy>chef) and enemy-chef > 1:
        print("LOSE")