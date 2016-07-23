import functools
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):   #这里不一定要叫wrapper，叫abc也可以的
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)
@log
def now():
    print('2015-3-23')

now()
print(now.__name__)
