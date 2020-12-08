import requests
import json

target_url = 'http://httpbin.org/get'
def get_proxy():
    return requests.get("http://192.168.50.149:8000/get/").json()


def delete_proxy(proxy):
    requests.get("http://192.168.50.149:8000/delete/?proxy={}".format(proxy))


def getHtml():

    retry_count = 100
    while retry_count > 0:
        proxy = get_proxy().get("proxy")
        print(proxy)
        print(retry_count)
        try:
            html = requests.get(target_url, proxies={"http": "http://{}".format(proxy)})
            print(html)
            # 使用代理访问
            return proxy
        except Exception:
            retry_count -= 1
        # 删除代理池中代理
    delete_proxy(proxy)
    return None


def crawl(url, proxy):
    """
    use proxy to crawl page
    :param url: page url
    :param proxy: proxy, such as 8.8.8.8:8888
    :return: html
    """
    print(proxy,'11111')
    proxies = {'http': 'http://' + str(proxy)}
    print(proxies)
    return requests.get(url, proxies=proxies).text


def main():
    """
    main method, entry point
    :return: none
    """
    proxy = getHtml()

    print('get random proxy', proxy)
    html = crawl(target_url, proxy)
    print(html)

if __name__ == '__main__':
    main()
