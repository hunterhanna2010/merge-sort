# two lists: list 1 = [0, 19, 87, 1001] list 2 = [-2.5, -1.1, 99.8]
# merge the lists ordered from least to greatest

#1. create an empty list so the contents of list 1 and list 2 can be sorted as one merged list
#2. loop through both lists. Compare which number is lesser or greater. If it is lower, proceed to next index.

arr1 = [0, 19, 87, 1001]
length_of_arr1 = len(arr1)

arr2 = [-2.5, -1.1, 99.8]
length_of_arr2 = len(arr2)

arr3 = [None] * (length_of_arr1 + length_of_arr2)

def merge_arrays(arr1, arr2, length_of_arr1, length_of_arr2):
    # Initiate the index position at 0 to increment after comparisons are finished
    # arr1
    i = 0
    # arr 2
    j = 0
    # arr 3
    k = 0

    # Loop through both arrays using a while loop: while the current index of arr1 is less than 
    # the length of arr1 and the current index of arr 2 is less than the length of arr2
    while i < length_of_arr1 and j < length_of_arr2:
        # Check to see if the current index of arr1 is less than the current index of arr 2
        # if it is, store the current index and increment to next index point. Else, assign the current index of arr 2 to arr3
        if arr1[i] < arr2[j]:
            # assign the current index to the 3rd array
            arr3[k] = arr1[i]
            # increment to the next index in arr1 and the copy arr3
            i = i + 1
            k = k + 1
        else:
            # assign the current index of arr2 to arr3 and then increment to the next position
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    # concurrent while loops for arr1 and arr2 to store the remaining contents of both arrays into arr3
    while i < length_of_arr1:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1

    while j < length_of_arr2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    print("Array after merging")

    for i in range(length_of_arr1 + length_of_arr2):
        print(str(arr3[i]), end = ', ')

merge_arrays(arr1, arr2, length_of_arr1, length_of_arr2)

