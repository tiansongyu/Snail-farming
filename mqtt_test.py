#!/usr/bin/env python  
#coding=utf-8  

import json
import sys
import os
import time
import paho.mqtt.client as mqtt
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
 
REPORT_TOPIC = 'test'  # 主题
 
 
def on_connect(client, userdata, flags, rc):
    print('connected to mqtt with resurt code ', rc)
    client.subscribe(REPORT_TOPIC,1)  # 订阅主题
 
 
def on_message(client, userdata, msg):
    """
    接收客户端发送的消息
    :param client: 连接信息
    :param userdata: 
    :param msg: 客户端返回的消息
    :return: 
    """
    print("Start server!")
    payload = json.loads(msg.payload.decode('utf-8'))
    print(payload)
 
 
def server_conenet(client):
    client.on_connect = on_connect  # 启用订阅模式
    client.on_message = on_message  # 接收消息
    
    client.connect("114.55.102.103", 1883, 60)  # 链接
    # client.loop_start()   # 以start方式运行，需要启动一个守护线程，让服务端运行，否则会随主线程死亡
    client.loop_forever()   # 以forever方式阻塞运行。
 
 
def server_stop(client):
    client.loop_stop()  # 停止服务端
    sys.exit(0)
 
 
def server_main():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    client = mqtt.Client(client_id, clean_session=True)
    client.username_pw_set("admin","123456")
    server_conenet(client)
 
 
if __name__ == '__main__':
    # 启动监听
    server_main()
