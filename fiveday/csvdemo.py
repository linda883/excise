# -*- coding:utf-8 -*-

import csv23


def read_csvfile():
    with open('username.csv', newline='') as csvfile:
        spamreader = csv23.reader(csvfile, delimiter=' ', quotechar=',')
        for row in spamreader:
            print(', '.join(row))


def write_csvfile():
    with open('username.csv', 'w', newline='') as csvfile:
        spamwriter = csv23.writer(csvfile, delimiter=' ',
                                  quotechar=',', quoting=csv23.QUOTE_MINIMAL)
        spamwriter.writerow(['linda'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['linda', 'Lovely Spam', 'Wonderful Spam'])


def read_csv_p3():
    with open('username.csv', newline='', encoding='UTF-8') as csvfile:
        reader = csv23.DictReader(csvfile)
        for row in reader:
            print(row['username'], row['email'])
            print(row['username'])


# 取一 行数据
def read_csv_1_with_name():
    with open('username.csv', newline='', encoding='UTF-8') as csvfile:
        reader = csv23.DictReader(csvfile)
        for row in reader:
            if row['username'] == 'linda':
                print(row['username'], row['email'])




