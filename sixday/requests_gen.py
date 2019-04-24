
import requests

urls = ('http://www.baidu.com', 'https://www.taobao.com', 'https://mail.163.com')

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
