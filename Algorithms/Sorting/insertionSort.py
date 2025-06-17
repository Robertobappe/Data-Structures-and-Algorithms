from typing import List
# Time coplexity (average and worst) of O(n^2)
# Space complexity of O(1)
# Use cases: if your input is small or mostly sorted
class solution():
    def insertionSort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 1:
             return nums
        
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                if i > 0:
                    prev = 0
                    change = True
                    while change:
                            change = False
                            if ((i - prev - 1 >= 0) and (nums[i - prev - 1] > nums[i - prev])):
                                 nums[i - prev - 1], nums[i - prev] = nums[i - prev], nums[i - prev - 1]
                                 prev += 1
                                 change = True
        return nums


def main():
     test_cases = [
          [3,0,1,8,7,2,5,4,9,6],
          [5432,5,4,86,2,1,35,0],
          [5,12,98,-1,45,4,8,3],
          [12, 11, 13, 5, 6],
          [5, 1, 4, 2, 8]
     ]

     sol = solution()
     for i in test_cases:
          print(f'Input  {i}')
          rel = sol.insertionSort(i)
          print(f'Output {rel}')

if __name__ == "__main__":
     main()