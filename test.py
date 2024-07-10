import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service      
from selenium.webdriver.chrome.options import Options
import time
# 测试函数
def test_baidu_search():
    # 初始化浏览器驱动
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless') 
    s = Service('/usr/bin/chromedriver')    
    driver = webdriver.Chrome(options=options) 
    #cdriver = webdriver.Chrome()

    # 打开百度页面
    driver.get("http://www.baidu.com")
    time.sleep(1)
    # 找到搜索框
    search_box = driver.find_element("id", "kw")
    time.sleep(1)
    # 输入关键字
    search_box.send_keys("自动化测试")

    # 点击搜索按钮
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
