class Solution:
    def peakIndexInMountainArray(self, arr):
        left,right = 0,len(arr)-1

        while(left<right):
            mid = left + (right-left)//2

            if(arr[mid]<arr[mid+1]):
                left = mid + 1

            else:
                right = mid

        return right
    
    # 852. Peak Index in a Mountain Array    
s1 = Solution()
print(s1.peakIndexInMountainArray([0,10,5,2]))