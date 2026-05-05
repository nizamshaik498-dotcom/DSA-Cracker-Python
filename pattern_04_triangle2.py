#create a right triangle printing same numbers in each row 

class solution:
    def pattern4(self,n):
        for i in range(n):
            for j in range(i+1):
                print(1+i,end="")
            print()
sol=solution()
sol.pattern4(5)