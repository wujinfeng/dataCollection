from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

# 请求URL,并把结果用utf8编码
resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode("utf-8")

# 使用BeautifulSoup解析
soup = BeautifulSoup(resp, "html.parser")

# 获取所有以 /wiki/开头的a标签的href属性
listUrls = soup.findAll('a', href=re.compile("^/wiki/"))

# 输出所有的词条对应的名称和url
for url in listUrls:
    # 过滤.jpg或JPG结尾的url
    if not re.search("\.(jpg|JPG)$", url["href"]):
        print(url.get_text(), "<----->", "https://en.wikipedia.org" + url["href"])
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
                sql = "insert into `urls`(`urlname`, `urlhref`) values (%s, %s)"

                # 执行sql
                cursor.execute(sql, (url.get_text(), "https://en.wikipedia.org" + url["href"]))

                # 提交
                connection.commit()
        finally:
            connection.close()
