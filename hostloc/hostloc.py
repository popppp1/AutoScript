# coding:utf-8

# update time: 20170227

# 脚本介绍：
# 1, 自动踢楼脚本 for www.hostloc.com
# 2, C大经常开金盾, So浏览器渲染
# 3, 由于hostloc服务器老是502,或由于"网络的不确定性",So 踢中为止

# 使用说明：
# 1, sudo pip install python-pip
# 2, sudo pip install selenium
# 3, sudo pip install lxml
# 4, python hostloc.py 踢楼地址 踢楼楼层 踢楼口号 账户 密码

import time
import lxml
import os
import sys
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def startPhantomjs():
    pass

def endPhantomjs():
    pass

def isworking(hostloc_url, hostloc_floor):

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 "
    )

    driver = webdriver.PhantomJS(executable_path='./phantomjs/bin/phantomjs',desired_capabilities=dcap)
    driver.set_window_size(1366, 768)
    while True:
        driver.get(hostloc_url)
        tree = etree.HTML(driver.page_source)
        current_floor = tree.xpath('//span[@class="xi1"][2]/text()')
        if current_floor:
            value = int(hostloc_floor)-int(current_floor[0])
            if value == 2:
                driver.quit()
                return 1
            elif value < 2:
                driver.quit()
                return 0
            else:
                print '当前楼层: 1+' + current_floor[0]
                if value > 20:
                    time.sleep(60)
                elif value > 15:
                    time.sleep(30)
                elif value > 10:
                    time.sleep(15)
                elif value > 5:
                    time.sleep(6)
                continue
        else:
            continue

def tilou(hostloc_url, hostloc_kouhao, hostloc_user, hostloc_password):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 "
    )

    driver = webdriver.PhantomJS(executable_path='./phantomjs/bin/phantomjs', desired_capabilities=dcap)
    driver.set_window_size(1366, 768)
    driver.implicitly_wait(120)
    driver.get(hostloc_url)
    driver.find_element_by_id('ls_username').clear()
    driver.find_element_by_id('ls_username').send_keys(hostloc_user)
    driver.find_element_by_id('ls_password').clear()
    driver.find_element_by_id('ls_password').send_keys(hostloc_password)
    driver.find_element_by_xpath('//button[@class="pn vm"]/em').click()
    driver.find_element_by_id('fastpostmessage').clear()
    driver.find_element_by_id('fastpostmessage').send_keys(hostloc_kouhao)
    driver.find_element_by_id('fastpostsubmit').click()
    driver.quit()

if __name__ == '__main__':
    if len(sys.argv) < 6:
        raise ValueError('请检查参数！')
    hostloc_url = sys.argv[1]
    hostloc_floor = sys.argv[2]
    hostloc_kouhao = sys.argv[3]
    hostloc_user = sys.argv[4]
    hostloc_password = sys.argv[5]

    if 'http' not in hostloc_url:
        raise ValueError('网址有误！')
    if int(hostloc_floor) <= 0:
        raise ValueError('楼层有误！')
    if len(hostloc_kouhao) < 6:
        raise ValueError('口号太短！')

    # 口号&帐号 有中文的情况
    hostloc_kouhao = hostloc_kouhao.decode('utf-8')
    hostloc_user = hostloc_user.decode('utf-8')

    while True:
        try:
            work = isworking(hostloc_url, hostloc_floor)
            if work == 1:
                tilou(hostloc_url, hostloc_kouhao, hostloc_user, hostloc_password)
                print '踢楼已中!'
            else:
                print '踢楼没中!'
            break
        except Exception, e:
            print str(e)
