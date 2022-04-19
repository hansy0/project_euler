#010

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

def decimal(N):
    decimals =[]
    i=2
    while i<=N:
        print(i)
        if len(get_prime_factors(i)) == 0:
            decimals.append(i)
        i+=1
    
    return sum(decimals)

decimal(2000000)
#----------------------------
#answer 142913828922
#시간너무 오래걸림 ㅠㅠ