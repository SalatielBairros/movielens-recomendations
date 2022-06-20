import datetime

def memo(f):    
    f.cache = {}
    def _f(*args, **kwargs):
        key = __get_cache_key__(args, f)
        if key not in f.cache or f.cache[key]['expiration'] < datetime.datetime.now():
            f.cache[key] = {
                'data': f(*args, **kwargs),
                'timestamp': datetime.datetime.now(),
                'expiration': datetime.datetime.now() + datetime.timedelta(minutes=10)
            }        
        return f.cache[key]['data']
    return _f

def __get_cache_key__(args, f):
    if(len(args) > 0 and hasattr(args[0], f.__name__)):
        return args[1:]
    return args