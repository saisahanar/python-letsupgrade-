# List1 = [1,2,3,4,5,7,8]
# List2 = [“a”, “b”, “c”, “d”, “e”]
# Convert to a dictionary in one line code using list comprehension (without using zip method
def comprehension(keys,values):
    d={}
    for k in range(len(keys)):
        d[keys[k]]=values[k]

    return d
List1 = [1,2,3,4,5]
List2 = ["a","b","c","d","e"]
listtodict=comprehension(List1,List2)
print(listtodict)


