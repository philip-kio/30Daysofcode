def string_test(sentence):
    '''a functions that returns the total number upper and lower letters in hte sentence.s'''
    upper=[]
    lower=[]
    space=[]
    for i in sentence:
        if i.isupper()== True:
            upper.append(i)

        elif  i.isspace()==True:
            space.append(i)
        else:
            lower.append(i)
    u= len(upper)
    l= len(lower)
    x= (f'Number of Lowercase letters is {u}')
    y = (f'Number of Uppercase letter is {l}')
    return(f'{x}\n{y}')


sentence='The Quick brown FOX'
print(string_test(sentence))