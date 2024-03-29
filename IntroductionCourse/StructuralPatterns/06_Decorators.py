from functools import wraps


def make_blink(function):
    """Defines the Decorator"""
    @wraps(function)

    def decorator():
        #Grab the return value of the function being decorated
        ret = function()
        #Add new functionality
        return "<blink>"+ret+"</blink>"

    return decorator

@make_blink
def hello_world():
    """Original Function"""
    return "Hello World"


print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)