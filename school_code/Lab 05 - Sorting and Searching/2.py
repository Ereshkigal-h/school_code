def bubble_row(data, index):
    for i in range(index):
        if ord(data[i])>ord(data[i+1]):
            data[i],data[i+1] = data[i+1],data[i]
    return data
letters = ['e', 'd', 'c', 'b', 'a']
bubble_row(letters, 2)
print(letters)