# isXSS
`isXSS` is a XSS vulnerability scanner that scans for reflected characters that could potentially lead to reflected XSS. These are the following characters that are checked for reflection: `' " < >`

## TODO
- Add check for SQL Injection (If `'` character is returning 500 error, then this should be logged to console)
- Clean up output (reflected in http://testphp.vulnweb.com//listproducts.php?cat=123%22 --> reflected in http://testphp.vulnweb.com//listproducts.php?cat=XSS">) change output to include only `=XSS + {vulnerable characters}`
- Clean output to say which parameter the characters are being reflected in when for than one parameter is in the request.

## Usage 1 - stdin
```
cat allUrls.txt | python3 isxss.py
```

## Usage 2 - File
```
python3 isxss.py -l allUrls.txt
```

## Other Arguments
- `-t {NUM}` - Specify the number of threads
- `-v` - Used for debugging

## Example
```
(base) shelled@DESKTOP:~/tools$ echo http://testphp.vulnweb.com/ | gau | python3 isxss.py -t 100

     ▄█     ▄████████ ▀████    ▐████▀    ▄████████    ▄████████
    ███    ███    ███   ███▌   ████▀    ███    ███   ███    ███
    ███▌   ███    █▀     ███  ▐███      ███    █▀    ███    █▀
    ███▌   ███           ▀███▄███▀      ███          ███
    ███▌ ▀███████████    ████▀██▄     ▀███████████ ▀███████████
    ███           ███   ▐███  ▀███             ███          ███
    ███     ▄█    ███  ▄███     ███▄     ▄█    ███    ▄█    ███
    █▀    ▄████████▀  ████       ███▄  ▄████████▀   ▄████████▀
    Version 0.1                             by  @Shelledlizard4

['"><] reflected in http://testphp.vulnweb.com:80//hpp/index.php?pp=12
["><] reflected in http://testphp.vulnweb.com:80//listproducts.php?cat=-1+union+select+1,2,3,4,5,6,7,8,9,10,database()+--
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=123%22
["><] reflected in http://testphp.vulnweb.com:80//listproducts.php?cat=2+order+by+5--+
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=999999.9
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=%3CscRipT%3Econfirm%281%29%3C%2Fscript%3E
["><] reflected in http://testphp.vulnweb.com:80//listproducts.php?cat=2+order+by+3--+
["><] reflected in http://testphp.vulnweb.com:80//listproducts.php?cat=2+order+by+6--+
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=z
['"><] reflected in http://testphp.vulnweb.com:80//hpp/?pp=12
['"><] reflected in http://testphp.vulnweb.com//hpp/?pp=aaa%22bbb
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=2%3E%3Cscript%3Ealert(%22Anmol%22)%3C/script%3E
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=FUZZ%22
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=-1+union+select+1,2,3,4,5,6,7,8,9,10,group_concat(CHARACTER_SET_NAME,0x3a
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=4
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=FUZZ
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=1%20AND%201=1%20UNION%20ALL%20SELECT%201,2,3,4%20from%20information_schema.tables--%20-
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=123%22%3E%3Cscript%3Ealert
["><] reflected in http://testphp.vulnweb.com:80//listproducts.php?cat=1%E2%80%9D
["><] reflected in http://testphp.vulnweb.com:80//listproducts.php?cat=1*
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=1%20AND%201=1%20UNION%20ALL%20SELECT%201,2,3,4,5,6,7,8,9,10,11%20from%20information_schema.tables--%20-
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=1+order+by+1
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=1+order+by+2
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=3
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=1%20AND%201=1%20UNION%20ALL%20SELECT%201,table_name,3,4,5,6,7,8,9,10,11%20from%20information_schema.tables--%20-
["><] reflected in http://testphp.vulnweb.com//listproducts.php?cat=1+order+by+12
```
