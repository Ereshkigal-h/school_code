def shifting(data, index):
    new_list=[]
    index1=0
    for i in range(len(data)):
        if ord(data[index])<ord(data[i]):
            index1=i
            break
    new_list+=data[:index1+1]
    for k in data[index1:]:
        if k != data[index]:
            new_list+=[k]
    data[:]=new_list#深拷贝和浅拷贝
    return data