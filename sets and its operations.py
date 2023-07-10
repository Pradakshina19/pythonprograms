list1 = [1,2,3,4,5]
list2 = [1,2,3]
print("Original list : ", list1)
print("Sub list : ", list2)
if(all(x in list1 for x in list2)):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")
