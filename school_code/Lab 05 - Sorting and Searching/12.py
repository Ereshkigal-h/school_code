def binary_search(numbers, value):
    mid_index=int(len(numbers)/2)
    min_pointer=mid_index
    max_pointer=mid_index
    while min_pointer>=0 and max_pointer<len(numbers):
        if numbers[min_pointer]>value:
            min_pointer=min_pointer-1
        elif numbers[max_pointer]<value:
            max_pointer=max_pointer+1
        elif numbers[min_pointer]==value:
            return min_pointer
        elif numbers[max_pointer]==value:
            return max_pointer
    return -1