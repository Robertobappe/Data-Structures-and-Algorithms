from typing import List

class solution():
    def mergeSort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 0. Base case
        if n <= 1:
            return nums
        # 1. Divide 
        middle = n // 2
        left_half = nums[:middle]
        right_half = nums[middle:]
        # 2. Conquer 
        sorted_lef = self.mergeSort(left_half)
        sorted_right = self.mergeSort(right_half)
        # 3. Combine/merge
        return self._merge(sorted_lef, sorted_right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        merged_list = []
        i = 0
        j = 0
        # Compare elements from both lists and add to the merged_list
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1
        # Add the remaning elements to the list left (if it exits)
        while i < len(left):
            merged_list.append(left[i])
            i += 1
        # Add the remaning elements to the list right (if it exits)
        while j < len(right):
            merged_list.append(right[j])
            j += 1
        return merged_list
        
    
def main():
    test_cases = [
        [3,0,1,8,7,2,5,4,9,6],
        [5432,5,4,86,2,1,35,0],
        [5,12,98,-1,45,4,8,3],
        [12, 11, 13, 5, 6],
        [1], # Teste com 1 elemento
        []   # Teste com lista vazia
    ]

    sol = solution()
    for input in test_cases:
        rel = sol.mergeSort(input)
        print(f"Input {input}  output {rel}")

if __name__ == "__main__":
    main()

    