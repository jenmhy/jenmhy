import pyautogui
import time

time.sleep(3)

# 立即购买
def buy(img):
    while True:
        # 查找有没有立即购买的按钮
        buyBtn = pyautogui.locateOnScreen(img)
        print(buyBtn)
        if buyBtn is not None:
            pyautogui.click(buyBtn.left + buyBtn.width/2, buyBtn.top+buyBtn.height/2)
            break
        time.sleep(0.001)

# 选择价格
def price(img):
    while True:
        price = pyautogui.locateOnScreen(img)
        print(price)
        if price is not None:
            pyautogui.click(price.left + price.width/2, price.top+price.height/2)
            break
        time.sleep(0.001)

# 选择购买票数，一个不用这个函数，两票用一次，三票用两次
def add(img):
    addBtn = pyautogui.locateOnScreen(img)
    if addBtn is not None:
        # 点击一下，买两张
        pyautogui.click(addBtn.left + addBtn.width/2, addBtn.top+addBtn.height/2)

# 下单
def enter(img):
    enterBtn = pyautogui.locateOnScreen(img)
    if enterBtn is not None:
        pyautogui.click(enterBtn.left + enterBtn.width/2, enterBtn.top+enterBtn.height/2)

