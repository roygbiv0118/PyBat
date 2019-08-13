import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import re

if __name__ == '__main__':
    conn = sqlite3.connect('lottery.db')
    c = conn.cursor()
    cursor = c.execute("SELECT * FROM ssq")
    conn.commit()
    # myr = [1, 18, 19, 27, 29, 33]
    # myb = [13]

    # myr = [5, 7, 8, 9, 20, 22]
    # myb = [2]
    # myr = [1, 13, 17, 19, 27, 30]
    # myb = [12]
    # myr = [1, 9, 10, 12, 17, 25]
    # myb = [5]
    myr = [4, 8, 9, 18, 25, 33]
    myb = [10]
    all_balls = []
    for row in cursor:
        all_balls.append(row)
        rb = []
        rb.append(row[1])
        rb.append(row[2])
        rb.append(row[3])
        rb.append(row[4])
        rb.append(row[5])
        rb.append(row[6])
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
        if cRed>=4:
            print(row[0], cRed, cBlue)
                
    conn.close()

    # print(len(all_balls))
    # for rw in all_balls:
    #     mrb = []
    #     mrb.append(rw[1])
    #     mrb.append(rw[2])
    #     mrb.append(rw[3])
    #     mrb.append(rw[4])
    #     mrb.append(rw[5])
    #     mrb.append(rw[6])
    #     mbb = []
    #     mbb.append(rw[7])
    #     for row in all_balls:
    #         rb = []
    #         rb.append(row[1])
    #         rb.append(row[2])
    #         rb.append(row[3])
    #         rb.append(row[4])
    #         rb.append(row[5])
    #         rb.append(row[6])
    #         bb = [] 
    #         bb.append(row[7])
    #         cRed = 0
    #         cBlue = 0
    #         for r in mrb:
    #             if r in rb:
    #                 cRed+=1
    #         for b in mbb:
    #             if b in bb:
    #                 cBlue+=1
    #         if cRed>=5 and rw[0] != row[0]:
    #             print(rw[0], row[0], cRed, cBlue)

        

