def get_position_of_highest(data, index):
    a=max(data[:index+1])
    index1=data.index(a)
    return index1

def selection_row(data, index):
    index1=get_position_of_highest(data, index)
    data[index],data[index1] = data[index1],data[index]
    return data
