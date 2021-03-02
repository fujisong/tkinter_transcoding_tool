import subprocess, jpype, os, chardet


class Decryption:
    def __init__(self, name):
        self.jarpath = os.path.join(os.path.split(os.path.abspath(__file__))[0], name)

    def getcommand(self, pas) -> str:
        return "java -jar  -Dpassword={}  {}".format(pas, self.jarpath)

    def commanddecryption(self, content):
        """
        通过shell调用java解密
        :param content:
        :return:
        """
        stdout, stderror = subprocess.Popen(self.getcommand(content), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            shell=True).communicate()
        encoding = chardet.detect(stdout)['encoding']
        result = stdout.decode(str(encoding))
        return result

    def __enter__(self):
        self.start()
        return self

    def start(self):
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path={}".format(self.jarpath))
        print("开启jvm")

    def jvmdecryption(self, content):
        """
        通过jpy启用jvm进行解密
        :param content:
        :return:
        """
        JDClass = jpype.JClass("common.pass.EncryptionByFun")()
        res = JDClass.reverse(content)
        return res

    def test(self, name):
        jpype.java.lang.System.out.println(name)

    def jvmjudgment(self):
        return jpype.isJVMStarted()

    def shutdown(self):
        jpype.shutdownJVM()
        print("关闭jvm")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()


if __name__ == '__main__':
    with Decryption("stujvm.jar") as f:
        print(f.jvmdecryption("1234567"))
