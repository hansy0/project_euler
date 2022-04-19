#014

def apply_rule(N):
    count=1
    while N !=1:
        if N%2==0:
            N=N/2
            count+=1
        else:
            N=3*N +1
            count+=1
    return count

def longest_count(M): #M이하 숫자로 시작했을 때 가장 긴 과정
    ans = {}
    for i in range(1,M+1):
        count = apply_rule(M+1-i)
        ans[count]=M+1-i
    return ans[max(ans.keys())]
#--------------------------------------------------
#answer 837799