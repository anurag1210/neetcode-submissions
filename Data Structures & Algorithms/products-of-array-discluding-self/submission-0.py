class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Pass 1: left products (everything BEFORE each position)
        left = []
        running = 1
        for num in nums:
            left.append(running)     # save first
            running *= num           # then multiply in

        # Pass 2: right products (everything AFTER each position)
        right = [1] * n
        running = 1
        for i in range(n - 1, -1, -1):   # loop backwards: n-1 down to 0
            right[i] = running           # save first
            running *= nums[i]           # then multiply in

        # Combine: left × right at each position
        output = []
        for i in range(n):
            output.append(left[i] * right[i])
        return output