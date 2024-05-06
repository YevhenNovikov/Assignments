def is_admin(func):
    def wrapper(user_type: str):

        if user_type == 'admin':
            return func(user_type)
        
        else:
            raise ValueError("Permission denied")
    
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print("Show customer receipt")



show_customer_receipt(user_type='admin')
show_customer_receipt(user_type='user')