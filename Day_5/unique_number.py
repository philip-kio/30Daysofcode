def unique_list(l):
    '''This function returns the unique numbers and returns a list, such that a number is not repeated'''
    x=[]
    for i in l:
        if i not in x:
            x.append(i)
    return x

l = [1,2,3,3,4,4,4,4,5,6,5,5,5,5,7,8,9,100,100,100]
print(unique_list(l))