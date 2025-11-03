import math

def binary_search(num, sorted_list):
    
    if len(sorted_list) == 1:
        return sorted_list[0] == num
    elif len(sorted_list) == 0:
        return False
    
    middle_index = math.trunc((len(sorted_list) - 1) / 2)
    middle_item = sorted_list[middle_index
                             ]
    if num == middle_item:
        return True
    elif num < middle_item:
        return binary_search(num, sorted_list[:middle_index + 1])
    else:
        return binary_search(num, sorted_list[middle_index + 1:])
    
#print(binary_search(0, [1,2,3,4,5]))

def is_list(item):
    return type(item) == type([])

def deep_list_copy(lst):
    copy = []
    for item in lst:
        if is_list(item):
            copy.append(deep_list_copy(item))
        else:
            copy.append(item)
    return copy

#lst1 = [1, [1, 2, [1, 2, 3]], [[[[1]]]]]
#lst2 = deep_list_copy(lst1)
#lst1.pop(0)
#lst2.append(6)
#print(lst1, lst2)

def merge(lst1, lst2):
    if len(lst1) == []:
        return lst2
    if lst2 == []:
        return lst1
    if len(lst1) == 1 and len(lst2) == 1:
        item1 = lst1[0]
        item2 = lst2[0]
        if item1 < item2:
            return [item1, item2]
        else:
            return [item2, item1]
    
    
    highest = lst1[-1]
    if lst2[-1] > highest:
        highest = lst2.pop()
    else:
        lst1.pop()
    
    lowest = lst1[0]
    if lst2[0] < lowest:
        lowest = lst2.pop(0)
    else:
        lst1.pop(0)
    
    return ([lowest] + merge(lst1, lst2) + [highest])
        
#print(merge([1, 4, 9], [2, 6, 8]))
#print(merge([7, 19, 22], [1, 2, 3]))
#print(merge([8, 10, 12, 14, 16], [9]))

def powerset(lst):
    
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [[], [lst[0]]]
    
    else:
        
        removed = lst.pop()
        subset = powerset(lst)
        removed_subset = []
        
        for item in subset:
            if type(item) == type(1):
                removed_subset.append([item, removed])
            else:
                add = list(item)
                add.append(removed)
                removed_subset.append(add)
                
        return removed_subset + subset
    
#print(powerset([1,2,3]))
