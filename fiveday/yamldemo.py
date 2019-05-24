# coding:utf-8
import yaml
import os

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "cfgyaml.yaml")


def read_yaml():
    # open方法打开直接读出来
    fr = open(yamlPath, 'r', encoding='utf-8')
    cfg = fr.read()
    print(type(cfg))  # 读出来是字符串
    print(cfg)

    d = yaml.load(cfg)  # 用load方法转字典
    print(d.get('test_post_tag')['url'])
    print(type(d))


def write_yaml():
    fw = open(yamlPath, 'a', encoding='utf-8')
    my_dict = {"login": {"username": "888888", "password": "8888888"}, "loginout": {"un6": "777777", "pd": "333333"}}
    yaml.dump(my_dict, fw)


read_yaml()

