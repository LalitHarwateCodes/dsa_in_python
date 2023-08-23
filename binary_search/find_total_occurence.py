
class Solution:
    """
    Same as first_last_position.py only slight difference is we are returning right - left + 1
    """
    def searchRange(self, nums, target):
        left = self.binarySearch(nums,target,0)
        right = self.binarySearch(nums,target,1)
        return (right - left) + 1
    
    def binarySearch(self,arr,target,side):
        left,right = 0, len(arr)-1
        index = -1

        while left <= right:
            mid = left + (right-left)//2

            if(target > arr[mid]):
                left = mid + 1

            elif(target < arr[mid]):
                right = mid - 1

            else:
                index = mid

                if side == 0:
                    right = mid -1
                else:
                    left = mid + 1
        return index
    

s1 = Solution()
s2 = Solution()
arr = [1,2,3,4,4,4,5]
print(s1.searchRange(arr,4))

