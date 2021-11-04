import win32api
import win32con
import win32gui
import pyautogui
import time


def MatchesColor(xpos, ypos, color, tolerance):
    pix = pyautogui.screenshot().getpixel((xpos, ypos))
    if(abs(pix[0] - color[0]) <= tolerance and abs(pix[1] - color[1]) <= tolerance and abs(pix[2] - color[2]) <= tolerance):
        return True
    return False


def resin(content_text):
    handle = win32gui.FindWindow(0, '原神')
    # 获取窗口句柄
    if handle == 0:
        content_text.AppendText("[error]原神未在运行\n")
        return
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND,
                         win32con.SC_RESTORE, 0)
    win32gui.SetForegroundWindow(handle)
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    if(x2 - x1 != 806 or y2-y1 != 629):
        content_text.AppendText("[error]原神没有以800*600运行\n")
        return
    win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST,
                          0, 0, 806, 629, win32con.SWP_SHOWWINDOW)
    time.sleep(.1)
    prelocated = MatchesColor(760, 600, (236, 229, 216), tolerance=10)
    if not prelocated:
        content_text.AppendText("[error]请打开风本'秘境入口'\n")
        return
    pyautogui.click(x=197, y=280, duration=.3)
    pyautogui.click(x=760, y=600, duration=.3)
    pyautogui.click(duration=3)
    while(True):
        time.sleep(5)
        while(MatchesColor(400, 450, (28, 28, 34), tolerance=5) or MatchesColor(400, 450, (255, 255, 255), tolerance=5)):
            time.sleep(.5)
        while(not MatchesColor(600, 390, (36, 39, 49), tolerance=3)):
            time.sleep(.5)
        pyautogui.click(duration=2)
        time.sleep(3)
        pyautogui.press('1')
        pyautogui.keyDown('w')
        pyautogui.keyDown('shift')
        time.sleep(5.7)
        pyautogui.keyUp('shift')
        pyautogui.keyUp('w')
        while(not MatchesColor(471, 327, (255, 255, 255), tolerance=20)):
            pyautogui.press('w')
        pyautogui.press('3')
        time.sleep(.2)
        pyautogui.press('e')
        time.sleep(.8)
        pyautogui.press('4')
        time.sleep(.2)
        pyautogui.press('e')
        time.sleep(.8)
        pyautogui.press('1')
        time.sleep(.2)
        pyautogui.press('f')
        time.sleep(.2)
        pyautogui.press('q')
        time.sleep(2)
        pyautogui.press('2')
        time.sleep(5.5)
        pyautogui.press('q')
        time.sleep(2)
        pyautogui.press('1')
        time.sleep(6.5)
        pyautogui.press('q')
        time.sleep(2)
        pyautogui.press('e')
        time.sleep(2)
        pyautogui.keyDown('w')
        pyautogui.keyDown('shift')
        time.sleep(.1)
        pyautogui.keyUp('shift')
        pyautogui.keyUp('w')
        time.sleep(12)
        # pyautogui.screenshot(str(time.time())+'.png')
        road = 0
        content_text.AppendText("正在寻路\n")
        while abs(road - 800) > 2:
            line = pyautogui.screenshot(region=(0, 0, 806, 629))
            pixels = []
            for i in range(800):
                pix = line.getpixel((i+3, round(-0.00005*i**2 + 0.04*i + 157)))
                if (pix[1] > 240 and pix[0] > 240 and pix[2] > 200):
                    pixels.append(True)
                else:
                    pixels.append(False)
            pixelsCOPY = pixels.copy()
            for i in range(800):
                if(i < 4):
                    pixels[i] = False
                elif(i > 795):
                    pixels[i] = False
                elif(pixelsCOPY[i-4:i+4].count(True) > 3):
                    pixels[i] = True
                else:
                    pixels[i] = False
            lightL = 0
            lightR = 0
            indexN = 0
            # printpix = ''
            # for i in range(800):
            #     printpix = printpix+str(pixels[i])
            # content_text.AppendText(printpix+"\n")
            while(indexN < 800 and not pixels[indexN]):
                indexN = indexN+1
            lightL = indexN
            while(indexN < 800 and pixels[indexN]):
                indexN = indexN+1
            lightL = (lightL+indexN)/2
            while(indexN < 800 and not pixels[indexN]):
                indexN = indexN+1
            lightR = indexN
            while(indexN < 800 and pixels[indexN]):
                indexN = indexN+1
            lightR = (lightR+indexN)/2
            road = lightL+lightR
            # content_text.AppendText("正在寻路,位置"+str(lightL)+' '+str(lightR)+"\n")
            if(road > 800):
                pyautogui.press('d')
            else:
                pyautogui.press('a')
        content_text.AppendText("找到路了\n")
        pyautogui.keyDown('w')
        pyautogui.keyDown('shift')
        time.sleep(3)
        pyautogui.keyUp('shift')
        pyautogui.keyUp('w')
        time.sleep(.2)
        pyautogui.keyDown('w')
        while(not MatchesColor(471, 327, (255, 255, 255), tolerance=20)):
            time.sleep(.1)
        pyautogui.keyUp('w')
        pyautogui.press('f')
        while(not MatchesColor(550, 590, (245, 237, 228), tolerance=20)):
            time.sleep(1)
        time.sleep(2)
        pyautogui.click(x=550, y=590, duration=.3)

