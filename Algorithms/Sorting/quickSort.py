from typing import List

class Solution:
    def quickSort(self, nums: List[int]) -> List[int]:
        # Time complexity (average) O(nlogn) --> good pivot
        # Time complexity (worst) O(n^2) --> bad pivot
        # Space complexity (worst) O(logn)
        n = len(nums)

        # Base case
        if n <= 1:
            return nums

        # 1. choose the Pivô
        pivot = nums[n - 1] 
        # pivot = nums[len(nums) // 2] Another opition

        # 2. 
        less = []    # Elementos menores que o pivô
        equal = []   # Elementos iguais ao pivô
        greater = [] # Elementos maiores que o pivô

        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else: # x > pivot
                greater.append(x)
        
        # 3. Call recursion and combine
        return self.quickSort(less) + equal + self.quickSort(greater)


def main():
    test_cases = [
        [3,0,1,8,7,2,5,4,9,6],
        [5432,5,4,86,2,1,35,0],
        [5,12,98,-1,45,4,8,3],
        [12, 11, 13, 5, 6],
        [1],
        [],
        [7, 7, 7, 7, 7],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # wost case
    ]

    sol = Solution()
    for original_list_data in test_cases:
        list_copy_for_sorting = list(original_list_data)
        sorted_list = sol.quickSort(list_copy_for_sorting)
        print(f'Input : {original_list_data} | Output: {sorted_list}')

if __name__ == "__main__":
    main()