#001

def solution():
    answer = sum( x for x in range(1000) if (x%3 ==0 or x%5==0 )) 
    return answer

solution()