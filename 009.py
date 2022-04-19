#007

def find_sum(N):
    list = []
    for i in range(1,N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if i+j+k == N:
                    list.append([i,j,k])
    return list

def solution(N):
    abc = find_sum(N)
    for i, abc in enumerate(abc):
        a=abc[0]
        b=abc[1]
        c=abc[2]
        if a**2 + b**2 == c**2 :
            return a,b,c,a*b*c

solution(1000)
#----------------------------
#answer = 31875000
