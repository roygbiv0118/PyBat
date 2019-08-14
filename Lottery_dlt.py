import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import re
import time

if __name__ == '__main__':
    url = 'http://kaijiang.500.com/shtml/dlt/{}.shtml'
    data = None
    header = {
        'User-Agent':
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }

    time_start=time.time()
    
    conn = sqlite3.connect('lottery.db')
    c = conn.cursor()
    # c.execute("DELETE FROM dlt") 
    response = requests.post(url.format('19090'), data, header)
    response.encoding = 'utf-8'
    bs = BeautifulSoup(response.text, 'lxml')
    span = bs.find('span', class_='iSelectBox')
    cnt = 0
    try:
        for ii in span.find_all('a'):
            if ii.text<='19094':
                continue
            
            print(ii.text)
            time.sleep(0.1)
            response = requests.post(url.format(ii.text), data, header)
            response.encoding = 'utf-8'
            bs = BeautifulSoup(response.text, 'lxml')
            table = bs.find('table', class_='kj_tablelist02')
            b_red = []
            b_blue = [] 
            for i, th in enumerate(table.find_all('li', class_='ball_red')):
                b_red.append(int(th.text))
            for i, th in enumerate(table.find_all('li', class_='ball_blue')):
                b_blue.append(int(th.text))
            c.execute("INSERT INTO dlt(phase,r1,r2,r3,r4,r5,b1,b2) \
            VALUES ('{}', {}, {}, {}, {}, {}, {}, {})".format(ii.text, b_red[0], b_red[1], b_red[2], b_red[3], b_red[4],b_blue[0],b_blue[1]));
    finally:
        conn.commit()
        conn.close()

        time_end=time.time()
        print('totally cost',time_end-time_start)