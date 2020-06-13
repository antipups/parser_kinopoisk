import re
import requests


def parse_proxy():
    # html = requests.get('https://www.ip-adress.com/proxy-list').text
    # urls = list()
    # for i in re.finditer(r'(\d{1,3}.){4}</a>:\d{1,4}</td>\n<td>transparent</td>', html):
    #     withouttrans = i.group()[:-26]
    #     urls.append(withouttrans[:withouttrans.find('<')] + withouttrans[withouttrans.rfind('>') + 1:])
    urls = []
    html = requests.get('https://free-proxy-list.net/').text
    for proxy in re.finditer(r'\d{1,3}\.((?!ago).)*', re.search(r'<tbody>.*</tbody>', html).group()):
        proxy = proxy.group()
        if re.search(r'hx.{4}', proxy).group().endswith('ye'):
            urls.append((lambda x: x[:x.find('<')] + ':' + x[x.rfind('>') + 1:]) (re.search(r'(\d{1,3}.){4}/td><td>\d{1,6}', proxy).group()))
    return tuple(urls)
