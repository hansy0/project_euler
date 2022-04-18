#004

def solution():
    palindrome=[]
    for x in range(100,1000):
        for y in range(100, 1000):
            answer= x*y
            i=0
            while i<len(str(answer)):
                if str(answer)[i] == str(answer)[-i-1]:
                    i +=1
                    if i==len(str(answer)):
                        palindrome.append(answer)
                else:
                    break
    
    return max(palindrome)

solution()

