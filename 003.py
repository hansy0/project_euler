#003 
# 가장 큰 소인수 구하기

# 소인수  
def prime_factor_generator(N):
    i = 2
    while N != 1:
        if N%i ==0:
            yield i 
            N = N/i
        i +=1
        

result = max(prime_factor_generator(600851475143))
print(result)


#def solution(N): 
#    factors = []
#    M=N
#    if N ==1 :
#        factors.append(1)
#    else : 
#        x = 2 
#        while x * x <= M :
#            while N % x ==0 :
#                if x not in factors:
#                    factors.append(x)
#                N = N/x
#            x+=1
#    
#    return max(factors)
#
#
#solution(600851475143)
#---------------------
# answer = 6857

