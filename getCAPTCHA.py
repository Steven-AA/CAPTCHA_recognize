#coding:utf-8
import wget
import sys
import os
import time

def get_captcha(num,url,path):
    for i in range(num):
        try:
            wget.download(url, path + str(i) + str(time.time()*1000000) + '.jpg')
            print('Successfully get CAPTCHA ' + str(i))
        except:
            print('Failed to get CAPTCHA')

if __name__ == '__main__':
    url = 'http://jwxt.njupt.edu.cn/CheckCode.aspx'
    path = './CAPTCHA/'
    try:
        num = int(sys.argv[1])
    except:
        num = 3000
    try:
        os.mkdir('./CAPTCHA/')
    except:
        pass
    get_captcha(num,url,path)