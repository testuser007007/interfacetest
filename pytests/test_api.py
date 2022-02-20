# author fc
import pytest
import os
from pytest_yaml.yaml_util import YamlUtil
from common.requestutil import RequestUtil
class TestApi:
    @pytest.mark.parametrize("args",YamlUtil.read_yaml(os.path.dirname(os.getcwd())+'\\pytest_yaml\\get_new.yaml'))
    def test_get_new(self,args):
        """
        获取网易新闻的接口
        :param params:
        :return:
        """
        url=args['api_request']['url']
        method=args['api_request']['method']
        headers=args['api_request']['headers']
        params=args['api_request']['params']
        validate=args['api_validate']
        res=RequestUtil.send_request(method,url,params,headers=headers)
        










if __name__=='__main__':
    pytest.main(['-vs','test_api.py'])

