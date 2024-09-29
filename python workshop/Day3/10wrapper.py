#made for other functions
#always have an argument
def abc(function):
    def wrapper():
        function()

    return wrapper
#had to remove () (call ) to call it after line 14 xyz()
#default def wrapper(): tells us we are making it
#  decorator funcdtion
#@abc

@abc
def xyz():
    print(";alksdjf")

xyz()