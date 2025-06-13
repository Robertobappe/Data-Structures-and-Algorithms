class Solution:
    def factorial(self, n: int) -> int:
        #Iterative
        '''
        fat = 1
        if n <= 0:
            return None
        while n >= 1:
            fat = fat*n
            n -= 1
        return fat
        '''
        
        # Recursive
        if n < 0:
            return None
        elif n== 0 or n == 1:
            return 1        
        return n*self.factorial(n - 1)
    
def main():
    tests_cases = [-8,0,3,5]
    
    for n in tests_cases:
        sol = Solution()
        rel = sol.factorial(n)
        print(f"Fatorial de {n} é: {rel}") 

if __name__ == "__main__":
    main()

# In both cases we have time complexity of O(n)