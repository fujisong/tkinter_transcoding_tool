# class Single:
#     __instance = None
#
#     def __init__(self, age, name):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, age, name):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#
# p1 = Single(20, 'roy')
# p2 = Single(30, 'alisa')
# print(id(p1))
# print(id(p2))

# class Mark:
#
#     def __init__(self, module: str = ''):
#         print("__init__:", module)
#
#     def __call__(self, func):
#         print("__call__:", func.__name__)
#         return func
#
#
# class Api:
#     mark = Mark
#
#
# api = Api()
#
#
# class Demo:
#
#     @staticmethod
#     @api.mark(module='demo1')
#     def demo1():
#         print("demo1()被调用")
#
#     @staticmethod
#     @api.mark(module='demo2')
#     def demo2():
#         print("demo2()被调用")
#
#
# d = Demo()
# d.demo1()
# d.demo2()

# class A:
#
#     def __init__(self, a):
#         self.a = a

# def __new__(cls, *args, **kwargs):
#     print("__new__")

# 如果class定义了__get__，则这个class就称为descriptor。owner是所有者的类，instance是访问 descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。
# （descriptor的实例自己访问自己是不 会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。）


#     def __get__(self, instance, owner):
#         print("visiting this item:", instance, owner)
#         return self
#
#     def __getattr__(self, item):
#         print("no this item:", item)
#
#     def __getattribute__(self, item):  # 无条件被调用，通过实例访问属性
#         print("__getattribute__:", item)
#         return object.__getattribute__(self, item)
#
#
# a = A(2)
# print(a.a)
# a.b
# class B:
#     b=A(2)
#
# print("***********")
# print(B().b)  # b引用a，才会触发__get__

# class A():
#     a = 1
#     b = 2
#     pass
#
#
# c = A()
# print(dir(c))
# from kkkk import people
# p=people()
# print(p.__module__)

# class People:pass
#
# class Teen(People):pass
# class Student(Teen):pass
# print(Student.__bases__)

# def task():
#     while True:
#         print(123)
#         yield
#         print(234)
#
#
# if __name__ == '__main__':
#     t1 = task()
#     while True:
#         next(t1)
#         print('继续执行')
#         next(t1)
# def singleton(cls):
#     instances = {}
#
#     def get_instance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return get_instance
#
#
# @singleton
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# if __name__ == '__main__':
#     c = Student(1, 2)
#     print(c.name)
#     print(c.age)
#     print(id(c))
#     b = Student(7, 4)
#     print(id(b))
#     print(b.name)
#     print(b.age)
# def nihaoa(self):
#     print(self.gh)
#
#
# sh = type("jk", (), {'gh': 123})
# ss = type("jl", (sh,), {"nihaoa": nihaoa})
# print(sh)
# print(sh.gh)
# ss.nihaoa(ss())


class Base:
    pass


# 加上方法
class ChildWithMethod(Base):
    bar = True

    def hello(self):
        print('hello')


def hello():
    print('hello')


# 等价定义，方法用的类外面hello方法
ChildWithMethod = type(
    'ChildWithMethod', (Base,), {'bar': True, 'hello': hello}

