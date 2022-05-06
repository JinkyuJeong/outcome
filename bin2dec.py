def bin2dec(s):
    num=list(s)
    sum=0
    for n in range(len(num)):
        if (int(num[n]) == 0) | (int(num[n]) == 1):
            sum+=int(num[-len(num)+n])*(2**(len(num)-n-1))
        else:
            return "값을 0또는 1로만 입력하세요"
    return str(sum)

    

