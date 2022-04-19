#007

def get_prime_factors(N):  #소인수분해
    factors = []
    M=N
    if N !=1 :
        x = 2 
        while x*x<= M :
            while N % x ==0 :
                factors.append(x)
                N = N/x
            x+=1
    
    return factors


def Nth_decimal(N):
    decimals =[]
    i=2
    while len(decimals)<=N:
        if len(get_prime_factors(i)) == 0:
            decimals.append(i)
        i+=1
    
    return decimals[N-1]

Nth_decimal(10001)

#----------------------------
#answer = 104743
