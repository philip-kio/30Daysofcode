def average(s):
    '''This function takes a string and then splits the string remove the white spaces and makes a list
    Then using list reassignment we convert the string into integers and then perform mathtematical operation'''
    a=s.split() #removes the white spaces and then create a list.
    b=[]
    for i in a: #This for loop is used to loop through the list a
        b.append(int(i)) #then the items in the list is converted from string to int
        r= sum(b)//len(b) #then using the sum function the items in b are added together and divided by the len b to give the mean
    print (r)



s='12 11 2 6 7 10'
average(s)