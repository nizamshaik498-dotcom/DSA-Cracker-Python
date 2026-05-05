#Create a right angle star triangle

class solution:
    def pattern2(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
sol=solution()
sol.pattern2(5)