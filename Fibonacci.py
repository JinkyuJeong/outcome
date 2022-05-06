class Fibonacci:  # 재귀함수
    def f1(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.f1(n-1)+self.f1(n-2)    ## 계속 자기 함수를 호출하기에 시간이 오래걸림

    def f2(self, n):
        fibo=list()
        fibo.append(0)
        fibo.append(1)
        for i in range(2,n+1):
            fibo.append(fibo[i-1]+fibo[i-2])    ## fibo배열에 하나하나씩 추가해감 

        return fibo[n]

