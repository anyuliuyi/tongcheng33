import json,requests

class httprequest:
    # get request
    def sendGet(url):
        responseGet = requests.get(url)
        # return as json string
        return json.loads(responseGet.text)

    # post reguest
    def sendPostwithHeaders(url,header,body):
        postRes = requests.post(url, headers=header, data=body.encode('utf-8'))
        # return as json string
        return json.loads(postRes.text)



