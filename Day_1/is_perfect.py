def is_perfect_square(a):
    ''' This function accepts a number(either int or float) then carries out math operations.
    Such as square roots and multiplication by power.'''
    y= a**(1/2) #divides the int to get the square root.
    z= y**2 #then the result of the square root is multiplied by  power 2
    z=int(z) #the result is then reassigned to z as an integer.
    if z==a: #conditional statements are then used to check via bool if it is a perfect square.
        print(True)
    else:
        print(False)


is_perfect_square(9)
is_perfect_square(100)
is_perfect_square(225)
is_perfect_square(500)