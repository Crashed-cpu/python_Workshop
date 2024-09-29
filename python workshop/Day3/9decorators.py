#made for other functions
#always have an argument
def abc(function):
    def wrapper():
        function()

    return wrapper()
#default def wrapper(): tells us we are making it decorator funcdtion
#@abc
@abc
def xyz():
    print(";alksdjf")

