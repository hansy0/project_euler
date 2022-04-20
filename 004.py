#004


#def solution():
#    palindrome=[]
#    for x in range(100,1000):
#        for y in range(100, 1000):
#            answer= x*y
#            i=0
#            while i<len(str(answer)):
#                if str(answer)[i] == str(answer)[-i-1]:
#                    i +=1
#                    if i==len(str(answer)):
#                        palindrome.append(answer)
#                else:
#                    break
#    
#    return max(palindrome)
#
#solution()
#
#---------------------
# answer = 906609

# N자리수를 곱해 만들 수 있는 가장  대칭 수 :
def get_palindrome(N): 
    
    for i in range(10**N-1, 10**(N-1)-1, -1):
        for j in range(10**N-1, 10**(N-1)-1, -1):
            number = str(i*j)
            for k, num in enumerate(number):
                if number[k] == number[-k-1]:
                    if k == len(number)-1:
                        yield int(number)
                    continue
                else:
                    break

# 3자리 수 곱해 만들 수 있는 가장 큰 대칭 수 
result = max(get_palindrome(3))
print(result)
