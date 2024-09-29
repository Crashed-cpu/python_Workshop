def fb(n):
    if n <= 0:
        return "Positive integer please"
        
    elif n == 1:
        return 0 
        
    elif n == 2: 
        return 1 
    else:    
        return (n-1) + fb(n-2)
    
#cananot call multiple recursion without limit have to give limit
#inbuit quark : print(fb, end=" ") then it will become end cahracter

for i in range(1, 11):

   # print("pause function endend")
    print(fb(9))