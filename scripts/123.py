import base64
#encoding=utf-8
data="我爱你中国"
data=data.encode("utf-8")
data_b64=base64.b64encode(data)
data2=str(data_b64,'utf-8')
# print("data:",data)
# print("type:",type(data))
# print("data_b64",data_b64)
# print("tpye2:",type(data_b64))
# print("data2:",data2)
# print("tpye3:",type(data2))

#解密 data2
data2=data2.encode('utf-8')
data2_decode=base64.b64decode(data2)
#data3=str(data2_decode,'utf-8')
data3=data2_decode.decode('utf-8')
print(data3)