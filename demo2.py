# a = (1,2,3,4,"哈哈哈",True)
# # print (a[4])
# # print(a.index(4))
# # print(a.count(3))
# b =(1,2,5,7,a,"西瓜")
# # print(b[4][3])
# print(b[0:2])
# print(b[3:6])
# b =[1,2,5,7,"a","西瓜",True]
# b.append("zhuijia")
# b.insert(1,345)
# b.pop(1)
# xx=["niahao","buhao"]
# b.extend(xx)
# print(b)
# b.remove("buhao")
# print(b)
# a ={"name":"zhangsan",0:"haha","age":23}
# #取值 键值对
# print(a[0])
# #新增
# a["high"]="188cm"
# print(a)
# #修改
# a["name"]="libai"
# print(a)
# print("--------------")
# b =(a.get("name"))
# print(b)
# b =(a.pop("age"))
# print(b)
# a.update(age=35)
# print(a)

# a=input("输入名字:")
# b=input("输入年龄:")
# c=input("输入性别:")
# d={}
# d["name"]=a
# d["age"]=b
# d["sex"]=c
# print(d)
# d.update({"age":33,"dizi":"dongli"})
# print(d)
# print("------")
a=input("输入名字:")
b=input("输入年龄:")
c=input("输入性别:")
d={}
d.update({"age":b,"name":a,"sex":c})
print(d)
d.update(five="nihao")
print(d)