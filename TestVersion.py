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


# print(os.getcwd(), jarpath)
# jpype.startJVM(jvmpath, "-ea", "-DJava.class.path={}".format(jarpath))
# jpype.java.lang.System.out.println("helloworld")
import jpype
import os


class Decryption:
    def __init__(self, name):
        self.jarpath = os.path.join(os.path.split(os.path.abspath(__file__))[0], name)

    def getcommand(self, pas) -> str:
        return "java -jar  -Dpassword={}  {}".format(pas, self.jarpath)

    def commanddecryption(self, content):
        stdout, stderror = subprocess.Popen(self.getcommand(content), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            shell=True).communicate()
        encoding = chardet.detect(stdout)['encoding']
        result = stdout.decode(encoding)
        return result

    def __enter__(self):
        self.start()
        return self

    def start(self):
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path={}".format(self.jarpath))
        print("开启jvm")

    def jvmdecryption(self, content):
        JDClass = jpype.JClass("common.pass.EncryptionByFun")()
        res = JDClass.reverse(content)
        return res

    def test(self, name):
        jpype.java.lang.System.out.println(name)

    def shutdown(self):
        jpype.shutdownJVM()
        print("关闭jvm")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()


if __name__ == '__main__':
    with Decryption("stujvm.jar") as f:
        print(f.decryption("1234567"))
