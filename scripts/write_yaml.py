import yaml
data={'student': {'student1': {'name': 'baoshizhi01', 'sex': '男', 'age': 21},
                  'student2': {'name': 'baoshizhi02', 'sex': '男', 'age': 22},
                  'student3': {'name': 'baoshizhi03', 'sex': '男', 'age': 23}}}

with open("../data_file/data_write.yaml","w") as f:
    yaml.dump(data,f,encoding='utf-8',allow_unicode=True)