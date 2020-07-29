# Take a list of tuple as shown below.
# [(1,2), (3,4), (5,6),(4,5)]
# Make a new list which contains the sum of the number of tuples.
# For example
# Input
# [(1,2), (3,4), (5,6)]
# Output
# [3, 7, 11]


l1=[(1,2), (3,4), (5,6),(4,5)]
lsum=[]
for i in l1:
    lsum.append(i[0]+i[1])
print(lsum)    

