def merge_sort_in_place(lst):
    """
    The function sorts the list in place using the merge sort algorithm.
    https://en.wikipedia.org/wiki/In-place_algorithm
    https://en.wikipedia.org/wiki/Merge_sort
    :param lst: list
    :return: None
    """
    if len(lst) > 1:
        # Finding the mid of the list
        mid = len(lst) // 2
        # Left half
        left = lst[:mid]
        # Right half
        right = lst[mid:]
        # Recursive call to sort the left half
        merge_sort_in_place(left)
        # Recursive call to sort the right half
        merge_sort_in_place(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        # Copy data to temp lists left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                lst[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


# Lists to use for binarySearch() and mergeSort() tests
lst1 = [1, 5, 2, 6, 2]
lst2 = [9, 8, 7, 6.5]
lst3 = [5, -3, 7, -3]
lst4 = [1]
lst5 = []
lst6 = ['hello', 'a', 'the']



def test_merge_sort_in_place():
    """
    This is a suite of tests for the merge_sort_in_place function.
    :return:
    """
    # The below lines apply the `merge_sort_in_place` function to the `lst_*`
    # lists. After the application the lists should be sorted.
    merge_sort_in_place(lst1)
    merge_sort_in_place(lst2)
    merge_sort_in_place(lst3)
    merge_sort_in_place(lst4)
    merge_sort_in_place(lst5)
    merge_sort_in_place(lst6)


    assert lst1 == [1, 2, 2, 5, 6]
    assert lst2 == [6.5, 7, 8, 9]
    assert lst3 == [-3, -3, 5, 7]
    assert lst4 == [1]
    assert lst5 == []
    assert lst6 == ['a', 'hello', 'the']

    # Below, please, write tests based on `lst2` - `lst6`. A sample test for
    # `lst1 is provided above.`
    # TODO 3: PLACE YOUR CODE HERE

