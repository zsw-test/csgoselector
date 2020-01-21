
import json


from selenium import webdriver  # 用来驱动浏览器的

import time



#一些纪念品和statrck的要求 默认是false
from selenium.webdriver.support.select import Select

issouvenir = 0;
isstatTrak = 0;
# attritionrate 磨损程度  默认  0--不限      1--崭新  2--略磨   3--久经   4--破损不堪  5---战痕累累   6--无装涂
wearcategory = 0;
sleeptime =3;                  #每次跳转时的等待时间 强制等待  网速好可以适当改小一点 = =
SearchGunList = []
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
from playsound import playsound
def playsounds():
    playsound('ok.mp3')

def compareEveryPage(driver,maxwear,maxmoney):
    # 先找到总页数
    pagenumsli = driver.find_element_by_xpath(
        '//div[@class="pager list-pager light-theme simple-pagination"]/ul/li[last()-1]')
    pagenum = pagenumsli.text

    # 每一页的操作
    i = 0;
    while i < int(pagenum) - 1:

        mosunElements = driver.find_elements_by_xpath('//div[@class="wear-value"]')
        moneyElements = driver.find_elements_by_xpath('//strong[@class="f_Strong"]')

        wears = [];  # 当前页的磨损数组
        moneys = [];  # 当前页的金钱数组
        # if moneys[0]>maxmoney:               #如果第一个价格就大于最大的价格就直接返回
        #     break
        for m in mosunElements:
            wears.append(m.text)
        for m in moneyElements:
            moneys.append(m.text)

        for index in range(len(moneys)):
            moneys[index] = moneys[index][1:]  # 去掉前面的钱币符号
        for index in range(len(wears)):
            wears[index] = wears[index][4:]  # 去掉前面额磨损两字
        moneys.pop(0)  # 删除第一个不要的价格

        for index in range(len(wears)):
            if (float(wears[index]) < maxwear) & (float(moneys[index]) < maxmoney):  # 如果小于此磨损和小于此money
                playsounds()
                print("yes")
        print(wears);
        print(moneys);
        driver.find_element_by_xpath('//a[@class="page-link next"]').click()
        i += 1;
        time.sleep(1)


    #如果找到了最后一面 最后结束的一面也要找  （一般我感觉是找不到最后一面的）
    mosunElements = driver.find_elements_by_xpath('//div[@class="wear-value"]')
    moneyElements = driver.find_elements_by_xpath('//strong[@class="f_Strong"]')

    wears = [];  # 当前页的磨损数组
    moneys = [];  # 当前页的金钱数组
    # if moneys[0] > maxmoney:     #如果第一个价格就大于最大的价格就直接返回
    #     return
    for m in mosunElements:
        wears.append(m.text)
    for m in moneyElements:
        moneys.append(m.text)

    for index in range(len(moneys)):
        moneys[index] = moneys[index][1:]  # 去掉前面的钱币符号
    for index in range(len(wears)):
        wears[index] = wears[index][4:]  # 去掉前面额磨损两字
    moneys.pop(0)  # 删除第一个不要的价格

    for index in range(len(wears)):
        if (float(wears[index]) < maxwear) & (float(moneys[index]) < maxmoney):  # 如果小于此磨损和小于此money
            print("yes")
            playsounds()

    print(wears);
    print(moneys);


def searchname(str,driver,issouvenir,isstatTrak,wearcategory,maxwear,maxmoney):
    driver.get('https://buff.163.com/market/?game=csgo#tab=selling&page_num=1')
    time.sleep(sleeptime)
    #先找名字和磨损程度
    search_name = driver.find_element_by_name('search')
    search_name.send_keys(str)
    time.sleep(sleeptime)

    #找到类别选择器
    driver.find_element_by_id("search-quality").click()
    time.sleep(sleeptime)
    if  issouvenir==0&isstatTrak==0:
        driver.find_element_by_class_name("quality_normal").click()
        time.sleep(sleeptime)
    elif isstatTrak==1:
        driver.find_element_by_class_name("quality_strange").click()
        time.sleep(sleeptime)
    elif issouvenir==1:
        driver.find_element_by_class_name("quality_tournament").click()
        time.sleep(sleeptime)

    #找到外观选择器
    driver.find_element_by_id('search-exterior').click();
    time.sleep(sleeptime)

    #根据磨损循环搜索每一面   崭新、略磨、久经、破损、战痕累累   没有搜索无装涂的（刀）

    if wearcategory==1:
        driver.find_element_by_class_name('exterior_wearcategory0').click();
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        driver.find_element_by_xpath('//div[@class="list_card unhover"]/ul/li/a').click()
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        compareEveryPage(driver,maxwear,maxmoney)
    elif wearcategory==2:
        driver.find_element_by_class_name('exterior_wearcategory1').click();
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        driver.find_element_by_xpath('//div[@class="list_card unhover"]/ul/li/a').click()
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        compareEveryPage(driver, maxwear, maxmoney)
    elif wearcategory == 3:
        driver.find_element_by_class_name('exterior_wearcategory2').click();
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        driver.find_element_by_xpath('//div[@class="list_card unhover"]/ul/li/a').click()
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        compareEveryPage(driver, maxwear, maxmoney)
    elif wearcategory==4:
        driver.find_element_by_class_name('exterior_wearcategory3').click();
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        driver.find_element_by_xpath('//div[@class="list_card unhover"]/ul/li/a').click()
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        compareEveryPage(driver, maxwear, maxmoney)
    elif wearcategory==5:
        driver.find_element_by_class_name('exterior_wearcategory5').click();
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        driver.find_element_by_xpath('//div[@class="list_card unhover"]/ul/li/a').click()
        time.sleep(sleeptime)  # 跳转页面之后要强制等待1s 等待页面加载完成
        compareEveryPage(driver, maxwear, maxmoney)


    # 通过text找到搜索按钮

    # driver.find_element_by_xpath('//div[@id="j_search"]//a').click()
    # time.sleep(sleeptime)

    pass


try:

    # 往buff发送请求
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
    # time.sleep(sleeptime)
    while True:
        searchname("AUG | 汪之萌杀", driver, 0, 0, 3, 0.21, 32);
        searchname("P90 | 往日行动 ", driver, 0, 0, 3, 0.21, 32);
        searchname("MP9 | 九头蛇 ", driver, 0, 0, 3, 0.21, 35);



   # 通过search找到搜索框
   #  search_name = driver.find_element_by_name('search')
   #  search_name.send_keys('巨龙传说')
   #  time.sleep(sleeptime)
   #
   #  #通过class找到搜索按钮
   #
   #  search_button = driver.find_element_by_link_text("搜索")
   #  search_button.click()
   #  time.sleep(sleeptime)

finally:
    input("请回车登录")
    driver.close()



