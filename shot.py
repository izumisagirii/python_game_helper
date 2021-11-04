from pyautogui import screenshot
# from cv2 import VideoCapture,flip,imshow,waitKey,destroyAllWindows

def getshot(content_text,text):
    content_text.AppendText("正在截图请稍等...\n")
    screenshot(text+'.png') # 截全屏并设置保存图片的位置和名称
    content_text.AppendText("截图成功\n")
def cam(content_text):
    content_text.AppendText("精简版没有彩蛋\n")
    # content_text.AppendText("正在打开相机,q键退出...\n")
    # capture = VideoCapture(0)
    # while True:
    #     ret, frame = capture.read()
    #     if ret:
    #         frame = flip(frame,1)   #镜像操作
    #         imshow("hahaha", frame)
    #         key = waitKey(1)
    #         #print(key)
    #         if key  == ord('q'):  #判断是哪一个键按下
    #             break
    #     else:
    #         break
    # capture.release()
    # destroyAllWindows()