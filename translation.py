import urllib.request
import urllib.parse
import json
import time

while True:

    content = input("请输入需要翻译的内容:(输入'q'退出程序)")
    if content == 'q':
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {}
    data['i']= content
    data['from']= 'AUTO'
    data['to']= 'AUTO'
    data['smartresult']= 'dict'
    data['client']= 'fanyideskweb'
    data['salt']= '15868495054215'
    data['sign']= '84a37daf45c409c09312a03f5b000bc7'
    data['ts']= '1586849505421'
    data['bv']= '887ddef35bb193fe341b77b7709d1160'
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print('翻译结果为：%s' % target['translateResult'][0][0]['tgt'])
    time.sleep(5)
