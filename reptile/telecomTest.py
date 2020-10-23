import json
import urllib.request
import http.cookiejar

import requests


def saveCookie():
    """
    保存登录的cookie
    """
    """
    MozillaCookieJar ： cookiejar的子类
    从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。
    """
    cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
    # 构建一个cookie的处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 获取一个opener对象
    opener = urllib.request.build_opener(handler)
    # # 获取一个请求对象
    # params = {'username': '13616880703', 'password': '1', 'Button1': '%A1%A1%A1%A1'}
    # response = requests.post("http://134.101.168.29:8080/telecom/theme/fix/LoginForm.jsp", data=params)
    # for key, value in response.cookies.items():
    #     print('key = ', key + ' ||| value :' + value)
    #
    # request = urllib.request.Request('http://134.101.168.29:8080/telecom/theme/fix/LoginForm.jsp',
    #                                  headers={"Connection": "keep-alive"})

    conn = requests.session()
    url = 'http://snake19840.imwork.net:18080/dxtest/'
    postdata = {
    'username':'***',
    'password':'***'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    rep = conn.post(url, data=postdata,headers=headers)
    with open('1.html', 'wb') as f:
        f.write(rep.content)

    # 请求服务器，获取响应对象。cookie会在response里一起响应
    # response = opener.open(req)
    # 保存cookie到文件
    # cookie.save(ignore_discard=True, ignore_expires=True)


def getHtml():
    """
    请求携带文件中的cookie
    """
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request('http://flights.ctrip.com/')
    html = opener.open(request).read().decode('gbk')

    print(html)


if __name__ == '__main__':
    saveCookie()
