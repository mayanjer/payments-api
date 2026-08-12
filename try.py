def sum_numbers(*args):
    for arg in args:
        print(arg)

def create_object(**kwargs):
    return kwargs

def create(*args, **kwargs):
    print(f"Args: {args} Kwargs: {kwargs}")
    
args = (1,2,3)

create(args, name="Mayanja", gender = "Male")
