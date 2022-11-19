from apscheduler.schedulers.blocking import BlockingScheduler
from msedge.selenium_tools import Edge, EdgeOptions
import time
from selenium.webdriver.common.by import By
def job():
    url = "https://xsgz.hufe.edu.cn/wap/main/welcome"
    UA = 'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI Edg/106.0.0.0'
    mobileEmulation = {"deviceMetrics": {"width": 320, "height": 640, "pixelRatio": 2.0}, "userAgent": UA}
    options = EdgeOptions()

    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.use_chromium = True
    browser = Edge(executable_path=r'msedgedriver.exe', options=options)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})
    browser.get(url=url)
    time.sleep(1)
    browser.find_element(by=By.ID, value='uname').send_keys("202005210146")  # 201905130122
    time.sleep(1)
    browser.find_element(by=By.ID, value='pd_mm').send_keys("hufe@202005210146")
    time.sleep(1)
    browser.find_element(by=By.ID, value='btn_login_save').click()
    print("登录成功")
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="tabbar-menu"]/ul[2]/li[1]/a').click()
    time.sleep(2)
    browser.find_element(by=By.ID, value='data_list_id_add_btn').click()
    time.sleep(3)
    browser.find_element(by=By.ID, value='form_body_save_btn').click()
    time.sleep(2)
    print("打卡成功")
    browser.quit()
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', day_of_week='0-6', hour=13, minute=45)
    scheduler.start()