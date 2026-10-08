list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)

common = sorted(set1 & set2)
only_list1 = sorted(set1 - set2)
only_list2 = sorted(set2 - set1)

print("Common elements:", common)
print("Only in list 1:", only_list1)
print("Only in list 2:", only_list2)