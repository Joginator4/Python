


T = int(input())
# for v in range(T):
#     N,A,B = map(int,input().split())
#     time1 = 2* (180+N)
#     time2 = A + B
#     finaltime = time1 - time2
#     print(finaltime)

def clockChess(tests):
    finalTimeLists = []
    for v in range(T):
        N,A,B = map(int,input().split())
        time1 = 2* (180+N)
        time2 = A + B
        finaltime = time1 - time2
        finalTimeLists.append(finaltime)
    return finalTimeLists
print(clockChess(T))