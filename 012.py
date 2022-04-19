# 012

def get_alliquot(N): #약수
    factors =[1]
    if N !=1 :
        x = 2         
        while x*x<= N :
            if N % x ==0 :
                factors.append(x)
                factors.append(N//x)
            x+=1
        factors.append(N)
    factors.sort()
    return factors

def solution(n): #n개 이상의 약수를 갖는 가장 작은 삼각수
    i=0
    j=1
    count=0
    while count<n:
        count = len(get_alliquot(i+j))
        i, j = i+j, j+1
    return i
    
solution(500)
#-------------------------------------------------------------
#answer = 76576500

