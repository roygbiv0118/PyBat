import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import re

import matplotlib.pyplot as plt

if __name__ == '__main__':

    val = [0]*33

    index = list(range(1, 33+1))


    conn = sqlite3.connect('lottery.db')
    c = conn.cursor()
    cursor = c.execute("SELECT DISTINCT * FROM ssq ORDER BY phase DESC")
    conn.commit()
    myr = [1, 18, 19, 27, 29, 33]
    myb = [13]

    # myr = [5, 7, 8, 9, 20, 22]
    # myb = [2]
    # myr = [1, 13, 17, 19, 27, 30]
    # myb = [12]
    # myr = [1, 9, 10, 12, 17, 25]
    # myb = [5]

    for row in cursor:
        rb = []
        rb.append(row[1])
        rb.append(row[2])
        rb.append(row[3])
        rb.append(row[4])
        rb.append(row[5])
        rb.append(row[6])
        val[row[1]-1] += 1
        val[row[2]-1] += 1
        val[row[3]-1] += 1
        val[row[4]-1] += 1
        val[row[5]-1] += 1
        val[row[6]-1] += 1

        ###
        bb = []
        bb.append(row[7])
        

        cRed = 0
        cBlue = 0
        for r in myr:
            if r in rb:
                cRed+=1
        for b in myb:
            if b in bb:
                cBlue+=1
        if cRed>=3 or cBlue == 1:
            print(row[0], cRed, cBlue)
                
    conn.close()

    plt.bar(index, val)
    plt.xticks(index, ['1','2','3','4','5'])
    plt.xlabel('index')
    plt.ylabel('val')
    plt.show()

