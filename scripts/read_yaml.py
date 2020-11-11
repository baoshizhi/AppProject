from scripts.read_data import  *
import os

ydata=read_yaml_data("data2")
print(ydata)

# import yaml
# with open("../data_file/data.yaml","r",encoding="utf-8") as f:
#     data=yaml.load(f)
#     # print(data)
#     # print(type(data)) #字典类型
#     # print(data.get("animal"))  #获取字典animal的Key值
#     # print(data.get("dic"))# 获取字典animal的Key值
#     # print(data.get("arr"))
#     # print(data.get("abb").get("a5"))
#     # print(data.get("abb"))
#     print(data)

    # data_login=data.get("login")
    # for i in data_login.keys():
    #     print("\nlogin:%s\nname:%s\npwd:%s"
    #           %(i,data_login.get(i).get('name'),data_login.get(i).get('pwd')))

        #print('\nuser:%s\nname:%s\npwd:%s\n %(i,data_login.get(i).get("name"),data_login.get(i).get("pwd"))')



