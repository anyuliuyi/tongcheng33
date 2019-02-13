#coding=utf-8
import time
import datetime
import random


class gl:
    @staticmethod
    def repaceSpecialCharactersinString(content):
        return content.replace("^", "").replace("a", "").replace("link", "").replace("text", "").replace("href",
                                                                                                       "").replace(
            "url", "").replace("link", "").replace("~", "").replace("；", "").replace("、", "").replace("=", "").replace(
            "<", "").replace(">", "").replace("{", "").replace("}", "").replace("/", "").replace("+", "").replace("*",
                                                                                                                  "").replace(
            "(", "").replace(")", "").replace("[", "").replace("]", "").replace(" ", "").replace(".", "").replace("-",
                                                                                                                  "").replace(
            "t", "").replace("\t", "").replace("\"", "").replace("“", "").replace("”", "").replace("？", "").replace("?",
                                                                                                                    "").replace(
            "：", "").replace("!", "").replace("。", "").replace("！", "").replace("|", "").replace("n", "").replace("\n", "").replace(
            "，", "").replace(",", "").replace(":", "").replace("～", "").replace("\r", "").replace("r", "").replace("\\", "").replace(' ','')

    @staticmethod
    def getTimewithSeconds():
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    @staticmethod
    def getTimestamp():
        return int(time.time() * 1000)

    @staticmethod
    def getUniqueDateTime():
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(10000, 20000))






if __name__=='__main__':
    # print(gl.getUniqueDateTime())
    # print('哈喽','\\n','你好呀')

    test1='[linktext url="没有收到保险短信怎么办"] 没有收到保险短信怎么办 [/linktext][linktext url="没收到机票出票短信怎么办"] 没收到机票出票短信怎么办 [/linktext][linktext url="没有收到贵宾厅短信"] 没有收到贵宾厅短信 [/linktext][linktext url="在线值机成功是否有短信通知"] 在线值机成功是否有短信通知 [/linktext][linktext url="提交改签后多久知道结果"] 机票改签结果会短信通知吗 [/linktext][linktext url="抢票多久有结果"] 抢票成功有短信通知吗 [/linktext][linktext url="退款到账有短信通知吗"] 退款到账有短信通知吗 [/linktext]'
    print(gl.repaceSpecialCharactersinString(test1))
    # print(gl.getTimestamp())
    # print(int(time.time()))
    test2="查询，退款进度"
    print(gl.repaceSpecialCharactersinString(test2))