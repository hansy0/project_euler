#003

def solution(N): 
    factors = []
    M=N
    if N ==1 :
        factors.append(1)
    else : 
        x = 2 
        while x * x <= M :
            while N % x ==0 :
                if x not in factors:
                    factors.append(x)
                N = N/x
            x+=1
    
    return max(factors)


solution(600851475143)
