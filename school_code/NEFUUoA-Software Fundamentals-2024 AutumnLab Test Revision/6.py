def example_function(a_list):
    n = len(a_list)
    for i in range(n):
        for j in range(3):
            for k in range(1, j):
                print(i+j+k)
#O(n)

