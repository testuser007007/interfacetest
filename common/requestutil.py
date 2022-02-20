# author fc
import json

import requests
class RequestUtil:
    session=requests.session()
    @staticmethod
    def send_request(method,url,data,**kwargs):
        method=str(method).lower()
        rep=None
        if method=='get':
            rep=RequestUtil.session.request(method,url,params=data,**kwargs)
        elif method=='post':
            data=json.dumps(data)
            rep=RequestUtil.session.request(method,url,data=data,**kwargs)
        else:
            print("请求方法错误")
        return rep.json()