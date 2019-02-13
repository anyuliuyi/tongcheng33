from framework.httprequests import httprequest
import json
import requests
from framework.framework import gl
test={
    "status_code": 0,
    "msg_response": {
        "update": {
            "act": "other"
        }
    }
}
print(test['msg_response']['update']['act'])

if gl.repaceSpecialCharactersinString("negative-answer") == "negative-answer":
    print('pass')
else:
    print('fail')