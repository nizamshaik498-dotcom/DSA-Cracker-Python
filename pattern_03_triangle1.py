#Create a star pattern triangle in reverse .

class solution:
    def pattern3(self,n):
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            print()
sol=solution()
sol.pattern3(5)