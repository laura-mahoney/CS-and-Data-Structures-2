#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    
    for i in range(len(lst)-1):

        been_swapped = False

        for j in range(len(lst) - (1 + i)):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                been_swapped = True 

        if not been_swapped: 
            break

    return lst 







def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    sorted_list = []

    while list1 and list2:
        first_num1 = list1[0]
        first_num2 = list2[0]
        i = 0
        j = 0  
        if first_num1 < first_num2:
            sorted_list.append(first_num1)
            list1 = list1[i+1:]
        else:
            sorted_list.append(first_num2)
            list2 = list2[j+1:]


    sorted_list.append(list2[-1])


    return sorted_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    
    if len(lst) == 1:
        return lst

    split = int(len(lst) / 2)

    list1 = merge_sort(lst[split:])
    list2 = merge_sort(lst[:split])

    sorted_list = []

    while list1 and list2:
        if list2[0]<list1[0]:
            sorted_list.append(list2.pop(0))

        elif list1[0]<list2[0]:
            sorted_list.append(list1.pop(0))

    while list2:
        sorted_list.append(list2.pop(0))

    while list1:
        sorted_list.append(list1.pop(0))


    return sorted_list



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
