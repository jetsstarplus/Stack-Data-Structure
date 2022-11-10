def recursion_max(list_input: list, maxVal: int=0, count:int=0):
    """
        Worst case Time Complexity is O(n) since we can find the last value at the end of the list

        Space Complexity is O(n) since we are allocating memory space each time we call the recursive function
        dropped
    """
    if count< len(list_input):
        if list_input[count] > maxVal:
            maxVal = list_input[count]
        count += 1
        return(recursion_max(list_input, maxVal, count))
    return maxVal

print(recursion_max([1, 3, 6, 2, 4]))
print(recursion_max([4,3, 6, 2]))
print(recursion_max([8,4, 2, 7, 5]))
print(recursion_max([4, 3, 5, 2, 66, 2]))

