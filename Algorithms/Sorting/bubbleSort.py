from typing import List
class Solution:
    #Time complexity of O(n^2)
    def bubbleSort(self, nums: List[int]) -> List[int]:
        Change = True
        while Change:
            Change = False
            for i in range(len(nums) - 1):
                if nums[i+1] < nums[i]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
                    Change = True
        return nums


def main():
    testes_cases = [
        [6,5,3,1,8,7,2,4],
        [7,2,9,3,7,5,7,6],
        [5,6,2,18,95,367,3]
        ]

    for i in testes_cases:
        print(f"Input {i}")
        sol = Solution()
        rel = sol.bubbleSort(i)
        print(f"Output {rel}")

if __name__ == "__main__":
    main()

