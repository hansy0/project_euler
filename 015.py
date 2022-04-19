#015 격자 경우의 수 구하기

def get_factorial(N):
    ans=1
    for i in range(1, N+1):
        ans= ans*i
    return(ans)


def get_route_count(N): #NxN 격자 경로 수
    a = get_factorial(N*2)
    b = get_factorial(N) 
    return a/b/b

get_route_count(20)
#--------------------------------------------------
#answer 137846528820