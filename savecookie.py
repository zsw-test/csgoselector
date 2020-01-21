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

    # 往buff发送请求
    driver.get('https://buff.163.com/market/?game=csgo#tab=selling&page_num=1')
    driver.implicitly_wait(10)

    input("请回车登录")
    dictCookies = driver.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    # 登录完成后,将cookies保存到本地文件
    with open("cookies_tao.json", "w") as fp:
        fp.write(jsonCookies)

finally:
    driver.close()