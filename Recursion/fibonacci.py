class Solution:
    def fibonacci(self, n: int)-> int:
        #Iterative
        '''
        x0,x1 = 0, 1
        y = 2

        if n < 0:
            return None
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            while y <= n:
                soma = x0 + x1
                x0, x1 = x1, soma
                y += 1
            return soma
        '''
        
        #Recursive
        if n < 0:
            return None
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
        
    

def main():
    testes_cases = [0,1,2,3,4,5,6,7,8,9,10,11,12]

    for i in testes_cases:
        sol = Solution()
        rel = sol.fibonacci(i)

        print(f'Fibonacci of {i} is: {rel}')

if __name__ == '__main__':
    main()