#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        n=0
        for y in range(len(arr)-1):
            if(arr[y]<arr[y+1]and (arr[y]==min(arr[y:]) and arr[y+1]==min(arr[y+1:]))):
                n+=1
            else:
                break
        return n
    
    def selectionSort(self, arr,n):
        #code here
        small=arr[0]
        index=-1
        b=0
        for i in range(len(arr)-1):
            small=arr[i]
            for y in range(i,len(arr)):
                if(small>arr[y]):
                    small=arr[y]
                    index=y
                    b=1
                
            if(b==1):
                arr[i],arr[index]=arr[index],arr[i]
            index=0
            b=0
