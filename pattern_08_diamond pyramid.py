#created diamond pyramid using stars

n=5

for i in range(n):
    space=" "*(n-i)
    star="*"*(2*i+1)
    print(space+star)
for i in range(n-1,-1,-1):
    space=" "*(n-i)
    star="*"*(2*i+1)
    print(space+star)