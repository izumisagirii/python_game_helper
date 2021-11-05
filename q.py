# coding:utf-8
import wx
import helper,shot,genshin.resincleener,genshin.testgui
import time
from threading import Thread
import stop


def start():
    global joinable 
    thread1 = Thread(target=workthread)
    thread1.daemon = False
    global stop_thread
    stop_thread = False
    thread1.start()
    while True:
        if stop_thread:
            if thread1.is_alive():
                stop.stop_thread(thread1)
            break
        time.sleep(.1)
    #content_text.AppendText("子线程停止\n")
    joinable = True



def workthread():
    path = path_text.GetValue()
    path_text.Clear()
    orders = path.split('&')
    for order in orders:
        readorder = order.split(' ')
        if(len(readorder)==1):
            if readorder[0] == 'help':
                content_text.AppendText("-------输出帮助：\n")
                helper.printhelp(content_text)
            elif readorder[0] == 'daily':
                content_text.AppendText("-------正在做每日任务：\n")
                for i in range(100):
                    time.sleep(0.1)
                    content_text.AppendText(str(i)+'\n')
                content_text.AppendText("你不会真的以为我会做吧\n")
            elif readorder[0] == 'cam':
                content_text.AppendText("-------触发彩蛋--镜子！！：\n")
                shot.cam(content_text)
            elif readorder[0] == 'debug':
                content_text.AppendText("-------debug：\n")
                genshin.testgui.debugui(content_text)
            else:
                content_text.AppendText("-------不合法的命令 "+order+' \n')
        elif(len(readorder)==2):
            if readorder[0] == 'shot':
                content_text.AppendText("-------正在截图：\n")
                frame.Show(False)
                shot.getshot(content_text,readorder[1])
                frame.Show(True)
            elif readorder[0] == 'genshin':
                if readorder[1] == 'resin':
                    content_text.AppendText("-------正在风本清体力：\n")
                    genshin.resincleener.resin(content_text)
                else:
                    content_text.AppendText("-------不合法的命令 "+order+' \n')
            else:
                content_text.AppendText("-------不合法的命令 "+order+' \n')
        else:
            content_text.AppendText("-------不合法的命令 "+order+' \n')
    content_text.AppendText("***结束任务***\n")
    global stop_thread
    stop_thread = True
    


def startpro(event):     # 启动任务事件
    global joinable,thread2
    if thread2.is_alive():
        content_text.AppendText("有任务正在进行中，请勿操作！\n")
    else:
        if(joinable):
            thread2.join()
            joinable = False
        content_text.AppendText("***开始任务***\n")
        thread2 = Thread(target= start)
        thread2.start()
        joinable = True
    
    # with open(path,"r",encoding="utf-8") as f:  # encoding参数是为了在打开文件时将编码转为utf8
        # content_text.AppendText(f.read())


def quitapp(event):
    global stop_thread,thread2,joinable
    if joinable:
        stop_thread = True
        thread2.join()
        joinable = False
    content_text.AppendText("***终止任务***\n")
    

thread2 = Thread(target= start)
joinable = False
app = wx.App()
frame = wx.Frame(None, title="穹批工具箱", pos=(800, 200), size=(500, 400))

panel = wx.Panel(frame)

path_text = wx.TextCtrl(panel)
open_button = wx.Button(panel, label="运行")
open_button.Bind(wx.EVT_BUTTON, startpro)    # 绑定事件

save_button = wx.Button(panel, label="退出")
save_button.Bind(wx.EVT_BUTTON, quitapp)

content_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
#  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行

box = wx.BoxSizer()  # 不带参数表示默认实例化一个水平尺寸器
box.Add(path_text, proportion=5, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
# proportion：相对比例
# flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
# border：边框
box.Add(open_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
box.Add(save_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件

v_box = wx.BoxSizer(wx.VERTICAL)  # wx.VERTICAL参数表示实例化一个垂直尺寸器
v_box.Add(box, proportion=1, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
v_box.Add(content_text, proportion=5,
          flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
panel.SetSizer(v_box)  # 设置主尺寸器

frame.Show()

content_text.AppendText("欢迎使用穹批工具箱——开发者sdfs\n")
content_text.AppendText("输入help获取帮助\n")
app.MainLoop()
