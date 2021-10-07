def func(a):
    for elem in a:
        print(elem)
    if a==a[::-1]:
        return ('YES')
    else:
        return('NO')
a = 'ghfjg'
print(func(a))

