import random
import time
import requests
import json
import pandas as pd

def gethtml(url):
       r = requests.get(url)
       r.raise_for_status()
       r.encoding = r.apparent_encoding
       time.sleep(random.randint(0,10))
       return r.text


url0 = r'http://dxx.ahyouth.org.cn/api/peopleRankList?level1=直属高校'
html0_json = gethtml(url0)
html0 = json.loads(html0_json)

num=html0['list'][0]['table_name'][12:] #stage


url = r'http://dxx.ahyouth.org.cn/api/peopleRankStage?table_name=reason_stage'+num+'&level1=直属高校&level2=合肥工业大学&level3=宣城校区计算机与信息系'
html_json = gethtml(url)
html = json.loads(html_json)
datas=html['list']['list']
datas_json=json.dumps(datas)

file_name = "1.xlsx"
df=pd.read_json(datas_json)
df.columns=['支部名称','人数']
df.to_excel(file_name,index=False)

print('OK!')
