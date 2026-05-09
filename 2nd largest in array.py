#Created a program which finds out the second largest element in array.

arr1 = [10, 85, 300, 250, 60, 560, 1500, 280]
large = -1
second_large = -1
third_large = -1
for num in arr1:
    if num > large:
        second_large = large
        large = num
    elif num > second_large and num != large:
        second_large = num
    elif num > third_large and num != second_large:
        third_large = num

print("The Gold Medalist (Largest) is:", large)
print("The Silver Medalist (Second Largest) is:", second_large)
print("The Bronze Medalist (Third largest) is:",third_large)