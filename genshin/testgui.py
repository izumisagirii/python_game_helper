import pyautogui

# line = pyautogui.screenshot(region=(0, 164, 806, 164))
# for i in range(800):
#     pix = line.getpixel((i+3,163))
#     positionStr = ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
#     print(positionStr) # 打印结果为RGB:( 60, 63, 65)
# while(True):
#     pyautogui.moveRel(1, 0)
#     pyautogui.sleep(.1)

def debugui(content_text):
    while True:
    # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        pix = pyautogui.screenshot().getpixel((x, y)) # 获取鼠标所在屏幕点的RGB颜色
        positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
        # print(positionStr, end='') # end='' 替换了默认的换行
        # print('\b' * len(positionStr), end='', flush=True) # 连续退格键并刷新，删除之前打印的坐标，就像直接更新坐标效果
        content_text.AppendText(positionStr+'\n')