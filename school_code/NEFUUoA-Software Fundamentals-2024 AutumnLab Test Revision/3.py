def index_of_closest(a_list, number):
    new_list=[]
    for i in range(len(a_list)):
        a_list[i]=abs(a_list[i]-number)
    temp=min(a_list)
    return a_list.index(temp)