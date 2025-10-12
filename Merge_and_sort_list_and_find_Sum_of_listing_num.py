list1=[1,4,2,8,5,89,9]
list2=[3,7,11,5,79,13]

merge_list=list1+list2
merge_list.sort()

total_sum=sum(merge_list)

print("Sorted list after merging : ",merge_list)
print("Sum of the List value : ",total_sum)