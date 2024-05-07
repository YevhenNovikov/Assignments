def catch_errors(func):

    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        
        except KeyError as variable:

            print(f"Found 1 error during execution of your function: KeyError no such key as {variable}")

        except Exception as variable:

            print(f"Found 1 error during execution of your function: {type(variable).__name__} - {variable}")
    
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})