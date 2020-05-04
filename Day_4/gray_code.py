#
def gray_code(n):
    ''' A function that takes an integer and returns the gray_code of that number.'''
    if n<=0:
        return []
    if n ==1:
        return['0','1']
    mirror= gray_code(n-1)
    return ['0'+ i for i in mirror] +['1'+i for i in mirror[::-1]]
print(gray_code(3))

