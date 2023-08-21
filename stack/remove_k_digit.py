# Remove K Digits - Leetcode 402 - Python

class Solution:
    def removeDigit(self,nums:str,k) -> str:
        stack = []
        for num in nums:
            while stack and stack[-1] > num and k > 0:
                k -= 1
                stack.pop()
            stack.append(num)

        return stack
    
sol = Solution()

print(sol.removeDigit("54321",4))