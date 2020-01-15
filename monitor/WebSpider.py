import requests
from bs4 import BeautifulSoup




if __name__ == '__main__':

    r = requests.get('http://www.baidu.com')
    soup = BeautifulSoup(r.content)
    print(soup.title)