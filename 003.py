#003

def solution(N): 
    factors = []
    if N == 1 :
        factors.append(N)

    else:
        for x in range(2, N):
            while N % x ==0 :
                factors.append(x)
                N = N//x
    
    return max(factors)


solution(14)
