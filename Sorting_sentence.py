class Solution:
    def sortSentence(self, s: str) -> str:
        s=list(s.split(" "))
        d=[None]*len(s)
        e=0
        for i in range(len(s)):
            s[i]=list(s[i])
            e=int(s[i][len(s[i])-1])-1
            s[i].pop()
            d[e]="".join(s[i])
        d=" ".join(d)
        return d
