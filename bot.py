import pyautogui, time, os, logging, sys, random, subprocess
from pathlib import Path
from maps import *

timeScale = 1.0
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

eventType = "totem_collection"
stateIndicators = ["play_home", "stage_select", "in_game", "collect", eventType + "\event"]
mapIndicators = ["sanc", "ravine", "flooded", "infernal", "bloody", "workshop", "quad", "dark", "muddy", "ouch"]
mapState = ""
x = ""
y = ""
resDir = Path('res/')

def main():
    pyautogui.sleep(1)
    while pyautogui.getActiveWindow().title == "BloonsTD6":
        menuState = CheckMenuState()
        print(menuState)
        if menuState == "play_home":
            clickElement(menuState, 1)
        elif menuState == "stage_select":
            selectExpertMap(1, 5)
        elif menuState == "in_game":
            selectGameScript()
        elif menuState == "collect":
            openBoxes()
        elif menuState == eventType + "\event":
            clickElement("play_collect", 1)

def searchImage(picName):
    # win = pyautogui.getActiveWindow()
    # return pyautogui.locateOnScreen(str(resDir / f"{picName}.png"), region=(win.left, win.top, win.right, win.bottom))
    # return pyautogui.locateOnScreen(str(resDir / f"{picName}.png"))
    res = pyautogui.locateCenterOnScreen(str(resDir / f"{picName}.png"), confidence=0.95)
    logging.info((picName, res))
    return res
def clickElement(picName, sleepTime):
    res = searchImage(picName)
    if res:
        pyautogui.click(res.x, res.y)
        pyautogui.sleep(timeScale * sleepTime)
    return res
    
def CheckMenuState():
    for picName in stateIndicators:
        if searchImage(picName):
            return picName
def selectExpertMap(sleepTime, loadTime):
    if not searchImage("expert_selected"):
        clickElement("expert", sleepTime)
    while True:
        for tileNumber in range(6):
            eventBonusName = f"{eventType}\\{tileNumber}"
            if clickElement(eventBonusName, sleepTime):
                clickElement("easy", sleepTime)
                clickElement("standard", loadTime)
                break
        else:
            clickElement("expert", sleepTime)
            continue
        break
def getMapName():
    while True:
        for mapName in mapIndicators:
            if searchImage(f"maps/{mapName}"):
                return mapName
def selectGameScript():
    mapName = getMapName()
    with open(f"maps/{mapName}_easy.ahk", 'r') as file:
        script = file.read()
        script = 'timeScale := 1.0\n' + '\n'.join(script.splitlines()[1:-1])
    with open("maps/tmp.ahk", "w") as file:
        file.write(script)
    ret = subprocess.run("./AutoHotkey_2.0-beta.7/AutoHotkey64.exe maps/tmp.ahk", capture_output=True)
    print(ret)
    checkVictoryOrDefeat()
def openBoxes():
    sleepTime = 1
    clickElement("collect", sleepTime)
    win = pyautogui.getActiveWindow()
    while not searchImage(f"{eventType}\event"):
        pyautogui.click(win.left + 685, win.top + 535)
        pyautogui.sleep(timeScale * sleepTime)
        pyautogui.click(win.left + 900, win.top + 550)
        pyautogui.sleep(timeScale * sleepTime)
        pyautogui.click(win.left + 897, win.top + 535)
        pyautogui.sleep(timeScale * sleepTime)
        pyautogui.click(win.left + 900, win.top + 550)
        pyautogui.sleep(timeScale * sleepTime)
        pyautogui.click(win.left + 1190,win.top +  535)
        pyautogui.sleep(timeScale * sleepTime)
        pyautogui.click(win.left + 900, win.top + 550)
        pyautogui.sleep(timeScale * sleepTime)
        pyautogui.click(win.left + 950, win.top + 930)
        pyautogui.sleep(timeScale * sleepTime)
def checkVictoryOrDefeat():
    sleepTime = 2
    while True:
        if searchImage("defeat"):
            clickElement("home", sleepTime)
            break
        if searchImage("victory"):
            clickElement("next", sleepTime)
            clickElement("home", sleepTime)
            break

if __name__ == "__main__":
    try:
        pyautogui.getWindowsWithTitle("BloonsTD6")[0].activate()
    except:
        pass
    main()