#  Create a decorator to print the function name and the values of its arguments every time the function is called.


def debug(func):
    def wrapper(*args, **kwargs):
        # Combine positional and keyword arguments into a clean string
        all_args = [str(arg) for arg in args]
        all_kwargs = [f"{k} = {v}" for k, v in kwargs.items()]
        final_args = ", ".join(all_args + all_kwargs) 

        print(f"Function Name: {func.__name__} | Arguments: {final_args} ")
        result = func(*args, **kwargs)
        return result
    return wrapper
    

    
@debug
def greet(name , greeting="Hanji!"):
    print(f"{greeting} {name} 😁")


greet("CatNova", greeting="Hanji! Beta")
