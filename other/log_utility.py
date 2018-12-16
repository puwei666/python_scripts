import functools

def log(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s begin %s' %(func.__name__, text)
            func(*args, **kw)
            print 'call %s end %s' %(func.__name__, text)
        return wrapper
    return decorator

@log('test')
def now():
    print '2017-09-04'

# ===== execute =====

now()

print now.__name__
