from typing import List
class Solution:
    def selectionSort(self, nums: List[int]) -> List[int]:
        # Time complexity O(n^2)
        for i in range(len(nums) - 1):
            minNumber = nums[i]
            change = False
            for j in range(i+1, len(nums)):
                if minNumber > nums[j]:
                    minIndex = j
                    change = True
            if change:
                nums[i], nums[minIndex] = nums[minIndex],nums[i]
        return nums


def main():
    testes_cases = [
        [8,5,2,5,9,3,1,4,0,7],
        [86,5,69,7,2,3,48,9,99],
        [4345,343,563546,8978,54,1]
    ]

    sol = Solution()
    for i in testes_cases:
        print(f"Input  {i}")
        rel = sol.selectionSort(i)
        print(f"Output {rel}")

if __name__ == "__main__":
    main()