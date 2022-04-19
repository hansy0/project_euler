#020

def get_factorial(N):
    ans=1
    for i in range(1, N+1):
        ans= ans*i
    return(ans)

def sum_factorials(N): 
    ans = 0
    for i in str(get_factorial(N)):
        ans += int(i)
    return ans

sum_factorials(100)

#--------------------------------------------------
#answer 648
