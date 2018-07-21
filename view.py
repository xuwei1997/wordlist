import mysql.connector

#输入单元
unit = input("请输入单元:")
print ("word list:"+unit)

#数据库连接
conn = mysql.connector.connect(user='root', password='123', database='test')
cursor = conn.cursor()

#数据库读取
cursor.execute("select * from word where unit = %s"%(unit))
# cursor.execute("select * from word where unit = 1;")
values = cursor.fetchall()
# print(values)
total = len(values)

#数据库结果读取认识的单词
print("认识的单词：........................................")
cursor.execute("select * from word where unit = %s and wkey = %s",(unit,"1"))
values_end = cursor.fetchall()
i=1
for word in values_end:
    print(str(i)+'：'+word[0]+'：'+word[1])
    i=i+1

#数据库结果读取不认识的单词
print("不认识的单词：........................................")
cursor.execute("select * from word where unit = %s and wkey = %s",(unit,"2"))
values_end = cursor.fetchall()
# print(values_end)
errorlist = len(values_end)
i=1
for word in values_end:
    print(str(i)+'：'+word[0]+'：'+word[1])
    i=i+1


print("准确率：............")
print(errorlist)
print(total)
print(1-errorlist/total)

#数据库关闭
cursor.close()
conn.close()
input("输入回车退出程序")