
#X - Miejsce GB
#N- Filmy Si-potrzebne miejsce ,Ri-IMDB ranking 
#Pomóż szefowi wybrać jeden najlepszy film (Największy IMDB rating)
#który zmiesci się na jego dysku
# #Liczba testów
T= int(input()) 
for v in range(0,T):
    N,X=map(int,input().split())
    m=0
    for b in range(N):
        Si,Ri= map(int,input().split())
        if X>=Si and Ri>m:
            m=Ri
    print(m)
    
     #liczba filmów oraz X miejsce GB
     #Followuje N , potrzebne miejsce i ranking IMDB
