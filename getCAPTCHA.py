import wget

for i in range(3000):
    url = 'http://jwxt.njupt.edu.cn/CheckCode.aspx'
    wget.download(url, 'D://CAPTCHA/CAPTCHA_' + str(i) + '.jpg')
    print('Successfully get CAPTCHA ' + str(i))
