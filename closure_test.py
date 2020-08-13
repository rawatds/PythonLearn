import logging

logging.basicConfig(filename="app.log", filemode="a", level=logging.INFO)

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def logger(func):

    def log(*args):
        logging.info("Executing '{}' with args: {}".format(func.__name__, args))
        print(func(*args))

    return log

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 4)
sub_logger(12, 8)

logger(add)(9, 20)
