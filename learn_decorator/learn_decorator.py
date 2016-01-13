from functools import wraps


def my_decorator(some_function):
    @wraps(some_function)
    def wrapper(*args):
        num = args[0]
        if num == 10:
            print("Yes")
        else:
            print("No")

        some_function(*args)

        print("Something is happening after some_function() is called.")

    return wrapper


# def just_some_function():
# 	print("Wheee!")
#
# just_some_function = my_decorator(just_some_function)
# just_some_function()

@my_decorator
def just_some_function(*args):
    print("Wheee!")


just_some_function(10)
print(just_some_function.__name__)
