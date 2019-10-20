import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import re

import matplotlib.pyplot as plt

if __name__ == '__main__':

    n_r = 33
    n_b = 16
    val_r = [0]*n_r
    val_b = [0]*n_b

    conn = sqlite3.connect('lottery.db')
    c = conn.cursor()
    cursor = c.execute("SELECT DISTINCT * FROM ssq ORDER BY phase DESC")
    conn.commit()
    myr = [1, 4, 18, 19, 26, 29]
    myb = [13]



    print(myr, myb, '19122')
    for row in cursor:
        rb = []
        rb.append(row[1])
        rb.append(row[2])
        rb.append(row[3])
        rb.append(row[4])
        rb.append(row[5])
        rb.append(row[6])
        val_r[row[1]-1] += 1
        val_r[row[2]-1] += 1
        val_r[row[3]-1] += 1
        val_r[row[4]-1] += 1
        val_r[row[5]-1] += 1
        val_r[row[6]-1] += 1

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
        if cRed>=4 or cBlue == 1:
            print(row[0], cRed, cBlue)
                
    conn.close()
    plt.subplot(2,1,1)
    plt.bar(range(1, n_r+1), val_r)
    plt.xticks(range(1, n_r+1), range(1,n_r+1))
    plt.subplot(2,1,2)
    plt.bar(range(1,n_b+1), val_b)
    plt.xticks(range(1,n_b+1), range(1,n_b+1))
    plt.show()

