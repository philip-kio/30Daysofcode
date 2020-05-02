def missing_num(x):
    '''This function accepts a list of numbers and finds the range of the already sorted list
     and then finds the missing values.'''
    index_1= (x[0])#this selects the first index of a list of numbers
    index_2=(x[-1])# this selects the last index of the list
    index_2+=1 #this ensures that the range of these number does not stop before the last number of the list.
    z= range(index_1,index_2) #this is gets the range of numbers
    complete_nums=[] #an empty list for the reassignment of i during the loop

    for i in z:# gets the i in the range of numbers
         complete_nums.append(i)# reassignment of the i values to a list
    not_there=[]#an empty list for the reassignment of the missing numbers
    for i in complete_nums:
        if i not in x:#a means of comparing the given list passed with the range of list.
            not_there.append(i)
    return not_there # returns the missing values



num_list = [1,2,3,4,6,7,10]
print(missing_num(num_list))
num_list_1= [10,14,15,19,20,30]
print(missing_num(num_list_1))

num_list_2=[10,11,12,14,17]
print(missing_num(num_list_2))