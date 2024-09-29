def xyz(num, *args):
    print(num)
    print("-------")
    print(args)

#only one args given and all are printed

xyz(1, 2, 3, 4, 5, 5)

#why did one printed first bcz one got into num and other went into args 
#after double star

def xyza(**kwargs):  
    print(kwargs)


xyza(Name="Sujal")
