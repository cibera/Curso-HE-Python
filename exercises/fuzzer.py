import requests #install
import io
from fake_useragent import UserAgent #install
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

ua = UserAgent()
user_agent = ua.random
host = ''
filepath = ''
with open(filepath) as fp:
    line = fp.readline()
    while line:
        combined = host + line.strip()
        r = requests.get(combined, headers={'User-Agent': user_agent})
        if r.status_code == 200:
            print(line.strip(), '\n', r)
            line = fp.readline()