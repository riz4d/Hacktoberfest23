def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example Usage:
if __name__ == "__main__":
    # Test the insertion_sort function
    unsorted_list = [12, 11, 13, 5, 6]
    print("Unsorted List:", unsorted_list)
    
    insertion_sort(unsorted_list)
    
    print("Sorted List:", unsorted_list)
