from appium_sync.multi_appium import appium_start
from appium_sync.multi_devices import appium_desired
from appium_sync.check_port import *
from time import sleep
import multiprocessing

'''
并发启动appium
并发启动脚本执行


'''

devices_list=['127.0.0.1:62001','127.0.0.1:62025']
# 启动服务
def start_appium_action(host,port):
    if check_port(host,port):
        appium_start(host,port)
        return True
    else:
        print('appium %s start fail' %port)
        return False
# 启动脚本获取driver 手柄
def start_devices_action(udid,port):
    host='127.0.0.1'
    if start_appium_action(host,port):
        appium_desired(udid,port)
    else:
        release_port(port)

def appium_start_sync():
    print('=====appium_start_sync=====')

    appium_process=[]

    for i in range(2):
        host = '127.0.0.1'
        port = 4723 + 2 * i

        appium = multiprocessing.Process(target=start_appium_action, args=(host, port))
        appium_process.append(appium)

    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

    sleep(5)

def devices_star_sync():
    # 可以并发执行测试脚本
    print('======devices_star_sync===')

    desired_process = []

    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        desired = multiprocessing.Process(target=start_devices_action, args=(devices_list[i], port))
        desired_process.append(desired)

    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()

if __name__ == '__main__':
    # 启动appium 服务
    appium_start_sync()
    # 启动脚本服务
    devices_star_sync()