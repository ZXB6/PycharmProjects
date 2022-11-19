from msedge.selenium_tools import Edge, EdgeOptions
import time
from selenium.webdriver.common.by import By

url = "https://xsgz.hufe.edu.cn/wap/main/welcome"
UA = 'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI Edg/106.0.0.0'
mobileEmulation = {"deviceMetrics": {"width": 320, "height": 640, "pixelRatio": 2.0}, "userAgent": UA}
options = EdgeOptions()
# 设置h5

options.add_experimental_option('mobileEmulation', mobileEmulation)
options.use_chromium = True
# 最大化窗口
# options.add_argument('start-maximized')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('lang=zh-CN.UTF-8')
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-browser-side-navigation")
# options.add_argument('window-size=1920x1080')
# F11 全屏  options.add_argument('start-fullscreen')
# 无窗口运行  options.add_argument("headless")
browser = Edge(executable_path=r'C:\ProgramData\Anaconda3\Scripts\msedgedriver.exe',options=options)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
browser.get(url=url)
time.sleep(1)
browser.find_element(by=By.ID,value='uname').send_keys("202005220237")   # 201905130122
time.sleep(1)
browser.find_element(by=By.ID,value='pd_mm').send_keys("hufe@202005220237")
time.sleep(1)
browser.find_element(by=By.ID,value='btn_login_save').click()
print("登录成功")
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="tabbar-menu"]/ul[2]/li[1]/a').click()
time.sleep(2)
browser.find_element(by=By.ID,value='data_list_id_add_btn').click()
time.sleep(3)
browser.find_element(by=By.ID,value='form_body_save_btn').click()
time.sleep(1)
print("打卡成功")
browser.quit()
