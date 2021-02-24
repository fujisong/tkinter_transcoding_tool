# class Spider:
#     def __init__(self):
#         pass
#     def kill(self):
#
#         print('成功')
#         return 123
#
# class C:
#     def lll(self):
#         return 12354
#
# class Session:
#     def __init__(self, spider_session: Spider):
#         self.spider_session = spider_session
#         self.session = self.spider_session.kill()
#
#     def last(self):
#         print('wwww')
#
#
# c = Session(C())

# class Base:
#     pass
#
#
# def hello(self):
#     print('hello')
#
#
# # 等价定义，方法用的类外面hello方法
# ChildWithMethod = type('ChildWithMethod', (Base,), {'bar': True, 'hello': hello})
# ChildWithMethod().hello()

# class LowercaseMeta(type):
#     ''' 修改类的属性名称为小写的元类 '''
#
#     def __new__(mcs, name, bases, attrs):  # 生成实例
#         lower_attrs = {}  # 定义字典
#         for k, v in attrs.items():  # 遍历类所有属性，把非内置方法(魔术方法)都改成小写
#             if not k.startswith('__'):  # 排除magic method魔术方法
#                 lower_attrs[k.lower()] = v  # 方法名变成小写
#             else:
#                 lower_attrs[k] = v
#             # 当前类mcs,名称name,基类bases,当前属性lower_attrs
#         return type.__new__(mcs, name, bases, lower_attrs)
#
#
# class LowercaseClass(metaclass=LowercaseMeta):  # py3
#     BAR = True

#     def HELLO(self):
#         print('hello')
#
#
# print(dir(LowercaseClass))  # 你会发现“BAR”和“HELLO”都变小了
# # 用一个类的实例调用hello方法，修改了类定义时候的属性名称！！！
import jpype, os, subprocess, chardet

# jvmpath = jpype.getDefaultJVMPath()
# print(jvmpath)
jarpath = os.path.join(os.path.split(os.path.abspath(__file__))[0], "stu.jar")
# print(os.getcwd(), jarpath)
# jpype.startJVM(jvmpath, "-ea", "-DJava.class.path={}".format(jarpath))
# jpype.java.lang.System.out.println("helloworld")

command = "java -jar  -Dpassword={}  {}".format("helloworld", jarpath)
stdout, stderror = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
encoding = chardet.detect(stdout)['encoding']
result = stdout.decode(encoding)
print(result)

