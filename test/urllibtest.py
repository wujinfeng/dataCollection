from urllib import request

# 方法1
# resp = request.urlopen("http://www.baidu.com")
#
# print(resp.read().decode("utf-8"))


# 方法2
# req = request.Request("http://www.baidu.com")
#
# req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
#
# resp = request.urlopen(req)
#
# print(resp.read().decode("utf-8"))

