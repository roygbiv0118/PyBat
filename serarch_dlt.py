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
    # myr = [1, 18, 19, 27, 29]
    # myb = [2, 4, 8]
    myr = [22, 24, 29, 31, 35]
    myb = [4, 11]

    # myr = [2, 15, 17, 25, 31]
    # myb = [3, 6]
    # myr = [1, 7, 19, 29, 32]
    # myb = [3, 8]
    # myr = [5, 10, 14, 17, 31]
    # myb = [4, 5]
    all_balls = []

    for row in cursor:
        all_balls.append(row)
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
        if cRed>3 or (cRed == 3 and cBlue == 2):
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
    #     mbb = []
    #     mbb.append(rw[6])
    #     mbb.append(rw[7])
    #     for row in all_balls:
    #         rb = []
    #         rb.append(row[1])
    #         rb.append(row[2])
    #         rb.append(row[3])
    #         rb.append(row[4])
    #         rb.append(row[5])
    #         bb = []
    #         bb.append(row[6])
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
        

