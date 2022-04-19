#016


def sqaure_two(N):
    square = 2**N
    numbers = []
    for i in str(square):
        numbers.append(i)
        
        ans = 0
    for num in numbers:
        if num!='L':
            ans += int(num)
    return ans

sqaure_two(1000)
#--------------------------------------------------
#answer 1366