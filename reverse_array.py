#Created an array using list and performing reverse operation on it

colours=['black','yellow','green','blue','red']
rev_colours=colours[::-1]
print("Original array: ",colours)
print("Reversed array: ",rev_colours)


#Created same but using for loop 
reverse=[]
for i in range(len(colours)-1,-1,-1):
    reverse.append(colours[i])
print("Loop reversed :",reverse)