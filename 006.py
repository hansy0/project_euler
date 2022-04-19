#006 

def sum_of_square(N):
    answer=0
    for x in range(1,N+1):
        answer+=x**2
    return answer

def square_of_sum(N):
    return sum(range(1,N+1))**2

def solution(N):
    return abs(sum_of_square(N) - square_of_sum(N))


solution(100)
#---------------------------
#answer = 25164150