def get_sum_of_neighbours(a_list):
    new_list=[]
    for i in range(len(a_list)):
        if i == 0:
            new_list+=[a_list[i+1]]
        elif i==len(a_list) -1:
            new_list+=[a_list[i-1]]
        else:
            new_list+=[a_list[i-1]+a_list[i+1]]
    return new_list
