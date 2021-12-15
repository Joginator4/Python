
#Siostry A i B grają codziennie na pianinie#
#import re
#Numer testów T , czyli prób 
#T = int(input())
# A = str("A" or str("AA"))
# B = str("B" or str("BB"))
# AA BB AB BA ABBA 
#string s , który daje nam wpis do dziennika


#for v in range (T):
    
 #   s = str(input())
  #  parse_list = s.split(0)
   # print(parse_list)
    # pattern = re.compile(s)

    # if pattern.search("AA") or pattern.search("BB"):
    #     print("no")
    # else:
    #     print("yes")

#n = int(input())
#pole = n*n
#poleczarnych = int(pole/2)
#print(poleczarnych)
#T = int(input())
#flag = []
#B = int(input())
#for B in range(T):
 #   print(B)
  #  flag.append(B + 2)
   # print(flag)

    #s = str(A and B)
    # if A and B in s :
    #     print("yes")        
    # elif str("AA") or str("BB") in s:
    #     print("no")
    # else:
    #     print("no")
    

#Mecz szachowy a + b  3+ 2 s na turę czyli 1 tura to +2 s  jesli timer wynosi 0 to koniec gry  po
# po N turach  N +1 /2 ruchy dla bialych i N/2 ruchy dla czarnych , gra konczy się kiedy obydwa zegary staną
# mają A I B Sekundy które im zostały  , po N-tych turach b = 2sec sa wciaz dodawane do zegara kiedy zrobil ostatni ruch
#znajdz totalny czas gry  numer sekund 


T = int(input())
for v in range(T):
    N,A,B = map(int,input().split())
    result = (180 + (2*N/2)) + (180 + (2*N/2))
    x = result - A - B
    print("Duration of game: " ,x)