import functools

def log(text):
    def decorator(func):
        #因为返回的那个wrapper()
        #函数名字就是
        #'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()
        #函数中，否则，有些依赖函数签名的代码执行就会出错。
        #不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#>>> now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-23')

now()
print(now.__name__)