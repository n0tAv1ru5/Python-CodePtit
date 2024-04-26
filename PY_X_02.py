def max_subarray_sum(arr):
    max_so_far = max_ending_here = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            temp_start = i
            max_ending_here = arr[i]
        else:
            max_ending_here += arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start, end = temp_start, i

    return start, end, max_so_far

input()  

arr = list(map(int, input().split()))
start, end, max_sum = max_subarray_sum(arr)

print("{} {} {}".format(start + 1, end + 1, max_sum))