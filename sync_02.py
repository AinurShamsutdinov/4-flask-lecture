import time


def slow_function():
    print('Beginning of function')
    time.sleep(5)
    print('End of function')


print('Beginnig of application')
slow_function()
print('End of application')
