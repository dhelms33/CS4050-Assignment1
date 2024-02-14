"""Dereck Helms"""
from typing import List, Tuple
import time


def linearSearch(list_of_items: List[int], item_sought: int) -> Tuple[int, int, float]:
    """
    Perform linear search on the given list to find the target element.
    Parameters:
    - list_of_items: List[int] - The input list to be searched.
    - item_sought: int - The element to be searched for.
    Returns:
    - Tuple[int, int, float]: A tuple containing the index of the target element,
      the number of comparisons made, and the elapsed time.
    """
    item_index = -1
    number_comparisons = 0
    start_time = time.time()

    # Iterate through each element in the list.
    for i in range(len(list_of_items)):
        number_comparisons += 1
        # Check if the current element is equal to the target.
        if list_of_items[i] == item_sought:
            # Update the index if found.
            item_index = i
            break
    # Calculate the elapsed time.
    elapsed_time = time.time() - start_time

    return (item_index, number_comparisons, elapsed_time)


def binarySearch(list_of_items: List[int], item_sought: int) -> Tuple[int, int, float]:
    """
    Perform binary search on the given sorted list to find the target element.
    Parameters:
    - list_of_items: List[int] - The input sorted list to be searched.
    - item_sought: int - The element to be searched for.
    Returns:
    - Tuple[int, int, float]: A tuple containing the index of the target element,
      the number of comparisons made, and the elapsed time.
    """
    item_index = -1
    number_comparisons = 0
    start_time = time.time()

    # Set initial values for binary search.
    low = 0
    high = len(list_of_items) - 1

    while low <= high:
        number_comparisons += 1
        mid = (low + high) // 2
        # Check if the middle element is equal to the target.
        if list_of_items[mid] == item_sought:
            item_index = mid
            break
        # If the target is smaller, narrow the search to the left half.
        elif list_of_items[mid] > item_sought:
            high = mid - 1
        # If the target is larger, narrow the search to the right half.
        else:
            low = mid + 1
    # Calculate the elapsed time.
    elapsed_time = time.time() - start_time

    return (item_index, number_comparisons, elapsed_time)


def trinarySearch(list_of_items: List[int], item_sought: int) -> Tuple[int, int, float]:
    """
    Perform trinary search on the given list to find the target element.
    Parameters:
    - list_of_items: List[int] - The input list to be searched.
    - item_sought: int - The element to be searched for.
    Returns:
    - Tuple[int, int, float]: A tuple containing the index of the target element,
      the number of comparisons made, and the elapsed time.
    """
    item_index = -1
    number_comparisons = 0
    start_time = time.time()
    low = 0
    high = len(list_of_items) - 1
    while low <= high:
        number_comparisons += 2

        # Calculate two midpoints dividing the search space into three parts
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        # Check if any of the midpoints is the target
        if list_of_items[mid1] == item_sought:
            item_index = mid1
            break
        elif list_of_items[mid2] == item_sought:
            item_index = mid2
            break

        # Narrow the search space based on the comparisons with midpoints
        elif list_of_items[mid1] > item_sought:
            high = mid1 - 1
        elif list_of_items[mid2] < item_sought:
            low = mid2 + 1
        else:
            # If the target is between mid1 and mid2, narrow the search space accordingly
            low = mid1 + 1
            high = mid2 - 1

    elapsed_time = time.time() - start_time

    return (item_index, number_comparisons, elapsed_time)


# Check if the program is being run directly (i.e. not being imported)
def testFunction(search_function, alist, item):
    """Test the specified search function with a given list and item.
    Parameters:
    - search_function (function): The search function to be tested.
    - alist (list): The list to be searched.
    - item: The item to be searched in the list.
    Returns:
    None
    Prints the results of the search, including:
    - Search function name
    - Input list size
    - Item sought
    - Item index (if found)
    - Number of comparisons made during the search
    - Elapsed time for the search
    Example usage:
    testFunction(linearSearch, [1, 2, 3, 4], 3)
    """
    res = search_function(alist, item)
    print(f"\n{search_function.__name__} results")
    print(f"    input list size: {len(alist)}")
    print(f"    item sought: {item}")
    print(f"    item index: {res[0]}")
    print(f"    number of comparisons: {res[1]}")
    print(f"    elapsed time: {res[2]:.6f} seconds")


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    # test functions with a list containing ~20 items
    list1 = [2, 3, 6, 10, 11, 17, 20, 23, 24, 29, 31, 34, 38, 39, 42, 47, 53, 71]
    item1 = 3
    testFunction(linearSearch, list1, item1)
    testFunction(binarySearch, list1, item1)
    testFunction(trinarySearch, list1, item1)
    # test functions with a list containing ~20 items and non-existent item
    list2 = [2, 3, 6, 10, 11, 17, 20, 23, 24, 29, 31, 34, 38, 39, 42, 47, 53, 71]
    item2 = 100
    testFunction(linearSearch, list2, item2)
    testFunction(binarySearch, list2, item2)
    testFunction(trinarySearch, list2, item2)
    # a list of odd numbers from 1 to 1e9
    list3 = list(range(0, int(5e6), 2))
    item3 = int(4e6)
    testFunction(linearSearch, list3, item3)
    testFunction(binarySearch, list3, item3)
    testFunction(trinarySearch, list3, item3)
    # a list of odd numbers from 1 to 1e8 with non-existent item
    list4 = list(range(1, int(1e7), 1))
    item4 = int(1e7)
    testFunction(linearSearch, list4, item4)
    testFunction(binarySearch, list4, item4)
    testFunction(trinarySearch, list4, item4)
