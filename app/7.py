import pyautogui
import time
import win32api
import win32con
import win32gui
import win32clipboard as w

def FindWindow(chatroom):
    win = win32gui.FindWindow(None, chatroom)
    print("找到窗口句柄：%x" % win)
    if win != 0:
        win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
        win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
        win32gui.ShowWindow(win, win32con.SW_SHOW)
        win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 0, 0, 300, 500, win32con.SWP_SHOWWINDOW)
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(1)
        tit = win32gui.GetWindowText(win)
        print('已启动【' + str(tit) + '】窗口')
    else:
        print('找不到【%s】窗口' % chatroom)
        exit()


# 设置和粘贴剪贴板
def ClipboardText(ClipboardText):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, ClipboardText)
    w.CloseClipboard()
    time.sleep(1)
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟发送动作
def SendMsg():
    win32api.keybd_event(18, 0, 0, 0)
    win32api.keybd_event(83, 0, 0, 0)
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)

# 模拟发送微信消息
def SendWxMsg(wxid, sendtext):
    # 先启动微信
    FindWindow('微信')
    time.sleep(1)
    # 定位到搜索框
    pyautogui.moveTo(143, 39)
    pyautogui.click()
    # 搜索窗口
    ClipboardText(wxid)
    time.sleep(1)
    # 进入窗口
    pyautogui.moveTo(155, 120)
    pyautogui.click()
    # 粘贴文本内容
    ClipboardText(sendtext)
    SendMsg()
    print('已发送')

# 调用函数（微信号或微信昵称或备注，需要发送的文本消息）
#SendWxMsg('文件传输助手', 'Python发送微信消息')
pyautogui.moveTo(655, 320)