import requests
import argparse
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
                print('[%s]' % ''.join(map(str,reflected)) + " reflected in " + url.scheme + '://' + url.netloc + '/' + url.path + '?' + url.query)


def banner():
    print(Colors.RED + """
     ▄█     ▄████████ ▀████    ▐████▀    ▄████████    ▄████████
    ███    ███    ███   ███▌   ████▀    ███    ███   ███    ███
    ███▌   ███    █▀     ███  ▐███      ███    █▀    ███    █▀
    ███▌   ███           ▀███▄███▀      ███          ███
    ███▌ ▀███████████    ████▀██▄     ▀███████████ ▀███████████
    ███           ███   ▐███  ▀███             ███          ███
    ███     ▄█    ███  ▄███     ███▄     ▄█    ███    ▄█    ███
    █▀    ▄████████▀  ████       ███▄  ▄████████▀   ▄████████▀
    Version 0.1                             by  @Shelledlizard4
    """ + Colors.reset)

def main():
    banner()
    parser = argparse.ArgumentParser(description="Check for reflected XSS characters",
    usage="cat allUrls.txt | python3 isxss.py [options]")

    parser.add_argument('-t', metavar='-threads', help="Specify the number of threads (default=50)")
    parser.add_argument('-l', metavar='-list', help="Specify a file containing all the urls to be scanned")
    parser.add_argument('-v', help="Debug mode", action='store_true')
    global debug

    args = parser.parse_args()


    if(args.v == True):
        debug = True

    num_threads = 50
    if(args.t != None):
        num_threads = args.t
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    if(sys.stdin == None):
        with concurrent.futures.ThreadPoolExecutor(max_workers=int(num_threads)) as executor:
            executor.map(requestor, args.l)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=int(num_threads)) as executor:
            executor.map(requestor, sys.stdin)


main()
