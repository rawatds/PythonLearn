from functools import wraps

def mylogger(orig_func):

    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Executing {} with args: {} and kwargs: {}".format(orig_func.__name__, args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def mytimer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()
        result = orig_func(args, kwargs)
        t2 = time.time()
        print("{} took {} sec to execute".format(orig_func.__name__, (t2 - t1)))
        return result

    return wrapper




@mytimer
@mylogger
def display_info(name, age):
    import time
    time.sleep(1)
    print("display_info with {} and {}".format(name, age))


display_info("Raju", 50)