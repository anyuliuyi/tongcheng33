from time import sleep
import threading
import os








# 测试文件路径
excpath = os.getcwd()+'/test-data/int1.24测试集.xlsx'

result =os.getcwd()+'/test-results/intent-1.24-results.xlsx'

url = 'http://172.16.100.16:15001/predict'

# 统计结果参数
passed = 0
failed = 0



class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()
        # threading.Thread.__init__(self)
        # 注意：一定要显式的调用父类的初始化函数。
        self.arg = arg

    def run(self):
        # 定义每个线程要运行的函数
        sleep(1)
        print('the arg is:%s\r' % self.arg)
        for i in range(4):
            t = MyThread(i)
            t.start()
            print('main thread end!')







# def testa():
#     sleep(1)
#     print("a")
# def testb():
#     sleep(1)
#     print("b")
# # testa()
# # testb()
#
#
#
#
#
#
# ta = threading.Thread(target=testa)
# tb = threading.Thread(target=testb)
# for t in [ta,tb]:
#     t.start()
# for t in [ta,tb]:
#     t.join()
#     print ("DONE")

