sum = 10
def xyz(a, b): 
    global sum 
    sum = a + b
    return sum
#global keyword helps in changing value globally

abc = xyz(1, 2)
print(sum)
print(abc)
