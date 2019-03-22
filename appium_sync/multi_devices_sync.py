from appium import webdriver
import yaml
from  time import  ctime
import multiprocessing

'''
多进程启动设备

'''
with open('desired_caps.yaml','r') as file:
    data=yaml.load(file)

devices_list=['127.0.0.1:62001','127.0.0.1:62025']

def appium_desired(udid,port):
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid']=udid

    desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    print('appium port:%s start run %s at %s' %(port,udid,ctime()))
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
    driver.implicitly_wait(5)
    return driver

desired_process=[]
# 使用for循环进行 添加进程组
for i in range(len(devices_list)):
    port=4723+2*i
    # 创建进程
    desired=multiprocessing.Process(target=appium_desired,args=(devices_list[i],port))
    # 添加到进程列表中
    desired_process.append(desired)

if __name__ == '__main__':
    # 启动进程 start  join 进程间切换
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        # 等所有进程执行结束后结束进程
        desired.join()