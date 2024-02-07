"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


class Solution:
    fib_memory = {0: 0, 1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.fib_memory:
            return self.fib_memory[n]

        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.fib_memory[n] = result
        return result


n = 10
result = Solution().climbStairs(n=n)
print(result)
