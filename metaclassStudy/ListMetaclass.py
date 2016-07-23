class ListMetaclass(type):
    #cls 当前准备创建的类的对象
    #name 类的名字
    #bases 类继承的父类集合
    #attrs 类的方法集合
    #那么类的成员变量呢？
    def __new__(cls, name, bases, attrs):
        print('name = %s\n' % name)
        attrs['add'] = lambda self, value: self.append(value)
        attrs['intvalue'] = 3
        print(attrs)
        return type.__new__(cls, name, bases, attrs)

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，
# 比如，加上新的方法，然后，返回修改后的定义。
class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)
print(L.intvalue)
print(L.__getattribute__('intvalue'))

#普通的list没有add方法
# L2 = list()
# L2.add(1)
