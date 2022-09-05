This repository ported main AHK script of [btd6-ahk](https://github.com/Valokoodari/btd6-ahk/) into python script, using pyautogui. I ported this to python script because AutoHotkey's default imagesearch do not work well on my computer, even if I set screen resolution as 1920x1080. It is still questionable why imagesearch works on some computers and not on others, with same image and same setup.

You can set logging level into `logging.DEBUG` or `logging.INFO`. Former gives more information to you.
Since pyautogui do imagesearch using opencv, you need to install opencv. I set confidence level of imagesearch to 0.95. Imagesearch worked well after porting this to python script.

Refer to [line 223 of pyscreeze/__init__.py](https://github.com/asweigart/pyscreeze/blob/b693ca9b2c964988a7e924a52f73e15db38511a8/pyscreeze/__init__.py#L223) to see how pyscreeze(pyautogui) matches image on screen. 

# Setup

## Anaconda3

You should install anaconda3 first. If you aren't familiar with anaconda, please refer to some tutorials.

```
conda create -n pyautogui python=3.10 -y
conda activate pyautogui
pip install pyautogui
conda install opencv
pip install pillow
```

## AutoHotkey v2

- [Download](https://www.autohotkey.com/download/ahk-v2.zip)
- [Documentation](https://lexikos.github.io/v2/docs/AutoHotkey.htm)  

I intended to download ahk v2 file and unzip into same directory with `bot.py`. You can change autohotkey directory by changing `ret = subprocess.run("./AutoHotkey_2.0-beta.7/AutoHotkey64.exe maps/tmp.ahk", capture_output=True)` on `bot.py`

## Requirements:

- Full monkey knowledge. (You don't actually need all, but I programmed it with all knowledge on.)
- Benjamin Hero selected
- All expert maps unlocked. (Not sure on this one, but better safe than sorry.)
- Game running fullscreen on an 1920x1080 display. (Changing the resolution on a higher resolution display might work)

## Usage

`python bot.py`
This automatically activate `Bloons TD6` window and execute script after 1 second sleep.

special thanks to [@Valokoodari](https://github.com/Valokoodari) who created original btd6-ahk repository.
