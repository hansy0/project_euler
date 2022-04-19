#005

def get_prime_factors(N):  #소인수분해
    factors = []
    M=N
    if N ==1 :
        factors.append(1)
    else : 
        x = 2 
        while x <= M :
            while N % x ==0 :
                factors.append(x)
                N = N/x
            x+=1
    
    return factors



def get_lcm(N):     #1~N까지의 최소공배수구하기
    dict ={}
    num = []
    for x in range(1, N+1):
        dict[x] = get_prime_factors(x)
        num+=get_prime_factors(x)
    
    num = set(num)
    dict2={}

    for y in num : 
        dict2[y] =  max(dict[x].count(y) for x in range(1,N+1))

    answer=1
    for i in dict2.keys():
        answer = answer * ( i**dict2[i] ) 
        print(answer)
    return answer


get_lcm(20)

#----------------------------------------
#answer = 232792560