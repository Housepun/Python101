import pyautogui as pg
import webbrowser
import time

url = 'https://www.google.com'
webbrowser.open(url)
time.sleep(2)

pg.write('The Silence of the Lambs 1991',interval=0.65)
time.sleep(1)

pg.press('enter')
