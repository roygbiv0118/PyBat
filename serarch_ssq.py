import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import re

import matplotlib.pyplot as plt

if __name__ == '__main__':

    val = [0]*33
    val_b = [0]*16

    index = list(range(1, 33+1))


    conn = sqlite3.connect('lottery.db')
    c = conn.cursor()
    cursor = c.execute("SELECT DISTINCT * FROM ssq ORDER BY phase DESC")
    conn.commit()
    myr = [1, 4, 18, 19, 26, 29]
    myb = [13]



    print(myr, myb)
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
        val_b[row[7]-1] += 1

        cRed = 0
        cBlue = 0
        for r in myr:
            if r in rb:
                cRed+=1
        for b in myb:
            if b in bb:
                cBlue+=1
        if cRed>3 or (cRed==3 and cBlue == 1):
            print(row[0], cRed, cBlue)
                
    conn.close()
    plt.subplot(2,1,1)
    plt.bar(index, val)
    plt.xticks(index, range(1,33+1))
    plt.xlabel('index')
    plt.ylabel('val')
    plt.subplot(2,1,2)
    plt.bar(range(1,16+1), val_b)
    plt.xticks(range(1,16+1), range(1,16+1))
    plt.show()

