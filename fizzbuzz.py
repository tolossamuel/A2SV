class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        m=[]
        b=1
        while(b<=n):
            if((b)%15==0):
                m.append("FizzBuzz")
            elif((b)%3==0):
                m.append("Fizz")
            elif((b)%5==0):
                m.append("Buzz")
            else:
                b=str(b)
                m.append(b)
            b=int(b)
            b+=1
        return m
        return Solution.m
