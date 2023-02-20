import requests
import argparse
import concurrent.futures
import sys
import urllib3
from urllib.parse import urlparse, parse_qs, urlencode
import re

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
                old = params[i]
                params[i] = 'XSS'
                query = urlencode(params)
                reflected = []
                header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                response = requests.get(url.scheme + '://' + url.netloc + '/' + url.path + '?' + query, verify=False, timeout=20, headers=header)
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
                    print('[%s]' % ''.join(map(str,reflected)) + " reflected in " + url.scheme + '://' + url.netloc + '/' + url.path + '?' + query)
                
                params[i] = old



def main():
    parser = argparse.ArgumentParser(description="Check for reflected XSS characters",
    usage="cat urls.txt | python3 isxss.py")

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with concurrent.futures.ThreadPoolExecutor(max_workers=int(25)) as executor:
        executor.map(requestor, sys.stdin)


main()
