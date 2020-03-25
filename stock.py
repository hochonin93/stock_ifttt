from bs4 import BeautifulSoup
import requests
import re
import random
import time
import json

def lineNotifyMessage(token, msg):
    headers = {
      "Authorization": "Bearer " + token, 
      "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def changed_val():   
    tag = soup.find("div", class_="txt_l font19 orange font-b") #搜找指定的tag和class 股名
    value = tag.string
    return value

def now_val():
    tag = soup.find("div", class_="txt_r font16imp") #搜找指定的tag和class
    value = tag.string
    c = re.findall(r"\d+\.?\d*",value)
    return c[0]

def conn():
    global soup , kk
    ip =[#'220.242.160.147:80',
        #'47.52.36.33:80',
        #'178.128.99.255:44344',
        '218.145.215.150:3128',
        '165.22.36.75:8888',
        '51.79.52.62:3128',
        #'156.54.219.29:8080',
        '51.158.186.242:8811']
    proxie = {
        'http':'http://'+ip[random.randint(0,len(ip)-1)]
    }
    kk = proxie
    try:
        if random.randint(0,2) == 1:
            res = requests.get(url1,headers=headers)
            kk = '原本ip'
        else:
            res = requests.get(url1,headers=headers,proxies = kk,timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
    except: print('IP問題:%s'%(kk['http']))
    return soup
    
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
num = input('請輸入股票號碼:')
soup = None
url1 = 'http://www.aastocks.com/tc/stocks/quote/quick-quote.aspx?symbol={}'.format(num)
token = 'TerXohktVMreHoOwCqLEHicuzVCiFZl5YoHxTnJeuxz'

a1 = 0
a2 = 0
a3 = 0
i = 0

while True:
    try:
        conn()    
        a1 = now_val()
        if a1 != a2 :
            name = changed_val()
            message = name +'\n'+a1
            data = {
                'value1': name,
                'value2': a1,
                'value3': round(float(a1)-float(a2),3)
            }
            url2 = 'https://maker.ifttt.com/trigger/stock/with/key/xRcl9phEHTwRBgoxP50LY'
            #if a2 != 0 or a1 != 0 : lineNotifyMessage(token, message)
            if a2 != 0 or a1 != 0 : 
                headers1 = {'Content-Type': 'application/json'}
                requests.post(url2,headers=headers1,data=json.dumps(data))
            a2 = a1 
        
    except:pass
    i += 1  
    
    print(i,name,a1)
    #print('次:{},名:{},價:{}'.format( i,name,a1 ))
    time.sleep(10)
