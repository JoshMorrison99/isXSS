import requests
import concurrent.futures
import sys
from urllib.parse import urlparse, parse_qs, urlencode
import urllib3
import re

class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    LIGHT_WHITE = "\033[1;37m"
    LIGHT_GRAY = "\033[0;37m"
    reset = '\033[0m'
    darkgrey = '\033[90m'

def requestor(line):
    urlString = line.strip('\n')
    url = urlparse(urlString)
    if(url.query):
        params = parse_qs(url.query)
        if(params == '{}'):
            print(url.scheme + '://' + url.netloc + '/' + url.path + '?' + url.query)
        else:
            for i in params:
                params[i] = 'xx1\'xx2\"xx3>xx4<'
            query = urlencode(params)
            try:
                reflected = []
                response = requests.get(url.scheme + '://' + url.netloc + '/' + url.path + '?' + query, verify=False, timeout=10)
                page = response.text
                if(re.search('xx1\'', page)):
                    reflected.append('\'')
                if(re.search('xx2\"', page)):
                    reflected.append('\"')
                if(re.search('xx3>', page)):
                    reflected.append('>')
                if(re.search('xx4<', page)):
                    reflected.append('<')
                if(reflected):
                    print('[%s]' % ''.join(map(str,reflected)) + " " + url.scheme + '://' + url.netloc + '/' + url.path + '?' + query)
            except:
                pass

def main():
    print(Colors.darkgrey + """
    _     _  ____________
   (_)___| |/ / ___/ ___/
  / / ___/   /\__ \\\\__ \\
 / (__  )   |___/ /__/ /
/_/____/_/|_/____/____/
Author: Shelled
Verison: v0.1
    """ + Colors.reset)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(requestor, sys.stdin)


main()
