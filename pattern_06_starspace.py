#Created a star pattern in form of pyramid

n=5

for i in range(n):
    spaces=" "*(n-i)
    stars="*"*(2*i+1)
    print(spaces+stars)