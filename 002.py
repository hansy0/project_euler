#002

def solution():
    x1=1
    x2=2
    fibonacci = []
    while x2 <40000000:
        y=x1 + x2
        if y%2 ==0 : 
            fibonacci.append(y)
    return sum(fibonacci)

solution()