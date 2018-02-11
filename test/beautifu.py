from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())

print(soup.title.string)

# 第一个a标签
print(soup.a)

print(soup.find(id="link2").string)
print(soup.find(id="link2").get_text())

# print(soup.findAll("a"))
print('------1------')
for link in soup.findAll('a'):
    print(link.string)

print('------2------')
print(soup.find(class_="story"))

print('-----3-------')
print(soup.find("p", {"class": "story"}).get_text())

print('-----4.正则表达式-------')
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

data = soup.findAll("a", href=re.compile(r"^http://example.com/"))
print(data)
