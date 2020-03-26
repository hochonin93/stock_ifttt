import requests
import random
import time
import threading
import MySQLdb

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        ii = 0
        while True:    
            url = a1 if random.randint(0,1) == 1 else a2
            ip1 = ips[random.randint(0,len(ips)-1)]
            proxie = {
                'http':'http://'+ip1
            }
            kk = proxie
            try:
                res = requests.get(url,headers=headers,proxies = kk,timeout=10)
            except:
                #print('IP問題:%s'%(ip1))
                del_ip(ip1)
            time.sleep(30)
            ii +=1
            print("Thread{},{}".format(self.num,ii))

def ip():
    
    cursor=conn.cursor()
    mySql_select_query = "SELECT * FROM `proxy_list` WHERE `type` = 'http'"
    cursor.execute(mySql_select_query)
    results = cursor.fetchall()
    for row in results:
        ips.append(row[2])

def del_ip(delip):
    cursor=conn.cursor()
    mySql_del_query = "DELETE FROM proxy_list WHERE ip = '%s'" % (delip)
    cursor.execute(mySql_del_query)
    conn.commit()
    print('已刪除ip:%s'%(delip))


conn = MySQLdb.connect(host="163.22.250.52",user="mqtt", passwd="mqtt",db="chonin", charset="utf8")
ips = []   
ip()

print("共有IP:{}".format(len(ips)))

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


a1 = 'http://www.nkut.edu.tw/front/News/news.php?ID=bmt1dF9tYWluJk5ld3M=&Sn=1202'
a2 = 'http://www.nkut.edu.tw/front/News/news.php?ID=bmt1dF9tYWluJk5ld3M=&Sn=1203'


threads = []     
num = int(input(''))
for i in range(num):
    threads.append(MyThread(i))
    time.sleep(5)
    threads[i].start()
    threads[i].join()
  
