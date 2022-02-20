# author fc
import yaml
import os
class YamlUtil:

    @staticmethod
    def read_yaml(yaml_name):
        """
        读取yaml文件
        :return:
        """
        print(type(yaml_name))
        with open(yaml_name,mode='r',encoding='utf-8') as f :
            data=yaml.load(stream=f,Loader=yaml.FullLoader)
            return data

