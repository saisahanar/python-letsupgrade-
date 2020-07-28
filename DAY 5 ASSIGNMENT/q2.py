# list1=[10,20,40,60,70,80] sorted list
# list2=[5,15,25,35,45,60] sorted list
# Merge these two sorted lists to produce one sorted list, but use only loop either while or for only one time
list1=[10,20,40,60,70,80] 
list2=[5,15,25,35,45,60]
list1.sort()
list2.sort()
# print(list1," ",list2)
res=sorted(list1+list2)
print(res)