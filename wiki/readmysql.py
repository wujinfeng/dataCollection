import pymysql.cursors

# 获取数据库连接
connection = pymysql.connect(
    host="localhost",
    user="root",
    db="wikiurl",
    password="1234",
    charset="utf8mb4"
)
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 创建sql
        sql = "select * from `urls` where `id` is not null"
        count = cursor.execute(sql)
        print(count)

        # 查询数据
        # result = cursor.fetchall();
        result = cursor.fetchmany(size=3)
        print(result)

finally:
    connection.close()
