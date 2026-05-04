#Create a star pattern in the shape of a square
class Solution:
    def pattern1 (self,n):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()
sol=Solution()
sol.pattern1(4)