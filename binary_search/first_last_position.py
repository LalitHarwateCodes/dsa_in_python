"""
In this code we have to find first occurence and last occurence and return it's indexes
"""


"""
    we have defined begin_index and end_index which is length of arr - 1
    We will loop till begin_index should we less than or equal to end_index
    Finding the midpoint and then the value of midpoint index in midpoint_value

    In if condition if midpoint_value == key we store index of midpoint in ans variable and then we do
    (end_index = midpoint - 1), because as this is first occurence function we check in the left side of arr.
    We will also check if target number as any other first occurence.

    and elif and else are same as binarySearch.py

 """

class Solution:
    def searchRange(self, nums, target):
        # 0 for left side and 1 for right side
        left = self.binarySearch(nums,target,0)
        right = self.binarySearch(nums,target,1)
        return [left,right]


    def binarySearch(self,arr,target,side):
        left,right = 0,len(arr)-1
        index = -1

        while left <= right:
            mid = left + (right -left) // 2

            if(target > arr[mid]):
                left = mid + 1

            elif(target < arr[mid]):
                right = mid -1

            else:
                index = mid

                if side == 0:
                    right = mid -1
                else:
                    left = mid + 1
        return index



arr = [1,2,3,4,4,4,5]

s1 = Solution()
s2 = Solution()

print(s1.searchRange(arr,4))



