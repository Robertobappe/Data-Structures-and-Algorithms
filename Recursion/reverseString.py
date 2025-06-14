class Solution():
    def reverseString(self, string: str) -> str:
        '''
        return string[::-1] # Time and space complexity o(n)
        '''

        #Recursive
        if len(string) <= 1:
            return string
        
        return self.reverseString(string[1:]) + string[0]
    
    
def main():
    testes_cases = ["yoyo master","Roberto","Teste"]

    for j in testes_cases:
        sol = Solution()
        rel = sol.reverseString(j)

        print(f"String {j} so reverseString is: {rel}")

if __name__ == "__main__":
    main()