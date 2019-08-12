import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import re

if __name__ == '__main__':
    conn = sqlite3.connect('lottery.db')
    c = conn.cursor()
    cursor = c.execute("SELECT * FROM dlt")
    conn.commit()
    myr = ['1', '2', '3', '4', '5']
    myb = ['6', '7']

    cnt = 0
    for row in cursor:
        # if cnt>10:
        #     break
        # cnt += 1
        rb = []
        rb.append(row[1])
        rb.append(row[2])
        rb.append(row[3])
        rb.append(row[4])
        rb.append(row[5])
        bb = []
        bb.append(row[6])
        bb.append(row[7])
        cRed = 0
        cBlue = 0
        for r in myr:
            if r in rb:
                cRed+=1
        for b in myb:
            if b in bb:
                cBlue+=1
        if cRed>=3:
            print(row[0], cRed, cBlue)
                
    conn.close()

        

