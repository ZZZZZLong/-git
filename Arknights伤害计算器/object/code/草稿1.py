import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='arknights_collections',
    port=3306,
    charset='utf8'
)
cursor = db.cursor()
# 执行 SQL 查询
cursor.execute("SELECT * FROM 萨米肉鸽藏品")

# 获取查询结果
results = cursor.fetchall()

# 遍历结果
# for row in results:
#     print(row)
print(list(results))


# 关闭连接
db.close()