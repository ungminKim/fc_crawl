from urllib import request
from urllib.parse import urlparse

url = "https://www.skyscanner.co.kr"

mem = request.urlopen(url)

print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('read : {}'.format(mem.read(100).decode('utf-8')))
print('parse : {}'.format(urlparse('http://www.skyscanner.co.kr?test=test')))

API = "https://api.ipify.org"

values = {
    'format' : 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(valuse)
print('after param : {}'.format(params))

