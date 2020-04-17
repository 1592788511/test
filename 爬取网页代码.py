import urllib.request

url_list = []

with open('urls.txt','r') as f:
    for eachline in f:
        text = eachline.replace('\n','')
        url_list.append(text)
print(url_list)

html_name = ['url_1.txt','url_2.txt','url_3.txt','url_4.txt','url_5.txt']

i = 0
for each in url_list:
    url = each;
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    print(html)
    with open(html_name[i],'wb') as f:
        f.write(html)
    i += 1
    
print('执行完毕！')
