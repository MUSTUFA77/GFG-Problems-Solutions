#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	result = []
        fact = 1
        i = 1
        
        while True:
            fact *= i
            if fact > n:
                break
            result.append(fact)
            i += 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends