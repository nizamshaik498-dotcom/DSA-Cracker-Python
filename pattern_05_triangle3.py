#create a right triangle printing numbers in increasing order

class solution:
    def pattern4(self,n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end="")
            print()
sol=solution()
sol.pattern4(5)