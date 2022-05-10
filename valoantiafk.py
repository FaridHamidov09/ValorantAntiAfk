import pyautogui as ag
import time
import keyboard
import webbrowser

time.sleep(1)
webbrowser.open_new("https://github.com/FaridHamidov09")
print("""
██╗   ██╗ █████╗ ██╗      ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗     █████╗ ███╗   ██╗████████╗██╗ █████╗ ███████╗██╗  ██╗
██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝    ██╔══██╗████╗  ██║╚══██╔══╝██║██╔══██╗██╔════╝██║ ██╔╝
██║   ██║███████║██║     ██║   ██║██████╔╝███████║██╔██╗ ██║   ██║       ███████║██╔██╗ ██║   ██║   ██║███████║█████╗  █████╔╝ 
╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║       ██╔══██║██║╚██╗██║   ██║   ██║██╔══██║██╔══╝  ██╔═██╗ 
 ╚████╔╝ ██║  ██║███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║       ██║  ██║██║ ╚████║   ██║   ██║██║  ██║██║     ██║  ██╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝
                                                                                                                               """)
print("Coded by FaridHamidov09")
print("Press f7 for start and press f8 for stop")
stopstart=False

while True:
    if(keyboard.is_pressed("f7")):
        stopstart=True
    if(keyboard.is_pressed("f8")):
        stopstart=False
    if(stopstart==True):
        ag.keyDown("w")
        ag.press("space")

