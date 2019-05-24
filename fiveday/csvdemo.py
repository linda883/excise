# -*- coding:utf-8 -*-

import csv


def read_csv_1():
    with open('username.csv') as csvDataFile:
        csv_Reader = csv.reader(csvDataFile)
        for row in csv_Reader:
            print(row)


def read_csv_2():
    username = []
    email = []

    with open('username.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            username.append(row[0])
            email.append(row[1])

    print(username[1:])
    print(email[1:])


def read_csvfile():
    with open('username.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
        for row in spamreader:
            print(row)
            # print(' '.join(row))


def write_csvfile():
    with open('username1.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                  quotechar=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['linda'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['linda', 'Lovely Spam', 'Wonderful Spam'])


read_csv_2()