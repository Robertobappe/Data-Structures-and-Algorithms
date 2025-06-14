from typing import List
class Solution():
    def reverseString(self, string: List[str]) -> List[str]:
        '''
        return string[::-1] # Time and space complexity o(n)
        '''

        #Recursive
        '''
        if len(string) <= 1:
            return string
        
        return self.reverseString(string[1:]) + string[0]
        '''

        #If we want to: You must do this by modifying the ]
        # input array in-place with O(1) extra memory.
        left, right = 0, len(string) - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left, right = left + 1, right - 1
        return string
    
def main():
    #testes_cases = ["yoyo master","Roberto","Teste"]
    testes_cases = [["h","e","l","l","o"],["H","a","n","n","a","h"]]

    for j in testes_cases:
        sol = Solution()
        rel = sol.reverseString(j)

        print(f"String {j} so reverseString is: {rel}")

if __name__ == "__main__":
    main()