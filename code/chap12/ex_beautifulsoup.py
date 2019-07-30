import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors -> https에 접속하기 위한 해킹적인 관점
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # url 입력
html = urllib.request.urlopen(url, context=ctx).read() # line단위로 읽기
soup = BeautifulSoup(html, 'html.parser') # take html structure

# Retrieve all of the anchor tags
tags = soup('a') # take anchor tag
for tag in tags:
    print(tag.get('href', None))
