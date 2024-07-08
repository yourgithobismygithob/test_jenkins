import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 测试函数
def test_baidu_search():
    # 初始化浏览器驱动
    driver = webdriver.Chrome()

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