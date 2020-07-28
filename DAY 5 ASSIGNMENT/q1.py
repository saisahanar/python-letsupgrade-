# [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
# Sort by increasing order but all zeros should be at the right hand side
def pushzerotoend(arr,n):
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count]=0
        count+=1
    return arr            



l1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
l1.sort()
print(l1)
n=len(l1)
l1=pushzerotoend(l1,n)
print(l1)
