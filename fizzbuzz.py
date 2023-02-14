class Solution:
    m=[]
    b=1
    def fizzBuzz(self, n: int) -> List[str]:
        while(Solution.b<=n):
            if((Solution.b)%3==0 and (Solution.b)%5==0):
                Solution.m.append("FizzBuzz")
            elif((Solution.b)%3==0 and (Solution.b)%5!=0):
                Solution.m.append("Fizz")
            elif((Solution.b)%5==0 and (Solution.b)%3!=0):
                Solution.m.append("Buzz")
            else:
                Solution.b=str(Solution.b)
                Solution.m.append(Solution.b)
            Solution.b=int(Solution.b)
            Solution.b+=1
        if(len(Solution.m)>n):
            Solution.b=len(Solution.m)-n
            for i in range(Solution.b):
                Solution.m.pop()
        return Solution.m
