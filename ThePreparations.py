#M minut od tera
#Ogląda sezon 1 który ma N odcinków i czas odcinka to K minut
#czy uda mu się skończyć oglądać 1 sezon zanim egzamin się zacznie ?


T= int(input())
for v in range(0,T):
    M,N,K =map(int,input().split())
    DurationEpisodes = N*K
    if M <= DurationEpisodes:
        print("No")
    else:
        print("Yes")



