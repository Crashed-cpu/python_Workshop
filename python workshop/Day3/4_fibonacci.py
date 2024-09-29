def func(n):
    if n == 1:
        return 1
    
    return (n) + func(n-1)
#cananot call multiple recursion without limit have to give limit


print(func(10))