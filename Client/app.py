# -*- coding: UTF-8 -*-
# Python3.x 导入方法
import requests,json
from threading import Timer
from tkinter import * 
def GetJsonData():
    url="http://infotag.xfox.fun/"
    JsonData=requests.get(url).text
    JsonData=json.loads(JsonData)
    #print(JsonData["hostname"])
    hostname=JsonData["hostname"]
    freemem=JsonData["freemem"]
    totalmem=JsonData["totalmem"]
    InfoText="HostName："+hostname+"\nFreeMem:"+freemem+"\nTotalMem:"+totalmem
    return InfoText
TextData=GetJsonData()
root = Tk()                     # 创建窗口对象的背景
root.title("InfoTag")
root.resizable(width=False,height=False)#False表示不可以缩放，True表示可以缩放
text_label=Label(root,padx=0,pady=0,height=5,width=30,justify=LEFT, bg="#e9d7df",fg="#22202e",text=TextData)
def UpDate():
    Data=GetJsonData()
    text_label.config(text=Data)
    #print("1")
    LoopObject=Timer(1,UpDate)
    LoopObject.start()
UpDate()
text_label.pack()
root.mainloop()                 # 进入消息循环 
#LoopObject.cancel()
