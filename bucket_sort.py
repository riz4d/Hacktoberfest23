def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def bucket_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_value) // bucket_range)
        if index != len(arr):
            buckets[index].append(num)
        else:
            buckets[-1].append(num)

    result = []
    for bucket in buckets:
        result.extend(quick_sort(bucket))

    return result
