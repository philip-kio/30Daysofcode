


def even_odd(x):
    '''Takes a list of numbers and then returns the even and odd numbers in the list'''
    even_num = []
    odd_num = []
    sum1=0
    for i in x:
        if i%2 <=0:
            even_num.append(i)
            sum1+=1
        elif i%2>0:
            odd_num.append(i)
    t=(len(even_num))
    x=(len(odd_num))
    w= f'number of odd numbers = {x}'
    y= f'number of even numbers = {t}'
    return (f'{w}\n{y}')

print(even_odd([1,2,3,4,5,6,7,8,9,10,18]))
print(even_odd(range(15,30)))