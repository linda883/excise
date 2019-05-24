import requests


urls = ('http://www.baidu.com', 'https://www.taobao.com', 'https://mail.163.com')


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


print(list(gen_from_urls(urls)))