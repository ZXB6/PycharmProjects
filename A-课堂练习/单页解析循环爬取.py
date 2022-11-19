import pandas as pd
import requests
import json,time,numpy,random
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
def parse_base_info(url,headers):
      html = requests.get(url,headers = headers)
      bs = json.loads(html.text)
      df = pd.DataFrame()
      for i in bs['data']:
        casts = i['casts'] #主演
        cover = i['cover'] #海报
        directors = i['directors'] #导演
        m_id = i['id'] #ID
        rate = i['rate'] #评分
        star = i['star'] #标记人数
        title = i['title'] #片名
        url = i['url'] #网址
      cache = pd.DataFrame({'主演':[casts],'海报':[cover],'导演':[directors],'ID':[m_id],'评分':[rate],'标记':[star],'片名':[title],'网址':[url]})
      df = pd.concat([df,cache])
      return df

def format_url(num):
    urls = []
    base_url ='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}'
    for i in range(0,20 * num,20):
        url = base_url.format(i)
        urls.append(url)
    return urls

urls = format_url(450)
result = pd.DataFrame()
count = 1
for url in urls:
    df = parse_base_info(url,headers = headers)
    result = pd.concat([result,df])
    time.sleep(random.random() + 2)
    print('I had crawled page of:%d' % count)
    count += 1