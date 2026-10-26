class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        l=len(arr2)
        count2=0
        for i in arr1:
            count=0
            for j in arr2:
                if abs(i-j)>d:
                    count+=1
                if count==l:
                    count2+=1
                
                
            
            
        return count2


