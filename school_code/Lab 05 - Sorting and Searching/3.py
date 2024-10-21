def bubble_row(data, index):
    for i in range(index):
        if ord(data[i])>ord(data[i+1]):
            data[i],data[i+1] = data[i+1],data[i]
    return data
def my_bubble_sort(data):
    for k in range(len(data)-1,0,-1):
        bubble_row(data,k)
    return data
