import requests
import random
import time
import threading
ip =[ 
    '80.87.184.49:41258',
    '85.238.98.160:34167',
    '101.255.103.201:53281',
    '118.200.73.124:8080',
    '168.228.150.5:39280',
    '119.81.199.81:8123',
    '1.10.188.203:45476',
    '134.122.112.27:8080',
    '119.81.199.86:8123',
    '179.127.242.97:34920',
    '173.192.128.238:25',
    '182.71.102.215:3128',
    '118.172.201.89:31813',
    '161.202.226.195:80',
    '5.189.133.231:80',
    '185.128.37.14:8080',
    '119.81.199.82:8123',
    '119.81.199.83:31288',
    '78.38.115.210:60490',
    '45.63.43.103:80',
    '194.5.192.154:80',
    '144.217.118.206:8080',
    '5.2.164.205:59914',
    '80.211.115.69:3128',
    '142.93.197.146:80',
    '185.79.242.253:50828',
    '213.6.226.202:58154',
    '125.25.165.97:39021',
    '27.116.51.115:8080',
    '117.58.241.164:52636',
    '95.79.99.148:3128',
    '103.108.157.98:8080',
    '103.102.28.134:38166',
    '85.10.219.98:1080',
    '88.101.209.96:61664',
    '123.49.49.166:23500',
    '134.35.231.176:8080',
    '151.253.165.70:8080',
    '45.236.130.214:8080',
    '115.127.109.2:45067',
    '144.91.116.171:443',
    '128.199.143.66:3128',
    '80.187.140.26:8080',
    '186.250.117.234:36241',
    '104.41.38.129:80',
    '102.165.69.201:8080',
    '5.255.26.222:8080',
    '144.217.163.138:8080',
    '182.52.90.117:45535',
    '144.76.214.154:1080',
    '189.9.55.7:8080',
    '45.77.233.125:3128',
    '177.134.231.93:8080',
    '148.101.44.100:999',
    '103.234.252.3:3888',
    '198.58.10.173:8080',
    '110.138.232.72:8080',
    '68.183.180.28:1080',
    '180.252.194.184:8080',
    '18.229.248.53:8888',
    '45.163.134.68:8080',
    '148.101.23.95:8080',
    '183.89.110.101:8080',
    '36.81.28.236:8080',
    '125.166.130.87:8080',
    '176.120.208.161:8081',
    '180.245.58.28:8080',
    '178.128.106.70:1080',
    '122.100.92.168:80',
    '119.237.73.133:3128',
    '203.245.28.120:8080',
    '168.131.152.152:3128',
    '218.145.215.150:3128',
    '165.22.36.75:8888',
    ]
print(len(ip))
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'mLang=TC; __auc=e7bcbd7417031ed220b2120a949; NewChart=Mini_Color=1; AAWS2=; DetailChartDisplay=3; AADetailChart=P%7c1y_day%2cT%7c5%2cV%7ctrue%2cB%7c3%2cD%7c1%2cDP%7c10%7e20%7e50%7e100%7e150%2cL1%7c2%7e14%2cL2%7c3%7e12%7e26%7e9%2cL3%7c12%2cCO%7c3%2cCT%7c1%2cCS%7cHSI%2cSP%7chide%2cAHFT%7ctrue; AAWS=; DynamicChart2=CPT=0&CPTS=&CPTM=&P=52&VB=1&CVB=1&CT=candles&T=dark&EP=1&EE=1&EAHFT=1&ES=0&DC=red&SPUP=0&ISQ=0&MI=SMA|10|20|50|100|150&TI1=Volume&TI2=RSI|14&TI3=MACD|12|26|9&TI4=&TI5=&H=300|null|null|null|null|null&ME=1|1|1|1|1&ConfigName=&ConfigID=1; __asc=bdb78e98171026b6ffe756c4909; CookiePolicyCheck=0; MasterSymbol=00228; LatestRTQuotedStocks=00788%3B03323%3B02282%3B00228; __utmc=177965731; __utmc=81143559; AALTP=1; aa_cookie=219.78.57.106_50181_1584884468; __utma=177965731.530051348.1581385589.1584883528.1584888005.25; __utmz=177965731.1584888005.25.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=81143559.657242277.1581385604.1584883551.1584888005.23; __utmz=81143559.1584888005.23.23.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); AALTP=1; __utmb=177965731.3.10.1584888005; __utmt_b=1; __utmb=81143559.3.10.1584888005',
        'DNT': '1',
        'Host': 'www.aastocks.com',
        'Referer': 'http://www.aastocks.com/tc/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    
} 
proxie = {
    'http':'http://'+ip[random.randint(0,len(ip)-1)]
}


a1 = 'http://www.nkut.edu.tw/front/News/news.php?ID=bmt1dF9tYWluJk5ld3M=&Sn=1202'
a2 = 'http://www.nkut.edu.tw/front/News/news.php?ID=bmt1dF9tYWluJk5ld3M=&Sn=1203'

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        ii = 0
        while True:    
            url = a1 if random.randint(0,1) == 1 else a2
            proxie = {
                'http':'http://'+ip[random.randint(0,len(ip)-1)]
            }
            kk = proxie
            try:
                res = requests.get(url,headers=headers,proxies = kk,timeout=10)
                #res = requests.get(a2,headers=headers,proxies = kk,timeout=10)
            except:print('IP問題:%s'%(kk['http']))
            time.sleep(30)
            ii +=1
            print("Thread{},{}".format(self.num,ii))
threads = []     
num = int(input(''))
for i in range(num):
  threads.append(MyThread(i))
  time.sleep(3)
  threads[i].start()