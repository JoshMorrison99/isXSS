import requests
import sys
from urllib.parse import urlparse, parse_qs, urlencode
import re

for line in sys.stdin:
    urlString = line.strip('\n')
    url = urlparse(urlString)
    if(url.query):
        params = parse_qs(url.query)
        if(params == '{}'):
            print(url.scheme + '://' + url.netloc + '/' + url.path + '?' + url.query)
        else:
            for i in params:
                params[i] = '\'xx1\"xx2>xx3<xx4'
            query = urlencode(params)
            try:
                response = requests.get(url.scheme + '://' + url.netloc + '/' + url.path + '?' + query, verify=False, timeout=10)
                page = response.text
                print('[+] Checking webpage: ' + (url.scheme + '://' + url.netloc + '/' + url.path + '?' + query))
                if(re.search('\'xx1', page)):
                    print('[!] \' is being reflected in webpage: ' + (url.scheme + '://' + url.netloc + '/' + url.path + '?' + query))
                if(re.search('\"xx2', page)):
                    print('[!] \" is being reflected in webpage: ' + (url.scheme + '://' + url.netloc + '/' + url.path + '?' + query))
                if(re.search('>xx3', page)):
                    print('[!] > is being reflected in webpage: ' + (url.scheme + '://' + url.netloc + '/' + url.path + '?' + query))
                if(re.search('<xx4', page)):
                    print('[!] < is being reflected in webpage: ' + (url.scheme + '://' + url.netloc + '/' + url.path + '?' + query))
            except:
                pass
