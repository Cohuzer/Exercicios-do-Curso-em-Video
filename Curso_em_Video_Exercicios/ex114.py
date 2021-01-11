import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mSITE INDISPONIVEL\033[m')
else:
    print(f'\033[32mSITE DISPONIVEL\033[m')
    