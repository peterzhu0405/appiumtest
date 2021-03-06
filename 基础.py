#!usr/bin/env python  
#-*- coding:utf-8 _*- 
# -------author  zhujaingtao -----------
'''
使用uiautomator 工具保存页面  进行页面元素查询。
调试脚本时  每做一步 都需要执行一下 保证每一步都不出错

脚本运行 需要先启动appium  保证设备和服务是连接的，脚本连接appium 执行脚本


需要输入内容时 需要配置  appium 两个app 手动安装
desired_caps['unicodeKeyboard']="True"
desired_caps['resetKeyboard']="True"


find_element 元素定位  通过获取异常的方式确定元素是否显示
id ，classname ，h5 list(选择相片),xpath,toast,relative,uiautomator,
==========================================================
id  获取的方式
例子代码
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('android:id/button2').click()
==================================================================
classname获取的例子 由于text　性不太好 appium 1.5以后 废弃了该放大
driver.find_element_by_class_name('android.widget.EditText').send_keys('自学网2018')
driver.find_element_by_class_name('android.widget.EditText').send_keys('zxw2018')
driver.find_element_by_class_name('android.widget.Button').click()
==========================================================
相对定位获取的例子：先找到该元素的有对应属性的父元素节点，然后基于父元素进行元素定位
父元素
root_element=driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
root_element.find_element_by_class_name('android.widget.ImageView').click()

xpath 定位方式
xpath定位是一种路径定位方式，主要是依赖于元素绝对路径或者相关属性来定位
表达式
/  从根节点开始筛选
// 从匹配的当前节点选择文档中的节点，
nodename 选取此节点 的所有子节点
.   选取当前节点
..选取当前节点的父节点
@  选择属性
通配符
例子
from find_element.capability import driver

driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('zxw1234')

driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys('zxw123456')

driver.find_element_by_xpath('//android.widget.Button').click()

# driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()
=============================================================
list定位   List定位首先是使用find_elements_by_XX获取一组相同的class属性的元素，
然后使用数组下标来区分标记不同元素进行相关操作
list 例子  例如嘀嘀出行 共享汽车业务线线上 地图上的个人中心和帮助中心 id和name就是一致的需要使用list方式 进行元素获取方式
images=driver.find_elements_by_id('com.tal.kaoyan:id/item_image')

images[10].click()

driver.find_element_by_id('com.tal.kaoyan:id/save').click()
=====================================================
UIAutomator  定位元素   查找元素
id  ,text   classNname
例子
from find_element.capability import driver

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('zxw1234')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('zxw123456')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()

text 定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("请输入用户名")').send_keys('zxw1234')
className 定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('zxw1234')
====================================================================================================
元素等待
强制等待
例子：
from time import sleep
#强制等待5秒 设置固定的等待时间
sleep(5)

隐式等待  只对所有元素设置的等待时间
driver.implicitly_wait(20)
显式等待   是针对某个元素来设置的等待时间
例子1
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver : WebDriver
timeout : 最长超时时间，默认以秒为单位
poll_frequency : 休眠时间的间隔时间，默认为0.5秒
ignored_exceptions : 超时后的异常信息，默认情况下抛NoSuchElementException异常。
例子2
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("elementID"))
=============================================================================
toast识别    需要安装 uiautomator2

配置问题
desired_caps['automationName']='uiautomator2'
安装相关的driver包。
cnpm install appium-uiautomator2-driver

例子
# coding=utf-8
from find_element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('zxss018')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()


error_message="用户名或密码错误，你还可以尝试4次"
limit_message="验证失败次数过多，请15分钟后再试"

message='//*[@text=\'{}\']'.format(error_message)
# message='//*[@text=\'{}\']'.format(limit_message)
主要代码
toast_element=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)

===================================
屏幕截图 有图有真相
例子1
driver.save_screenshot('login.png')

例子2
driver.get_screenshot_as_file('./images/login.png')


============================
检测是否有活动弹窗 有则关闭
#检测是否有活动页面弹窗，如果有就点击关闭
try:
    closBtn=driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closBtn.click()
=============================================================
数据配置 yaml文件配置
例子
新建  jichu.yaml
内容
platformName: Android
platformVersion: 5.1.1
deviceName: 127.0.0.1:62025
app: C:\Users\Shuqing\Desktop\kaoyan3.1.0.apk
appPackage: com.tal.kaoyan
appActivity: com.tal.kaoyan.ui.activity.SplashActivity
noReset: False
unicodeKeyboard: True
resetKeyboard: True
ip: 127.0.0.1
port: 4723

例子
读取yaml文件
import yaml

file=open('jichu.yaml','r')
data=yaml.load(file)

print(data)

print(data['app'])
print(data['port'])

数据修改:备注 此处只是变量类型的数据变更，不会真正修改到yaml配置表中的数据
data['app']='ios'

python 数据类型转化成yaml
import yaml

slogan=['welcome','to','51zxw']
website={'url':'www.51zxw.net'}

#python data
print(slogan)
print(website)

#yaml data
print(yaml.dump(slogan))
print(yaml.dump(website))
================================
日志模块处理
log.conf   日志的配置文件
例子1
from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging
import logging.config

配置文件位置
CON_LOG='../log/log.conf'
加载文件
logging.config.fileConfig(CON_LOG)
获取日志对象
logging=logging.getLogger()
添加日志
logging.info("check_updateBtn")



==============================================================
tomcat 安装  jenkins安装 https://www.jianshu.com/p/897b9a8fb210
推荐安装后 可以搭建Android 打包环境  appium自动化测试代码自动运行  接口自动化测试代码 拉代码进行测试
jenkis 配置学习

===========================================
封装account.csv 文件存储数据  在公共类中封装 从csv文件中获取数据的方法
数据与业务代码拆分  用例编写和功能业务拆分。

数据驱动 测试用例  ，用例驱动功能
=======================
用例执行和测试报告生成

所使用的python环境的在pycharm 查找python 路径 把 bstestrunner.py 文件拷贝到 python/lib/sit-package

appium server 服务启动 只进行用例的执行。

手动触发和定时触发任务。
==========================
python 脚本运行 appium server 端

命令 脚本和服务器需要端口号  设备和服务器进行通信  需要指定端口号 bp
appium -p 4723
appium -p 4725

-a ip 地址

-bp 指定设备连接端口号

--no-reset seesion 是否重置

-appactivity

-app  远程 app地址
appium -h 更多命令行指令。

====================================
appium 并发测试 多进程并发执行执行测试脚本

需要处理 appium 相关的apk 安装到经常使用的测试手机 进行一次性配置。

多进程 对于一个变量有隔离 多进程形式互不影响
import multiprocessing 导入模块
# 创建进程
    desired=multiprocessing.Process(target=appium_desired,args=(devices_list[i],port))
    # 添加到进程列表中
    desired_process.append(desired)

    进程执行
        for desired in desired_process:
        desired.start()
    进行结束
      for desired in desired_process:
        # 等所有进程执行结束后结束进程
        desired.join()
=====================================================

docker  + STF （设备管理） 远程的操作
https://github.com/haifengrundadi/DisCartierEJ





































































'''

