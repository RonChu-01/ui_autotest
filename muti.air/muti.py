# -*- encoding=utf8 -*-
__author__ = "chuyong"
import threading, time
from airtest.core.api import *

auto_setup(__file__)

start_app('com.wdsm.kkkwan')

sleep(10)

wait(Template(r"tpl1552569145542.png", record_pos=(-0.005, 0.556), resolution=(1080, 1920)))

touch(Template(r"tpl1552569554670.png", record_pos=(0.002, 0.555), resolution=(1080, 1920)))

# dev_list = []

# dev1 = connect_device('Android://127.0.0.1:5037/5LM0216A25001147')
# dev_list.append(dev1)

# dev2 = connect_device('Android://127.0.0.1:5037/b03690e5')
# dev_list.append(dev2)

# # dev = device().serialno
# for i in dev_list:
#     dev = i.uuid
#     print(dev)
#     print(type(dev))

# for i in dev:
#     print(i)
#     dev_list.append(connect_device('Android://127.0.0.1:5037/{0}'.format(i)))

# print(dev_list)

# dev1 = connect_device('Android://127.0.0.1:5037/5LM0216A25001147')
# dev_list.append(dev1)

# dev2 = connect_device('Android://127.0.0.1:5037/b03690e5')
# dev_list.append(dev2)

# dev3 = connect_device('Android://127.0.0.1:5037/711QEBSD2572X')
# dev_list.append(dev3)

# for i in range(len(dev_list)):
    
#     set_current(i)

#     start_app('com.wdsm.kkkwan')

#     sleep(10)

#     stop_app('com.wdsm.kkkwan')
    
# def loop():

#     set_current(int(threading.current_thread().name))
    
#     start_app('com.wdsm.kkkwan')

#     sleep(10)

#     stop_app('com.wdsm.kkkwan')
    

    
# def loop():

#     set_current(int(threading.current_thread().name))
    
    
#     print('线程{0}，设备{1},准备执行脚本'.format(threading.current_thread().name, device().serialno))
#     start_app('com.wdsm.kkkwan')
    
#     sleep(10)
    
    
    
#     wait(Template(r"tpl1552569145542.png", record_pos=(-0.005, 0.556), resolution=(1080, 1920)))
    
#     touch(Template(r"tpl1552569554670.png", record_pos=(0.002, 0.555), resolution=(1080, 1920))
# )
    
#     set_current(int(threading.current_thread().name))
    
# #     注意：这里需要再次执行一下设备切换操作否则只能操作最后一次切换的那台设备
# #     set_current(int(threading.current_thread().name))

# #     print('线程{0}，设备{1},准备停止执行脚本'.format(threading.current_thread().name, device().serialno))
# #     stop_app('com.wdsm.kkkwan')
    
    
    
# thread_list = []
# for i in range(len(dev_list)):
#     t = threading.Thread(target=loop, name='{0}'.format(i))
#     thread_list.append(t)
#     t.start()
    
# for i in thread_list:
#     i.join()















