def shift(data,index):
    current=data[index]
    index1=index
    for i in range(index):
        if data[i]>current:
            index1=i
            break
    new_list=[]
    new_list = data[:index1] + [current] + data[index1:index] + data[index + 1:]
    data[:]=new_list

def my_insertion_sort(data):
    for k in range(1,len(data)):
        shift(data, k)
    return data
letters = [ 'k', 'm', 'z', 'n', 'j', 's', 'o', 'p']
my_insertion_sort(letters)
print(letters)
