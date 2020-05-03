def itos(numb):
    '''This function converts an integer to a string and also returns a value error if a different data type is entered'''
    if isinstance(numb, str) or isinstance(numb, float):
        raise ValueError(f'Enter an Integer: {numb} is not an integer')
    elif isinstance(numb, int):
        t= (f'\'{numb}\'')
    return t


print(itos(1234))
#print(itos(12.34))




def stoi(covern):
    '''This function converts a string to an integer displaying it with out the signature `''` marks, and also returns a value error if a different data type is entered'''
    if isinstance(covern,float) or isinstance(covern,int):
        raise ValueError('Input is not a string')
    else:
        x = (covern)
    return x


print(stoi('14646724689247729497347864865'))




f= '12.34'
def ftos(work):
    '''This function converts a float to a string and also returns a value error if a different data type is entered'''
    if isinstance(work, float) or isinstance(work,int):
        raise ValueError('The input is not a string')
    else:
        x= (f'\'{work}\'')
    return x
print(ftos(f))


fs=12.34
def ftoi(fsnum):
    '''This function converts a float to an integer and also returns a value error if a different data type is entered'''
    if isinstance(fsnum,str) or isinstance(fsnum,int):
        raise ValueError('The input is not a float number')
    else:
        x=('%.d'%fsnum)
    return x

print(ftoi(1344.344456))

