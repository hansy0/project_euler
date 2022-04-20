#002 
# 4백만 이하 짝수 값을 갖는 피보나치항의 합

def fibonacci(N):
    i = 1 #피보나치수
    j = 1 
    while i < N :
        yield i 
        i, j = i+j , i

result = sum(x for x in list(fibonacci(4000000)) if x%2 ==0)
print(result)


# def solution():
#     x1=1
#     x2=2
#     fibonacci = [1,2]
#     while x2 <= 4000000:
#         y=x1 + x2
#         fibonacci.append(y)
#         x1, x2 = x2, y
#     return sum(x for x in fibonacci if x%2==0)
# 

#solution()
#---------------------
# answer = 4613732
