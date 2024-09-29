import time


def tm(func):
    def wrapper(*args):
        start = time.time()
        result = func()
        end = time.time()
        print(end - start)
        return result
    return wrapper

@tm
def pause():
    time.sleep(2)
    print("pause function endend")

@tm
def quick():
    print("quick function ended")
        

pause()
quick()