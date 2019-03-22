import subprocess
from time import  ctime


# 指定 host  port  启动appium服务
def appium_start(host, port):
    bootstrap_port = str(port + 1)
    # wiindos 命令行格式
    # cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    # linux 环境下命令
    cmd = 'appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' %(cmd,ctime()))

    # 当前文件夹下 存放log日志 没有该文件夹则 创建文件夹 创建log日志
    subprocess.Popen(cmd,shell=True,stdout=open('./appium_log/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

if __name__ == '__main__':
    host='127.0.0.1'
    # port=4723
    # appium_start(host,port)
    for i in range(2):
        port=4723+2*i
        appium_start(host,port)