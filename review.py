import mysql.connector
import random
import operator

#输入单元
unit = input("请输入单元:")
print ("word list:"+unit)
# unit = int(unit)

#数据库连接
conn = mysql.connector.connect(user='root', password='123', database='test')
cursor = conn.cursor()

#数据库读取
cursor.execute("select * from word where unit = %s and wkey = %s",(unit,"2"))
# cursor.execute("select * from word where unit = 1;")
values = cursor.fetchall()
#print(values)
total = len(values)
print("本次测试单词量："+str(total))

print('...........................................')
random.shuffle(values)
# print(values)
i=1
for word in values:
    print(str(i)+'：'+word[1])
    input("回车查看答案")
    print(str(word[0])+'：'+word[2])
    while True:
        key = input("认识请输入“1”，不认识输入“2”,退出输入“3:”：")
        print(key)
        print(" ")
        if key=='1' or key=='2' :
            cursor.execute("UPDATE word SET wkey= %s  WHERE eng= %s", (key, word[1]))
            conn.commit()
            i=i+1
            break
            # break

#数据库结果读取
cursor.execute("select * from word where unit = %s and wkey = %s",(unit,"2"))
values_end = cursor.fetchall()
#print(values_end)
values_end.sort(key=operator.itemgetter(0))
errorlist = len(values_end)
i=1
print("不认识的单词：........................................")
for word in values_end:
    print(str(i)+'：'+str(word[0])+'：'+word[1]+'：'+word[2])
    i=i+1
print("准确率：")
print(1-errorlist/total)


#数据库关闭
cursor.close()
conn.close()
input("输入回车退出程序")
