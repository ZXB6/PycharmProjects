import requests

headers = {
    "Cookie": "JSESSIONID=9512D2BCDDA537F54ADAB90B65BB81D8"
}
data = {
    "uname" : "201905130122",
    "pp_mm" : "hufe@201905130122"
}
url = 'https://xsgz.hufe.edu.cn/wap/main/welcome'
#response = requests.get(url,headers=headers)
#response.encoding = 'utf-8'
session.ost(url,data=data)

print(response.json())
