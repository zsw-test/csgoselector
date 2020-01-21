import json

from selenium import webdriver  # 用来驱动浏览器的
import time

'''
===============所有方法===================
    element是查找一个标签
    elements是查找所有标签

    1、find_element_by_link_text  通过链接文本去找
    2、find_element_by_id 通过id去找
    3、find_element_by_class_name
    4、find_element_by_partial_link_text
    5、find_element_by_name
    6、find_element_by_css_selector
    7、find_element_by_tag_name
'''
# 获取驱动对象、
driver = webdriver.Chrome()

try:


    # 初次建立连接, 随后方可修改cookie
    driver.get('https://buff.163.com/market/?game=csgo#tab=selling&page_num=1')
    # 删除第一次登录是储存到本地的cookie
    driver.delete_all_cookies()
    # 读取登录时储存到本地的cookie
    with open("cookies_tao.json", "r", encoding="utf8") as fp:
        ListCookies = json.loads(fp.read())

    for cookie in ListCookies:
        driver.add_cookie({
            'domain': '.buff.163.com',  # 此处xxx.com前，需要带点
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })
    # 再次访问页面，便可实现免登陆访问
    driver.refresh()
    time.sleep(5)



finally:
    driver.quit()