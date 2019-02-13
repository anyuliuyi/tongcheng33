import os


# 竹间-同程项目下两个机器人 appid
# 在线端机器人 appid
online_appId = 'b6ad1f823d8d4ffea36568330239f237'


# ivr端机器人的 appid
ivr_appid = '19106fb32b2844fbbb1dc22023ea8afe'



# 同程项目 openapi 地址如下
# url = 'http://shadow.emotibot.com/openapi/chat'

openapi_url = 'http://poc1.emotibot.com:1680/v1/openapi'


#nlu接口url地址如下
#是否接口
confirm = 'http://poc2.emotibot.com:10999/tde/usp/parse'

#选择接口

parse = 'http://poc2.emotibot.com:10999/tde/usp/parse'






#测试意图 测试文件路径
intent_file = os.getcwd()+'/test-data/1.25intent测试语料.xlsx'

intent_result = os.getcwd()+'/test-results/1.25测试结果.xlsx'



#testcase数值:
testcase_file = os.path.dirname(os.path.abspath('.'))+'/data/测试题上传.xls'


TestCase_result = os.path.dirname(os.path.abspath('.'))+'/data/测试题上传_result.xls'






payload = {
    'userId': '005D6083BAC610C83AD6F7E3F0FB1A8EA',
    'appId': '6afa4f2ddd96cb643b7438d8dff94bed',
    'inputText': "苹果手机的颜色",
    "responseFlag": "all",
    "properties": [{"name": "answerTag", "value": "Web"}]
}