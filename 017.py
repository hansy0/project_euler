#017

def num_to_eng(i):
    eng_num = {0:'',1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    # 20 이하
    if i < 20:
       return eng_num[i]
    # 20이상 100이하
    elif i <100 and i >=20:
        return eng_num[i/10*10] + eng_num[int(str(i)[1])]

    #100이상 1000이하
    elif i >=100 and i <1000:
        if i % 100 ==0:
            return  eng_num[int(str(i)[0])]+'hundred'
        elif ((i - i/100*100)/10*10 ==10 or (i - i/100*100)/10*10 ==0) and i%100!=0:
            return  eng_num[int(str(i)[0])]+'hundredand'+ eng_num[i - i/100*100]
        else:
            return eng_num[int(str(i)[0])]+'hundredand'+ eng_num[(i - i/100*100)/10*10] + eng_num[int(str(i)[2])]

    else: 
        return 'onethousand'

def length_eng_sum(N):
    j=1
    ans = 0
    while j<=N:
        ans = ans + len(num_to_eng(j))
        j+=1
    return ans

length_eng_sum(1000)
#--------------------------------------------------
#answer 21124
