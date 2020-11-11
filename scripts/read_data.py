import yaml,os
#读取yaml格式的数据文件
def read_yaml_data(filename):
    """
    :param filename: 数据文件名
     os.sep 反斜杠命令
    :return:
    """
    pro_rootdir="E:\\AppProject" #项目根目录
    data_dir="data_file" #数据文件所在的文件夹目录名
    filepath=pro_rootdir + os.sep +data_dir + os.sep + filename + ".yaml"
    with open(filepath,"r",encoding="utf-8") as f:
        return yaml.load(f)