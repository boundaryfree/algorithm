from functools import wraps
from datetime import datetime

def time_profiling(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        begin_time = datetime.now()
        result = fun(*args, **kwargs)
        cost_time = datetime.now() - begin_time

        print('{} cost time: {}'.format(fun.__name__, cost_time))

        return result

    return wrapper