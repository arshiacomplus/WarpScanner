import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import os
import ctypes
# import sys
import base64
# from playsound import playsound

import urllib.request
import urllib.parse
from urllib.parse import quote



import requests

import re
# import socket
from concurrent.futures import ThreadPoolExecutor
import threading
import time

import webbrowser

from retrying import retry
from requests.exceptions import ConnectionError

import random
# import subprocess
import json
# import sys

from icmplib import ping as pinging
import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey 
wire_config_temp=''
wire_c=1
wire_p=0
send_msg_wait=0
results = []
sorted_results=[]
save_result=[]
save_result1=[]
best_result=[]
WoW_v2=''
isIran=''
max_workers_number=0
Cpu_speed=""
best_ip = 0
do_you_save=""
best_result_avg=""
i_ip_scan=False
is_sub=False
is_v2ray=False
check=""
def focus(entry):
    entry.focus()
def check_ipv6():
    
    try:
        ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php',timeout=30)
        if ipv6.status_code == 200:
            ipv6 ="Available"
    except Exception:
        ipv6 = "Unavailable"
    try:
        ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php',timeout=30)
        if ipv4.status_code == 200:
            ipv4= "Available"
        
    except Exception:
        ipv4 = "Unavailable"

    return  [ipv4,ipv6]
def Check_for_update():

        
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("https://raw.githubusercontent.com/arshiacomplus/WarpScanner/main/windows/NewVersion.txt", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("https://raw.githubusercontent.com/arshiacomplus/WarpScanner/main/windows/NewVersion.txt", timeout=30)
                return response.text

    output = file_o()

    print(output)

    if output=="""vdiv
""":
        return [False, output]
    else:
        return [True, output]

    
def start():
    global check
    t=0
    for _  in range(5):
        if t==0:
              sp_label.config(text="Check for ipv6 and ipv4 availability ...")
              root_splash.update()
              check=  check_ipv6()
              
        elif t==20:
            sp_label.config(text="checking images...")
            root_splash.update()

            try:
                with open("mahsa.png", "r") as img_f:
                    img_f.close()
            except FileNotFoundError:
                sp_label.config(text="Creating mahsa png...")
                root_splash.update()
                with open("mahsa.png", "wb") as img_f:
                    image_da= base64.b64decode(mahsa_img)
                    img_f.write(image_da)
                    ctypes.windll.kernel32.SetFileAttributesW("mahsa.png" , 0x02)
                    os.chmod("mahsa.png" , 0o4444)
            try:
                with open("nika.png", "r") as img_f:
                    img_f.close()
            except FileNotFoundError:
                sp_label.config(text="Creating nika png...")
                root_splash.update()
                with open("nika.png", "wb") as img_f:
                    image_da= base64.b64decode(nika_img)
                    img_f.write(image_da)
                    ctypes.windll.kernel32.SetFileAttributesW("nika.png" , 0x02)
                    os.chmod("nika.png" , 0o4444)
            try:
                    with open("profile.png", "r") as img_f:
                        img_f.close()
            except FileNotFoundError:
                    sp_label.config(text="Creating profile png...")
                    root_splash.update()
                    with open("profile.png", "wb") as img_f:
                        image_da= base64.b64decode(profile)
                        img_f.write(image_da)
                        ctypes.windll.kernel32.SetFileAttributesW("profile.png" , 0x02)
                        os.chmod("profile.png" , 0o4444)
        elif t==40:
            sp_label.config(text="checking setting...")
            root_splash.update()

            try:
                with open("warp_setting", "r") as f:
                    f.close()

            except Exception:
                sp_label.config(text="Creating WarpSetting ...")
                root_splash.update()
                with open("warp_setting", "a") as f:
                        f.write("1")
                        f.write("\n")

                

                with open("warp_setting", "a") as f:
                    f.write("2\n")

                with open("warp_setting", "a") as f:
                    f.write("2\n")

                with open("warp_setting", "a") as f:
                    f.write("2\n")
            
        elif t==60:
                sp_label.config(text="loading ...")
                root_splash.update()
             

            
 
        progress["value"] += 20
        t+=20
        root_splash.update_idletasks()
        time.sleep(1)
        
    root_splash.destroy()


root_splash=tk.Tk()
root_splash.title("splash")
root_splash.resizable(False,False)
root_splash.geometry("500x500")
root_splash.geometry("+200+100")

splash_img="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KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA//Z"
mahsa_img="/9j/4AAQSkZJRgABAQEAYABgAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcgSlBFRyB2OTApLCBxdWFsaXR5ID0gODIK/9sAQwAGBAQFBAQGBQUFBgYGBwkOCQkICAkSDQ0KDhUSFhYVEhQUFxohHBcYHxkUFB0nHR8iIyUlJRYcKSwoJCshJCUk/9sAQwEGBgYJCAkRCQkRJBgUGCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQk/8AAEQgD9QQAAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A+qaKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFGKACiiigAooooAKKKKACijFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFGKACiiigAooooAKKKKACiiigANFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRiigAooooAKKKKACiiigAooooAKKKKACiijFABRRRQAUUUUAFFFFABRRiigAooooAKKKKACiiigAo70UUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFGKACiiigAooooAKKKKACijFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUE4FABRketJuFU9S1ex0mBp766it4153O2KVwLuR60ZHrXlGsfHzRrO9aCxt3vY1GPMU4BauX1n47a5dxFNNggsyTkORvYD+VFx8rPf80ZHrXzLF8Y/G0Eyu+oQTIDkxtAoB/EVs237Q+txD/StItZP+ubEfzouFmfQOR60ZrwST9qC2sSv9oaJNGrHGUbNdJo/7SHgjUwqyXMlo57SLwKLiser5oyK5uw+IXhbUlBt9as2z0HmAGtC68RaTZoks1/bqkjBVO8cmi4GpRTEkV0DKQQRnIp24etMBaKMiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKMii4ATgZNU9S1Sz0q0kur64jt4E+9JI2AKzvF3i/S/Bujz6pqlykUUSFgpbBc46Cvi34ifG/W/iKktvOxt7US5ihjJCquO/qaVxpHunj79pWxshJp/hCIX9yQVa6fiOI+o9a8el1nWPENy13rerT3Ujnd5bMdo+grzW3nuYhhJePY1eg1W/j5EtQzaMdD0SMKBhMYFSM4RclsV5+Nf1LH+v21FJqFzOP3tw7evzUi7HZ33iC3tUIQiSQfw54/OsSXxXeOxKrGq9hjNYavkfeBoLDpmmHKXL/AFWbUUVJwmAc8DFUNnsKeSg6kfnTQynpQLlHJNLFjy3dcejYqWXVL+dAj3tw6joC5/xqA4prFE5ZgPrRcVkep+Cv2ivFXhG2hsrsR6paRDCrMTv9vmr2H4e/tA6b4tvXGpvBpYVABE7dXJ65PbHFfJWVcblYEVFICMODjHAxRclxR+iZ1qxFk96LmNrdF3mQNlcfWrkNxHPGskbBkcAqw6EV+e1t468Q2WlS6VDqk/2OUgtEW4yCD/MD8q91/Zz+Nlxe38fhDXp1O5SbSZzgluuz/CqRm42Ppiimhw3SnVRIUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRTJZkhUs52qBkk9AKAFMigcnHavOfin8atB+G1pJE86XWq4/d2aNlue59BXkH7QH7SBglk8M+EpxvR1ae+U5KMjB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4T45eCZ/Hnw7vLKxiEuoWzLc24zyxUjcv4rn8a7rmpojg9Mj09a2pT5ZXMa0eZWPzYnge3kaKVGSRCVZWGCp9DUNfTP7SvwYKvL400KD92+PtlvGvQ/3xXzS6hfWvZjNSVzx5Rs7DKKKKokKKKKACiiigAooooAKKKKACiiigApc0lFABRRRQAUUUUAFFFFABRRRQAUUUUAFevfsw6ToWr/E21j1wRSBI2e2hlHyySjp+XWvJoIXnkSONWd3OAqjJJ+lfS/wH/Zv1yHVdO8Wa9M2nR20izw2w/1kmOQT6CgD60iiRIwiKFUDAAHQVIOBikUfKKWgAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigApGOKWobovsbyxlgpxnuaAPk/wDbO8VRT6npXhuJ8yQIbmVf7pPC18xHg12HxXutavPiBrc2vq6XzXLhkboqg4UL7Yrjz1oASiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKUUALSUGkoAmjfauKR231FS5oAKKSigAp68qQaZSg4oASiiigAooooAKKKKACiiigAooooAKcKbThQB9BfspeLRDqd/4WuJMLdp59uCf416j8R/Kvot0dHK88V8H+CfEc/hPxRp2sW/37aZXIJxuGeR+VffsEsWo2lvfRYMdzEkykdwwBH8683GU7PmPSwdS65SCF33dyKvrziokjA7VKOK4DvH0ZFGaTvSd+gh2cipIhk/SsvXNcsPDelz6pqdwkFvChY7jjdgZwPU15Z4C+J2v+OfGy6q0aaZ4Sso5Q3mcecdpCsT65Oce1dFOm3qznnVSdj3JraG6tpLeeNZY5F2urjIYV8RfH74P3Xw215r61jd9CvpM28v/PNzk+Wffg49hX20uo2UemHU5LhFsxH53nE/LtxnOfpXxP8AHz4z3XxN1NNPtR5Oh2ErGGPvK/I3t+GQPTJ9a9KimjzarTZ5JSU7rikYbSRXQYiUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH0h+x78PrLXtT1PxNqNsk8enssFsHGQJSMs31A2/ma+wURQAAOB2r51/YnwfAuuDHP9qE/+Qkr6NAoAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACkKgnkUtFAHzt+1H8Gp/FNovinRLdWv7RMXMajmSMd/civjaRSjlWBBU4IPY1+p8sayAqwBB6g18ofH79mkWYn8UeDoHkUuXurEAfIDyXTHbPagD5doqWaF4JDHIjI6nBDDBqKgAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAFpKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKXNJRQA4Egg5r7n+Bmv/APCSfCvRpi7SS2qG0kJ/vIcAf98la+Fq9V+EHxo1v4dRSabbWKajp80gkeA53Ke5UjoTWGIp88LG1CfJK59nAGlyK4/wv8VPD/ia3haSSTS7mQZ8i8GzJ46E4B5I7/hXYAKx+Ug59DXjyg46HrxqqQcnpXMeNfiR4f8AAVi9xqd2sk2CI4I+XdvSvO/iv8cb3w/fSaBoGnSteH5TNNGRyf7o7ivN9N8Itan/AISv4h3rOka70tmbLO2eAffvit6dG+sjKrVb0idAV1b4r6g3inxjcNpnheyy8VqW2iQDkDHf3qtf61c/FDUl0Dw8yaH4RtMtPcn92HVec/8A1qgtm1D4tyS3l/INC8GaWCzBTtMoXnAz1OOv5dTVSw06/wDipc3WmeHoP7I8LadG58xAQ02BkKfUn07Cu2KS3OWTutCP41/GhdWsrPwh4WupRounwJbvMDta4Krt/Lj8a8PLE8k06UnJHOM96jrqSS2OJvXUUHmny8uTTBQSSaYgNJRRQAUUUUAFFFFABRRRQAUUUUAFFLQRigBKKKKACiiigAooooAKKKKACiiigD7I/YnX/ihNbb/qKEf+Qo6+jB0r5h/Yt8QWEXh7W9EeeNL03ouVjLYLIUVcj8U/Wvp1TuAPrQAtFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAU1kDAggEHqDTqKAPmr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5NeLWg4ysz1qU1JXGBeRzivLf2ldV+w/DuGwV9jX9ym5c/eVfmP67a9VA9OtfO37Vms+brOj6MmNltA05+rnp+S1eEheoicTO0DwU0lKaSvaZ5IUUUUgCiiigAqWFsNg9DUVL0oAkmi2nI6VHU8UwI2PSzW20blPFAFaiiigAooooAcnWhhyaTNK3rQA2iiigAooooAKKKKACiiigAooooAsWVxLZ3MNzC5jlicOjg4KkHII981+mnhLXoPE3hzTtYgIMd5bpLgdiRyPwNfmIDivtv8AZG8VtrXw/k0maQvJpkuxR3CHkf1oA94ooHIooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACsfxJ4T0fxbpz6frWnwXls4OUdenuD1B+lbFFAHzhr/7Gfh+81Az6RrV5YWzHJgZRJsHoD1/OvDfjF8CdY+FLR3Lzrf6XO+yO5UYIPow/rX6A4rm/Hvgyx8c+GbvRL9QUmU7Gxko3YigD80MGkrf8b+FLzwX4kvtEvkKyWshUEj747MPqKwKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACl6UlLmmgOz+F/xBuvh/4lt7+N3a0dgtzD2kQ9ePUV9oLcQXdvDd20wmgmRZEkHRwRwfxBr8/QeRX0r+zd4/m1XT5vCV65d7NDNaux58vIyn4E5+hNcWLpXjzI7MLVtKzPbl5YD1OK+Qfj9qv9qfE3VCDlICsCj02jFfXSvsbJ7c18Q/EK8OoeNtbuj/AMtbyVv/AB41lg177Zri37iRzppKU0leiecFFFFABRRRQAUUUUALmpBcNs2nkVFRQAUUUUAFFFFABT2+7TKdnjFADaKKKACiiigAooooAKKKKACiiigAr6F/Y11p7Xx1faWZCI7u1ZwvqyHP8ia+eq9T/Zn1Q6V8YdDYDP2hntsf76kUAfoCOlFA6UUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUhHFLQaAPm39rb4US67pcXjPSYN91YJsvUUctCOQ//Aec+30r4/ZCvcV+pd1aRXdtLbTxrJDKhjdGGQykYIPtg1+fXxw+Fs/wz8Vy20YdtOuCZLWQ/wB3P3fqKAPN6KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAFrofA3iibwl4nsdVhYqIpBvweqnqK52nChx5tGNO2p942moW+q6al9auHhmi8xWXuCM18N61IZdVvHY5JmY/rX0j+z34mOoeBdTtbiTLaUrsqk8iPYT/Q180XziS8ncc7pGOfxrmoQ5ZM6K8+aKK5pKU0ldJzBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABSjpSUooASilpKACiiigAooooAKKKKACiiigArvvgQ234v+E8Zz/aCf1rga7z4Ff8AJX/Cf/YQj/rQB+jA6CikX7o+lLQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAHpXhP7XukwXfwtbUGVfOs7uHYcc4ZtpFe7HpXz5+2Tq4tfh/Z6cHAa7vUJX1VQT/ADoA+LqKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAClHWkpQcU0B6N8GvEg0TU9bspJCsWo6Rdwj08wQsy5/I/nXnbnLE+tLHO8Tbo2KtgjIPOCMH+dMJzUpW1G3cM0lFFMQUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUALSUUUAFFFFABRRRQAUUUUAFFFFABXe/Aj/ksHhP8A7CEf9a4Ku7+B1xFa/FnwtNM4RFv48sTgDrQB+jI6CikB445paACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK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SJUXBXBrgZ5vEyKY3W7UdMEGsS6huw/79X3n+91ranh2vtHPVxEduU03ttKj+Yzgj0qvNc6VGjeXEXbHGazpLOdRuKHFVT1wa64w8zzqla+lhWIJJHHtSZpKK1OYKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAClB4xSUooASiiigAooooAKKKKACiiigAooooAKKKKACiiigAqzYX02m3cV3bStFNEwdHU4Kkd6rUUAfoH8AvicnxI8FxyTSZ1GyxBcg9SccN+Neo1+fHwD+JM/w78c2sjNnT79ltrpCcDBYAN/wEnP51+gkUqSxLIjBlYAgjuDQA+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACgjNFFAFLU5LWCwuJr0xrbRxs8rSfdVQMknPtX5n+KLq1vfEWqXdgmy0mu5ZIVxjbGWJUfgMV+mWr6Xba1pd3pt4nmW13C8Eq/3kZSpH5E18OfHD4AX3w0xq1jO19o8rld+3DQkk4Deo96LAeNhsHNSLcyJ913H0NRshXrTaBptbFr+0boDHnyY/wB6n2GqXGn30V7C5E0TB1Y84IqlSilZFKpJdT0JPjb4qVQv2zGPRQM1QvvijruoAie6kOfQ4rjCaBU+ziWsRNdTbm8XanLnNw/PvWVPeS3D75ZGdvUmoTSVSilsRKpKW7JTMxHLN+dRnk0lFMgWikooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAHq+0gjIIORX3T+zH8TE8a+CU0y7n3arpQEUgY5Z4/4X/mPwr4Tr0v4C/ENfh58QLG9uXI0+5zbXQB/gbo34Ng/hQB+hNFQ211FdQpNCwkikAZXU5BHrU1ABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAARkEetYvi3w1aeK/Dt/ot4iPDdxNH8w6HHB/A1tUjDIODigD8xPFOgXXhjXr/RrxGSeymaFgw64PB/Gsevof9sPwZ/Zni+18RwRkQ6jEElIHAkXj8yK+ecUAJRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABTw5HTg+tMooA+rP2Z/jxZWunx+E/E195To220nlbjB/gJPvX1KkyuFK8hu4r8sVkZGDKSCOhr3b4WftT6/4PtodK16P+2NPiAWORziaIdgD3/GgD7borzbwZ8fvBHjGGPydUjtbh+PJuDtYV6JFdRToHidZEbkMpyDQBLRSBs8UtABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRQKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACg8iiigDzL9oPwYnjD4aanGsQe5s0N1Ecc5UZP6A1+fbDGR3BxX6l3UMc9vJFMgeN1Ksp6EEYINfm58T/Bk3gLxxq+gSq/l21w3kM/WSEnKN+KkZ98jtQBylFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABS5pKKAJEmeNgyMysOhBwa9F+HPx28W+ANQieO+lvrIECS0uHLKw9vSvNqUHBzQB99eBP2kPBHi+3iEt7/Zl6R88FxwAfZuhr1G01C1vohLazxToRndGwIr8thIykFSQR0I4r3v9knxFrF18S102XULiSzNlK5hdyVyCuDg0Afa1FItLQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUADDIrxr9oT4KJ8TdIhvdNSOPWrPhHIx5yf3SfY9K9lpNooA/NHxF8OvFHha7a21PRL6Jx0YRFlYeoIrAe2ljba8bofRhiv1Hnsra4GJYI5BjHzKDxWXL4I8NTsXl0LTnY85aBSf5UAfmTswBTSMdq/QjxX+z38P/FRaS50WK2mfjzbX9236V86/FX9lXWPCcEmp+G3l1WyU7mhx+9jH070AeAUVLPA9vK0UqNG6nBVhgio6AEooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAr2v8AZFJHxdjx/wA+M381rxSva/2Rf+SvRZ/58Zv5rQB90ClpB1NLQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFHeiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooACM0jIrLtYAg8EGlooA8o+Kf7PnhX4gwS3EdtHp2rbTsuYF2hj2Djof518YfED4aa98OdUNjrNqyAnEcwHySD1Br9JiAa85+Ovw4T4i+BL6yt4lOpQIZ7Rscl1525/2gMfjQB+eRpKnu7eS2uZIJY2SSNirKwwVI6gioTQAlFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAV7V+yMM/F2L2sZv5rXite1/sjEf8Ldjz/wA+M381oA+6BS0CigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii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qStLxFYtpuu39mQQYZ3TB9jWbQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFLijB9K7L4c/C7X/AIl6r9i0q3IjUZkuHBCIPr60AcciMzhQDknAGK+nPgL+zR/aSQ+I/GVofs7jdBYv/GCDhm/POK9B8A/sp+FPC80N9q5l1e8jIcJJ8sStnI4HX8a9xiiWJVVFCqowAOABQBl6T4T0PQolj03SrO1AXb+7iAOPyrWVFHG0D6U6igAwKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACmsM5p1BoA/PP4/6A/h/wCKmtQbNiSy+egHcNzmvN6+lv2zPCU8HiTSvEkULG2urf7PK4GcSIcjJ7fKwx9DXzVgk0AJRS4pKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKANvwl4dn8V+I7DRbY7ZbuZYw390E8mv0a8G+D9L8GaLa6XpVpFbwwoFJUDLkDqT3r4w/ZS0mLUvivaySruW2hklGR3HSvu7GKADFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAGX4i8N6b4p0ubS9WtIrq1mXDI4z+Xoa+Y/Fv7Gtx9omn8O6qpiLErFOOQPTNfWFBGaAPg7VP2WPiJYO3kWEV2o7o/WuE8R/DLxf4Th8/WdAvbOHOPMdMr+Yr9K9tVr7TLXUrZ7a8gjnhcYZJFDAj6HigD8ttpoxX2F8RP2QtP1rUpNQ8L36aYsgJe1dNyBv9n0rj7P9i3XZCBc69aRL6rGSTQB824oxX1Ev7E1zjLeKowf+vf8A+vXP+Jf2PPFWl27zaVqFtqW0Z2Y2MfpQB8+0lbviLwV4g8K3JttY0u5tXHOXQ4P41iFSKAG0UuKXaaAG0UpUikoAKKKUKT0oASineW2M9qQjBwaAEooooAKKKKAPpH9jDR2m8VapqZU7IbcID7k19h18/wD7HGgiy+H13qrAh768ZRkfwoABj86+gKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKADFGKKKAAikK564paKAM/UtA0zWYjFqNha3aEYxNGG4/GvMvFX7MPw/wDErNKlg+mzMclrRto/756V67RQB8xz/sU6e1yzQeJ50hJ+VGgBIH1zV/U/2MfDcmnqlhrN9DdjG6WTDKfXivo2jGaAPijX/wBj/wAa2LO2m3NjqC5+VQ2xiPfNcjqn7N3xK0vHmaC03/XCQPiv0E20bRQB+dUXwK+IcsgQeGbwEnHK8V1mjfsn/EPUJUW7t7OwjYZ8ySXdj2wK+6NgznFLtoA+VX/YxYeHvk8QZ1cZPKfujxwvr1714D43+GfibwBdeTrunvApPyyr8yN9DX6Ubec5rF8VeDdG8Z6XJpms2iXNu46MOVPqDQB+ZG33ptfVXjb9jJnlkuPCetIq4JW1vB1PoGHT8a8K8YfB3xr4HLNrGh3CQAkC4iAkjYA4zlc4H1xQBxVTW1u9zcRwxjc8jbVHqaa0LKcEY+vFeu/s2fDW48a+PrO+ubZ20rTGFxO5X5WYconvlsZ9s0AfZXwz8Lx+DvA2i6KsflvbWyeav/TUjL/+PE11NNVcY9qdQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAJimS20U6GOVFkRuqsoINSUUAcrqPwu8HarcNcXfh7T5JmOWfyQMmtrSNC07QrQWmmWcNpApyEhQKP0rQooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA//2Q=="
nika_img="/9j/4AAQSkZJRgABAQEAeAB4AAD/4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAQwAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAAHRyWFlaAAABZAAAABRnWFlaAAABeAAAABRiWFlaAAABjAAAABRyVFJDAAABoAAAAChnVFJDAAABoAAAAChiVFJDAAABoAAAACh3dHB0AAAByAAAABRjcHJ0AAAB3AAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAFgAAAAcAHMAUgBHAEIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhZWiAAAAAAAABvogAAOPUAAAOQWFlaIAAAAAAAAGKZAAC3hQAAGNpYWVogAAAAAAAAJKAAAA+EAAC2z3BhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABYWVogAAAAAAAA9tYAAQAAAADTLW1sdWMAAAAAAAAAAQAAAAxlblVTAAAAIAAAABwARwBvAG8AZwBsAGUAIABJAG4AYwAuACAAMgAwADEANv/bAEMAAgEBAgEBAgICAgICAgIDBQMDAwMDBgQEAwUHBgcHBwYHBwgJCwkICAoIBwcKDQoKCwwMDAwHCQ4PDQwOCwwMDP/bAEMBAgICAwMDBgMDBgwIBwgMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDP/AABEIAzQCrQMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APyT86SWXy9o2r0PpVoXEcSeWWOe46AVZS289dqx7QB2qlPpsVs3z5bPJwc149jq9CGW6YBgnPqR2ptpq7QNj7w9KJLRmT93lV/nTLS3aI/MF/GixPNbUstqpcn5fvdq0LHw/Nfp9okXC9snmoNNsBeSAbBweTW41y8Nv5Ssvy+9SPmvuZjSR5Me4nbxmqdxE0khWP7o9quyxx27Fm2+pAqtPrKFNsa7V7k0xc1im0XljDtgelQ70t++O3A5pL++BcbW/Kqcly5Rtob396drk9SLUr/LddvoPaqqW/2hyyhvx71MbMSNvYr+NOlmWNQobPbirC41Z1hYbhv9c9KNQ1P7XHjI6bQoGKE/0iQLtCrjqamvo7PTY1/frK5/hUdKtC6mStpMx+XoOfpTTbqrfN1HNWG1AyS7VDAfzpssm0ZZvm6YqhFeSHzGxtO0etXbWJbWBpGUNxyW7VArkqdwLUSXTXKeW3yrngUbgNmvvtb43deOKqvYM0mVP41YSBYT2HvUovRYj5V8wnvijzKv3JNP0tYVDSZ6ZPvUt1dKg/dr83QZrNuNWluj/EuKmtr3EfzAs3rVahzIniKs+XJGKg1UrMy7WJx1zSNLJMVPXPTFPuLeSbbuX5vWqJK6bI/mbv8ApUzaj8gVVBCjrTjp29d0kiqF7VE1xb2q/Ku7vzRysCdby5lVm2k5qS31mWDg7enfmsy61qab5V+VcdBVYTu7bfWizE/I27vVFn5aQs38qqS3i7uF+7VVJB029epNSrCWj3Y+uaA5iSZjcR5bb+FbfgL4XX3i15tRnjkh8P2Qze3R+VQvXap7sfSsa1RftUZuFb7Opy2Op+laV18QNU1DSv7NW7mh0mMnZaA4jGe5A6n60ItbajPGupabqWsyR6JbNY6VEojjjZtzSEdWPuao2P8AoHzKNrA5U+lQyTRxxfKOVpLaNp1DyHbHjPPepKua2kabHqVy15fSbokO7n1qh4o1U6te7Y+UByMdhTLzVmvrdYY8osfHH8X1qCG4WylVtoZg2cetVysOYSDSGW3eab7sZ6mq0939phWNcBF6AVptqEms6bcN8sbKQdvqPashwIhtXt1oSJlIbIyxLjPzUWmlmR9zHC9adY6c1zKpb171vLYqiBflodgT1K8Mfpwq9M0tyyyDCjc3X8akuQxbZGvfAq/bx2uk2ZeRlaXHCGpe40ZYRolzLnkfKKq+Wwfc3yqavxK11cedL3PA7VFezK7BQBjvQhS7k1jbLOd2cbenvU3iO/LwwwhlYDpgdKj0lCWPTb61DKizagc/dWjqEdixpFqrou716VsTwLaw+Z09AR1rLhiYThl/hq9PM0kKrJzkflRIE2O0oLcytJJ25A9a0LicGBcDvnNZcK7XDfdUDnFTLcb327vlzxScdQQtxdMU2/eOeAKZHBsT5uM81YNuPN3DHzDj2ptzcrBHnglelKxXMV7uRdm0H5u49aqwmQBt3QnAFanw80v/AISPxfGkpyrAmofFkf2DxHcQJgLC3QDii2tiulxEkUIqk8t2qpf3LK22Phzwox196kaeO0XzZBxjGPU1L4fsWlc3Uxxg5QHsKHoNana/Cmz03wP4U1rVL9oY7xbfFqGPLueuB6151YTya7qDyyL80jFs49an8b+JP7cuIbeMBY04IXv71reFdLXyUZvl4rHkt7zG6l3yo1tLVbSz2/N/Shpyz8NyxwMUt3cKsixjp3rpfhv8P38Wagp2SeQDkvjgVMmktS403J2Rr/Cn4fTeJ7xV8tvs4x5j4r3Gy1yPTLaPRbN1jt4z+9Zf4hXONq0fgTRV02xKedL8jMByRWXouozR6osK4kZ3ALe3eueV5anfGKjoe0eH7yGyso5rdf3anaT1z717L8MorXRLePVPLCso3PI33q8/+C3w7/4SuRBGr/Y4PmmkYcKR1q78WPiFBDrVt4a0128vdtaRB97FcNSonLkiehTpuMeaRqfGf9oCbxLfS2dnLu2jb8n9TXmi6NcQWMk0kbeZJ95/TNdN4b+Hsdhq7yXCsI25+Y43Gt74g31vD4d8q12qNpyD0NenhcPyq7PMxGJcnZbHE/D+w0XQ9Su5LwBrzyyUk6gH3r54+O9//aPxGlRis7Sn92q/Nya9H1fXGzJHbsdshIdj2HtXFeFPAbal4w/tK6RmRXJQt0PpXXKVjm1kd38IPAc3hzRbdfLw9wFZyF+7ntXU+INGY6vPcMvykbEDfeJxjNbPhN7iXam3ZDFgtLjjGK0NF0GbxV4gYMn+jw/OXPQAVyM2jocXd+fp+gR2NspVpvmkPavOvF1q7lYZ/vK25iegFe1+KLVYdRkhXy9pGS390VxHjzwustm37vyppsEM3SiLDqeWW3h9vFXiKCMrujQ7iMZ+UetemS+Hf7F0SzjXMcOHmYn09/yrJ8F6C3hyx1C6mZA0gEaH3PTFdl+0NqNr4N+BOiu0itqWqKsG3uEPU1ald2IlofLfjOT+2PENxMVHl8iPjqKy9G0mRbyKFR8q5aQkcYrrtUsYnhMkah2XA/pWI6vp9rNNn7w2CtIy0MLamJrkD3NxJJ13ttT6VsaNp8ejWTzNtHkxl3Pqe1OstIa6jjaZdscfzAnuaNahaDQZFflrhu3ZRWi3syTldKt21XXWupMHJMjn29K2rJjfNJcttVi21VHYULpn2HTo1VdrXalsDslT6GEbU1tY1yI4tzAfnVSIMK4sz/bPPVn/AEq9qyL5+3qigY+tO1+H7FK0oBEjEcemala0E1jDIfvbulTcRpaNb+UjttHyxnFGpIx09VbsQT6mtHw9a+dbqrffkBBwabrVt5j+Uv8AAcZPoKdxpXKNqGSK/CLtjEajp2JFEukC9tbeRGUFk+bnvWp4Ut49T0PVCyncu1QfXBzVbTbdo7TGCRuYgHtzU3LseerqPlxlY931zVC4uZye3HemxzbGxgMf5U5LdpVO7aN361nyom3Yh/tKROCxFTadO13cBQtQ/wBnHzP4mGema2NH0ZolLN+7XGfSh2Ijds0EZ4IWULtUjGaRJksoizDcx9Kpajrcduvlrlsd6qR3sl4Ny5Ue/ekkOXkW76YTBmKlfqay57pSv3tvtV0hnHzspH61QvbeNJdy/NQiRoKsex/CnTnzDtVePSpbCNWXlFx71JJdRxkqkalvWqHrYyJNFuLh++3rmn/2T5K/vG2+hq1NqDAkHj6GoJ70MP71F2TqRraQ4KtIx7ZFOj0G0Vd32hc9cE5NUpXZpPummNGynvVREWriGK1zhlZu1U5LveT+7/SnM207uOP1qGa9VvuqKoAa4bGelM8xX+834etQPI7txUZhLj5iwqkBaa6C9MHnvRJe5H8P4VWaPaAF+alEfO6jlAGm3/w4+tPFx5KbW+b1IpnlGQnd09qdHbKW+bjtVaCsINQZPudalFy5GZHPPbNRy2i7vk/HNA013+ZmqrE6jZb7Yu0fNUW17g7QtTrBFbMufnPoKne5VIvlUKaoZSWykZtvCjvVmOzhhXLHc386u6Ro91rZYxL8qjLM5wq+5pt/Db6a22S4WeVeoiHy/nRqGiKAEkrbVXao5p5KxEbm3bew9ajl1Es7f3fQVGjtOMLwvbNLoHmieeZpyA3HoBTcrjaW202YC1C7juf+VNt7dp8M3C9zU8rHfuWUs/tCEqq47k1DKJJ5dpPyrwoFNu9R2t5cbHHT61atl+x26tJ989Fp3LsMdlsrbYq/vGHJPaqEsjLIB1yOtWLy5DMzbuvbPSoYTvfhf0qgQJKyZ/2u1Ot9Oa4kzVyz04zN83H4Vq21msMXPyhf1qLroHKQWemC3izRdSYO1emcGnXt4qDCtmqFxdNI3tSBJ2Fe9No3y/e9fSqcYfUrrLMWOafITMenHrU9nOtngAZJ60wNGYfZbXntxWcLczP9T3rQvpw0I/2hmqts3O7+KkHoPlkWxg8vOGNVrV9s3dvrUdwzSXHPzHPHtVq2gwM/xdKA0Ltrd7H6Akjg5qWS48w7twz9arxwgH73brTTxMfbvQGxPI3l8Z4p9tOqnOOveo2RZcUKu373RelAdNC1cXu2EjP5VTMhnb/e9aa8hmlKr0PWplh+zx/3j/KkBteBPEcPgjxFDeTQecqg5UfxVn+INXTWtfur4R+Sk77gnXAq74Nu7K18SWsur25uNNVsSqOpFZfje+tNX8WXS6TBJb6fv/dITk4peZp0K0SHVr5t3+pXn8am1zVVtbXy42IK8YFNeVdJs9vy7sdKy7OJtVvt7crnmjclytsXPDWltezBmHuPpXaWkRit8Y2heMisvTYks4tu0KccH1q9pvm6ncCFWP71gMZrObKpxuzovBnge48a67b2kKl42PzMepr36+k0v4U+EYdKs9jTuoErnnBrjfCbwfCPwuzS+XLqNyuY8feGaZpvh268TxT6lcl/s+0uHkOFzXm1Kl3dntUaHKrLcqaxrkUUomml8yZugHavQP2c/hjeeP8AX/tTK32d2AD44H0rivhP8Gb340+M41j3LbW7YDj7jYr7Da+0v4D+DY7OBY4ZPLwrbQMHHWuHEY37ETuw+DfxyGfEH4j2/wAGfAP/AAj2lJturjiZh29ea8g8J6zGnif7ZPIssm/PJ+6fWub8VfEaPV/EVxcXVx5yNnZzyawofEUd2kkyfutx2rz1rbCYa3vvc5cZirvkWx7bq/xDa/1nZGftTOcKF7H8Kh8dXco0yMagy26vxgHmvIR8TX8KvGtmYmusDGeSKvxeMNR1BPtGuTeZuO5UA6CvbpysrM8mSuLLbwS6jJMy+XZr0Un73vVjRNYa812FVjWO3Y7YYwfvGue13xVHIzzSMFt1GAoHWk+A+sf8JH8SVuLv/jxgzsGeFx3qJNN6FqyPpCTWbXQfBlrYrCiSykNLJ6CtjRfEK6N4FaMQjzdQkBV8Y+XvzXmHivxDH4g1k29tJtWNxGu09SeK7v4k+I7Pwn4PtYR80kdvsGB0YisZG3TQ4vxPqEf224WFmaZiTn09qj02zv8Ax4ITMm21gG1mIwCB1rm9H1KS+vYm+9M7ZXPTOa9f8d6Evg74bWtrbzR/arqISOB3ZucUcpmzgrrwRH4i1aCxtNi+a4iReiqueWzXmH7W2uw6p8Tm0SCfzLbQ40gTnjIGMivW7rVf+EQ0SfUm2mSxtcIT3kPTFfM94bjWNXu9UvpN9xeSF3JojvcUuyIZwbSzbb/D3NV7nRhq8lnayNtX77n2rasbUzWi/aF4ZjtwOpqxdaPIJWZV+WNMtxyxrZMgrzaZDrutQ28SGO3h4OO4Uf8A1qxdf0p9V1D7LHGyxysVX2UHrXo3hXwzLZfDm/1iSPbNcMIYM+nc0aLpDvoUM9xH9nlu820BYche7D61V+ply9Dy9bSKSS7udu6G0i8oEnt0qt4b0abQPD1/qMkOJtSPlwBuoT1/Sui1bQho2nyRyNtt5JC0r452jt+NSPrMfia1sYVX5Y1ZkGOi5wBVc2grHn/iKVo5drH+Hn24rSsrPGk268u7DP0qLxNpu7VvKX5mY4GBWwtp9luYI1UttQZx60EPRl7RLPyvL67uvPTpUd+WmDY27uc+/atjTbbFtLzgovOKz3tmZkSNctJ/OgIpk3hqxfTdAuWPHmKSox973qGG3VLeNmHzOMnitZZd2lzQqDlVEX05BNSR2EZwvTaqgjHQ4rPqbvY+e0ljbczcY9KhuLsgblOPx60iQK4+9+FW9A0lZ7r96Nq9smn0uc1huiiW4ustu2ity9eYx7F+VcdatfYY44MRvGoqs8Akk253L65rK5exQS1jQEs25s9Knhi85tse0VZj06NmO1B9c0y4vFs12oi57+1VzENalSexkibJbjpioJEjB+78x9Kt3GvK8W3yd3rVSS+QjIjO70x0ouSRNayTJ8nyqP1qu8GyTDH5q0Iz5/8AeUehpksaq5Hyn3o5hlSa2jhjOW+ZqovcxxN8vzYq9d6errncQ2emaoz6Y4+6vtmqTRLIZbvd0B61VkvXY4WrRsdh+ZttRyMijAUHnk1asIqkyOeaZIuGxip2uFBIXAoILc5BqgIWjZvu01rd6sRxNigwSKCSafMBVERU7utD+Yx4FTNFjvmmidU+8KOYCOOR1BGPrTkmKMO/t60rTqR8o5NJvbacL+NHMB6d8e9J8LweFPB1/wCG3Vrq+sANRgU/6iZeCT9a8vCyZ2lm561PaXU0UZG4t7HmmXKTSOWwR71rzXZGvQAkcS/NUIdQflX6ZpfKYrknNRmdQPlpj2JZLi4kh2vIRHnO1eM1R++Sqr171YeTeh3NT9H0i8127WCxt5LiZzgKgyTSK3I1gW2TLurFu1SxFgnH3evHauksPCtj4QZpvEEM0t4o/dWinGG/2qxrkDV7hltUW3LMfkzwopcwuUz2kjBbOWNQTX8kg8teFz0FXL7wffWsu0qrA9NrZq5png27lP7uMsyjJOOKOZFcpm2sK2zCWTrjgGkubmS9l+VTz0x2rWvfC9xbRiS5KKd2AM1JZQw2MBOd0jdBjpRzdRcttDIt9Jkll/efL3Oa0rSwSL5uD/SrEaNJ87L8ue9TNIiLgrnI7dql6lWIluFjXPU9vaqk91JMTk1YEWSx3YWq1xfKuVUDjjpQAki7Y9x61VkLFtxq1HEZF3SZ9ge9Muwu0ljtOOnrQV1KU9wdoxxU1jFvlXd61HGuXz19BU3mZOcbRQRrc0tQRYo029cc+9UZLrDenHQUktxgZZvu9KrW5N1Lux8uafQbZbtY97bquGI+X8oqSytxHDkjHepCFaQbenrSKIoYym4cmleNlx/tVLFIIpMLSzXSqc7gzfyoAYI1jC7ulVbm5MhKjIXtTpW8+T73SmxW4V/mP04oAk09Wg+Yr+dXtqyhWIBXvVVWZ48KMVXu79oY9kfJzg1PKGxJqurEt5cfA6VJpMH2O3e4k+83TPeq9haeSPMmPuM1Deai12zIv3R0xTsTtqR3ty+p3fA4JxxW9oumiyiztXJ9ap6HpSp+8bOTzzWsDnEa/wAXT2qZPSyKik9WOEzSzKu35elejfB74drrss1/fN9lt7ZSyswx5rDoBWf8HvhFe/EbV5FhX9zZr5s7dgo5Oa9avn0/WreG1tUWy0vSVy7Y/wBa4+9z+VedisRb3Yns5fhb/vJFHR/DL+KdYj1Cd44LW3BVFc8HH+NWIE1L4ma7Ho+lxvDpsEgWUAna/PaqeiHUPjv4pj0rQ7eSHT7X5ZpYxhSBXvug+HtN+DHh6OaNlV0QKysPmU9c/WvHrVraHs0qd9TZ8NWmlfs8+DFfbDHcbS20PytfP/xp/aXbxNLNDH80YJCEvnBrC/aE+Psmv3skMFwWjbKkZwTXjqzG5k8yToxHAatMHgXL95M48dmCj+7gddHr80kvmMwcH17UyfxpMGKqzccADtXNy6ixQqo+Vau+GbT7TMsk3yxrz9a9qK5djxHU5tWd38PrRpP9MvMtuO5Se9bN74sOoajtU/uo+orjNW8YfZrTarbVUYAHpVDSLy41QSMuVjxnPrVOTsGiN3xj4hW+lwp/1ZwFHQmrvgPxLLo8TGNvLLc/X2rlJIvMbhSeefWtrw+mZY4413EUeoWuz2T4K+frHjGG5nG1Y2DHJ+Umu2+KerLrnikWcLFi+Aqjnmub+GNmLFLdf7oMjNn9Kq+JvFI0HV5r8ssky58vHrWWp16HdWnhO38O6NGss0cl4SCyD7yjPWrninxAPEl7DFb75Gi2xIOu5uleU+H/ABhNqNk15NIxmuGJY55A7V6V8CNIm1sXPiGY4sdPDCNT/G9OTM47mb8er/8AsvwpbaTGq7kAaZjwQ2OleV+HvCi6neWqzjy7eM+ZKxHGPSu9+I0U2ua402oeZDDJLvAkG3d3GM1S82zisHTa0OCDwOo7VcUS46mOnhJtW1CS4gj8uztnIjJHWun1HwC2ieErcyIv2zUZvkTuy8YNdLqelw6Hp/hizhVW/tVxJP8A3lBqzqWsw3fjlSqiS30+Dy4wozmQ8D+dWtNSZFvRfAVt4vurPSVBjsdNQNcnHyLxk/rXG67pEnjLxTI1vGI9Pt2aC1IHCqOC1ej/ABh1EfCP4f6fo8LGPV/EmHn4w6K3OK5bxfeR/D/4YPqH+rWG3+z2wx95yOTVLUzZ8/8Ax+uIUuLfS9PUttkxIxP3hVXwtpqm+i+X93HDg46irNnZ77uO4uo/OkfqCM5Ymun8P+DvtD3cy5WO3jLMB2oUtSbdTzXWrL7LO1wvVcqvc9as6VGxu2+9lFH1q3rVlt1Doyxq/Ge/NaUNiLUqyqWa5PNBm43Lej2Cvpdw2C2QNxplhbi1mTaoIxgZ/hrovDelLLpF1/BuZRWU9osniN7WNvkhUFmoctDRLoVLWxWwsjj5mYFsnnk9K1NE8OTahbs6QyPz8xzjmpLjTS2nzTR7cKwRfcDvWp4c8RRaHokKrcKGkZnYHGRSRXKfHdujDLbmPHpV3R1ea9XMmFzUCuzPtUcY7VMHjgC4X5varfY5Vc7SOxsZ7Zd10u4ds9aabKxQfu5PMxXKWtw1xNtVMH1rds7NYVBeZY/x61m421AsXD/ZovlVRmqV85VMmNc46VZmv44D8gMh96h/tFrs4aDFCQmZ8c4R/wDVKM9qcbuANjb83sKvLZ25fcy/N6VDdNCiEbdv40XFqVXjWVsq23PrUE/lxL6n1qK8mAGenpg1RecynG75aOXqSyxLOvP3twp8d8XG0DjFUniIX5WyfemsXjH3qdkBNdWAuTw3PvWbd2Dxf/Wq4l/t43BqGv1IwWX6U1dFGXHprTP3/KnNprxDgn8avLckN8vHvUE0ryHOetVzhykEayRmnNvkXaxpGZ1bA+b+dQTvMjcqwHrTuTyu5NHZN3aiS1VT61Tl1Mxkdat2c/2obV57YNUHL0IA0Yfrgio7vUVj4XP1q9P4YeV9w+XdzTk8FSN824fQmnzR6hboZtnfM8qs33c1pXNyZ4Pl444q0nhQ+VtXrSp4baJxub8M0KSDldjJt7Z3Lbuh6Yqn/Ztzd3O1Efr2FdPHYfvNu4KK0LI29kefmZfwqucFFmHongGa+uY1mkWCMHLOx7V2mlfFKP4awG18M2Ma3mCrX0kW5x24z0rJv9W+1Hake1QO1V4oZZh+7TafpUylcpR7lO+ivtXvZLy+maa4kO52Y96ktNAhjZZZGMh9BV5dHkJ/eyZb0NSPpkiKN1xHGuegqQ0uUbiGRdxt1kGOmD0qW01PUrCHaZtik8jHJq2IpIyscLNJI3GAOtXtW+GPiSwsvtl1pd/HBt3bjEcEVXQNTmL57jVJQpUtT4NDaJdzL26Vvr4xs4tLitYNH8u4j+/O75LfhWRqmu+aDtXyyOOKqIpOxDLDtT94wUL2qjd3yw52+npUcxmuG3Ett96altyC/Ge1VZEavYhMs1zzUkNm0e1m5PepzJHAp3MPYCs+61zLYUYA7+tIrWxdu5/Ji3fePp6Vmxhr6Qs3SnedJcD0X1pxkS3XP4ACkPUGXyIz7dPeo4JGm5b5V604J9ofdI21RzVe9vt0vlxqSvSgevUSe7+0ybV7cVq6LafugNvPU1FoWgNPJnbx1JNb1zZLZINrDc3oaL9CoxInjzFtVu3T0qP5YI9vU1C87JJtB+tRz3LFgu39aB6DWvNpwv8A+ql37l7GmBNz/XrTiCrYXsKBCZ8s8datWcLTfe6VVQ7G3N19KnS983hfl+lAIkvZPJPlx89iaLDTliO+T5uec0IipmR/u5zz61n6tq7XTMseQo44oDQdq2refOUjxsHAo0XTzLMCV75NVdNsWu5lU/NzzXVWtotlDu4Bx0x1pN2DcYSbVF2464Naej6Y19MqJlpZDhQO9UbWE3U/Ee5scCvWPgl8ILzxbq0c1vhWiwSzfKsY7nPtXJiKypx1O3B4d1ZpLY674f2p8L2P2TT2mVp4QdQOMcf3c9hXN6rNefFfxsnhjwusjQyMFneNTtQZ55+lO+LPi1n12Hwb4JeS7vrhzHe3EfPmOeNoI7V9HfAH4VWH7NvgFZJoVXxBfR75ZmG4oTjjJrw6tTlXPLqfSRpp/u4bI2/DPgrRf2a/h6tvH5S3QQGRj94tjnJr5f8Ajz8eb7X9ZlijmVY2bK7M8DHFdj+0b8bpL7zoPtSyFDhsdCa+bdU1N9Zv2mkXv8pzU4PDOpL2kzjx+M9lH2cCSSaTVLppJj0PPvU6bQV2qxI6elV4mLDamee1a+m6UghDM3K847mveUbbHgq71YlnagLlhtDdQasTagtpFjoPQUoRSvQsxHyqKn1Lwz5WmrcXT7Cw+Vc9aXNqaxpuxnWjSeI79VX5YUOGz6V11wsFnpUcUA2qB6daxvA+kfbH3fdi6sfWn+KNU2Xfkw8qo4wOopSd3YuMeVXJBMsc6/xL6iu8+GmgqszXci5XHQ9q8/8ACVi2rXqx7W3M/PFexaBozWttBZp/rXPzAelZzmr2RVOm3qbF3qy6DpwaMspkXHXtXnXiTxTJqd6fLOI2O1c881ofGXxUthf/ANn2smcAK5B+761mWGlRDQre6VdwDYGeue5qtkOTuzc8HzTNdw2cSlppiEVcdSa+pBPp/wALPC+k6G0cfy7bm8weD/F/9avG/g94Vj0b7PqdxD/pdw2bfcOQo6tWb8Z/ii91r18zXJaRv3QXPQADrUrVlL3Vc2vj18Xbf4j+OD9ljjhs7M5VE6Z9KyfCsTeJdatLWZSouCWY56KK8v07WStrJM7bWkYknPWuw8EeIWtNOe4Vm+0OpEftW3qZ81zstf8AGrL4lkmX5k05DHCSfumun+A93Y28T69q/wC7t1lL4brM3QY+hxXjBv5dWvo4FZl+1Tje31Nd38Qb5dP8M29naOpt7MAEL1ZqNQOn8Y+L1+KnxTOvzyK1jY/ul/2R2Ao/a48W2us2/h/TbFVNrDEjzInAztBz9a4fwdeyJZx2u3Cz3CtIccY9KzPix4nWTx1dMj7reAiJV7Dtiq5tDOUe5vfDfwDN48g1W7tlVbbSI/MYnt3yfyqXRXX+w9Q8j955xK5AxnFXf7bvfhj8EJLLT3WO+8TNiYH73l1oaL4U/sjStPtGYFpYxI7f3QRmkLoeQalpbXfiD7DN8rmUHFd5beB/M1sLGqtHDHuJx34rBttAk1/45x2lqvmDcc474HWvTJNDktb9reNj5jMFYAdPrSuEYmd4g8Bt4espGzxNGsnHYmuL8O+GPMi1S8kjYL90FvpXtPi/TGj0xlvG8pVVVT3xXExWQg8FXCqPMkmlIOB1Ao5hnPXuhtp/gKBcHzbrLZ6YBNZXhrwzb31vIrZCxEKufzrovicfsXh9eWjW0QKAB/EQP8a1fA3hWSXw/AUi3MyBnOOpNVzAfCSXX8K/KtXNO09rhmb8yabo2ltctuk+WOtO8byY9seFVenvW0n0RxRI5JEsotsRy3cio0u1cZk+b61Xcu3JO33qJ5Fj4LbvwqUhSNA6kU+6i8dOalt9bI++236Vjb/NY7fwqSKxkK7mbH1NHKguXL3V3Y/u/wD69Zs2pSFyXbjHerMcawnPmDNWV0GHVcK1zHEx7miwjHllW5/iqpK/lHhq6HUvBEenL+7vIZ2H8INVBpqRcSLu+gzVCsYwu5s8ZoM0zjla05THAdqwsfqKrSybmO2PAp7gU9hUf71MkgZTk5Wra2plbP3ferCac10NqsGpOxSRlq7I33s+1SJfvnbt4+lbEfhXcNzZLela2jWNvYoPMs/OYeprNyRRR8Nz2jQ/vrdvOPQ4qxPpMcjEtgqT0x0rYW8tUHy2qxt2AHSo5TbzfMzbT0xUXA5+80PTynTB+lUYtOgtZP3dbWoWqyN8p3HNVWs0RfmdRV8wWHWzeb95mxTrq/W2T5dpqs75+VeFqKOJnk6Kfxp8qKVh8FzcPJuB257VdhiacBnPJqFSqNtyPl60u7zG2xnrQCiTPZtnBYLu96UadDGMtIzU1dOIT55dv40eSsC8yfL0571egWB9QhgcLHH9DT/7WY/xbcegptsLdDkt8v8AOq9/eqZP3SfL/OgPUnmklul649eetU2huGlKrwPU02GRs5kcrntS3OoMV/dsV7UEE9lcSWFyrecysp+8p6Vsar8X9Yvofs7ahdSRbdhWSQsCPpWDaaTcarOkdrDPdXUnCwxKWZj7Ck8VeF9Y8Gzxx6vpOoaVLMu+NbuBoi6+o3AZ/CgNNgfUWmByFj9x3rOu51RtzN93tVaS+8oFe/tVcM15JjbnPGa0MuUnuNb2j5KryahLcH6dTmrJ0QIMs6jv1qOee2slwPnz1qtw66FVoJbkcsTR9mWAjzG59KSTXpPmSNdo9qbDC1025ifpRsUPkvmcbVXpxmlSHLBm6VI9v5CfM2PUVXkuGnk2r/8Aqp+ZOoy8uGeTbHnnr7Vr+HrJJV+ZVz7jpVWwh2fLs3Me9bmn2y2UIaT5f8amWpdO7epcji/s+LaMEmqd3c54Xp25pz3n2s8cKO9VZdvmHbzx1qFE1v0GSMUUn5ST3qsz7j/hT3LXEm0VKIEtxlvvelUJiQKETpnPrT1kCn5eWqOMNMfl6VYjiWFd3GTQCshI9NaYZJxT5oUsY9zenAqOXUltIjjO6sm6v5NQk+bNHkGjJrzUWvRtXcFqvDbsJAv96pI4PLjBPzf0rW0nTCyGTaTjmgJRLGlW66bEG4LNzirUcjTt838X3Qe1VzIZJPu9K1/B/hi48R+IIbaHc0zuNoArOpJRXMx04Ny5UdT8KvhzdeOdUtrSy+Z5z87Af6sdyTXtXx8+Jdj8Gvhxp/gjwrGLzxHqyiOeaJfmQHjAPXrXk/iXx9cfCZP+Ed8Mp9q1+/IiZU+Z4yeMACvrj9iH/gn+3w6hs/iB8RJnutamj82K1kcFoc84+teDiZ3ftJ7H1WCo8kfZxWpa/ZN/Y6t/2ZfDH/CTeK/stxrmqRi4hMi5+z5Gc89+a89/ar+PlvaGS2hmWWViSjL97rXoH7bP7YcNnBNBHJmRt0Kwlh8qjgcV8F+JvElx4w1WS4mkLSMcjn7orjw9CWIqXlsPGYyOGp8kPiK/iHxBceIb95GJ65I+tGnWDXMgTPA606202OADc25m5NbejaSJAWJ8tR39a+gjFQjZHzPvTlzMg0/Smi3N933q5B5lzJ5cEZZumcVfsNCl1u42wgiJOGP96ur0rSbfRYvIs4WuLh/4hztrKdZJHo0MG5GLp+iRaFEs11+9lcZVfQ1V8RyyeINQiWRVRGHCivTfDHwlm15/OvDtWMbmzxgVha5pcV14tEMKr5NueWAFYRxCb0O6phXGJjCzXwxoKsyhGcY98YrkbASXuovJnOeBnvXUfEfV/PuhDEF2xnH1qt4U8PGR424Z252+lb81o3Z5843lZHXfDjQIbYfaGVl29eOprp59ZXRNIutVL/MMpEueR24qnaR/Y9KjsY93nMuZGH8IrgPiZ4vMs62kOfs9oPXq1YU/edy6j5Y2Ri319JrGuSSO3zyMWcsa9C+D8H/CY6pbws2zT7Nt0pPQgV5H5siqGVv31y20A9hX0X8L/BLeFPhrDbpGWur4l5GxyErSpUsjOnTu9D0HV9esfD/w11LxJNNs8mNraxQ9wB2r5T1PxdJ4k1Vpnz5k7bjg9K6v9pD4oNdw2eg2br9jtEwRnq1eZaO/2a0aeQ/N2961prS7Mq0knZHVJqfn3Cw5+VeorrND1kRw7Y+FUYxXnvh+RpJGlbJMhruPBawjJnG2KPLZz1rUzi7nXaFY4khkP+sXMhX+76VqawT/AGbGHX/XNyO59K5O38TyW938v+rlbbx6VueJ71YNJW68xSqjaAT3oNC94eupLjWraGEsPLyxH0rnDo73eu3H2r5YvM82RjzjknFWfD1y9u7XyS7flI4PrXP2/jP7Zd3lvJ92aQnceSAKQpbHeDxQvjDxpYQTfcVUiQddoyOn4V65Jppvre9nXlYFEK14X8GiNW+ICXDR/u4QTnqMivZD47t9E027iZd2+QsD68dP1pmetjnvh/bR+EviJ9tiZGldXQseq5HOK9V0O0jt/DZvfLVry7uMR7h615j4f0k3Ekcyo3nS5fnqAa9rsbOO303SpJgix24Vgp6ZxnJpF7I4z403zW1zb2027ewCov8AeY1Rh0ZbbRIVZfLWONn57tzn+lZPxV8S3njz4notvbySmyIkcIMhQM4qPWfEd3qlvdSDI2Q4VB/CQeaXoSEnhVvGNhJFMjbZIxcMTzlgRXoHgvwxPZaaqKfKXYnBHJODVT4b+Gnn8OwvKW824h8tU9T1/Kq3xC8UaxoWpxw2kf7lV2ZHQkYrRaIfkfn2q+QCvyqo6moJrpGB+6R61HqVwXO1Dx3qqls1wMk7V6fWtFHTU4eboQXtwzcL+lQpaPdSD+tbNnosbr97Cjqxp7GGD5FjZyO+OtPnS0QuXUy5IGtI8JtLY61XJnYcg+9a9xMzpxGu7txmqVw83l/6tvypLzGyobso/PH1rV014JU/eB3J/u9qyJYXlk/1Zx/KpbeWS3HyqyrVCjc2LnRvM+aFmHfDVGLK6B2qrH04zmqa3VxOv8S++alg1O6txxI34mswLg0u6MZaaHaP92qF1bJEfTPp2qW61eacfNM+T23VQupgoyXJ/GgG7bBMkSggNmqvnNatmPjHemtcrng81FJeHpigC/b6/OG5YA/StWPxIkafvG+bHeuYW42NwKc90ZzypPbNKUUylsb1z4m3v8qjcO4HWo18TPG/zRK2f9nrWfZzrbD5l3GrcB+1PzHtB6GlyotRJbi/l1SRfLj2fQU6TSfswDTsdzdBWlbzw6fbhYI/MmPcjgVXksJbuTzJm2lqluxrGm3sZqQ+fIVXO3PpVoWaWuF+9mrA0tmG2P8AOtTRfDXnSjzutRKskawoN6GG1n5rDbG2fpVyz0ORjkKy/hXoGn+D0kChY1P4dK1o/BSQxN8u5uwxXJLHpaHXHL21qeZTeELi5j3KpqCTwvNbRgSfN7V7JY+FZpYlXycDp0q9b/CqHUJFVztbrgDrWP8Aaijubf2a2eI6f4SkeVW8p5Ez0HaqGq27Q3TxpCy4Pp0r6p8O/Cm08OKLhrX7RgcRnoakk+GmmX0xkm0ONfMO7JHSs/7aimV/ZLZ8jR6RdyyBlhf2OOKgm8PXyk7o/lzmvrLVfAsF/utNM0VU/wBtlx+VZd1+zsdULLI3lyLyVFXHOI7smWVs+cfDOueIPCOqw32kzXFjeQMGiljA3KfUVq/FT4meNPjBd283i7XNQ1yayTZC10dxjX0Fe1QfACa21LaIZCF/jbp+Vaafs62GqSsbxpFCDsPvVr/a0DP+y5M+U306EFdwYydwKjSxaSTEfy9uRX1lqH7H+l+Ss0CzKJB3btXMa/8As02ehuzeYWCjcMjoa0jmkGZyyqS1Pmy90O6aXjcw7n1qumkNFnzh83pXrniP4f3i3Yt7eMlW5Dbegrk/F3w8vtFbLBmz6DpXfTxkZHDVwc4anJCzjQ/dVR0plxOLVdq8ntVyXT/KlCybt2ajvdOdHG1VORXT7RHH7NrQzDJJKzbuhxV7SbNpT8q555461oW+leXAu5PvcdK0rcx2iLlNu2j2iew1TaKsdvHpsW6Th26D0qtv+3T7SxwpqxdTrqN10yfftUN5J9nPkwjLMecURG+yJpcBFSPp3NV7n5DhR8vc057Z7aFQ33u4qACR+MEZ7UFJlf7Q0cnQfWpELXTqOatvpqSIMde5qa1tooFO5gzYoGkxiJ9lTHyse/HSorp8qOg4p8haUNgfSohDtf8AvMegqeYasVZ49q7mbvRYWrXeVjjz+FaVr4WudYnwqtjvxXdeBvhbNEgaRdqLyT7VnKtFI2jRbOR0nwnI48yZSE47Vcd0tpljjxtrpPGF/DBK1vDIrRoMHaMVybqSTj1yM1MZXQ5U10LFvbLdys0arwOAT1rSsviJN4Es2Gm25l1mb5I2A+7n0rHSxmYL5YbLHnBr6Q/Y+/Z40W61ePxF4smhjtbIeaiswJI9MVjWkjfDU7Sud1/wTq/ZkGk6nc/EDx1Ztd6lMBLbJMpzF/tcjFdt+2b+26nheyl0rTSsl04HlhD9z6/4V5/+05+3OHibR/CLfY7WA+Wsy4HTjpXybr2s3Gs6lJcXlxJeTMdzSOc8nmvL+qOpPmnsejWzJU4clLcs+KfEuoeNtXkur64aaR8sxYcc1UgtVjBEfzSHuB1qqkjEKM53cYFd58PfCMZhEtxE2c8H1r0rRpx0PGjzVp3Zn6B4b86JWkU/N0Brc0vw1Le3YVg0duv3jj9K7O28EW+nWzTXkkca9VQNya1PBHhG88ear5FrH5dvGw68ZHTNcNbGKKue1hcBexlaD4Zu9QY2+n258tRhmVa9T8A/CKPTbdJJNu/AYqw5r0nwx8M7DwDoiyyKsckY5HXearx2Nxqsk0jbYbfjAHGfavFqY6U3Y+kp4NU4nG+Nr/8AsPwzcTWcG3ygVct0rxmwhb7BeX0hAeVi2Ccce1epfH7xFBpXgttPhWT7Q7ZYdjXhOua9JLp8cK/KBjI9a9DA07x5jyMdV9/lM/UYn1GVpmOCrYHpXc/C3SMSSXUyb1jXj0J7VzFhatrAihSPap5IFeueFPD8OieG187iOL5y/rXbUlpynnU4a8xjeKbhfBvhn7VJxe3ucA/wDtXhmrXTXd7JubdubcT6811Xxm8Zya5rLxbmaGE4X6DpxXI+X/oLyMCZJB8orWPuo5qmrsanw503+3fFW6Rd0NoN5GOpr61+JM1n4I/Z2tdUtp1+2T2+XVuqA+leCfBrwz9h02NpIdlxfFUBP8QJrpP2t/HsOj20fhuGZmCxj5D0UYGaxb5pWOiMVTptnz7NJN4g1NpGZmDNkk9RVjUH8t44fTAOKl02D+zNN81siRuar2J+03DTt/Ca9BHlSZs6bcLaSpGvbmupstQWLT2DfX61x2lRGe4aXBwxxmti+uGhkhhU/M2M0maQOigu1l8n723I4q/r+sNPb/Z1+aMY4rE0SVbi6Ku3+rFXLNjd3fouc5rNyNok994lfTdFkjDbVfHHpWH4VZbu4lmkO5RnkVS+IWqrbGSNWPzNgUmhM1r4ImmbKschT6mrWxjJ62PV/wBm99+malcNuURlghPf/OK2l12PXtdgtkb5Q2WB/i9axvh+yeF/haJmkVZbpdwUVQ8J6oun+KY5nZWWOMsM+pqgParbxBbaJpsk8jLuIEMa/pWpf/ERpbVbQzbl2javoMc14rqvjE6nq0UcYPlxnJGe/XNb+nStqniyFQzNDbpuk96L20K3Pc/h5faR4L8AaxqlxGraxqpKRZGWReg/nXlus3sljdpCsmXupMMcdAasL46bWNQkDRstpCFRexbH9K5+fxAbuW6vm2K8c2yEHsR0P60nIPQ9e1Pxcvh+O1gt2VpljSCPHZjj/E1d8aaKbrUImeZY18sYBPfvXFfCzTpviH4ihsvNjMtuDeXLN/CBzx9MVY+I9/Hc6+w+0t5MP7uLB6gAZP55obDc+A3XyvmPpyfWltEkuyZGOyFafM2P9b8qryRnrVG91h7ltqLtjXooro6HCWNQ11ifLibai/rUNnqsiPukZmXoagj3SEMVG7sKnMS7MOwX2paAWH15nHy/u/QbaF1S4A3bt34VDG8UfRdxHSlkvQx+581FwHPqTe3PJ+Wq8l60jfdx/WmSl5Dz8oqNk2jI3fSpDW+hJJdsnXj2zVeW/Ynp+OabNBLKOhpotGC0XCzF88Nzuz7VEZPMPerUFkSfun3NSS26x8AZapctbIfKzMkGw8Cmxl5unH4VovZfL83FPgtUiGD3o50ONN3KCwbUx1b2pohZGwM9a1JYcfdX5fWptK0v7XOqqm7J6iodVJam0aLeiKdhpkly3H3e9dDpuklR8xXj26Vtx6JFplohkVFU9FH3mNOhs2kf7ojHYDrWEq7Oynhytb2MNuN23c5GOBT1sll+/mtKPSPLi8xsb26D2rS0Dwt/aDYYbmJzgVyVMSkrs7aWGvojD03wzJcTFl+VM8V13hzwNI8mW7dciu68HfCSacq21VXGRmu60b4f21kv7z5mHXHavHxGYrZHs4fL+rOH0bwl5VsOFUdN2OtbFp4WiYL8rPjvjiu6j8INcKqwxrjp06Vv6F4CUuquuD1wBXj1ca9z0Y4VJHEaP4KWRUKoxz7V1Vj8PYY4lfy/nxyccmvQdE8CKdvGF+la934Yayh3LGAijqa86pjG+pr7GK2POovDXlBSqqqjrkVdi8P+bGG2oSvr1rV1Z1ZvlYqq8tgVWt0k1CVvLbanSp9vIl00Y0unrBcBV+aVjwMVow+Clkg89ocM3oKu2ei/ZrpZfmdozkjHJrr9J1FNQshGqrnuPSrVdvYx5bOxyelfDZpLjczKzN0UjtW5F8K4nm3eRHJxyAOK63SLONJN4XcyHiuy0myaa2AaHbHyc1MsVJbGkaaPIrf4dxm6w0OIzwQR0puo/B7TZbZv9Fhlf1KZr14+H2u5tpiVc8rjoa1bPwbGERiqq38Q/hAp/XpLqaexiz5E8SfA+S0RmsdJWaXnlk4NeE/FfwFrGoXbb9HW3Ygr+7TgYr9PNS0a0+wSfu1HGAVWuVm8E6fcOvmafHcEj+KPpXVQzicJXM6mXwmrH456/wDC/VotQ/fWsyMzYB8s4ra+G/w0TQtcj1DxBp8l5pa5DRj7zGv1e1z4K6L4i0zyTotrtDBhJ5Q3A/Wuduf2UdBjs2hWxjkWTl129M160eJLqzR5kuHoXumflFr+k3mueI7ptP024hszIRBGI+g7VSvvAmtR2+HtZIxIONw5PtX6ly/sv6GL1oYLNYZFG1SFGBXGeP8A9lKK4lWNCgA6uF59666XESehlPh2KW5+bT+DbyzgaRgYyo6d6i0rRJpLvzGxiP17197az+wlFrulzfYpj5rKSTjn8q858Q/sGa54X8MSeXGskhPLEYavTo55Sluzza2STi/dPlK9ka7mZVXDNxR9nTSh+8IaQjgDtXe/ED4Eat4NkEhs7nIHB29PXNchb2cSzt9rRlkAwoI6mvWo4qFRe6zyamFnB+8jILtMzNyM9OKIowQM/ezXRQeHJdUt5JET9zH1YDgVn3egGDd5bbu9dHOjn9nJELacxhVgyirGjaS1zdBmXdtqG0tpEjO7OfQ12ngeC1jIMjfvMcCsalRxWh0UYJvU0/DWi7bZpNu1V6kjrTdf8dzafatZwsqoeDjqa0dRuH/s8pCQFI6ivPdRhY3sm47mPeuOj70rs6qj5VZFW6aa+lYlt2Tnmpo7Pz2WPazNjsKs6VpM10MFWHPXFbtpp0OhL86+ZIwz9K6pStscpJ4FudL8K6o1zq8LXMXlFREozyehrM8RfEHUp45Iba9u4rORsiINj5fQ81U1Kc3sziNfmPbNZtvo02o3Wxfoc1nGPWREuZvQrvdtO7SM3DDAHXFXLDRZr+UAK3ltjce1b2m/Cq5ltYWUFg3zYxXovw0+Gn9ozJFcRSeUwP3RzmpqYiEUa0sHUmzjPBPwpuNaufkib92c9PvV6p4d+GtxaW25wVOflB6V614A+FC6VEgiTbG64bI5FdVp/wAO4Zr/AMuGEyovGSK8PE5l0R9Hg8oa1Z5P4X+DUl0Tc3zs6g5QMM5r1z4e+FV0lF+y26r/AAl9uDXZ6R8LZFWLdGoVRkLjrXf6V8PbXRNDa4lkSEKOQRXiYjGczsfR4fBqC0PNdQsZBMrXQMiIvOeRXNSJc6vqUlyreTpltycDCsfSu48W3cN3E6W/z28bfMQfvV578RfFi2HhuaztY8RspYsOBTw6cnYeJ0Vzwr9ojxpDqWqvFbrs2sFAHevIby6D3SrI271AFbPjfVn1fxGwQNtiPzY6VS0jQ5PEXiaOGMZaY4UDtX1lGKhCzPjMRJzmdJ8NtOk1/wAQR+TvWGMYcL3rufjf4uXwnpEdjC3yIPukYJ4rqPBnw9g+Ffg+S8umWG4Zdw4zXzt8X/HcnirXHyzPGhIBPVqIe9K5Nb3IWMGZpNf1VpmY7c9z0FdR4E8JL4z8QwwcrGrAZxwAOuaxfCWiy6rPFb2/zXczcj0FerWFjH4R0JUt2VbsPsYj7xY/0qqkuiMaNO+rNhtO/svfdRSLHBp6loyeMha+f/FHiqbx74zuL65kaTHyqW+pr2T48+KG8KeA/LVlE97Hlv8AYGK+e9Nu2TSGkb5fMbcSO9Xhab5bsnGVLNRNbVNR+0Xi26H5cc4p+BbKIR95xziq3h+3a5vGmI+VhnJ7VreHrT+1NS848LGecjrXZKSijzox5pGvpdn9lsVU/WoJi0lw0rH7h4rbhtW1CfaNoVB1FY2uSrBIVjxwcfWuaNS7O2VOyLvhRmnuS39/9a2b6X+yoev1xUXhS1jtbFZuDtGcYrP8ZalvQx5/eTHCis+bmkacvLC7OW8Q3v8AausojZ25ycV0FzdpLpUdkn3eGwK5vVLaSwCs3XPX1q/p7bpFkLc46etdUThlKzOy/wCEpml0yC33HbbptA9Kn0jUV/tFVb5n8vcSD04rl4L4JER1Oc07QtTU6jI7MflGK0sTzHUR6t5VyJC33m7dq7rwhrWGlG5v36AEjtXmKuWeNuoY5xXTaNrX9l6dNIWXONq1PmaR0O21PxdDHdx2tsdrbfnz71V1y5lim0+wjj8yS6l3Ko+83rXD6GLi71fzZAzbmB/DNd/4Y8ZafZfECTUpY42/suz2xox4L9Pz5pblbnpXwK8P6jf+PNQsNPYLqkNk8koXuuOR/wB8itHT0tfEupX0zKuyJhEOOMjO79a5H4JeO7/wh4yvNet2Rbq+s5opVPJ2vlR+hqHXLm6s5kh04sFUF5Np/ibk0pBbofEV7e+ePvdqithJcuAvT2qSy0hp3G5ju6mtNUjtEZUCn+8fSumU0locaiQJF9nHJ3N29qikl3SfNyafLcNKdqjiiG0beNw61HW7KGIGcnaPxqe3tnkwKvWWn+an3dq960rXS+VCKPxrGVVLQqMG2ZK6W0md3T6VCNNZpGVRXUtYBR5Z6+3eq91DHp6fuwCzevasPbPY6o4e+rMb+yvKiJkbnsKrx2iluATWk8Lztuf/APVULx+Vn3oUmV7FbFadBEFUdagntgx+Xk1sWelecm5gWOOKq3SfZnKquTn8qOd3sg9jpdmeYvL+Zznb+tOit/OG8jHpV6x0aS9ctIuB29xWpBpMcU0asu7d90VMqqRcMPJsydO0CTVXCANs7muktjZ+FbMog8y4YfJitD7ONKsiqbXmm4OP4c1N4Z8GpA/2q4Jk2knB7/SuSWIR208N0RV0Tw1Nfz/bL52VWG4A9BW7beHvtQ3xodq9/Wuk0TwnJ4ikVnCw28eCFPSuv0zwXHdblRGz0AXgGuGtjFE76OCbPPdF8ETahOu5X+Y8ADqK9a+HnwljKRvJCy+meK7DwL8M2hjWSSEYUAA16To/g/7PCF2Bv7oHavBxeZSlpFnuYbAqOrOQsfCsdpb7IUZmztwB0ra034cNcSK21m9eOtekeGvASvsJi7c8d67LSPBUURG2Mrxg149TFM7/AGaR5zoXw1VW+aFl7YxXSaf4Bht5Fk2gtjoBXfR+HPsse9vyHWoZLBYSfrXFKs29RqJydxpUOn7crjPOAKx/ECS6jbtHGsix9M13Vx4dWaTzPmP1qneaCxH3Rt9qj2gnBHncPhSFkOVz65pdH8Jx20rFQvPbsa6e90vyg3Vaj07S/MfEf3vc0/aOxm4mX/wiqyb2jwvGOBzXmPinXNQ+EWsyT3HNgx3ZI6ivftI0uS3fYwUlvxrI+LXwmi+IXg2+t2tlmmWMlGPVfpW+ErLntLY568bRuip8Ifid4d+KFjHHb3VvDK2AFZtrE165ZW7aXbbvKj2MCMnv9K/JnxrY6t4Q8T3Frb6jcaX/AGYzZlDFGVhzxXpX7P3/AAVV8YeCJIdN8VLHrGiQvs84ptnRR34619BWyaUoe0ps8unmkFPknofoxZpG8vnMw64CVuLbx3EK7VZSvU+teP8Awu/a6+H3xc0WC40XXrX7dI21rSU+XKD/ALrYr0rQvEkN3Kdz793Cso+Vq+frUKkH76PYpVIyj7rNy1sY3ba0Y9cHvUdxo0JPmbdvsByac0shfzP4egJPFDy+Xb7pGUntjvXLzPqdMe5VuLSMAhV2Rs3pWb4ltltrbbHlXlHGOtXpbnzFbzCd3pjisvUGZrxJm+ULwmatSLIU8NJbxLO6b5cc1Rn8KQ6pfiVk2j+7jgVuQGWaNg2Nh/lV6CGO2sm2gFvrV+0a1C19Gc3Y+Blguy0Maqg6HHWttPA9vN8t0kcu/qMcYrX0k7lj+7yeTjpW5b6P9rl3qR8vXipeIknc09imeG/Fb9n3S/FEUm3T1UynYSF7V8m/tF/8E+/7Y1aK60uFo48HLKo29K/Ts+FFv4U81fl7cVmeK/hzb3MTR+Wpjcc5HSvXwWazpu6Z5+Ky+FRWaPxL1/4Ka18MYrqzuoGNqxySo6j1rzXxBpUsjs1u3Cn7uPSv1d+PP7NNvftcRw2ok+2KR5jD7vtXxN8af2Ybn4fySSR8iNiQuPl/OvtcDmsaitLc+Tx2Vyp/CfNNpG0jhbhGU/zrfs7M2vzRsM44561a1jw5JPqClovLbOCAetQ2dts1KS3kbay/d9q9aU7o8f2bTNXRpGu9NZJG2ndjPpWeNDW41LbtwM4yamzLbqyqRuq5oN6t4fLuGCuvOfWpWmqNI66MuTaDNp9gDHCzr6hetc3Poeta5fMsNncSeYdqhUJzXqvgjxVCtqtnMiSJnPzelet+AbrS5biOW1t43miOdoHSueWJcNz0qGChU3Z8y+Hvghrd7eRoYJoptwUoQd3Nex+F/wBjS6gubeZtzcZcFe5r6r8D+DdHv9Pj1G6WGO6m5wqg811+j+Hd9wyvGp2j90K8zEZpLZHsUcppI+bvCv7LcmqX3l7vLhhGAygfpXtPw7/Z20vwdpw3QtcXBH3jjivW/BXw0kdBI0KJv7AV6RpPwzh0rSWldVZmGeRmvEr46cj1KODpQ2PB9P8AhBjdN5bRq33V44q9oXgiHT7kNHG23vnpmu/14faLjYuxV6celULlo7KyLDDJnHHavPnUbZ2U42K+h+H4TO00uPJtxuYdABXA/E/xUfFmt/Y9POyzhOHIPWtfxZrlzeWht7XfDbN/rG6cV5/cMkWp+VazfKuNzDvRTjd3Zo3Yq3+jT30MkFqvlwxgl27tXiH7R3i618L6I1ss3+lMpBQdq96+JXjCPwN4PkkmVOYyRt4596+D/iX43ufH/i/y2kZi8uFHoM172X0+aXMeNmVblhYp6bpwe1kvJmYGZssvtXSfBvww+teM47i3jZbeNsAk96zfi5JbaFZ2Gj2syvdMgL7OcZr1j9nTSIfD/hzzLpdq2qGbc3c9RXuylpY+bjFc1zY/aMLeBPBqWdxKJLiSPKqTkLkV8hz2zxu1xKQyknp616Z+0L8Yr74geKHa4kbyYHKInTgcCsPwB4OPiW9kkuo8WkKeaWxxx2q4+5GxhV/eTsa3wf0VtJRdWkD/AGq6zHbJ3+uK6TX57Lw14ospri482OIebNuPR+uDVOz8QHQbOTWnRF8hfJs4QOD74rx3x140u9Y1OaS6kKzXPzEL0qYxcpFykqcC58UvG9x8VPGswXP2cviNE+7tFc9ejfcrZp8qx8EfyrZ8Mwjw9orahKuJ2T92CPWm+G9Ma5uTeXAz5jZPsK7qckkeTWvKV2WrKxbT9IVePMkHI9BXQeGtH+wafuPLPWbbyDVdVxHkQhwOnpXfaLoi3l1EPLxCvYVz16/KdmDw7k7iJpv9kaK1w21dy5rgr1PtmqyMP9XuHPrXffGeY6HosaYVd/GM9K4vw5ard/ZmwWXqxPc1nSl7tzprR97lR0nlrp+kRMTtXHPNcbqeonV/ECyR4WO3rU8d66YYDDHj5Rx7VzdhdJZaJLMxzJMMCtKUerOatLoVdX1NtQ1vy1bcqdfrWhBLtZeyqMVg6W4a73H73XmtGW7MMW3PfIrujGx50nqb0CgWDHcOMn9KoaZMY4mfgZb9Kr2+qN9kZP72c02znaW0k24wvNUHmdBb6o01xGoYj6V1elwHUrLyW+VQclq4bw4ftJWRuAvSu/0Vf+JW7MflxnNZlx8zcu/EFroHh9tse6ST5FbuMVwGj6pNda0su4/vn2ketSeLdbd7YohGyEkc96q/DaVbjWo2kw3YDHepk7IvmvKx7V4Y8QRB7pI42+SAIp7k10Hh2a5sbZmY7mkA3ZHpXF6RdwaJq0zZ6QEYPcnpWtd+N5bO3t4w4X5Nx465qTblPlsL9mh2r97HzHNRwzbpMKvy9CT3oEb3Mm3btWrdlpyzyqiZJzzWjkkrnFFN6ISCwVCW28dqtWWlm5blTycVrRaarqioAxXgk1f0/S3gAZh7cd65Z1tDeFFsqW2lrbwj5fu9Sa1rbSFS38zb8zdB6Vf0vw/5x3zYEcfzMR0+lRalcm4cxwYVOlcM6zbPSp4dLUyNSuI7Vdq/e7t61kyp5rcfxGtHUbRRJ6nHJqrAF3/KtVCWlzo9nYh+zeYuPuqPaprXQRLhmx5ee9XNPsWmky/yoK0JJEjhPr2AHSqcrbB7LqYup3Iso/LVfmboB2qro/hyS/mLt8q9elbVh4bk1S68yQFV7k9xWhqU8NlCtvBhSBj3Y1nKtZcsC44a7vIyWihtcRqu5s+lWtM0gkGaTP8AsDHWrXhvRpL+5aUrxnA966B9JUyLGQct2A/QVy1a1tEzphQvqc7plik9601xuxnhe5NeieBfBcmuOtxcQMsa/dU9hUngz4WefeLeXB2hSNseOleueHPCmEVVXy4wM8V52IxiS0O7D4bqY+meChPbxpH8sanpiu++Hvw5a/uFZocqnHHetnwZ4BXV9QUKreWMEjFet6D4Wj0+HZDGqsvUgda8DE4uT0R7FGgkjn7DwNHawJjIweFA6V2fhnwZlVYw4z6jrW34b8KNNtaRAwzke1dppmlLaxf6sEjocdK8qdRnUjnbLw8tl8zR9qvW0IWLaibT7962zp7MPmTG7oDTzoatIG2t6YFc0psfKY6ae5X5lG0+9Emmqr7toJYY6VvW2nNJLs28D17Vei0L93zGpNZuQcqOTew2ISy5471l3VsZJSFT5fUCu7fQ2lViFGenIrPutN+y/Kygt7Cp5h8p57qHh1p5N0kbZFVE06Oyl3EBfbFdhfpLPP8AKuF65IrA12CWSNlVRu9T2pe0D2Ylou8hoyobpWppyNDMPMKsOx9a5UNJZr94q3bFaWm6vjbuZiw4/GtKdRKVzGpSuj5Z/wCClf7NN7fWsfiLRbdXhDF7sD5cDvXw7cWESSSRNEGjjXJZTxmv2Q8U6dD478OXmmXixtHdRNGS3OMjHSvy6/aN+Fk37PvxEudJulV7O4ctDKEwpQn+lfoGR45VYezlufG5tgeSXtEeU2tk1nqUeoWtzJbqh+UxPtYNXtfwS/bM+IXwu1O3iXU/7W0+FtxjufvKvpk15LBrNnp74t4o5o+p3Ddg1H4g13+05o/LKRKy/djXBJr262DhWVpI8zD4qVN+6z9PPgn+3voPxMijsrhobS8jQExO4Gfxr2K48c291b2s0NxE6yjhV5APpX403HgXxFDpkGpWf2qORzktESpx7GvSfhv+0b8S/h5PGXlnurOHCFbgnB+hr5jHZAlrTZ9Pg8yk1aaP1eh1xbjSt+1YzIT1FVdODX7hZF3Kr5ye9fHmj/8ABRa2j07T4dbs7rT5siNmH3ef4hXtHgH9rHwxrgh8vWI5PNAIDMAw+or5+pgatPRo9unWjJXPZ5l8q5aMB1DDC571p2tjuaP5dwK5Nee2PxRsdS1aGSK8SaOYgKA+W5r2LQraG9jUKm1iAVLHqK5JxlHc6o2Zd0Xww1yExDlU5IWu58JeDIy0ayRtzzyOn1p/hDTobW3jWT5Wk4xnqa7OwiSG48sNllHRT1rlWruOUtLIo3nhKK1gDMq7VGRjvXK+INOjjikXyvwrvNYbdDhd2AOB6Vwuu5lDqxPmZ5x2rfmtsZ09dzzzXfC8Os3HltHt3DArx74+/s9WOp6DP5kEcjr90euR0r6Sh01LeXzdvzgd/WsHW9EXVbmR5YwxY5AI6V24bFyhNNMVbDqcdT8j/jD+z9N4R8Z28+xjG0vEYHABP9K85+LHwj+za9LfWGPLgx5gB71+mvx9+CDanM07IgjbIDBcla+QPHfgaTwr8QJNNmhBgvlIDY6nsf1r7XB5k5x1Z8tisv5ZHzqnh3+1NPS6hjwYztkXufesjX/CTIRdWoZVX/WDPSvRde8N3/w68QzQyRt9nkbgEZyDTtV8D3EK/aLVGaC6XcwPRa9eFa6ujypULaWPN9DDkeZGxXbwcmu2+HmqXyXDGGSRdpwWVutQ2vgSS3nfy0+9z04rY8DwyaJfSSTR4WM5IC9TRUmpIujeLse/fs2Tq2uQyapeTSRq4xGzcV9keCfCmm67cx3Vu/nKOnt7V8MfD/yNdm+1WM0vnKeYx0Br6r/Zv+PFv4KWLTNQiaSSQ/K2Pvmvn8ZTbd0e9h6zaPpzw14NWO2XbCqx4445NVfiEwtdIkhhRo2UYBre8B+Km8QpF91IlG7H90Gs34uQwttZG3KeAFPU14tQ9SlrueT2Phhrthnlhycms/xRobRlFijCr1c+tehWujJBaxbVzJJ39Ky/FUCIPJaPdNnaNvpWSOpbniPiWG+8SS/YbOF4V3bXcjrVG58C6d8O7eW9vJVjKrlw3evcLbQrTStOmnuPJg8tS5LHBr4v/a9+PL67qdzYabmXyWK8fdaumj7zshPRHkH7RPxauvHniw6bYzO1mrEKg/ir548SRyeG/EcjMGabacEdV96+1Pgb+yjHo/w6vPiN4gmjazWMlYz8xVsV8aePNbXWPi5NZWsX2j7ZMVjjTlgCen/1q+pwGqtE+YzTbmZ1/wAAvhTc+PNUl1e4SS4ghPLNziu8+IHxc0fwBGdPkjZWUbAqcbeOprcv/E9x+yv8F0W8t0t9U1HBt7cL85B9a+S/GniXUPit4wmkvH/0iVs7BxgGvSjT5veex4UqzWi3Ovujpfj3xPJd2LyNboct5n8f0rubyxutLtLdbONoLN1yU/iYDrn2rj/gX4BvtS1ZbHTYfOZjmR2HyJjrzXffFnV4/Dkg0e3ulmndNss6HPljjj6VhWqa2RvQj7t5GToFvY6pqjaprTPbaLYwuYwfuyuAcAfjXnfw8+Hp+M/jG+1Hymh0uxkZyxGERB2rrPGWsj41HSvBWg2zCSMqJ3jXJkbPHAr0/wDaJ0rSf2cPhBpngmwjh/ti6jEuoTJwyZGdrfmOta072OSvZs8L+Jur2Oo6lDaafFttYzsX6LxVex05hpbx9OCd3SsjT7Nr65My5YSNtVvavRNA8Otqtpsjt3kSEbWO3pW9Sagjmo03VkZfgfw0XhP8TNyK9s8JeE00qyjE0a/c3ZPesr4X+AFklTcm7DZHy11Xj/Wl0nR7qRcbbVNnpzXj1qznOx9Lh6Cp09TwL4467/bXitbWN9yI+01astJXRbOJduG27iPSsLw1ZyeKvGNxdkbk87Az0610vjW8Y3oVcLtGwgd69CNkkjzZ+9K5534zvmEM8xI+YYA/Gq+h6XLd+H1un/1aD5Qe+ah8d79Q1GCzhX7xwcdyTXYeNbeHwt4Q0vTkVVkWMNKQOSTXRT6I4qkd5HCWG1Lx8c0txc+ZLnPCk8U1GWKKRhnrmqw4Rj6mu3qeaW0utiMxyd3A9q0NOm8rSph/fPeslyzFAO3UVokhUVfQU5BG9zpPAemm9iCg/d5NdT4nn/sWyjjD7dw55rnfBd+1rAqx4GeaZ488QnWZ1VTyox7CsWbLYzNS1bz4XYt8u4103wUe3i1FbiYAhWJU/hXCayy28KQ7ssxr034W+Evs+keZINsaDzPrUzaSNKMW2a+s3M15r9wyt/tY/wAK53VfEd1cXjLJIVaP5cE9q6XRJITd3twy/Kse3k1gtaRs7SbflkJIJGamJpNM8/it92FjX5m71pW9mbSLy0AaRup9K2V0GLTIFbAVmGF3Hke+Kv6boMNqvmyKSzcjn71Y1KqCnQI/DehbIhv/AIuea2LeCN7hY41DMoxuPQVmRC4vr5Vi+7GeAK3mtGtLM7eZGHzN6VwVpPqz0KMOxU8Q3LJa+TCRsX7xH8Rrl5b3G7/ZOMZrauJrWFz51wZG/uRr/Wq7zQwAtbWaHnhpfmz+FZQ8zq5bmPNNJcHakcje4XpVm10FwgZtygnJ+Xk1JJ4u1OOQorxwxjjCoBUH9tTTBmaR92fWumN7D0RpCJAPmO1V6KP60kcityqjOfl9qrWsr3BVfl5POa0rKx23W7H3RkY6A1hVqcqNacWxL65NhZi3i3GeXkn0q74f8IKSZbj70g+XdVjw54c868+1XO7LH5QR1rorjT8yx/3m4A7AV5tTEWdkd8aN1dlewtVtkXyYd23gACuq8LeDkk2yzR5dTwfWm+DNF8uBpDG2yPj612FjZtEsbZ27ui45FcNSt0RvGmrmpoGjB2jToFPTHJruvC3hyS4nSMISJO+KoeCdFZpFXC7mAwfrXufw+8DLDHExCs8Y646E14uIrHo0YFjwL4Lj0rS49sPOBmuu0nRF25MXHckVraPon3F+6O/0rUj0pUVtu7bxXmzl1OyKGaDCsMeFT7prbs9OZz/Edxzj0o0HSlhHyqfmrorHQ5Lhfl71jKTG7GbFoqyIv3uuTjvV6w0Myt8sZ29K6DSvDzO33d23rxXSaX4TwOE2r1NQRscfb+FWlb7p6+nStS38GrH83PPYiu4tfC+FUqMe3rWhF4WyvKZ3U+QTkea3fhXK4WPvn0rFvPCJeU/u8tnpXskvhMIpyM+ntWXdeGFidmWPr171jKLNIyueK6r4MJYv5bKMY6VxviPwi+W2ozHGDx0r6I1Tw0siMCGB+lcr4g8JxtE3yYx1xWZaPm/WdINuCsit74rm77Uf7Kfkr5a9Mnofevd9V8G27TSK0e1s55rhPFPwus/EEc0ccYPB6/Lg11Yend2YqjOP0rXZIrhH86Nom5JU9PWvH/27vglY/GDwBcapbxrPqVpCzRgjsBXFftDaP8Rv2bPFbatpc1xqugs2ZLfG5UHpXFeGP2+7zxjd3mn6hZx2f2hSixup2D/69fU5fg6kJqrSZ8/j5RnFwkfKum2Vn4YF2dQhnMmfLRV/hIqxoWmR3sqyRIWP3hx92t747aHIdda4ijVYp38z5cYJNcLb65e6Dfj5WjVlx061+gU5c8E+p8XOm4S8j0y5+I+oeGNGh83Y0MOVAUnoetfRHg/9oD4ca38EUs5LSGDWVXCRudxdsYBNfI9zq0mt6S0Y2lmUgnHes7RtQ/siwaOSORpE5TbyM1zVcPCa1N6OKnTd0fp78Cf2a/Cfxc+BcuqX1tFPdW+6RTGRIu3HGBXH2n7GOm+ONRmmjgubSJflR0Hl7Fz1wK+MfhZ+1t47+HNubLTdevLPTGfzGjz8r+xz2r67/ZY/4KO6P4Hhg/4SDbq98xJKsAF3HoMV4+IwE0rxZ7eHzJSXvHQ6B/wT41gaso8M+KdU84AMiud+0/nXoUtr8dP2YZLOfXLGHxBpMa5ZhkSFfau1+Dn7amn/ABJ+JLfYLWx0VOgLsACfz969y+LfxM8P+NfDmn6LcalDPdzZWZkIIHoBXzeLw8lpJHsUMWrq2x414D/4Ke+C/F19b6PeWt1oWqRDZItyu1d2fU9q+sPg7fx+ILCLVIb2G8hlG4SI24V8n+Nv2LPDPxZ8TafodnpcMl3NGXndcKydwcjmuV8ZeAfip+wCQvhyXUdX8NKTLLbyJ5ixL1wDnNeNWwtneJ6UakZe6ffniPVraaORY3bcv3iBiuNnXz9y/eYn73rXi37Nv7aWgfHm0jtxc/ZtQjx9ot5TtZW9Bketex6pehrhViXy1AyGJ61yVLxdpI0jHl0FjhBPzKp/u5PIpl5pCrF5nzfNUmmOt1IrcttbnFbV1bxSWjD7vfAopsrmZ5j4z8PR6jayRvHvVQeD2r51+M3wWg17Q7i+jtFN5ASEK8nHrX1frVmJEYKrAHqfWuI1vQ44pWTadsgJYY4Neph8Q4nPUoqR8M/FD4OQ6t4TtbySBmmWPa/y8hhXm+iWsVveDTbiFts3bHQ19xeOPA8cttdQ28YVSuQWGckV8/6l8HZJ/EDXfk/6RbtuG0cAA19Dg8d7tmeXiMHrdHn3jv4VWmkeFo9QhGJEAzH1JHrXlkQ8y5XMOxJPlcAV9OXPhGbxj4X1pwFE1sdwHTjGK8v+FHwtuPG2oX1jsWORQzAtwxx6V6dDErldzhqYX3rmX4Q1S38BWszQJue4AVTnoa928L/Dq+0Hw1Y6xeqV+0fvVkfsvoK820L4fWl34R1KOUMdRtW2xDHQjvXa+BviHrXiLwqmm6pNugsU8tQB0Fc9aXMtDpo02j6E+E/jttO8NXEn2xmacbVRWzxXW6FPMukQ/ankmkmO8Bj0zXzx8HNTaeW4jU/6nO3cfSvon4P6tF4hsttz800Ywn0rxK8fePWp25TqfDKR3BmacbfKHyluAK5vxNqlvaO1xGRJJGflC85NdBq+hXF7eRwRv5ccxwzDuKty/C6z00RxqoZs7i7GsdNjWJ4h428A6p8RJBJdXUljZMOUDcsK8+8MfsyaHdeJltdTjJtZJizSOwUhfUmvoHx/p/nXXkxo3PygKePrXMar4Ft/Dfh65vL64e6uJ48CFPvAVrRk09BVpWifLX/BSP4+WHwq+G6+E/DCxLZqDGxRtwIxjPFfMH7C/wAGbfwZdy/GHxbIr6PpJM9vC4G6eQcgY9K6f/go74usrfxJZ6LYFPtGd8sbDLIPevnXxD8UNYvvCP8AwjNvLNDp8I3FA3BJ9q+0y2nand9T4vMqnPUsdN+1D+0zcfH/AOKOqeJrpo1jyUtbdT8kS9AAPpXK/Cj4Jaz428Q2N0yyQvq0m2M45wasfAb4B3nxD1UX1xC0Ol2J33Dyn5W/+vXs3ivxzZ+DNHnbTbmNLiyHl2uz7qcY4PrW1etZ8sDnw+H055ndfEnxNoP7Mfw7j8HaYqXHiC5QfaLlCMw5HIz+P6V8q+JvGcnm3gDG4uGBLvnJb2puqa3qni2/kvJJprq8mz5jueD9DV74R+B5vE2vzzxwybbUZllcZjIHJFKnG24qlRvY9e/ZO0BP2XPAjfFLXY/NvtQ3x6fAR82SCA2PQZrwr4qfEu8+IHiu81S8lmkm1KZmK784re+Nnxl1LxXqK6XdXEbWOnARW0EP+qjHrgcZrm/gv8Lbz44eMYdN09ZXup5fL3KMhFzya6Y8sFzSOHlc5csTb+GHgjU/H99b6fpse9gw3Op4X2r6sm+Gdn8MPBi2CpI2qTrtl5zg+oP417R8FP2V9N/Zr+GP+l2sZ1R41csyDJGOvtXL3duvivU21KRVVS+xEYcbfWvDxeMUnZH02BwCpxu9zhvCekrpOkuCrLIgJ3H1ryT9ojxKug6E1nGzb5mHJ75r3rWimladqDZCrknJHAGOlfJfj3XG8b+PHjZvMihYKqjuaMHHmlzsrFysuVF74daI1rbQusLfvux/iqPxLbf2X9qvpAPLUEKT2PNd5PZf2Bo1nEu1XgQAZHLMR/SvKPjr4iFnZW+nKS1xvPA/iJr0ISujzZwsZ3wN8Dy/ELxzJfNGxtbWTO7HApfj5fCbxc9pGqqsJAwOwFfQv7PXwyb4efCH7ZdRCOO4iaaSVh9046V8seKr1ta8c6rdbvMiaZtjHuM1tg6vPNtbI5cdD2dO3cyL9824GflDDNF3LugVv4VxgCjVwqhYULF2xmo9Rj8kxwpndjmvVjqzw3csaXAZ5tzZG41fv4hHIqruz3NM0iMK0Y7rycVNbA6lqojX7u7B96iT1uaK/Kdv4U06I6WuMeYsfUjrWJ4keG1CwqV8wfMzd67O50ZfCXhuCSfcrTRlhgflXmOp3DXNzLI2WJFYp3ZVrEFpG2ueKYbX7251x9M19BeJ9D/4RX4decsmJJmESgDtgc15T+zp4Qk8Q+O2uvJ3Q2aiR2I+tenfGfWJL77PbxlRFA/zY/ven5YrOUrysjsoxahdnI67qf8AY2ifK20suXH941zMOuSeUp8zqOmelV/GviF7u4aPdlQcEfhWbFMwiX7vIz0rZLS5z1JO51dtA+q3L3VwzLDF2z1NX7aeS6jadUbaTtT6VRVZLiXyY/ljXrmugu5YPDOjID+8kxkA9s15dSZ6lOnfcTTr2PQbeSW4wzkdKwNd8RXOszsW3RxZ4VTWbd6xJqV/li21j0J61ZbdejyY14XBJ9ay5dbs6OlkJaxqqqMn19c1eiWRo2ZiUXtmmWttDp0fz/PJ6U261YyHa3foPSjUqOhUvRGJOC3qT3NN3AW/yjjpz3qe1svPlLt93HAqG9jZBu2nbnAFVGa2NOR9iXTZfJkVmz83Su+8L6St6keV5Hf+9XFeHNFkuZI5ZN/lg5r0XwJdw3urx28fMijPtXn4ypfY7cLTtubi+FpJGi2/MueSOi1NqGgeZexAfMu4DjsfeuwtNN+y2S7gPm5AqPS9PW51PdIu1I2wAB1NeBKq73PVUPdL8elR6TpscYjVvlBb3NaPh7TmublWZQd2MelMntftcm07txPCntXb+CfD0YWPdHk5HBrnqVLDjDWx2Pwz8LqFjkdVZs5FeyeHbHyIs7cZHGBXF+ENLIkhWONVwPoBXoukwuyquQuB1NeZUld3O+CsjZ0gySqPlI44roNM0lpkY5PpiqGg2eWb1x0rsvD+kt5alv4j6dK5ZGjZNoWiLtVdpzXZaN4dQKu1Qq1FoWlqHVP7vr1rr9I0xX7cnj8anlJHaL4YVk3bQN3tW5a6EsShcNnrViysWiiX9MDpWhDCw654rVRJkUY9MbcuFwverkGn7nq0sJI/3ulWI7dgevy9sVXKzNyKsGmLICCBzRdeHo2T5V5/nWtBZgEH7tWhAoXn/wDVS9ncxlU5Xc4HUfDqqfuqfXiub1rw+ojb9yvua9U1HT43Vtq1xviWyZYWK/L7Vy1KfLqdlGfMeSa/oUIu2kOPTBFcN4s8PebGy2m0SNnA6frXd+NGmWdmjXAXg5715N4z03UL+dpI7yS3wCML2pUKyUrHVKjdXOO8YeFIb5ZLXVLi3mhKndCSGzXw5+1Z8DvDen62X0+3is7qRyd0YIAOeOK+uNZ8EXemX8k0WoXE11JkESHcBXmOv/s/teXtxeajdLdMzFwpGcGvpsFilBppnl4jD82jR8BeIPhLrwhmmaa4uI4TvHzcAU3w38PG8c+GZMxn7fbsQVPtX2D4z+H0lnYNHBHG0TcOAPvD0xXnl34Kt9A1SGSzt/IjY5lXGAx719RRzFuNzwKmAipHjvgj9nD/AISu3jtI7oW2oTvtVWfAPNe2eFv+CW3jnyWuo00u9jWLKgyHpUHhfQI7zxyt5b2kyxQnLIT3zX6IfsreIG8YeFo4baRVXaBtI3bcVSx0nK1zLGZfGNL2kUfmz8T/APgl7428O6FBqllBb3JziS2STc6/hivJrv8AZt8TaLfCOTTbi1uLdtpJTgH8a/eOTwGpYNHHHJNnJbZ972r81v8Agsn+1LrvgHxMvg3wtDbWc0iBr26hiUOFI4VSB19+td1D2knY+dlWUGfHngb4nzeFfGdzp91rDJeQnymO4qVIPavYNN+PWvab4rs7pNUu7pUX9zI/3YwO+K+H7+zvG1lr26knkvJDvMjk5z65rq/D3j/xNo6CSOaRlx8pkJPArpr5bGeqOzD5hy/Efrf+wZ+2zeeCPGepXPiZmuri8GYJ24IAHAxX6NfBL4h6T+15pFxNJHYSabGoR/MUHzPXiv5q9H/a51SK5tYb6OaNoyEMsbbSBX2v+zN+3FrHwx8Eu/hDVo45ZcGVJHJL98ivBxWUyjq1oevRxkJ/A7M+4f25f+CeHhbwJbXHij4eTLoXiK3JlIimZI5wOoIzjrXzN8P/APgoZrWq38PhHXpWtdYtZlgPyD5wOM5FbPiL9uvxB8a59N0eGOTW9auWVGWH7nIPUemcVvfEP/gmVDYeCU8Uahq0knjic+eYIFz5PBO31rwMVg6adpHuYfFOyjJn1Z8HdUj1Dw5DcLJIysMs7D7xrrzd/aXITaqr+tfA37NH7UGp+FvGZ8PeKJJbMWDeUI3OwyDoDjNfY9n8RLXV0t/sU0cwmA4jOStfOYim6cvI9ONpbHS3Vk15P1zxyKo6n4S+2J80f3ckV02gaWv2eOSTDNjJ5rUmtY3Vgq847URqFcp5Rc/DiK5tmaSP1GM1w/iL4SppUM1zDDiRhtzjrX0DcaJ51sVxtbvxWFruhOINiru9eK7qdZoxnTufJH/CD3HhmfUJWhXy7gnenTIryWPw3ceGvEkl9as1uzO33P7pNfZfjjwC0xZnTMbenrXkGq/DYaZ9o3ruEhO3jpXp0sVY5Z0bs8f07Tv+EeW6vJFWRLrI+buay/DkqaVaXU+3cZCePSu78V+FJriz8uNV8uM9AOtYGvaDDaaDIu3DbcjHHNdsKqtqZyp20OY8E6hdT6vdTQs6RyNj5e1fTvwNmlito4Fk+fbnPc5r5t0WePRpLG2hX99cSYIx+tfRnwQjmF3cN937OgJz3rLEG0NrHvPg/SVvjmR2Zo+SewrU8R3Frp9n5zY8leGYmuO8N+KnjgYq/liU4OT1re1iCLXfCtxa7syuh2kD7vFeffWxpE8p+Lfx48I/DDSL3UtW1i1gRR8iswz+FfIfxs/4KxeEbDSZ7fw202qXy/dlSMEKMc9fSvVPiD/wSl/4aL8f28niTVL6PSYiWWOJyoYHk5r5P/4KifADwL+xj4ctdB8H2Ie7unEUl1IFaU554PtXr4GFKTSerOTGOaTtsfPuk67q/wC118dJtWFnczRQktcPs6KM9cU7V/gbqPjD4iPZ6HHuaL55Ao5QD1r7a/YZ+Bcfwq/ZHutQayt7fVtai/e3MkW59pUng465NeXeCPh9rnhm+vLzSbW5v9b1OT7OipHkeX7n3r2frseblj0PGjgrrmlueceOdAvPhV8KoRc3kdraM2JrdH/eXLZ7gVwugfCjUviZMuqNayaf4fHLyyMQgUf3Se5r7k8O/sV+HdOgTxB8Xr+OS9WLzodJX/Voeyt718wfta/tPp4p1lvBvh/TYbXTIj5NraWaDI7DOMZNVRrc7sjKtTUVZnmWi+EY/iB8T4fCvgmIzK3DSMSSo/iY13P7Q2saP8APASeEtMuoV1idWW9ljIJ9+fXtivPn8df8Mq6c8llN9m8VXcZSQAfvLdGz/wCPVpfsl/sOeMv2qtfuPEniC31KHT2ffDJcKW3g87snrivQlKNOHtKjPNp0Z1Z8lNHm/wAHPg3r3xn8WQwaXbySxyPgnPyoM8kn3r9af+Cd3/BPXR/gV4fj13VLOOTULgFnc5wvJqb9kL9hrT/g+trb6bDb3UcjAzO0e0k56+tfUfxg8QWvwo8EpCFLO8W3aOpPsK+bxmaSqu0dj6XCZXGive3Pnf8AbCuLjUfElrpNm0arctteJDwVFeJeIdMh0e/jtRDiOEbiN3CkV7zeeHFsNMm13UN0lzcKShbnywfrXg3jfVVH2yZuJJVKoO5rlozlUdjsqRUUeIfHX4gpomkX0QKq0wKx5bk14X8EfC0niDxTb3Dp5xmdm9jXUftIO0WrRLMjedIwG3oQDWt8FtDbwzpbXUn7sRxNtPuemK+iivZ0bI8Oouer6Fnxov2zXGVPlislbdk9CK8p+Cfw+vv2lv2mW0m1Xzrex/fOc9MH/wCsa7/x3qp0LwdqF5JueZ43kU569hXqH/BPj4PQ/Bzwha+Nrh3/ALW15XmEZA+SMep9CDWcq3s6TfVh7LnqJLZG1+3d4ttfhH8C20GDEepXSCGIIeq8AmvhGSL7FZRsxLNJ6165+2R8Z5Pi/wDFWaY58iF8RIOVQAkcfWvKdbDTGJD823oPSvUy2nyUlfdnz+ZVueq7FTR4PtV60kmMR8nPbFUY7lry+kb0bIxWreoNP02RlXDdCfSqfhiz+1XqDaMdWzXpU9Ls817mxYReQ3T5mXitr4Z6E2ta5HH8oZpcn3rPtrb7deSY+VY1xx2rt/hvdW/hqG4u/kadBhD6VjKV0adTV/aA1KPTLS3s4c7o1EZJNeO3Vx+8+Ubj93HrW54o8STa5rtxPPI0kaZ2Ka5/RbWTVtVjVd0kk0wUKO2TWfwq5XLeyPo/9m/QbXwb8ILzWrhAs90+wZPXA/lXAeJfE4lu7maRt+5iwPYk969C+Mupx+APhHpHhy3jYXMkas7Hjk14T4jvWN1HAGztXDc1jRvL3md1VqMbIzZA+p6nJzwzHHvV1gsR25Py8cUkSrp8ZkKgu3C4qeKHfCrMrNuGeBXWtEefq2dp4V0hr+5kmkH7uPk/7Rql43aRGIkXG45H0rttE08WltJNJ8kUC7nOMAmuB8Yawms6jJIrNjoorwudydz6TlUY2M/S0X7Sgf5mY9Kv6hqrWu6OMKq+1Z2mHyLmE7S25u9aHiG3W2dlbpjIxWl1zGevKZsmrecuCdp9c9au2Dx+Yu47mY4ya5x38+7WOPhema3rGWOxnQLiR8YwOcVVSyWhVC7ep01vZNONsag1raV4KXUGzJH8qnPPrW58PPAc2oaWby4VljxxngYrpL3Tlj03ZCpVOhPqa8Spimnyo9ynh9Ls4HxX5Wi6U0cOBtHHua5PwB4ims/F9mzsyhpMHFdR8QYvKjEZT7vJNcLZWbDXIZFZlwwII9a0h70HcmUbS0PrbTT9t0u2eNSy4yeautaK9/HHD8u0ZapfhHYR6t4eglYHakH3jxk4qwlr9muWZdrNIcEelfOVJe80ehHYueH9Dae/8wqWA6mvSvCOmBpo1ztXqPfFct4XsWZF/h3dDXoXg3TN0yoBubP3jXNNt6mkUdx4Ss95UDGf1Nd34d0tpC2PXOTWT4b0lbOCN5MMSOuOtdlo8flqq7fvDPArimdETa0Gxw6t/F9K6/SE8sFv7v5CsPQLbzE3McbeK6jQ4BtbAJVuPrWJR0/hiy81kOBvPU12ul2igLu+72xWF4UsFjhXcpzxz6V1FpEpRht6AYraMSZFpEGBx9DViOPbH9epojG0DK9KmhXceQRnpWnKtjNsIYduPm71bjj56d8Gooo8cmrlsd23P1OK0UTGTJI4sf0qRo8r7+tCpjvn69qcWXH4YquU573IJ9vlsOFauW8Qw7IjtxXTXzmNfl+bjr6Vz2q2TSqzMcrnvXLXirHdh97nlHjqeGLzN21sfexXj/iK8jmvmjjX5c4Zh2r3Lxl4ZWdZG2ltx7dq8l8TeG30+eWRYW+YHnHFeVHSZ7MeVo831rT7cRySbhk8HPevNPFN/FJJNDasXk6Eda9L1Xw9Lf3u7bI8XcAcVCngG2t2aRbfazHNerQqKOpyVadz5/PgbVLy/e4uoD9m/gx2rQ1P4cWM2jrJcWdusq8rx97617NrFtALJYFj3bPvBRzXNHw7b3KTtNHcOyDKJ2r2sPXurM82tR10PknxdqGqfC3xHML+1jbTr4/uTHGfk59fxr6z/Yc+I8OoWTQyKLaFTtjI431y+tfChvinHJa3cf2e2g5jJUbvwq78HPhHqHww1o7vOurVG/dxqBnNepTqJyTRnWpqVBwZ9k6j4ogtPC1zIsbMVjZsh/mXAr8Rf2v/ABt/wsr9pnWnuju8y9dQHPzKqgAYr9etC1+HUfB2rWc0NxFdS27qm/ny/lNfh7+1d9q8M/tJav5LPK8V4zISOoI6V9Rg5KTPz6th2ptMxvFWkQGa82xqsUJIVj1r2rS/C3gvwz8ArS+vGj+1PCXZgA0jtjgD9fzrxDWb+61jS/Nbb5j/AHkHB/EVreBpJviT4dPhuaZbXywzI7N8zY6CvU3RwTvYteA/Dfh34nW+ofZ7dcwscrjBx61wGtXF98LPFMkWj3Fw1uCSUHpXS/BnwbfQ+JLyzgleCGOQpcSI33VBxzXaeLf2XvF3im/bUvDOi6lrGmR4XzUhyoPfmnKPvcr2CnJxd0zU/Zf/AGjtS8FePbHxJpd0qTafHmaFxyx4r7e+D/7avi34r/2lqmh21xqmryfL5ZJPlqeuB/npX5YzaDq/hn4lQ2NvbtFqEMoW4gX7x5wRivrr4F/HK/8A2H/jfpOpS2d49tqVsvmWssbDeWx90cZ6189mmXRfvLc+iwONlsz2r41/A7xt4ptl8b6po50e6VSWDKwkYgnnH416l+w/8YLW9t2tbxpft8TeWVJwcjviuqg/aW8TftR2ASx0GS3s2h2TO4wAD1IFeO694CvP2eviFY6ttkNtfXG2U/wqTjGf5V8TmFPTllufXYGs2kz9EvCOqSXdlGw+4qg4Y11mnK5Tdt+8ccdq8r+DPiwarodm+5G3oGABzxXs3hiD7bKGwu2vnI3vY9SWiLlj4aa8gEjL92s3V9DS2Zu+7px0rtoWJjWOP5RisnXdOZhz65rtT6mMZXep5r4h8NLe27Bo/lY1wfjLwOIrRtsS42/LkV7Rqdi4gIxXJeJNON5atH6jk1pCpZmjgfMeq+E1smaSZfkyTiuCufCz69q3liMmFmIxjpX0P488IlLA28aFyx445rnD4ThsdJYxKqzxpk57mvQp1rI55R1PB4PhxJo/jVblog0cJwgI6V7d8LPDn2VpZn3L54BbI61HongCbxHcQ7vlCtuJx1rovE18tjq2n6FYxszyHE8oHQfWtJVm9A5LBOyS6isEeNq9MHrXfeE9OmOn7yjbs4Ga5nSvD0curyLFG7G3wM9ia9U8LaUTZx5O49celc8pl2sjD+JPiRPCnw+vd8yw3l1H5cWPvEmvyt/ai+DN18e/2idB8OtcNeTecHmdwWCAnmv0++JXw7uvGGvWsk+77NbMWC/3j2rjtJ/ZKsfDXxG1LxZ9n829uo/Lh3gYT3HetKeKcHdC9ipKzMTXbDw98OvhBYeGrO3tr67tYEQbPmIKgA5rhbG5uPCltb3EcFjp0c53xF0CMh+tdn8UPDOl/B3wzJr2ozppsSsWkmnIVT1J5Nfl5+33/wAFHbf4o6iNJ8M389xtBj+0Q/LHGucYHfPHWvSy2jVxD0OHH1adCPmelf8ABQ/9sTSfh1plxp41KLXPE10BhYn3RwZ+meQK+C9A+Mkfg2+vdYkjXUPEF25MSleYSe496x7Pwxr3xH15ZLa01LUtQnbKs8bPgdBX6If8E3f+CLtx45vYfEnj6zu2mWQSRRPHtjcH1Br6eVXDYOn7zuz5unRxGLqXWiPMf+Cb/wDwTW1/9szxIvjjxcuNJaQPHbSk+ZLznJ9RxX7GaD8GtK8B+CbfRbCxhtba1jCFo02gADGK9I+Cf7Pml/CnQrez0+1ht4bePYyoAoA+lO8eW/2WSSOIfuuTt9TXy2PzCded+nY+owOCp0VZb9zz/wAE6HYeE7m4vWU7VI2R9yB6V5f4802b4g+PpL68Zls4nMcMDevrXrV34dmsdEa+upGXzD8kYrnfEOgPYwqzZ3zrhcdQa5qXdnROKvoeT/F2zj03wsqqdyqu1YyOpr5P8XlTJcSXDLHHb7m5HAPtX1N8WmudTmjsVX95G2CpHavlj9rPWLb4efDq+2/NeSB347AelejgY3kctbSJ8qeOrlfH3xKZ4pBItvKqBfvbTnn9K9IurCGPQvs1uwb5lTgfewOa83+Evh68WWDUJl2tqTfaAuOVz6/lXqWsTw+GIJ7iYL5NrbnkDjcw6mvaryu1FHlQjb3meO/ECyfxz8UNF8L2e64F1KsTqMlcdWr6K+MGvr8OfC/iDR7GZII9J01LeGE/wlsdPyP51g/8Esvg7/wtr4s+IfHGpsY9P0UN9n6EO27GfyzXnP7b/wATvt/xe1xbZvLia5KlR3VMAZ9e9Z8nta6proc9SsqVKU31PCdZJvdWZuP3YALdyao2kKzXkrsv3e+OhqSC881WZi37zJPv6UaYywwzSOxYbcY9a+oUVGB8hKXNK5l+J7rz3WFVGOuM9am0eI29nJMw2seBVERDVNSLcqo7ntWqpWULAu7ZntT0tYhau5dtZvs1rtUfNMMn2rf8ptO8JSSSGOPf8xPfArD0GNb7W4Y2+WOL5mJPpT/HWq/2gq20PyxkY61NtBmPLrW+0ldFVUzx6mvUv2LvhjD4t8WHV7wL9l0tTcSbuBkV4/eQkWkcMQ+Z2C5Ir6n8OW1n8Dvglb26yK17q1t505Y8AkZArDEaKyOnDq7uzzX46+P28dfFi6uFk/0WxQqFB+XPb8q86iRtSkkuXwF3ce9bmvWwQBVk8ye5+eUketZOrTCEJbw/djGSa0px0shV5XY6G3a8vVjwxA4FdI2mKEUZ2kDkY6VU8BaS95eiY/dC5xjrXQ61Z+Vd/I3DUqkraFUad1dmz8Q/E6xXcenwsFWQ/vPQk9K4i/04LN83y7OwroPjppD+GviDdWZ5S3lMYI9RWYtr/a+ls3/LxBwT/eFeApqyaPcnrKxQ04+TKJFXcsZ4zVzWLRruxZi26Trg91qPR7Jlba3ehjMdVWNF8zdwB7VamriUehT0bwZcXOnyTBP3jH5AfSuu8A/D7+z7qGa8X5nICofvP7/StjT9C/sC3tbudm+ysuVQHqferWhWVxq/imG6STzIWxsVf4a5K2Idmerh8Kk0z2Hw14fjv9Djt14z1A6Vc1HwLixSFU4XnOcVreD9PaCzgOPvAZ9q6X+z2vSyjZxXzEqz5j3vZ6Hzn8RfBZilb5SzYP415zaaLIviK3QR/LuGa+qvF3hOOferRqSwOTivNx8MvN1qFflX5h26c13UcZaNmctSjrdHsHgvR/7J+E9iyqd8vy8VHBbfZ7iPKcsea0rWRk8O2GmKzN9nGcj3rU0vSM30e4ZJ5rypzu7msYsvaJYPJcR7VGDz/u16Z8P9EZfmYfNnP0rH0Xwrsh88pwQMCu68NRG2t9iKu4jk1lKWhpGJ1GmAzuuAGCn5h6V2WiQKMsNx5wTXJ+G7TZtBbdu5/GvQNFt1jC/Lxjoe9ckmaI19Ih8uP5V+ua6vQbD94qt93joelYGnW+1Fbj72TXX+Fk3TbgFwCMZqY7hI6nS0+yLHGDt3dK6KzXCD2FYFoPPu/Mz3AA9K6S0JKj5a3iQy1GMAMxP5VOowin5se9MijyF/X2qxEgHy8etaxWpmSJFhx9M4qzAmx888jFMiBIz69MVNGm335FbKJz1JEscXy08RbhTomwvepUXJzgjdWvKrHO3YrSWvmRn+VZupaSZItqqeuetbxiUfw89qikiAH86561G6Kp4hxZxl34dUoVZQwYVyfizwHb3UTApuUdsV6hdWKzPxWTqWl+WjZ25rzKlG2p6dLFXPB9U+E8OxvLj2DrXM618PWtIsxr8g6+9e7apo7S7tq5zXO6j4c3KwYfpXOpOJ6MZcyPBz8No50eTb5Z756mqNv4IttNeVMlnXkHHBFe0XPg5pWdduB2Nc34n0KLQLNi0fmHpnFelh8QupjWptnmNt4Ms/E7tDazQxmMnOTjNY97ZJoV9G0UjfaLfJXyxnNdXJZx2V0zWcXkyt13cZzU1r4bhuVmkunWJmHyMFzXqUMSr6nDVotbmZ8OfGLSa6f7ejNva3AwrlMlu3avzk/wCCuv7Emp/C34snxtpMM11oOuEzMyDPkHb39Aa/Ru6hs7KcRstxe+V8ygDHNet/A/4J6R+0t4d1fR/F2mpdaTdR7RHL1GeMDj9a+my3GWklc+bx+DtepY/na8Dzx2Juri8j+0b0IVS3CmtXSvg/feM9RhutLuobOZhlWMmza3Yc1+g/7cv/AAQI8XfCfxJrHiT4arZ654bVnmWw80/aIB124745r4Zi1ObwBqk1h4m0fVdLvLV8CNrdo+V75OK+woVYSWjPnKmFb1Wx0n7JPwIvrDxlr0Gt3R/1bNhG3G4k7KMZ619N6ldeJPh78AtYgtf7Z0G3tYWmgDKB5hx2JHfNeGfCv9oHT/AfiGy1rRLOe8vomVvKkhEglI65Ga+2PAPgH40/8FSdb0W2n8MR+EfB1iE+0SeUITcY6n7udvtWlWpBK7Yo4Nnyf/wRx/Y61b9pb9oLUPFmtabJeWFrOVcz87sn5ia+/wD/AIKL/wDBPXR/EvizRtetbG2Sz0qBYwI1P7pVwfz4NfoP+yp+xt4X/Zb+HVro+k2NrHKqL9omVBulfHJJ9zVP9oXwBH4i8HahpbRhUmjZ9wPI4rx8VUb1PQwqpp8sT8gf2P8A4/Wvgf4g6hoFwxksfPIhCjlecBSelet/tg+EG8Y/DK+ltrcs0aidAB8w7ivmT9rDUZv2dfiLp2k6XYAQtdi4nulXLH58EbjX3H8I2t/jL8JNNvo5VmjurQq+R1OK+EzunyzVRH2OXRThY8s/Y1+Mj6l4fsQ0jJJAnlsreowDX258KtXk1GBZGXdkA9a/OHwJYTfDL44aroqqQguWlVRxgMc/4195/BDxKTaxhht4APtXyEpWqHs8vuHuVkdjbfl571FqyLIvJzzVLTr/AGoGLZqS7vhcn0xzXZGWhxqOplartSJhXI6vFmRQuWaui1+diduetYKBmuf5VnKetjpjormLr2itLbnbGGc+3Irj9U8HrYJ50yEbuoPSvWIbZEbzJOVA6VRvdLh1x9ske5QeBjrXRTmRKNzy2ynZ42tbG3bzm+USY4Ga6Pw18IXsImubn57h1/1hHIr0HTvDVnp6rsgjD47CrN6kk9q0a43dvatHVaI5ThND8JpoD7irN5x79zXYaPpps4VkVSqrzipbbRHmeMMNxU10dl4alkiHPy04zdhuy3MZdLS6mEskZ3E5+lJrcaxRfu49zLxyK6ZdJ8mM/wCzVGbS/PzlufpnNKVyotHzH+2n+zXP+1l8MpvCjt9ijkOTcZPyD296+PfDn/Bvno2i6y0ctxJqEczK0szZXb6hRX6vDQYUC4Tc/Uk1ch8PNIQ2PLboR611YfGV6UeSDsZ1qNGb5po+Z/2av+Cb3w9+A2gxNDoFnNerwZ3j3OB9TX0d4R8Gw6NCsdlCYbfgYxnGK6Cy8PLbw/vFyWrRixbJsQbQPStuaU3eZyylGOkDL1Sx/s+ybC/MQCa4G+043epKzfc6txXoequHhbLNu9D3rk9SK20rM2Pn4+lVY2o3tY43xRpzeKvEUFvDGotbMAkY+UkGuV+J8f2NvOBX9zwAB0NepaTpseiWNzcN80kxO0DsK82+Kdobmw2rGVZm37j3xW0LvYqUUjwzxlYrJeNdMF81WLMpOOK/Pj9sDxXF8RPjrHoNixuGZSJoU5jUZGa+v/2zvjvD8FPAmpXsKNdag0LLHGOdpxivin9lT4V69L4V1n4ia8D9u1+5K20UhJKISf8AH+Ve1hoqEednBWk21GJ0Vh8O/wCxvCtzfbI42sV2RgjpkcAV5r+01eNY/DBY45C15cEM4X6DrX0n8QtEl0/TdL09PLk3BWl9uK+V/jJbzfEP4+WPhm3mVYxteYKemCOtb0W3K5yVopRsfTnw2W1/Zu/Y2sU03/R77VrQXM7g7WZiCcV+eHj7xHP4n8S3NxdSGS4kJLtnO4mvsj9uL4nxeCvAdho8bDNtaRxDafvsV2818P2CfappGkVmZiPmPXNeplVH3nVkfOZxXVlTRYnmNpbxjcu7ZyKr3tz9i0dv+eknao76ZriRR0JfA+lR6pN/aF7HAg+WMYIFe7M+eiFlF9n0/wA3d88vAFXrNWRejZUZLYqFYXvbiOGJdzJhUQdzXaeO/Av/AAr/AMLab9rY/bL/APemNesS44BPqaz5rlxj1ObtH+zDzF+aSToDxxVO/d7+Tdu9uKJrkrMsY5bHQ9qhubnYqwKMNuyTjrVCNrwl4e/teZWZW2hwFH94113xm8QXRtLOzAKxBghy2fugcU34WeGZk006xcRtHY6f1foGJ6Cs3WdWt/Fc7SySHyo3eXDDjnpXNy3nc6tYxsijLcxw6asjNmaRsAd1A6VV0uz8y7LMhbjkk/pWfquqLNIph42nmup+Hnh6a9sjdS/c34xW8pWVzGN5SsdX4L0eOC0EgDbnUkD0qDxFpshvAQ21iORnpXb6Ho5j0pnVVDRp9Mg1ymriS5u9y7WHv2rzZVbs9eFFqNkL8Qbn/hO2jv5mJkvI94kJ6v3rldPkbTbn592Rww9a1fB5k8UeAphGrGSwkDA9cetPuNOOp+RMI8NGNr8V4tOVvdZ6MoXfMiO0haS5kKruU9OM10nhL4YajcxteLayNjlOOtQ6GbfST5krbRGATz98+lSa94t1K8bbFeSQw8FURsfrRJvodFGlHdnY6V4auItPlXXlhtoZFK7dw3Kfp+VZXgKwk0TxIqruMcc3ynP8Pas+C9uLp42uJGkkwOGbOa7TwppbajqMMv3cYyAK8uvUtdHtUYX2PXtJuftFpF5a4yMiui063+zMob5mxk47VzfhlfmVXUj0OK6mOQRn5Vzngmvn6ktT1lHQh1eKOQYIGWHBrmrXw/HHqqlxuZTwa7CW1WdFUld3b2qhcWnlaqvKtxikqhm4i+HbF7rWT/dU4BxXomg6EqzLvCtjnOKx/BmmLuX92FLZ5rudOttkq7V2jGDS5rmPKaaWyyWqxL0Y85PTitrR9PaLaWXPGQap6LpbNIn8W79K6y3smKIu3avr71MpFLQ1PCltiNGYfN612mnpkBWPzZyM9hXP6BafZYF53HNdVptp5iBv4u5rnkUbWmpiJeMgdveuq8Mp+73BdvOOa5y0XaI/uj5eeOldHp0vkQxqOWIzxU7EnYaJEzBWyO/FdFZEbd3XsawfDqb44/l+8Mmuks4PJjH3uea6ImM5dywjgjgYycGrEUQU5UdOOtV8L8vPNW4xhcduoIrojqYyfYlRdi89Rz1qxDynuajjXjOKmgTavXr29K3gc1QniXJNSr1qKNyDjAwasLHk89O1b8pyylbcUxgGgRb/AJcfd5pyKRwM896njXaOhzVezVjJysUZLXac4FUL/T/NB/KtySAmq81iJCOP/r1x1sOmbUsRZnJz6WYew25rL1LTo2H3Mmu0utPwNvFZd7prR9F9q8uth5RPVo4tM4u70sNDngVg6r4YjvfvKCRyMiu+l07n5o/zrO1HSg/Kg5X3rlipR1PThVTPDvGXwnvru8jmjUNHnBHc/wD6q5vXbWbTTHFeLJHDGf7vUV9GLAQNhTOOvFUL7wFb6sZPPVXV+MEdK6KdaRTcXozxjwt4d0vVQt3bxtMynBQnvXQ+KPGd94S8KbtHt5ob/ftYRAgN+VbOv/CKfw2JJtGlaGSQfd25zXFX9vrSO66lBceXEuBKvC5+lenh8a0c0sFGpqtjq/A3xRvYtJt77UtSS3bO94JDzMB97Oa2tG/4VT+1jq0wvfA2j6xZR5V7qWyRlQ9DlsV47e+GofiA8Om7ZI1tzueRn2kHrj6V658PPF//AAqvwjDpenabb/Z1OwyKO59a9vDZpKKsmeZisqhulqeieE/2N/gt4WtVXS/BPhW1kY+YjJYRBxj0OM16B4G1rR/DMsmmWCWsH2cfcQKuB7Yr5r8LfGcL8QZre7VplXJzG3UH0FejaJoHhnxXqEmoWeo3drdSJ9wzcKR6ivQjjpzaZ5dbLFDSo3qe0WvjKHWbllSRl2HaQxxk1l/GNlj8LyyL0K7SQB0718x/Ez4j+JPAV/c3cdvd3NjpL7mngJYSR9zx3rPu/wBse1+NuhbrM3dlYwQ5lmlynmYzmuiOKlJNSCOU8soypvQ+KP8Agqp4CuLnwndXVnbL5MUnmROU+Z8NkjNL/wAEmv2lrXVorfwreReRMAVhjLZ2+v6A1d/aD/aHsdXupIpkXUNPtiSwfJQj9a+Rfhb8XbDwf+1NpuuaTbvptpcXJAiDfIB0PNeTmEVUpPyPpsHQ5Y6n3n+0p8L5PDf7R8erRxqsN5EMsF6kc8/nXtXwhlaOyhf+I4xxWL8TLb/hY3g/R9YjaP8A1Svx/FkCuq+EtkbjTY49wbAHFfA/aszui/dPVtI1IpborNuNWLvUjGhY8VQhtMRqVI+UY4qDVJ2SHB9K6OayMVFNlbU9W8yRiO9VLK5Mk/zevGKzb+5MLf7x7VY0C5+0O3qKz5+5Uo6G5b2zTzYPK1oW1ssQO1enpU2jaYZkXn3rotN0NU9D6110zmlUUWYNnpsl1NnovTpW7Y+EfNi3Hj1rasdCUPuxitm1sVRf71dcKbZxVcVbYwLbw/HaqvyL9cVfMISE8dBxWk1qrkZ42+lLJZCSPFbRpnP9Yvuc5eHeSKpiFmYbBx9K6SXSQ52gdKI9FVfqKJUmzojiopGPpmhuXDNj1xW5b6asfUc1KlrsqUoY0+btW1OmkctXEOTKtzHtHXAAqjJKpf8A2sdauXv7xSvIzxWXdM1nGzfeA9ap6GlHValTUZtkDZP/ANauS1WfzZPmwe+OtXvEevrBnzGCL61xer+NIrMMY2Env6VnzXPSpRtE7KaOOLTNx+6FzzXivxW+JQurqS1hhXbDlSw/GtTWviu0luVSbZt/hJrh21KHVNSllmIXfweOK7KMtDObtufIvxT+DGs/GH402a3C40+a4/fo6lozGDkZ+temfGH4d6bo+oaLoul26x2NjHmaNI/lOMdP1r2bWG0+z8trfyd3Zh1Brk/FUtuZbi4Yr50ybN+6ur2zasYaXufOXxDhtdHsb7WrhVb7OpiWInj7v9DXyB+zx4R/4TD9oG+8SXaM0bTMqD0x0Ar6s+N+mTajczWMbE2zEsyFvvGsn4L/AA60r4a/D2+1a8jWNbHfd7nO0fQmu7D1XblXU5MTFbs+Hf22fEFz4m+LVzYCRnitZyGCtwuO1eV3zrp1mo+YMTye9d/8Sba6+IHjXVvFK27rZ6nduYwB8uNxGc1594w05tIvUglY/Km8j0z0zX2ODiowSPg8deVRzKNoTK0kzBv3alsGm6YzJvm2li5/Krt5pz2kUNqqnzLgb2A6gGt3wX4LWe6ZbhisWMbiOGP92takrHLTpuTsjtP2Y/AscXxDsdW1u3VtHt1aWQP0fHSud+OnjxvGHju6nX5bVLhvKU9NvbFena/40t5vhVHo9jpnl+WAr3LE5lYZOF9B/hXgPiB/9M8tvvxsQeeM1NN3Z0VYcisXfCemrrWuW8UrbInb9456gd/0p50+2fVJDJI3kq5VWA7ZrKsb+W23yL8qqNp7DFejfs3fC/Tfiv44hg17VYtF0OMmWa5lPGFBOPqcYH1qqklFXZjHVkWueJ7vTPhR/Zkc7/Y7qYPGoGGOODmuHurp4dL8lOWfCDmvaPFtn4S8SfGI2dnfNB4b0uCSQvKQfMEaEjAGPvMB+deIo51LVZljTEYYlAPTPFZUnpqaS10NDw14fkurtXkj3KSFAJr2v4M+HpNVvjaKirEDkAjhu1edeHvD1w1zDGUb5VG0AdSa+ufh38OLfw14JtbxYFW4m2kk9RxXn47Gcqsj1svwfNK7OW8XaHHouhNwFYp8wU/lXkus8XA2fL/WvYvilN5Ntu2nrjHXrXjfihjDfKPbPBrgo1G1qetWpqKsix8HtX0nwzb38d4Hka4h2eXH03Edc1X1W6ksnmbaFt92EUVzuhabNpHiy4gl+7kqSK0tQkOp6bKAxUwv0PU1yyspXQRu1YoyXlxq8rLu6N244p17qzW08aKqsUcLn+tXvDtktxKse7Dsp59eKydQTfaSSqAJIXxt/GtbqxUW0zvfCFq19LuK5+XGa9X+G+mtbqrSbcKcAHvXnHw9h3R2rKA3nMARXtOn6csLxxfd+UNwa+bxkvesfQYdKyOltyttCGVfujIA71d0ZpLpGXHzt8wyelSaVo3nW6v12jA966DRvDjM3msjANxn1ryJzPQ6GeNMkPljlWzz6Gm3WmsmtW0f3tzA5rrP7GZ49saksvXPas64s93iKxjVWbHLcVm2SdZ4b0jy/Kbaq45PpmuksLJTdbm7HAAPBqnp1lmIBVxtHI9K39Ktd8abl7/ypqVkYyRseHtKJjYgZ29PpXSWNgXZVXJXON1U/D0bSwELgY6iuk07Tjb7VyGJb6YqJMlFq0tfKUK21mz1FdBYoyf3l9qy7aAmQbgMqcEetbVsnmbOMj0rGTKka2nRMz/M2dtdXpUG9xx2wTWBplkGCDpg9q6nS0Lz7fQjr2oWuhL3Oi0RdpCr2HUHpXQWkn+0WH8qxtLtRCrMuPmxW3ZndF/snmuindGUy7HHufa1WIfn9qhtf3vPXtVq1j8tvQGumBzNk0XP3QF5qUZRu/0qOLO8NtyOal27znj3rrhqc89SaNfnUVZA/PNQRfK2atQy+o/GuiOxyVNB2zBB9KsRxZ5/yKjA3n5qnRQMVrGPQ5pS6CMuB9P1oe3BGe+OlTGLb+NGdwxSlEy5rFCePanTNUJlWT+HFbMsPB5FVntlbtXHVpXOmlWMmTT1lXgA/hVGfQgf6Ctw2rIMdT7U2W0YiuOWGTO2GKkmc3LpHlj7u76Cqt5YeRHu2fMK6h7EMO/vVO8siDhRke9c0sO0dtLGN7nF3ryRwNL97afu45rNTT7XxdCY5lZeeeMZruJdF3n+lRt4ejj5VVXHpUKkzvjioKNupws3ws0jko/2bzO+OtYWvfDiXQfLe1umuo+rJgbWr0vWPD0eoxbZGPuc1ljwx5EPlxtI3oGNVFNKw41L6tnl8HwKvrnUv7QFuy+Z93bx+dEuj6h8OtekaKGR4ZF2kHv0r1zS7i/s4fLkXco4HPQU7UtNXVolE0KgjkEjkV1UcVKLMqkm5Wlsef2nxitNHgGm39jI1jecSKy52k9Tn0rk/iX+z34f+JNuq+EYvLjz+9SFtofPJGK9M1vwVa3yqkkKtgYBAqrpHhNfC8zfYW+y5BwF6GvXo5i7WZh7BJ80NGfLH7R/7DNz4N8Mx3tpo5k0tY91yIwHcZPIP/1q+F/2yPBXhv4Y6do91Z2A03Vp7hSWXLIqfT1r9qbDxFfaro0ml6lDHcWknyHnkivlb9v/AP4JcaL8XNBj1S3vrfS4IBvbIPHf8OmOK6KlWNSF0FPFzg+SoYH7JusH4k/AnT7eScXU0NuqYHyt04OK9z+F3h2bS1WGWNgyYGa+S/2Cfsvws+N0PhldQa+s4sQJMXyshXg8V+jZ8Kwx3fnJD5asB0HWvisRh3GpdHZ9Y5dH1MG30vyxj5cdeKz9esgI/l9a6yXTfLBbHFYeurhO3PrUvbUcJXehxGo2OU55+lRaFaMbgBRjmtPUEby9y9c1Z8LWfmSZ2/p0rPU3lLQ6zwvZsygN6V1lhYZIwKzfDumgBW79hXUWNt8y/wBK9LDwZ4uKrWYtvY4xV+O08tasWtqMDtVkW+3tnNexTpaHjTxBRWx3tkila321qQwMwxtptxb7UPy1sqJh9Yd7GVLGoHQVAxANXZkC1XkTYN39KlxsdUJXIAVFQ3M+Dy1FxLt6VQurnglmrCTsddOnd3HSyKZPmJ/Os7W7uFbZlZwp/lTp7pUTczYAFcj401iFIZGWT65NYSqHfTo6nI+PtWksUmYf6VH6KMkV5Zr3imxuiFW6axkbgpIMZrX+JHxFbQ4i0Ue5mOPlOTXzj8U/i5bandsuoKWbBx5ZKsv41pRpuTua1KnKjvtd1K4hkaS223CqeTuBya4/W/ifeaWGF1byKqHGVFfOvif46ahoOsKLGe5kgU5AMhx+NYPiH9qjXLhPLMCzJG2WJ7161HAzeqOCpi0tz3rW/j1FbkMkm1u4cYzXN6l8W4tZ37boKxHILfKD7V8zeOv2hJtdZhcWM0B6bgP5VwviH4qXXh+3knjkuJFUjcmCc13wy5s5XjrbH1LrGorfSlnnDyZ5O7tXm/7b/wARxoXwej07S5lZrqExSKuflz614nF+0Pq89v8ALZXYhmHDbDj8TXJ+PPifdeP7rT9Lmjk8qCdS7c5Iz6134XAuEubscWIx3PHl7npPg/wTptp8CrazuCzTWdq17Mcd+w/Ovlq+1+HxLrLCRW8nzcSuB1AzxXv37QfxG/sHwFNp+kxNHNPEkBbd99TyQa8l8CfC3PhFfMhb7VcE4PoTzXsYeXLFymeNiKfO1CJR8GaXceJdfnkt42aOM4DEfdUV7l8F/AOkR6HLqGtymOzbeQMZyenFY/wa8Jw6BpmoSSOqNIhhUkfNuxXUa8bmbwRZ6Vp8IuGmTBdegGcHms6tZylY6qGFjCF3ueP/ABV+IMMmoHT9NRvscOfJG7GQSck+9eY3brNeuyqxjzjr8xNd38V/D1p4J1GZWk3XWAqAHOCQck/jXHaTYrDZteS/Nzwp9fWu6i1yXR5OIi1OzEXTJrq8trK3QzSXbhFReSSeMV9s/Dr4C+HPgd+zzqz+JWsZtX1Ky86Ayyf6knBGAvPQHr3rwr9iH4O+K/HPxOsta0nQTrNrZyYk8yMNGpPRsHrWv+3n+0U2sX7eE7eCS2vreYpqL8BmYdFXHQDHQGuOtKVSahEmFo6s8J1Odria6mhZWa4kMaIoOdg7/jXSeE9Ls9F0uGa9jZjIeiD5iewrN8CaBefEjVNlnGtu0aqkagfNKRwQPf3r6a/ZX/Yuv/i94687XFWHStJO6WJXO3epAxnvWeIxUacdWdmDwspu6Om/ZA/Z3uPFMK+Jtegkt9PtlzaRsuDLXsXjeO1NvJ5Y2wqMKo6DAr0jUrBdH0a3sreJbW2tBsSNRgYry/4gPtT5W2rI2Nor5KeKdWpfofZUcOqcLHj/AI8tUuo9rM+1vmDfw14346s401j7xXivbPGkSsWXzNq7c4968T8fTLJrWNrKFXA969LD3Z5+Kasa/wATdBh8O/Em+t9uGW5ZskcqK4q9m/s+aReu+T9K96/bI8Df8I/8ZcxMrLMwZzjjJxXhni2zY65KNvyqcD34rkpyukyqkbXaJNM1VNGmWZlaRQ4OB2FL4i1LTNKimjt/3z3jF1JH3PQGqco82wX5dvHXNYp1W30zURNcKHjQ7iM8njiu2nqrGMpNanp/7O/iBfFUvlq0ZltHJkAP3cV7/wCHl/tK5eZmVm+6uK+MfgF8RG+EHirXtZntmk067Roo9/AZz6H15FfVH7PPxH0zxvNAsNyu5hlwDuwT2NeNmmFlFuUdj1MsxanHllue+eGNNjSGNWX5WAOTXbR6ZGunRouBzkY9K89tvFK2dyY2zsVeuOld34R8VWdxaqVmV/LXnca+dt1PauxmoTLp5VWYfvOB7Vk6dF9o8WhjjbEnO3t6Vc8S3Q1TTJruBY5JNPzIyKev+cVX+GEy+I9Pj1DG2S5O4qP4eelZybLjax3mh23mIu47c9feuosNP4wFJwMA1R0uxSG2TC7s1v6TayTOq4wF5z6UGEi/4fs2DKxyvHOB1PpXU2lr5ce4/N6DHSqnh7TSkSg9zW7HaLGPvEntUMkdY2wFwv8AeA7+lbdlbZeNvqOBVOygZpFZR83BOa1oF8tlHU5rIDU02Dcitu285xXR6RFiXd8vPVc9ax9Li3oN3VORz1re0mIFWbuvT2qogb9hgFVxjPBArct1aOJV25wOKx9Oj8woerKck1rwTKRhd3XmuiJjIt2bARkdF6nHartu2D3Pp71Stk2Pt/vVoQWxTr9M110zlmTwRsic/lTlXA9AT3705IqVoSGY/wAIrqic8mSRMrKtWYj823HNVotyLuYfTirEUm48enpWsTnqJFkcN+FWI04GOKrxMc8/dqzGd2OldETjnoTK2eoOaGj+ahHOeKcozwa0tcxbIygUdKjNtzVryufbFNePAGazlDuT7RrYpSx+XUTHAq+8fNRSW6kVzypm8aq6lGcfKdvX0qsE3H3rRaHbUTpt7VjKmdFOstip9lVl561HNYjbV5oN3WmvB+H1rN00axq+Zjy6b82dpojtFU/drUeDIprQK4I9/wA6n2J0Ku7GZJaKTx8vc8daSO3U8bc/UVoPGsanimbFzQqJftropS6PDLjIH5VVu/Dscg+7+lbYjVytTJArrjGPatI0uxKxEonGT+GVtn8wE/KcgYqr440q38a+FZtLvPMaKZdrDPau4uNKWRDleOn1rOuNJWJWXZ19q0vKGxftY1Lcx+f/AMW/2LW+EXjy18aeG7i7drWcPLAgyAmeePU19y/DPxAvi7wDp94wkWSeFWZW/hOBRdeDUvDJHNCrJJwQV7Vr6F4bh0HT1t4F2xxjCj0rhxUeZ8xrOrFw5SLUUjgixjtXG+IU+0M235f6V1WvvsX/AGq5m7BllwfWvJqSWx24dNK5y9/F5C7dp+tanhK1EkwwMVJeWqtJ174Ira8JaT5cm4Lx3rOMXc6KkkoXOm0Sx2gD0FdFp9uGZeKzNKt8Hit/Tk3FQRXuYOKejPlsZU1di5a225+lXks95+7S2VuFI96vpH8vSvoqVBNHgVKzuVDB5Q61SvZVHQfjWhex7EzWVMnH40qy5VZGlHXUoXa/NVG7lwD81W7uZQ2M1mXkw2n5uO9eZUke1Rjcz7+8ZFY9h6Vk3N6GXJq1qN4soZR3rNuyohxuHqa4JSuz26UbIy9Y1tY7ZjuPy8Y9a818beIlmtJA25Q3Fdp4ov7ZIzEsiqzdq898c6JAtlu8wtuGMZqDrijx74o65DbWp/eSKP1NfPHja+g1F5P3DtJnB45UV9C+O9Ba4k2x25m2nOT6V55e+BpJJZZJLMQqwyCw5FepgpK5zV4NngvjnSdNltAscDKzADEa/eNcLr3gq3XR5JLPzftHUo56V9BX/gqG2WSSSZnbfxGq84rldV8F2ui6n9ovJtsJOTGE+Zl+tfR0aiSPKqU7ngq/BbU9StHuFaNpGAkEIG7Fc7r3h/xdZXf2f+y7d4ozks8AIavfNX0zT9XvZjp91Npsajcrv8px6CvMfG00VvcfZ5dYutrsRvU5/Wu+lUuzgq0ktDzHx/4j1KzsYbO8tLWPHCgIFUfgK8h1idtN1xpJHRSo52dM16R8VdPt4L3Nvdyagqcs7k5/CvLdb0U6l5ztudWBxjoK9KjFM8rEbm5pxtvF8UPnN8qyBiXf0/8A111F1rC2GsQfY5I1tbdi3lqmRtA9a8bsru48L3XlH5oWPfNdZpPjpbZmj+XEiFenCZqp02ttjOnW1s9zuk1qE+HJCoKyzSO5J6be1dFofjFPAnhqG8lZvOW2aOMD7q5z615bB4jt9PXDOsjyEEZb7o78VjfFv4kSa+sccbeWsKiMRr0IA61z+ycpWR0yxSjC5yXj3XLj4hfEG4uG2hZmJIH3VqZrQatcW+n2qibcQCF9u1c+NQayjkVf9ZJ1IH3RXQeCPFEnw91JdQghgubqaIqgYZMRP8WPWu6UWo2R4iqc8rs908Mftd6t8EfhZN4X0X/iUXRwjy252zPjscHpXzV4jnv9d1qTzorq41S5m3u5G5iW7/rXY+GfDuo+JPFUcMdq15qV8Scbc+Vk5zjuea+zPgn+zFa/BS0stV8SW0d1qn2YzRwzJnexPy5HUY9686rWjQV+p6WHwTrPXY85/ZX/AGT9Xs9a0hrqNYdQu4f3Ei9YwRksR2P1r73+FPw2s/hp4UFnatvkjRQWP8bAck/jmsH4HeA5/AcV7f3sRa81FWf5+sRbG1V9AB/Ou1sLcjzGZWMobla+OzDHSqSsfYYPBxpxOV+IN3IZEX5VXPP19a8p8cWiT2TswVhHySOpr07x5dtNqEjMPmiULsHGPevN/GoWTTd3l477j3PpXLh5ao7Kmx4f40mke6mIZR5a5HHX2ryTxHCtzfeZJ1YcAHpXrvipnuHuo5FWPcGJP932rxfxZr0elXyx/e4znrX0mD1PBxdj6p/bF8NTeNNaaWzt2a+tfm46lQAdxr5i8WaQ8dxMko8uVTy2e9faviTUofEtlJeaPbPdSNprIx3ZLnjNfLHxb8PPply0xj3SMNpH9w9a8OjUd7M6pK6bPPU0tpLRY+uBkkVw/iiy8maReWVCelelaNIJFKtw2SD7Vw/j+A2E8+1d2Tk+1ezhpe9Y4cRflOe17U18QfDqHRQzeZFO8yMOhYgfL+lc58CPjBqXwe8bxzrI0cbP5ciP61L4huv7PtYYY8qZDvz71jeI7Qapok2qBB9st3RZ4wOvP3xXt06MZQ5JLRngVMROnUU4s+1PDX7b/h291pbXVJhZzqgU7j8pOOvPrXodt+0j4VttGjuo9a0/y7ghWAfkH8+lfmX8S5JB4iDN95okP5rXO32t3wtFha4l8voFJ7V50uF6U7OLserT4oqQ0krn6c+Of259G+HktvYw3EN3NqKqqJGcrIWOBk+n+NfTvwOj8/w5ZNGu1GQPhe2eTX4zfDWO6+KXxU8J2uWeK3kghP8AshWGa/bb4IaY1j4dtUXHliNQf9nivl88yylhOSMHq9z6LKsynioylLbod7YITMkf3jnp/Sux8O2BlclVx9e1Yvh/TVLLL1bPpwa7bwvYYQPt3MeD9a+cPUkaWm2uwqMfLjOcVoRWYZF4O7r9KcsPy/dBO3Aqyh8scfexgik2TfQlsIdxVu7dcdq0rWJSrfd9M+lV7KH931+UmtDT4xvZfSoA0tPXyoFzuXnj3re0tPLAb7wYcismztfPK56rWtAfIG5cDnGPWmgNixmYt8u5cj0rWtdzSBSxPqaxbKRlUFv73A9a3tNbzIWZfXntW8TKWxpWUZ3Ix6gYrQC4yuenJqnp7bguF6Dir8aDGa7aRxTepIh8sZ+b1qVDvjyw2t39qbCST0HXvVhyQ69MemOtdMWcsxPL3p2PPapbZNvSkCKq8fL7etTW8eRXRE55Mei7m6cVLHJjPNMAYD1qRYtvWuiKOWbTJkOG/lUgXIzTI49oNSKuw/8A162itDGQ45NIIy1OVtw+7TlLL2o5bmYzZuzTGtuOatdByKDGHFS6dyeZ30KL242/7X86Y0AA7Gr5tuOfzxUb2itxWcqTNI1UUHgJFQyQMP8ACtFrfAoe2UisXSZtCt1MeWJkGAfwpvlMR/nmtSWxz1/Cq4syzVn7No6FiFYomLIpggLSZ3D8q0/sOD0oNgq8j8anlKjiEUVhY/8A1qcsTxnqTWhHbqgx7+lO+zKD79adhe2RUTpzTZ4MmrLwbqQZPb8RUS1GpdUUxbqp5qtqEpVWxWjOMD3rL1Fscd8Vy1tjooy5pGJqjec201g39qQ34dRW7eW+wn8+aypsCUq1eHWWp71HRaGVbaf58vPrz711Xhuw8iLrWdZ2y5wvy10mmWmAK0owuYYupZWNjSoOM4rVsrfdKv8ASqGnR+VHt/lXQaPbBiC3WvpMFRb0PkcXVtqaGn2W2MZqxJHsHFWIIAsdQ3coQkGvp/ZcsTxPaOUtDL1JgCfm+tZN7JsU1oalLh81k6hIGU815GKkethYszL+X5qw9XvvIXr/APXq/ql0saHJrjfEmr+Uv+7XgYmtZn1GDw9xmsatsUtnb71zmqa1dTRMtvuO7im32rm7O1m4q/p19FHaY2CRcccV5kqrb0Z7ns1FbHEX+kX9xc73c8/pUepeGpbi02swLba6TUrrdKxC457Vn3AydzN17VpGTvqEjh5fCEdt8swZt/pVLxB4Ct9QtdscYDdMkdK7+7RHC/Llh0rMvE81vl2qc9u9dlKs4s55K54n4s+DPk3g2Rptx8zbM5ryf4vfC28g2tZbruX+GER4r611RsfLtHTNc9q3huO7YsIVZ+xx1r0aWOaMZUUz89PjFoPirRrWNL2zazRzhCI8DHua8L8VaZf6RdqMtMOSzFdwXNfqF8Qfhhb+LbU2t9b+cnPJP3a8L8bfstTaZPJF4d0WO+a6QpmZsrD6kV7WEzJPRnnYjCXWh8AeJbWSWDhVyuSOMbveuInsdQhWQt8qt0Gc8V9c/E79lzxd4RvAsmiJJbqMkL82c+4ryTxn4AXRbWaO40y5ju4+SmCPwFe/h8YraHg1sNK54DrVvI1qSxVs8DjpXJySyWbvvb5hnpzmva7z4e32pxrHNbNaxzKXQZy2MV55rngGW2u3hjj/ANI3YwfSvTo1k1Y8ivRknc5FtRlkbcZFzisnUtae6l2qdzg9a1tb8Ptp8g8z3wF70WWjQ2llNcvtUqCQrdTXTGKepwyctmY9paeV88u4tIDtHqK7n4Y/Dy41FZNUlUtDGQgU/eYnuBWN4T8Otr+pwkxMyB9zkf3fSvoLwF4QmkS3s9HjQ3l0y+SztgIR1z26+tc+JnZWOjCUU3dn1t+w18DvCPwA8ML4m8d2rahrFwjTadbADcjbcqX4yOcVk/ErVLnxvazX9xdMs02pxAxqfmSPcGC/TpVP4F/FPxDrVhq2g+IrhbiWztnaIygGQygY2humKwV1pbCSz1KaSSNJLoSNCyfLlevPpxXzdVSlJtn1NFRitD608R6vDrHgd7q1/cTRqmDnnIUDj8qp6N4lXVNKjlVf3siAH6jivNNC8fNqXg63ilbEZJkzn7y5Jz+Vavh3VYr3T42jkYRMo6de3SvmcVRak2ezh6iasHim6+2X0nzMZFGMY61w/jqXfpKxqV+Q5IPXJFddqF0qxSzL/Cdq56muP1Yx3FrJJdDbubJVT3qaN00aVNjwf4nXf9myykqyiQYJxXls3g6XVp3m2rszhMc8V6N8XZW1XVpILfP7zlSOcDoan8KeFLP+zVNxNhiowD2619RhZcqPCxEeZnvvwJ8Q2OraFqVqshtbia2mt42QY8t9nQ+leO6l4UuNcsdQjvlPnQlssRy3PWtb4e+Jrnwr8SLiwVQougUIP8L9M11OqX9vdyrHcAQXm4ozgfI2ODmvmZXPRtqz5f1zRH0HXefmR+jDvxzWF4s8NNqsjMv3Wj3Y+lelfGzwnfaZ41aSOPNrKmVZeVB+vvXO6DHDrW5GPlyQ/fBPT2r1cPVdlI4qsbqx8/fEeyXT9Zt4WG0LHnntWXJqMNvo6PNtCuDHIMY3qf8ACuh/aS0mXSfGS7iCoX+HtXA6hIl5oW5j8qgjHvX1dD3oRaPlsVG02mR/Fu3WK6sZEVtrWy9f4vQ/lXFai+5Fb+LHWvVdXtIfEHg7Q9xVWmgaBWPXcpOBXmusac9rcyQyYRoR8wx3r0KM9LHm1I6nr3/BPfQ5Na/aH0aMqzxqTKeOuOlft58LNHCaRGqjYqgDp7V+UP8AwSG8CLrnxfu9QYMyWFuqjju2a/X/AOG2ntCvl7dwwCPavzfiyupYvlXRH6Bw9ScMLdnU+HNJ8q3XgcsSa7HSYgkPy444wKzLK0bytu3t6VraVbBIlUfWvleY94v2tqLkL0XaOvrVtYMHdtzsPHvTtKRiD/s+1XfIVmDH5VXjBpMNhtpDiReBlhyK1LW2MaAAcjrmq1tZjd7E8VoWz7n6cjkmkBftYtmcMv0q6CqBR6+vrVa2fPOPmbA+lWbdWkmZW+bnOTVIfKaOnS+YF3D5u3vW7ZSbIvu7fUVj6dGwk3bThf1rSupmFvtXG4jitI7XJklsb2kXiXH3PpWmiZPHrXPeH0VYFxneODXRWjsU6V2UJXPPrxtImQZkzUwwTzUJX+dTxIK647nFOQ9Rjbn1qxCN+D0qKJd3y+nSp4hsY+nFdMOxz1CXaN2e9TqFkqGMb5KkRea6YuxxyLG3eKFXFAbBA9akVdp9a6I6o55XGqny59akjBz/APWoDVJDHxWsYoz5gReKkSPf3p6RblA/pT44sDtW6pox5iExZ4x+NNa2BNW1UNSCHKGlKihKWpTZNv3ajeJiKutDgn2pkgwv3azdFFxqMpCPGaTy1JqwyZqIxBTXPOidEZEbIoFMkVQOlPc56VEx2nH51zyiaRGldy+lNY7DjinM4U+tRvIAB/e6c1g4m0bkiMGSo5T5Yzim/dHtUc8qsNv9aykjSMdSN5N5PSqN6FKnjn1qSWcLn1/nVG4uWdWG6uSozupU2ncoamm4jr17Vlm1/fdM+tbcqCQVVFmpevNqUm2erSqWViOxswG+ZV/xresIeVqjZ2+D8w+hxWrZKc/KK68PRODFVDT02Pe2K6bRYFCj5eax9EsmZh0y36V1VpbiGH5vrX2GV4XTmZ8jjqyvZDmk2RVk391yavX84ROPSsG7uTITXRi61lZGOFpX1Ibu43HNY2q3Xlir99NtXiuc13UREjH+LtXzuJrWV2fRYKjeVjI8RaoIFP8AerhdZM2pSZUtgn1ro7/zNSlPpSQaV5arwK+YrVJVJn12HjGlHzOZh8OuxXd29auTWH2C1z0NdBdxfZYQ2PpXP63qpddu35s9e1KFOy1NPacxzupyMsy/wrVS8n3LuPXPynFWr2TzdzMyjb1BrKutYtrWL958zDnrWlypRuRXk7KCzNuK1l3mrCNV28NnrTrzxHDMjKv3myFz6VzF/wCIo3dhuVlUdO/vVRkT7M6SC7+3BjIyrxjPpUVzeLCyhDu7A1xl/wCLo7eNVDfLKcqQa0PCerx34Zg25ccbjjFbRvYmSSNG8sWvbdjnDMfunvVVrBbWFlbcjMMLitO5m+bdE6/KuDg5xVSSNGdfMkG7rk9DWkKjRny3Ocv/AAn9rul82Ey7jkIx6Cs/W/gBoPiqJlvNCs5Nw+Z2XLGu5MkLbCvzydye1PhcwPtmdisjcADoK6qeKlHVM550UzwTxR+xX4PeWZYrVVELEuYxkk44UH0+leEfEb/gmzp3iVNSutP3x6ouZEVm2pFgcKeK+/rO0hv7hvKhVl7nb3ovfA9tZXYk2lpJuZF67jXpYfMqkXe5y1sDCSs0fiX8V/2MPiN4I1Ft2hWepR27eYhiIKop9sc14r4h+HF7Prrx6hDNb3HClNu1Bxmv3m1/4S28t9cs29vNzkjnYMV87/Gv9nrwzFeTMuix6hcMeJFiCsnuxx2r3sPn7taR4tXJIuXMj8p9MtG0ZNsVwqtbgs6mLGe3WvQ/hp402w2kccwS5ikG1mGGOea+k/EH7PGl6HdzS3Wmx3Fu5JeOOH5gP51458bPhhpujyLN4f027tZI343Rk4B5NegsdCroznWXyp6o2fG0mpaNq73y3EktxCgeQxvjzFOOSKPFvjiG8+FVmi/LdR3J354KqT/9f9K8k8T+PNY0e9s/7V3xpKoAkc4yvXBrS1m6km0/7dpe65s5IwZY3PETf4VpGkt0HtHHRnsfws8b3Gt381tNcGRLdBEgJ+XaMc17l4SlhS2jjSTzIo1IjAP4/wBa+Sfhd8Q7aOGTzmFvdRx7Yii4LnPQ19AfDDxWot7H94WN1tCOvqeoNeJmeHe56WCqnfakv2a28sbpBIS2PQ+lcP8AEXUl0rTzH93zOQcfd7cmuv1KdFvgu5guDuJPXFecfE6+a6tPLXmKRvL6c88142Hi+ZI9SpLQ8907TFvtUmmkhZnZfvMMEIOprzvxx4uk07W2jhcxwjhFDDIxXqHjTUJPD2hSmDLfudjt6jNeB+I7xrvUPNZlDOMkE4xX0WFi5Hg4qfK9D2TTPE7W/j/S72YN5cVwrM27lh3Ga9G+I9gun+J9ShjLbbhRcwlvQjtXn/jTTvs726xRqJbeRdy4612nxL+Jln428R2tnDB5MlrYQ25kVsZcdfzr523Mkz1JaM5K08VM1jNp+osk0O0hQ4yQe3PavPr/AEKPRdcdoyyPMQSH4DKe9dV4r0e40bWzKyhlbHmKemKvasNP1XS7FrxAqynZBIP4GHYmtIScdjOSufPX7Tfg5rLUZLif5o2UFPoeleGXdv8AZdK8t/4nIr7Q+Kfh631KK4j1a3E9rbx4Ux/6wjHUetfN/j74VWl5b+dousWstqzbhDcN5cqn054r6jLcVePLI+dzDDu/Mjjbp2h+GemtH963vJFBPbOCP1rN13Tv+EkhjvFCrcKmLgDowH8X8q6fV/Dtxpfw2vLW4hlW6t5hNHj5lkU9SCOK4awu5biyVV3CTPAPcehr2Iyuro8WpHVJn6R/8EV/hk0fgLXNakVdt1OsaHAyQBX6SeCbJoEVtp2sOtfK3/BLb4Yr4I/Zf0ING63F6nnvkd25/rX2N4csvKWMKvyrzxX5Fm2IdXFzk+5+mZfS9nh4x8jWs4v7y8A9q2tIscJhmPJ61W0614ZsZrc0G2Xd83rxXnxOos2dq0e1QNvHGKtNBnDHt7VYeDykDfeK1JDF5oGc+9USmR28fzFvVeD61bjixt7noaI4lQ/7OMCp7dA49PwpFEkRWAhfm4q9aybv4GG7Gagt0x83rxWjZw7htbgrj8KpIpF+1lVtuM8HB9q17aNQnK89az4YU2Ko+ufWrVs29toY9RitEzOp5F20tTHdF42IHXBrbs7lio+lZdkwUr2zwc1o2ZKn5eldFLc462qsXRJnFTQkMfun8DVeA5fmrC8HPrXdA4J2JlOxvwqUMS2N2faosFxmpI1yQf8AIroi2ckrE8bfN97BFWEGetV4lyenNTodxxW8ZHPJdicHDfhT1Yn+Ko422n/PFSBSTXTGRzzHg5XHv1qeFtp61Aq7qejba2jIxlFFxOKmVPmz+FVY5O1WI5CRXVGSZzyumOZd1NyYzzTjJTJjlTVORKEZ93SmMcVUnnaHmhLtpFrOVQ29nYklcZxVeeTYPWpHfcPp7VWnkDL9K56kzanB3GPJ+tVZZfLbd19akuJs9Ko3EuQeu7+dcc5HdTplk3YB6ZqCa8wOv5VWa4aJfWqk1zuP6VzSqHVCjqX/AO0ML61BPeb146+nrWe9xhx2p6yblBzXNKo2dMaKWo55iwzUTS/P9aVjuO2k8pQ1c7bOlJIcVyvTNJHbqx9Panp/kVZgtxnPNUo3ZnKdh9la7h9K07C1/eLmorG1wea2NPtFZ1+Xp3r08LQbdjxsXiDa8OaZsTd61q6i3lW/B/Wl0m38m2UY4xVbV5SG219nTpezoWPlnL2lUzLic7Kyb6by6vXkmBgcVi6jcYfbXz+Mfc97C07sp6rd+TGWz+tclqc7XcnLHGexrX1e5aYsufyrJSIM/wB38a+YxsnJ2R9Pg6agrszkTdIVH8607W2Yldy8Y9KakCwyfz4rQjvrW2hYyXEcXljJ3HoK4KdG71OqrV00KeoWSzxfNxg9PWvNPiXrMOlMy7ljx1LHFdP8S/ihpnhbSHna+h8zGUBYYNfH/wAav2ntBu76ZtX1q3t44iVVITuL/wA6qpp7qOnCwk1zSO48Q/Gax0mOYz3EcbJnGXHJry3xP+0/cWayG102a6KqWDDJU/SvOfEX7TfheB9mn6TNfTMNwldSwPvg1j237XWqaTL5tvoFisLfKDJGMnniiOGnJnVKrGJta58YviB4s0ie5sdJnsodxSOSVTz7muSbXfilpNkshkhnZiS5KnavtnNavif9rvWr3QZDNpkMFqw6quF+vavP7D9tzw5aaPeRz6hbzXUKhYQZQvltznjvXpUcFUlsjgq46EdGzetPEPxbaaT/AEOObzOUHluUwemDW6PjN8UvA1jHcXfhu4kt1XEnlwO3I/DFVP2fP22bPS1t5ZpLW6e8ucRGUgpnoABX11pH7Qvh/wAe+MLCy1RNJtLSONXu0KjYxxkkE8Y5rrWFmnZo5vryex81+DP23obmBG16yv8AR2c4aWSFljB98jr9a9c8OfHbRPFulrJpuo2d0rrkSeYN3PtXcWFx8Jf2mPjxqXgXTLCyfQNNgE17qUCgIsp6Ip798186/tq/8E3bX4D6jHq3gXWrqOOU7xBHIW/iGMDPT6A1NbAJrXQdHHwlKyPcNA8TLMPOjuPNWTuvOK2Y/FAmdV+6c7fmPWvinwR+0x4o+E/iA6P4s02ZYowN12gGCuM5Pevov4V/EfRviJrFjHp9yLoSATyMH4HXrXmVsLOkz0qcoyPojwpYo9lHIzBVIyfXNbFnpkupXTeWjlVOExyTWdoZj0OxSS6y0chCxAfxk9K9N8CeHmsbATTKY5X5yeij0FZ0Z8xnUfLqzHs/h/DLbN50PLDOR96uV8R/B63u5nZrdVDZHAG7HrXsTiPyxtI68n1qnqumLdKVVQze9d8ZtHJe58ueIv2XtCmv5Li2K/bCctvf5fxrxb4ifs0Wp1jz9Ua3jEcmCUG6Nh7mvtvxD8PluEdlXbJICGcDkZ9K8o8Y/C9tHt5CsrXEe4lknAK59q6adaSe4clz4G/ab/YU0Pxx4LZrPyImUfu51kGBIBwMV8IeMdI8S/s/+Jrjw7qVu8kTNuXI+WZD6flX6vfH74NS2VidV0i6dZIl857d2+Rsc8D1r5j+MfwxtP2i/h9fXV4y2+tWYzFIqgMpH9O3417+XYxp8stTzsXglNc0dz4l0nV9+oLfW7GFbdt2w+h4INfSnwf1KHUryxNqVdVInC5xgcE1892Wgf2LeXWk3W1bhiySFR9/aeDmvcvgX4C0/wADeDtL8Tp4u0XULrUy9u+lwu32qwYZ4ZSMYOOucV6mOipQujy8K3Cdme5eIr83U8kibWdgQqL2GK8/hgk8Q3LQSlT5ZLux/gwen5V1d/dCPw9HPHukkkPDYxwevFctq1zH4b0u+ufmVvK2kHpuIr5amrOyPcqS908z+JutxzRSWqyKyZwdpwTg4AIr5/8AHviuOx1sxNnco5Of0/CvVPFVzHbx3F5cNtZl3hfQ96+edfvG8QatNcSfdZjs+mTX0uX0ro+czCs09D721fQo7m+G6Nt20gYH38ZrzLxAXTWoWj3IGlBJ/ugV7h43tJNHjab5d1vIVVvrXmHiey/tayknRVWSF8TY7ehr5KjUuj6Ga7FzxBaDVvDKjDNLEoYN3Za4fWZ5D4YhhVm/0W53nd6V3Hh8yXVglvG+7d8qse1c1qlr5+s3Fk21PP3cejD/APVW1PsZSKmk+IbXxF4iOk3UnDoRHJn7hPr7dK8H+OXw0k06yvxC2xoXJYAfeXPUV6NfWksesyXK/LIsRQ7f51Q0rXo42k0/WFF9FqCeUrP8zQt2OPTNexg5cjTWx5uMp80T5v0PxDe2zPYw3U5WZSoVzlQRz3qjoHh268VfEzS7OMqJb26SHYBgA7gK2/H/AIck8C/FhLWSPyVjnG09nUng/rXqP7EXwu/4S/8Abb0GxniWSGK7N1x0KqQa93EYiNKjKouzZ4eHw7nVUPM/Zz9n/wAGp4P+GOg6aAFNraRxnaMchRXqvh2Bow20dOg9awtAsltRDH5ewKMBR2rsdAtFlI7cd6/Gqj5pNn6PDSCRp6ajLGB/e61uadAsabiPmzVTT7TZJnaSBWvBbKyjnGTWkYi5iUfN7e3rVqCBRGvBHPSiGJC6+361etLXdn/Z71XKK+tyu8GFVWAH0qZY/lDNUxt/NI6gjn60KCZFX3osWTJHujGeWq9ap8ingHoTmoba2HG6rkYCKq4zg5zVFJlhZQF4Tn61Ysmydyn7vY1XaPzI+34Vcsov3S/7XWmiXsaVvJuHzfLWhav8uQx/xrPgXcy+3H1q9GAgGPwrenucdVGhD8rbuaswncapWr7nI5FWkbYPWu+LPPqItRnZU0TKq1Xt23R1NGuD2reMjlkrFiIA9D71Io5pkaYFSqMZreJyy30JIuGqUnmoF4Ge9OW4JOOpHWtoSRi7kwUntUkY5+ao1YkCpY1659a3ic8kSocVMjYqs2ccU+KfA5NdCkZyuWi2RTHbd+FIJ1JamSzAfl2ocjNJ3ILld/HSq4fZUtxOPWqEl4Qx4rmqVLHZSg2iwbjeDVe4m2jpUMl75dV577zF547muSdY7KdFjpp/lNU7ibcGJ7UXVyAKozXhPHSuWVY76dEWefn/ABqlc3Zdh7Ut3c7MVQvLgENz+FctSoz0KVEsfaxuzt6VPFOW6d6ztysKmt5GZ2FZxnc1lTRoK+8fNw1SRDP/ANeoYx69auRxZHFbRhc5JNIdBFlufwrRs7bzB7VBZxAnHXFaVrHtRduenSuylSbZ5+Jq6aFqxtNz4xWxpVkodRjvVOxjIVf6V0Oi2yld1fR5dhbu585i61kaKAQxe1YeqXYkm+laWp3HkxH6VzN/c7mb+VezjJ2jynHg6fM+ZkOoXW3dXP6ldHcav6hckR8VhXVwZWNfJ4yofVYOkkrle4bzN3Y1DHFsGO9TJFlvqatRWW72r5+oryPUjU5dCrDa53ZX8K4v4o/BOH4j2+I9QvrGbPBglK5r0hbPKdOlUbseUc45XvUuipKzHSrPmvHc/LX9uf4K/EjwL4xtbSxvNWubKZii3Es7Fe2OnFeVz/s5TLplrHqk3n6iwDMjybiWP1r9hvE2j6b4usGtNRt4ZlcYDOgYj6Zr5c+PX7D1vp+ty6/o8lw0kY3KgOcY5q6dPl909anjOdWktT5O8J/ss6pq88MUNuoWQbSCSuBXsWi/sK/Z9MiW+kijYjOd5O2u2+Dd3Not8YdQVY5FY4H8TGvdvET2kPgv7e0a7o0JJ9OK+mwOEpOPMeJmGKqRlY/Lb/gpdr2n/ATRofCul3kE2oXcQL7DudAeoz2r88rf4YXHi12SLzPNydoDElmPpX0d+2/r7fE/9pLxBMryPHBdNDCpbJwCf8elaH7JGnWen+PrGK8tVmWN2mdBErs4XnAzX0uFwkFFcqPmcViJP3mfK8ukatoG7TbXUbxLqwIk8tGOI8c8+mOtdNL+0Z8QvDnhNY5tYvJLbG0SMMluOQSR/OvTvjL+014E8U/tc6xN4X8MS6Rpr232aZJgu93BIdgAMDIrc/aivPCmteBtG1DwhFaSaS1mq3kQQCTzhkMT+Neh9Sg90eZHHSi7IufsBftQt4Ia/VtTvG1K+xIBGfvMegOTX19+zp+1NqninXvt3jq4u9cjhkZbCGRsrEuR1HtX5V2Hhe88OxR69okr7Y2y6o+3Az0r3D9n/wDaEbx5rS6TGz2N8bcqU83PmnOcD/61eDmWWu7nA+gwOOi0ozP0u8YfDjw78f01C7hktY2mXZbRL8xuGxyPavO/hn+xf8QPgTrr+JLKaC2stOUzvazE/vE59u3FeE/AH9rFvgh4naXV5ppl02UOLZs/MAQc/qfyr7W8H/8ABQvwr+2pqlj4V0y11FWuWVJ5kTaigHJjHqTzXzNSjUs1JaH0NHFKNrDv2Wv2sJfjN48uTrirBHpr+XDbMNu0rxu/Q19VR/E6HxDfLaWErSRx48xzwqH0r5d/b4/Yrj+AngmHx54BlitdRt2Ml5aPPte5jOCVUfxEelUf2JPjrH8VtNja6v4IWtjumhdvn3c9fpivFxGFdF3Wx6VKtCuuZH3NYXCyW0bdW244qaSNpV3bflHv1rh9C+Kdncx+UjKyxcZXlTW4PFsd2VVW2qR0zRTqxatczlSkmbCyKW2tt9Oax/Engm38Q2c0Mir5bjkA4oi1PDbt+c9Ke2psUIaQbvSt41F1JlTe6PkT9pv4d3ek2VxYxtIsaqfKKn5h6c18JajLqPwv8Xy2N40v2aRizg5zKnWv1T+M+kLrqSSIqtIqnaT2NfFn7SPwpXX7dpriFFnXlZB0Vq9XB1OhUo3jc/Pb44svh/4lR6tp8K/YdQ8zaSmQeDx9c15j8LNQj8O/Fmx8xnzdXBQDnbICOM/n+leq/G6zutIvb3S75S0LSiW1Zekb5/kRmvJ/DGjzal8UNNuIlkeGG5Xbn+HBxX1UZJ0Xc+Zr0/3yaPuXQ7DzSkDNsijTckbDH8I5H41538WtT+0yLpaMuEy8mP4yOOa9G0u7mZY7rd+8mUgI38CgDpXjXxL1qPRL3UtSkwvmFmyfyr5qjByqaHpVpckDxj4zeLd1ubGJV86Tr/sr615vZaKIg7yZ/eHKgdhTvFWpT69rtxdFizSjCc87fQVt3cUVvBbrG22RYgJNw6mvr8PH2cUj5PET9pJs/QD4kxi88PzRzOq7Rhmx3HQ15Vayx6Zcq0i7o7o+SwJwp7A17VrlvDqUs0Uu1IbwEAnna3avK/HHhldKtRDNG3mQvhcdD71+c0paWPsGSeG/DC6ZdGMqxaF9ykd161wfivTn0z4iTLIMbpdwB64PevZvCFusEcLzg+W0YOe4OK4n4y6I0mpfbAy+ZCoyCOSOxrow9T3rMzlHoeYeOFW21KeKERlmiJyvf0xXl2jeJLfSdX86e2S4uFVonB6DJ4P4V7V4h8Hxy6YdalnWGPy8pEWAab1AFeE6udP0/wARzSRtI0k7Aqjj5Qa97BtWscGIM/40aRF8SfDysUFvr2it5iHGftEWen1Ga+i/+COfwXk8T/HhvE8u9V0vT23KfvLIWAxXgnxt1C41HRIb22SGO88uOOYphcEAf4V9yf8ABD3wbef8K017Wrw/vr648tXPcD0/Ws8+ryhgdH5EZbRTr3aPvbSbbzpDJt5z+VdroNv5kaEAdeeOlc/oVl5JC4+ViSTXZ6NbJ5iqMBcfnX53E+qlLQ1LKyAHy+2alcCOLd15x9KlhjEUQ285606S3aeIIvds9K2MVK5NYJmMnj2rTtY/M+63PeoNPtwMfL90VoRxYxtB+Y4OO1aIbsAhZmHoPSo44RIR7E5NWoUx83GAcc1IkC7jVW7DTsOtbbA69qtRLkY/hYVFbsVA4O3pVuP5z/jU2ZpcFXyV5Gc1atIyfp9ahROdv909amiG1wvr3FNEykXrdscEdD61eiClQe+Kp26Yxmr8A3Pt611UzjqMlhfDbqtq/wAuT+lVkXa2P71WFXHFdMTjlqWrYZSrEHU1Tjm2f/qqxFIcZrojuclQtKxDVMj4696rpJkZp8b4NbROaRKf8imiPL5pVb5se1PjPzVSMdVqWIV+QVYT5u1Rw4K4zUsfLV1U2c0xTxSFNw/DpUqqCKjlGwVpJ2JjuV5HaMdajkusCkuJ8qazru4weDWMq1tTphSuWprv5eazbu/UN96q9zfkA5NY+paoIwfm6e/WvPxGIsj1MNhG2ad1qijq3X0qs+qKB973rAn1QyrwfxzVQXzbjz0ry5Yp3PZp4BWOma/WUcNn8elVZ79c/erHF78v3qikuSdvNT7Zs6I4OxfvLrc33j/jVXzVc4Vvxqm93vPt3otmMpYc4qeZs3VFRRpQS421oW0W9/8APNUdMt2z93NbVrDha7KMGzhrSSJIYPNbv+NXreLaOaZBCNqnv3xUu1iK9GnGx5NSV2TQFWfjjNbFlb7h7YrO0+DcRu+tbNgn7we1enhad2eTjKllY0NPh6D0rorOLyYV9xWbo9usj52/pWpM/lw19ZgaPJDmZ8zianNLlMvW7nZ8vbGa5q+mKD2rX1Wcu7fzrB1B+GzXm46tqevgadkjNv5sAnqf5VlyHdL81XrxsBu9Ugvmvn37V8niJXeh9HRskPtoQ0orVtrLPt/WoLK2ywFa0Ee1a54077mGIrW2IZbTEdYOsR5DMP4a6mdAyVhara4LDn8K1dPQMJV97U5HV5DJZtk7R6jtWbY+II9Nsf8ASm863bhiw6CtzVrLzY3HOPSvNfFk8unxTWbLujkztNedVvTlzI+lw8I1FYj+JvwK0v4g2P8AamgtFHdRgtmPHJrgo59Y8M+Gr6wvYfOCkj9DW/4I+I918ONQkjkDCxLfMMZFeqW1hoPxd0wzWIUXmPmwf5+tenluLvK19exy5hhJQXvK67n8837SdvdWH7Rniy3l/wBF3X0k6ZON2TnFcFovjzUPAfim21KykZpoWyGXPPciv02/4Kw/8EubzVrl/GXhu3mW7gjJuQACsn1/WvzX8LeFJNQ1ZraZYkls2IYHue/8q+/wNZVIabnxuMoOL8jA+ObeEJfHfhnXPDlxNHea/Jt1SFh81vMSM7f9nmvo/wAH/sHXHiP4o2vg+S6mg0vWLBbyKYxn+OMP1+prn/BH7M3hPxVrFnqd9bzQ3lrJv7LGSPqPpX6GeBPh54o8N/DG38YzyQSWUVuLSyYxqF2YAUk9SPpXqRs9zwq1Npo/Lf8Aaq/ZB1L4CeE5l0LX7K+lt7oxtDv2uoBI6dzx0FfP/wAG9S1hPjZ4ZkjiYanaXce9QNvmfMMgjGelfZfxr+E7eFP2rJrvxDrtvaDUI3v2SZ9sHYhQM9wa9E/Zh/ZY8N/tNftkaDrGgpLfQ6CyXOtXkKKtsHBUhUAHcA8VjOotUzpo05aHsf7Tf7BUPiX4W2/izT7eFNa1a3EnlxjgAoCM/rXyD+zx+0D4g/ZJ8dXOkw2lnY61HOUiu7uTy4bYO2PMPHJFfuZ4k8HWs+kQR/Z/3MKeXHEMbVH0r8sf+Ct37KNmJ7nXNMsWgvBHudwPlcjJ5H4frXiThCTcXsz6CjKSjddD62/Z1+PHwj+Hl1b+IPij8VU+KXjK/iDJYI/2i2tHODthTcQcdMmvn39vH4n2+h/EGXxp8N/C8vhrTb/bBcIR/rT/AH9gwBwec18G/sffFrQvDfxA0/TdUTT9P1ZZ1igvrlj5cZzgljnHT261+wvgz9m3w343+Hcl54h8YafqzX9szpZ2bCQy5X8cdq+czTDunamloevl+Ig37ST12OW/ZT+NU3jbwpp8s18ZrmRVzHGCFyRX0t4f163uHWJZP3ygb1zkg1+YfwQ+KsfwK/aJ1rwvJDJbaStwUs453+dYzkA9f1r7c+HfxJ07w/ai6muox55BID7nYnpxXyNajKlU20PpY1lUifQA1dUT9233flrJ1bxVJErLuUHnGKwbbxtHe2sbRlRHJ1z1xWT4u1dZ9ObyfvK24MOpArup6sws0Gt+LvtgZd+5VzkA9DXz3+0NqFwnh27jijVpOGO49hzxXdXvima0bc0bBXHKsea87+ImotqxmjaMM2w7gT1Fd1KVmOWqPhf9oHR4/FlhJdNGYbqzwxQD7wJwTXC/BT4bL4n8TssD7lt3V8henTI/OvVPjXYSXU18liPnkcq6/wCyCP8A69dr+z18Lo/A3hS4vWiC3pQM2emK9X641SsjyalFOpzD7+GDT3lEhUNCmSMdMD+tfI/7RfjY6s82nQ5WTa0j4PyjJNe8ftH/ABWXwtptwqttnVSzYH8RAwK+Szcya9f32oXb7z91j2bvgfga9DK8Pa1Rnj5piF8CMvQreO00SO4ZvmWP90rDkuTg1V1m82Tx4kYEoCcc1JqNx5c/lr8sUS7gnvWZPctKkcm0P5gyfavoVHqfNylY/TbxLYeZZyXESs0MLbHI6pjoa5jxZa/27pPLBriGLKED/WAdK9I8bWEejXf2qx3NZSKBMhHUHrkeoridasfJCyWbfuYXBAI52ngivy6Lsrn3iKHgHXWm8KyG82hrcsNx9B0p/gXwxb/GjW7GS6fy7PTWeS65wZUUHH4UvijSo9N8KOtvDtknm5A6HNW/heU0adY44dv26KSKUDoDjirjJbomUbnkvx+tLfW9Rs9Ys4fJ020c2zQof9WB0yPevmf4raWLLxNI7ufsrlWVgfuAk19VatfW91p2q28jx7bpmhmi7I3OGr5z+OHg1ltreQZZI12sw5UjPc19Bl1Rp6nn4iNkcbfay0ulxqkfnSKBvXruUZA/MYr9Yf8Agkd4RbSf2XrGfydv2pzMAe+c1+RUV+sMVlYwsy3UkwBfrlM4AFfuV+wf4Q/4RT9nHw7a7utnG+AOhIz/AFrz+J5WpxgdWU2u5HtWkW4Nwqt9a6vSrVZH7AdawtEsdx3NxtOOldVYQrGq465FfI00exIvWtttViPTvU1nGGLUJ8w2r361bs7fCBvzrblM9iWHbGn1OKsKPl44oQKOcDHWkI+UDpuq7iJYUMQx/Cec1MI1Zh81V03GXb0HSrqx5T3qrou6sLEwQKKsbsOMc96jiRTH71JED8zL9DTAm3fL2ye1WrZNxBFQwx5HTketT2jgSBfShK7CRdhjxjue/tV6AAtVOI4y2OtWIpgGH3V9a6I6HJULSx8jmpB8vH61HEPMH608HBxW8TkluPL7TzU0Ex69vSoAN9PT5T+GKuLZnJIvQzZHpUvm/nVZD6elSIOM966IyZySirlmJstnv6VKkhzUFsSW5q3DGMVpE5qmhPEdtTodx6VCnymnqwIreMrHLJJkpcsajnfig8U2dmI4pyk2KK1M+9k8sVl3Nzg1qXsO8fTtWZcWnmE+vpXNK7PTouJk38xZPl/lXOatIV3bs9a66603932zXP61pXlRMxGc/pXFWpOx7WDqRuYMDkj6Hj3p00u0fhxTF3CTai7j7Vat/DN7qHUbV+tcMaLZ7HtYx1bM83rGQ7W247U/7QSvOcnvit228B+SMu25j1FSv4ZESZVVNaewfUX1yn0ZzixSOav6ZbbD6ZNXV0fy/vLirEWnhVHt1qo0XcVSvFos6fBmPitazgCgjFULOMolbNiiv6V6VGKseHiJu49ITt4qzBa561JFbZPrVqC3AxxXpU6NzyalcbaWyx4rUsIQx6cmo7Wy3S8LXQaVpAC7mCmvbwWFcnZHiYvELqWdMg8m3X6VHqdxsSrsg8tKx9TnLP1r28RL2UOU8qhHnncydQk5Oec1h6jMeQf4q1tRk5NYd0fm7bvevk8ZVbPp8LTsindNnPSo7RMsOOv6U25lw2Nv3j1qxpkZc/N6+teNKzZ6T0jdGlZwqi8Dr61aGVAqOJcDjv6VMse41pGJ5kpXdx5GUFUNRh3Vfziq16Nwq+U0otp3Rzuo2irkevTNcT478Mi5tJJAq7kBIOK9GurXzVY4rD1XT/OjZWGa48RS5j6DB4hxZ4Jq9tDrFjJC37uWPrgd6T4Va9J4F1xpkl8xW6gHAH4V03jXwv8A2TqPnJEPJlOGx2rh/GGjTeHSt5GGa2ZMEA9/evLi3CVz6ZctWHK9mfRnifx7ofiX4R31zfC3ZTbMrK3OTtPavxL/AGxf+Ca/xU+E19c/ErS/D7XXh/VpXuBFZ4ZrdCcqzJnPTPQV+inh27m8QaWZZmkS1VhiLd8r/hXvHi7432eo/DD7D5Ue/wAnZJuUGMDGOAetfWZbmbvzT0sfI47K3SlyQV039x/PCPjfcX+jyaZqE81rcQyASI6+Ww9Rzz0r6O8AftdXVz8HbLQdU8RSSafYAeShmJVVByqhRX3VffsRfAv4y+Ivtfi/wXp81wzFnu4Ywmc5+9ivbvgl/wAEqfgJ8PRDqGi+DdEuMkSRSzxCYAdehr6ihmkZxt1PBxeXqm9dj8kdd/4J0fFb/gox470PUtN0K80nw3HIsc+r3avEskQ4BjUgErjp+Ffqt+yH+wZ4V/Yn+Hceg6DALi5m2G8u3JZ53A5PtyTxX1lZQW+j6ZHZ26Rx28KbI440CqoHAAA9q47xZqUemq7KobnP0p1MQpbGNGnrscfqulQ20fzyc5ycdBXyV+3X4QtfF9tJakrtZCDgbgBg9a+ovH/iO3tIizNyFOADXzF8a/EbaxYXe3AkQH5z2/yK46ko7M9KjRlufhR+0z8OofAnxf1C0hDJJDMWRwMZOeea7L9nz9q/xJ8NtZt4Yda1aOPeqSFZ2xtzzwfbPpXeft//AA/j/wCFjS3EbI3nkF5f9o18xan4em0y4KIxfd8rNn9c11xpwr0rSPKxEp0Kt4n1z+1v8Sm1D46+HV0dbQfbIYBHcxtuknkPLbmz78D3r62/ZodYobWTUtcgmuoo1M8csgYIexx14r8oNQ8a31z4dsYVjZrrQpWuI7pWPmdFwCc9Bt4Hua+u/wDgnZ4l1L4wXMMEN9b/ANqXTGOR5GztAHfP88eteHmmVpUU0tj2cpzRuryy6n6iaB4ysn0xW+0wzSKOMfKAPYVl+I/iRHZW0nlSKrZ7968T8Sa9a/DWVdPnna41SE7HnU/Ju64H0/pVK48dx3lxEsrO4Ylsk96+VUEmfVc1z0HxF4pYv5kbLNxk5HSvO/E3jJ0nl3bd208ZwBVXX/F/no0cLt5bADhsEH8K5S+aTW5Vt7cr5gfJY9GHpVRkRKRyfhnQ/wDhIfH63F1HGLVg24YyXJz/AI11vjvxXH4I0O4b9z9whhjC7R0H/wBetzw74Rg0GGW4uIQxt8MuDjB9q+bv2rvih9rW8s7W4x5j7AA/vjP0rvwdJ1ppLY4MXWVKDfU+ev2h/iHP4s8XLHG2RcSNKwHOemBj0rm9UuV0TQUtwqqzkSN8vXPH9DU2oRZ8UT31wIpBZ25ROckv0Fc/4rv2MSiRzyoLe1fb0KajFRR8XiKzlJyZl6jP5zPt5bbjmqU07xhQvy8cjPSp7dlllw3Jb593oKoSCWSeQ7tvP512RPPk7u5+s3jG6uPCHiy4tbqTfa3aeVcAjiJvUVyWmSyWUt95qgiBtxz92SP1FeofGq3h8Z6vLcJCsOoQx5kgI/4+lH8Qrh9LtYL3wzqCyeYs7QssPHI9jX5HzaH6HFXRcvreLxH4W/0eNZQwEkR78fzrDsLVdH8VQhdzQzvuH+yxFdL4T8K3Og/DPw3cM2yS4kCxlv4xvOav+NL21Xxt/ZTWvk+SwaOVe7YzzRF2dhs+SviXFJY+LrmOGNkWSZyRjqQe9cRdarHfXM1rqG3yryIwT5PyhugbHava/i34WluPE0t7ar58J3ecoI8yNvXFfPHiuX+z9TvEmhyzAE5GD7GvosHJNHn1l0OP8PeBZIvjFolt+7eH7dFGoPO5S+OK/er4K6MuhfD/AEy3jTy0S2RAPoAK/Ev4Jv8A2p8b/CtrJtkZtQiKDGW25zkfSv3T8Eaf5Hh+zTGdsSjOPYV5PEVRyqRv2O7LYKMWzqdIgMaZPO71resFV3+7wBmsSylxKq9881v2acDH0r5+J6Ei5B97J+UVcgkBTj7pqKJMfNjtirMEYRBxwa0VyNCaFGYZ4qQDI/3abACn0qeNNq5J/SqFzDFG85wPmPSpvMYHn06Cmr8p3L0/lUkK/Kc8ZFOxRLbHch29ccip4W2tUIIGNveponU/L+dWHNoWol3uvbI9auQWw83lapx53rxWtbjcuT1qo7kSukBh3x7RxVG7ElvN3NaozimGITHJra11YwUrMk06UtAvarUbfPUITYtKkoXj+taR0VmYSV2Wtm5fSnoNoz196hD70zxRExJrRM55RRagl3HFWYBhvaqYPvVu1jJK10RkclRIuQRkVYRcVDC9WI/n5x/9et4nDNtEiD1pwIB/+vRjPrUkMO6tUjEEXcaXyie1SrFjjmh42VhWkYkuRUuLbctVpbZYR0rYW23DNU9Rt/kPbHerdEqnUd7GHfSrHCSSBiuR1q7OqXXkx/cHU5o8f+Kha332WN1y3UZrL0jUdrhsDBrysZiIp8iPrMDg5Kn7Rm9pWiw2qfcy3rWxEqqo6CsO11cMcVpRXisnX3rGnONtCMRTn1J5ZArc9KrSzKxwOlR3V3u4FRBsDIrTmTZEabRLJahk/wAKYIVQ/wCNTI5ZaZKvz5quUtSa3JIow44/QVo2EG0f1qpaICa07MZFddGJxYipZF2ziytaFpbbiBVW2XeBt5re0Ww83DEV7uFo8zSPn8VW5dyxo2ncBq2o0wKbbw+WoUU5vlr6vC0VBHz1ao5O5DeNiOsHUpMsa2L6T5etYd83X1NcGZVOiO3Ax6sy798lv7orDvpNr7q2NQ4OKxrvlvXNfI4iV2fS4dWWpQkBeTGK1NMt/LG4jtWfBG0k/wBTW1bJ8i8c9+a4IpNmtepZFmBNq571Oq4PNRwpxx0qbbheK6YxPN5tRrJhf61UlOwVbDYH0qtdqo/4FVO5vTkUndcEYrPvrdTlqvTr5Zz2qGZQR0HzVz1D0acrao4/xbpUd5p00bLncOK8nmtGubqbR78kRNnY/tXt2t6cbgArnOMGuR1vwvHLMJHXEq/xYry8RTd7o+kwOIXLZnkN/wCH18J3bacg/d3HCMwp/jewL+FbLT41/fTfLI2cZG7Ndj4m8K/29bNIyt51sflP0ri7rT5J9VRJHdfLXGD2qaNbldjslT5/e6ol1XVZj4F/sPTdPgha8/dNP5eWQDg81F4D+N9/8BdANutw2rzTSFjbgYECjsK6OC2Olad+9aQ5Q8L715j4s8Ki/wBR+0WKXMkyyBSwbGOhP14r2qFZ2vc8vEUYy0a0PavBv7ePhvxI/wBk1ZpPD94w4jujtz9Ks+L/AIq6bdMzRXkc0D/KjpICPqa+Rfir8Eptf1iTUjDLchSVjy3zMR2PeuB8TaVq/h8fY7W7vt0i/JEkuctj09q7PrNVanMsvo3vHQ+qPjB8QrC30fdHcKw27t5avlP4x/tBR2WnXlmqRzTTDC49K8b8QftQ+IPDmtr4a1TTri8igbLSKDuwah1D4zeB/EltJJdSLZ3EIGVkyD6elZTxVVs7aWEpwW54/wDteeHIvFHg+G+upo45nbcq9CgwcV8ny6FJbQ/vg0m4YVzX0R8ftX/4WGJo7OQNaqxWHyzyR615ToX7N/jfxarfZ7OaSzQ583+FRXv5bUcYXqM+dzqipT9xHmEom0mSRYU+adTHKM/eU8HNdb8IPH2p/AjUoNY8PXk8NxEeSOgz1BrqLv8AZi8VadaySTaZcSBf+Wm3IH/66veH/wBhr4jeNrOOe102RLOQ/ed8BfwxXdWxVBwtOSseHRw9WMuaKZ7x8I/j3c/G9lkm1DztQUB54Djc7YOSK9d0eFrXSjJdedCu0EFl5x0xXn37M/8AwTzk+FDrrWoaxG2oRkP5CHCj2ya9pfw01+fs7SK6Nk/JyfpXw2NlS9pem9D7HBSqOCU0YFlos2phVhLM0jZyB0GfWus0Twzb6ZOVkz5igFNoz7mtCw0FtEs9saqr7QM4qtca7b6VYzXFxuVo0ZVOe4rih77sjvfuq7OC/aa+LVv4K8IzRrJsZxtBA755zXwXqPiSTxX42vXZpHiWFuSe+etenftPfFl/Feu3dqjh4VYpHvbqT1P614xYsujpeTBo2Z4/KVv73PJr7PK8KqVPXc+RzLFOpOyM7VdVX7RcL/EpUtkdT2/ka5HxJqLTTLGzLkgE4/QVd1TUPMvtq8+Zy1Y2qETTf3mznPoK9+EWj52tO+hb03dKXf8AiWMjGOBRO0cAVX+ZsZOKn0XDaddcKG28H05qMwxu53fMcCqV76krY/cT9pb4Lzab4ntdatY9n2QBnjU/mv0xzXmWv+FItSvJ5LNliFwPNVfQ5+YV9k/Fzwm3jTwVfNa5+1NbsrIPvZxXyPo7yaQqR3Vv5clqxTEv+sB71+NxlofoVOV0ZOt+L1hvNN0vbui0yFRtA4D5ySPzNcx8UNYj1Hxu0it5bAK4Y9GP+RUqRS3HxH1CYqywjLKW78ZOK4n4ztcx6pb3EO4xwbWLDuM85randvQ2asjB+IUax3+oND5gmDK4dT0JzXlfjnw/b+JtLe61i1XdGCr3EBw233HtXoUOqP4i1nUSk22NbYuRjup/+vXC6nrKwpcPI26KZTFIg5Ge3HvXr4eTicFSKYn7NvwcuNO+PngvVbPy77SPtyhJxyy8HhhX7OeGABp0Sr0CgHNfll+yJJHY+NNJjWHEbX0aLz8it14H0/nX6peHYsWkSr/dFePm1Rzmrno4OKUDW02MyXI4BX1rprGFQvzAVi6TCoZRXSW8arGvr7V51NHRIkiTK9c47VbhTKjP8NVrXmXnsc1cK5Xdzn0rdIxHQoxHUeuKm6D/AGahDbTlf5VNGAw68VZVrjlCg8cBulOaML3pr4+Xb/DQXZT/AJ4qZeQK47+HbVi3bJXpxjmqq8xnP3utXNNIdcfjSuVsaVum5AWx+NXrZs4Gapo2NoXp71ahOBn+7WkdzKWxczjHoaF+Q42596RBlc/pT15H41uu5gOjG+h4eOKhM3lP93irUf71c1orGcroijbEm2rCtsbn86h8sifNWY13GqizGViSI/PWhbNkVRWPC8fNjpVu0XIraEtThql2KP5watQfMahhAZfpV6CPBFdlNHn1JD44fmqaNMYpq9anjUV1RiccpDo7beuc1J5GBT0XyxTnHze1dEY2MXJ3Itu0Vw3xZ+IUPg7R5pGYblUkD1rq/EerDTLJ2ZtvHFfOPxz146nY3LSyMVZSAK5MZiPZw03PoMhy14iqpy2Rg+DPFUnjbVrzUJG3KrlVrqbbVliP0rw39nnxskL6jYSSDzEnY4Ldq9Nk1fzJtuQK+KxlWd7n6N7FL3eh2VrrW9vvFc9PetSHV2Q5/rXGaXqSnCb13CtmCYtGdrZPasqNaZx1sPE25NbLmrNjqgkK/Nye1cpdSyRtk7umRgUtlrhX19MnvXo0sQ/tHPLCxa907b+0flPapE1D5RnmuSTxB5mdzdu1X7DUxIfvcYrup4hM46mEaWx1tjcAjPrWzZHeRXL6Ldq0f3u9dJp0gPzetezhZJngY6Nja06HMnvXX6ZbrHbr9K5jRArSq2M4P511VtOqp/8AX6V9flkY2ufH4+o72LJGyop5cr1pxlyKq3MoX2r1alTlR59OLbsV7yYtkflWRfSEE1euJtwOKzLqTcPevnsXW5mevh4WRm3r+YKxr3g4/Wtm8+8TWPeje20V8/iNz3KOw7TYMnnr1rUiTFVLOPYn4c1ftU59q56auZV5a2J7dcx1KyYA/WhFx0oJrujHQ5L6kLjANQyjfH+vSppd2ajk+X6dal9jeL0KV1HvHPWqU+AMflWhI2Tn/wDVVWeJZFrkqI7adQoTKT2FZmr2KyR8jNbUsXyenFVZYPMXawrhqXPQo1LPQ4290xopF2Zww5HrXN+KPA63kZkh+WbqW716Rc6au6svU7ERxbgfzrzqi7ntYfFaqx5Rqd7JZym3ugxUjarVXso4bGYzHaLfcMBj+ZrtfEui2+qwMsigSAcEVwut6bcaLtWb5rcHgetOjipQep6EqcasdNDP8XXccl00mn7Tbl+Fwe45NeV+LNDW4nmms/8Aj7iOUO3ofQV6N4i1CM6CwtG2tG21cdieK5Wx0Z9Bso5LqTzmjYyuv989a9mjmEZOzPPq4OUY3R4f8c/CsOieCre6msYZvEt4+FRYQzbPUkfjXzb8UfgFHf2Nq0MbfaJ5N8oCcL7Zr6u+IGuTXPiCTdskmmz5Ab+FO/0rz288KTeI9ZmtIbhY7eaPywT/AAMa7PrMFqjjjTqrc+QdR/Zv1Sy1Fmg8yNZGHAXOxT3r1z4C/D3xD4AXy7i6+0ae2Gki2gbgP1r6G/Z7+FUOk/EVo/EFrHqFvDAI5EP95T1B961tJ+G8P9raoVtVhhWeRolOeFzXPWzRpWRp9Vcnseb32m/8JPHI0Kx27zbUaORBt2+g961NA8PzeEAoa68yFBlYwBgZ9a2de+Hv2b95ho2IGAvt3rAnsmt1ZX3bs4JzxXk1sZKp1Oing1HYr67PLq96rpM0a5JYAfKe1aGhWv2G1aSNQxxjdt602LTFdY96hYzwMDk1pApp9kUVT8vJzWKqNm0adjP1G63yRiUEt94qDwT2rxP9rT4nr4W8MyWdtIq3EqjLE/NknoB+NereIPEEOmwtfzNGPsqF8sdo4Br4g+PPxah+KfiO6vYpN1vaOwViMeY3+Ar3snwrqS5jyc0xChHlR5D8TtYOpX4jRt1xkKp6M3r+lcn4h1D+zbGOI5VlXJ75Aq7q+sf2jrqsm1Wtf9ZIT949f06VxPi3V2u7tpC7HqoGa+8o09bHxGIqbtEcN+s91u3Y+Q/jTFbzNzDng/jVK1mWNWb5twGPpVqM+Uy/3cZrrasede5u6Fb/APEruF6fu9wyPeomDRgbVzkc1paG4ddu0KGixgd6oaw7Q3m2NSq4BrK5t9m5/SB4B8Wpqoa43cY2XER7e9eLftHeAWtfGf2qGGNra8O4YGOeK7qNX0vVG1fTVJ8tNtxb+3r+VXtZtrf4iaCybl86AeZF7e1fi8W0rH30Wk7o+Y73wncJJceWqtJg4I+8wrynx3bOs+ZFzAy+W4PY19PeIfD72tzLMsakqcqB69CDXiHxW8Or4jt7l7ZfJmhYl4f7/wBK2oytLU6ua6Pny3u28P67qFv5WDLG0Ib2I4x9a8z1kzWl7sYHaxKMBzg16Z8SrdbXX9NZlaFpD5b+xB4rj/E2if2p48SOFGja4VTIO2FPJr3KOxyziemfs3SS2XizwsqyMga/VtjD5m6mv1W8KsTZRf7or8m/hzqVuvxg8LQxSiOGzvI4/cHPP61+snhpM6fCwG7Kg5rxcz0mmd2H+Gx1ehRbz06Gt63HbpjnNZGkgeWMGtaLOM1wxkbSJrLJkxz6g1bjAU55qquAVK8etWkj+Uc/gK2JBfljz6HpViMA9sbqZGgYbf507BXp+dAbhMu0fjzTiP71NC7vqaj3sSR+FAEk/wAkZx0qfTDuOTUCKfut92p7VdsnFAGtDIDt7kd6vx8pnP4Vn2S5+Y+laCHBwtaRsYy7FqI4X+VORgfUVCrEBc9amDcVqpMzlG444c05FMJpg6BqUTYbmtEYu5YSTcelTInzfpUERy4q2gyqn3rWMTGZNHDhqtQrs4qGA/PUysQa2irHDUi2XIhtar0PT71ZcMxZh71cilw3rXXTkcNamy+DtNWYjzVGOTBA71at2H4n3rspyOKSLStx1pzksf1oHzJgcmhuENdPmcz3OB+K+p+Xb+Wu7r2rwn4l25vtJlXDEsO1e5fE2ItExxXkPiaxM6lc/KRXz+Y6s/ROH3GFFNHyZeXf/CuviosvzRwXWVfPrXsOm+N7eS3jk3N0BJ9RXO/HH4X/ANu6dLJGq+cnzB8dDXkfhvxtdaXdNp987r5LbRn+KvI9mp7n01SpfVHt3iX4iXNqWks5MBRu4FeK/FH9tjxl8KJRcKIriBM8OvWuwtNe+2W+3g56e9eW/tKeF5NU8J3SiBWk2HYcdDXbRwkepjGpG9mYfhf/AIOD/Dfh3xDHpHjLQLy3XeY5LqAAqnvjrX2J8GP2lPAX7Sfh9dS8G+JbPU0ZBI0KyBZUz2K5zX4E/Hv9l3xHrvi64uI7OZlkbA2qevaup/Zd+F3xE/Z+8YWWs6PJqGnXUEm9lRnVZAOzAdc16GIy/DuheEtTn972lraH7/tcy2Kncp+pNWtO1x45lzz3615D+xn+0tD+018NIo76FbXxJpqiO6iJ5cjjcAa9Gntmt5yudvNfMyjKnI7IxUlyvc9K8O64rFQ3PPrXbaJfJIRXi+g6o1vKo3fdrv8Awxr43IMmvay/Fa2Z87mmB0bien6fc7F4rZtNVwOea5XRb7zY13fWtmKUdm/KvrsPiZRSsfBYjDq9pHRR6l5iioZ5PMJrPt7oInzGpHvQFrulinJas4FQs9AuPlWs28f5qsyz7z1qldSblNedWqXO6jEo3j5B7Vlgb5wvXFXdQkwfaqdiMzbv1NeRWnd2PUhojRtxtT8KvWwBQVVtl3NV6NQf/rVpRWpx1HckC4Ht/Ol8v5akRMpyKULxXco3RzopzHP4VXlOf89avSJx0qjcJhqynGx0UpXK8zblyeKrFtn09akkfBbdUEknzcnNcVRnZGLQF1YdKjdN4OFFSH73tQE4H96uWUbm8XYzbiBmaqeo2fnR7dua25I938PzVSvIC/auGtTO2jWOL1HRWF+HX7vcdqpeINHt7y0ZJFVjj8q62+05mOawdcsvkbd97HNeXOLjc96hX5rankPiP4eM0TSQbgufu+p9az/FOgM2kW6vHskVcMQK9YsYVFuQdp2nvWL4x06HZtbDbuRXPzuKuj0lV5mos+Z/G3w/j1DU5LiNW8xUIX6Vx/h/wvNpmqQxMh23A3sSPmB56flX0k/hyOQyM0a7dpO/HSuB8DeFv7d1a/ulUTLDKyJx0we1V9Ymla5U4Repm+CdI+ya0ZZVfk9T/EPeuu1jwkLdhIo/1wyFC9Qa3tF8HfuV8yP94DkcdK6aTwt8kQeIsQPlJHOK0puTepzSsndHhPirw89udv3uO46VwOr+EUuDJvwSX3bhXu3xB8N7lmaOJV2gj+dee3Wim3syVZcg4bjkmuvZEeaOF/spbcSMV+RRxkVy+sTebf7QDuUZZc8V33jidYdOjt41/eMclh2HWvE/jB8SIPAGh3lxM6pIVKg5w1XRg5TUY9QqSUYOTPn/APbn+ODJbQ+H9Hm/0y8OxwPl2p3/AK18v/Em+Xwz4ZW3hX5jHzzzn3roZvEs3jrxnqGqXCNIjlwXbrGgPAB968n+J+t/btWktVJZWO4nPXnH9K/SMrwqpwUep8DmWIc5ORj2lw9o3mOP9cORnrXPawyi48tc7lPJ9a1ru4B+VfmEY2jPrWPfRkgNyGPBr3YRs7nz8yvaNmRd3U9a24bXLRDlueciqGl2yvIN38XAJrpNNg3Ttu+YqMg05yIhG+praJZgSr83/LMj05puu6VuuEZVX5lqbw/G3ztt2lPmGfSreo2kssoZGypGcelYSZ0xhpY/bm68fFvHjSW1wnlRqPPQcq46V02nQtCGvbCQLHjzQinqM/MMV8k6l8Q7rw14xWbzv37oSB/C+B0NeufAL44HxHpUvmSNC9vJtkVuhBr8ZjF21PuqlO2p6ZrES3VzJcQqphuF8zBHXPUfnXlfjzw6l1cXElnCvnRchR1YV65fzW9/pDND8hlBKEH5R2IrynxJHc2918rFZ4MlXB+8R2Nax0ZpRlc+f/jB4CtdTtPtF1BJF5Tb968Muf8ACuBGk2EM0915wluhAY4WcbeOeTX0R46uZtZ8M30gtbe6kgG8xMNpIA5r558dana615LWtr9huo8oYScJL24PrXrYed0D8zkvCWdB8a6TcTnLWd4kknGd/wA45z+NfsD8Mb0ax4VsJk+7Lbo4P1Ffj6z/AGDS7lfnS4jDbNwyyngiv1c/ZH17/hKP2fvCd1zuk0+MP7EDvXn5or2kdFDQ9h0eIfZz61pxttRW9azdPDIiqPSr1vLtfDBq8+OxtIvK20K3tVqMfKvVt3T2qmhVwe3FWrVitax2JLMYLD3PFOC/IRTYcBM9xUgHme1MpIiZGVajQ/NyOtSXHyfxZqOY7iOelAbkyLubdU1kMyc+uarrJtPWtG0ChhQS00X7OPJz04q7GOfeqkPCgr3q0mCck9K0RnK7JVbGc/n6UqSYf271G3OO+evtTlOG4+8aqJmSZ4zn8KA22THXvTYyd3zVMEBOR1rSJMo2LFs+T2xVyJgTn0qnGAcVIknNbRlZHLONy8rY9OvrSpP81UBPk/eqSO5Ab+taKormMqJpQy/vBVyBjn6VkwzE+lXbWfaevWumnI5atPQ1LeXc3PpVu3k2mstXz25NWrabHfHvXXCXQ82pTZqxvuWlZ/lP0qrDc4GM0/zOP71dXMcriYHjjTft9mx6968b8QWpinbcte8X8P2qNlP415n8QPCm12dVPGa8vGU3ufT5Li1H92zyDxJY+fGy7dysCDXh3xg+Ea6n/pFqnlyRnOR3r6K1Wz8ssrCuZ1/SkuIiu0dK8xRsz6yNRnh/gzSfs1msciENHwcjrWp4m8LWnifSjE6feH5110/hZhIcRgf1qSPw/wCSoby+O9dcZ2Fza3PGpf2cLWZ18uNGK8/MB1qv4l+AnkWuEt0aQDste3pYbj8q7cGpptOyAz4bA5o9oivas+bfh5oOpfA7x7DrdnuhjDDzkH3XXvX2FFrkPirRrXUrVleOZAx29q8v8X+DYdW0xwqLyD2p/wAAr+bw5BNpU7M0QbKA9q87Exurm8JXdz1fTZFJU9CDXWeG7v5l7YNcnboEfc33c5rU07UUtZVO7HascJLllqTiqanE9e8PXeEXndiujtbjOOea838K6+Zwq7s12dhqO5Vr6uhW0PhcfhWpM6IvlaPM4qrZXqyoMmrQdDzxXapXVzxJQcXYRpTj/Gqty/FSSTLndVS6uQVPSsatTQ2p09TP1F8kfWjSxvH41DeSbpSvvVqyTaB/SvOesjulG0DStky1XUTNUrVeKvREFa78OeZUJk5WlxtFJGMqR+IxSsNvrXajG5FK2FNVZ4/NFWpeAajRA+KzlG5cZNGZc2xKfd49Kp3EOwf/AFq3JLXch/nVK8s8D29q46lE7qVZPczVJC/3j9achWknhI9qgwynr0PNcctNDqirlhgN1QzId3fBFSBwy5b73enOwK1jKNyo6GXd2zOf4vasnVtHNwPXnpXSyopX+lU5Uy/SuOrh09z0KGIa1RyM/h1g/I2j+VYev6NJcSrGwLDp0r0K7jU9j+Has29sFlOfSuCphbLQ9WhjH1PMta0D7Jp8qhWYlMLx0NYvgjwMfDukyJtbdI5kJHuc16lf6ZGyEMobkdaqz6RvUqoC7q5vq7vc7PrV9DB0XQyqpwd2Mn61rXGk7l/iP0rVstMW0HYnHWnzogjYbclu1dEIWOeVS70PI/HmneZIFbLMcgjNeX+MLNrG4VduMdRmvdPFOnrbI07qqpGjMcivnvxnqbXutXkyjcqsFRf7341s4ux005I80+JGsDRZZZLjzOmExXwR+3H8VLrVtQ/se2kVrmRuSG+4vf8AGvqz9qr4oQ+A/D1xeXH76Vs7Fz39BX536z4hbxDq95r19+/JlLoD2z0r6DJMHeXtJHj5tirR9miDxPqEPw/8IwWcbbrhk3Stnncf/wBdeL6hM09+00jmQkk89RXReK/EsusTzec26WQZ5HT2rnIRkSMwBYfpX32Hhyq58RipczsU7ljNK3+0R+lNkt2uodnXDZHFT7MRux//AFVLp0Re23fxAHiui90cVhtlZNFcZ7Lya0rWTY3T75HSoYFC2sgz7H2qxZxCazVtvMb8Vm5aFRjY29OkzIzZ+6mBjvW29v58ETY/h7GuY06VhPj2z7V0cFwotY/MY9OCO9ZM6IaH3F4o1aK58RXm75o1ywOfutjt+Fdn8MXz4Q1Sexm2/aIllQH5SxGK86TU11HxObG4VvujDqvU+/1rprLX18MyW8Mcnlwspg2gfePUV+VShaNj7xn0h8L/ABZJqfhOFWb5vLWU5Odp7/hxVHX9ZhtdduPMj3QXQ3DP/LNj6VxPwV8a/wBl6lb+cT5aq0Iz3GT/AI10XjHUIliaSRQVjcjcB0H+TXPYxStI5281GOx1qW1lj3eYmQQPvqeK8N+KXhGHTLibdtkhkJkQDsR6ehr2HXZGubm3aNgs1qdyZ/iBryDxj4gjn8ValpN1GzeYRLDIP4X7r+ld+HbRpLVnn1/qNvpi+bMrSROfnK8kelfpP/wTj8UR+KP2ctJSNt32LdCOc4Abivzoe2s0vJlkaRdwMbgjKofpX2H/AMEi/ExstJ8RaJu+S2lEqrnoCeCKwzD3oXN6fkfctqhjj+bGRUu8kBulMZcRL7nNPGHCnmvMjsa8xcsZNyZq7D8qtgj2rOtCR07dquAlTu/StYuwupoW4/ddvpmnIdoPNVVz97rTmcrg+tUO9xbl9i5qKV1U9804yL5e38arzNlxz1NJlFiKTP8AF+dalpKCy/yrnJCyXGVbitfTJsgcrn2pcxMl1NyGTLirYbJHYfSqEEylB6+1WIZGf29vSruZ8pcTjnNOJ3Ecc1XjkxJ149KsI24fSqRLiSIvA56VMjnFVXlKn5cGnC9UR+9XFkOJcByKTzdtUP7QwrY7e9V5NSUjBbn61VxeyZsLLgn6U6N9prGXVVUY3Ur64qxfK2SPej20VuV9Xb2Ohhm3t16VbgfcevSuY03XfOOK27W9DLXVRqp7HHWw8o6M147nB5qzBN90Z6VjC83tU1vd4PBrsjUPNqYc34pPlyKsRz/JisuwvVYDmrySgiuqMjzZ02ixtGfvDpWP4n01bm1bjdxWj5hDUtyvnQn1xSlqrMKUnTmpI8U8WaF5c7fLtFcpf6Xk9OB1Ne0eLfDP2qN22/lXner6QbeVlZcYryqlNxep9ng8UqsNDizoau+7mnHRlMf3f/rVtG08lm479qU2/mLgCoO3mZyV7oIhYtzzWFrcLQxsPu16Lc6duUbhmsDxRpCy2zYX5u1Nlxl3PPZ9Va1j2t0Pel0IRy3oljXDD0qa68PSSO25fu1Y0XTWs/l27cd/WueSb0OmEkjqrTUmCqGY1I2psJhycVjwT7z8zcirUFym71audQcXodCkpaHXeHvFX2GZc59smu/0PxvHcgL8q9O9eMQzM84/hrStNVuLOQFWrvpYiUUcOJwEap77Ya+qRrlhVl/EUar/AKz9a8NPjS6jA+Zvzpo+JMsD/vS34VpLMGjyZZDzPc9w/wCElQn72ahk19XFeRaf8Q1LL+8bNdHpfi2O5UfNuJ96yjjpTdiZ5Oqep2ttc/abnuc1tW68Y6VyfhW9NzOfQcV1Nu5Yj613Uve3PFxsOR8po2x5/rVuLiqkByB61biGcV6lHQ8eoWEOBmhjmhDj6U5hlf1rsMSGVSBSRJtP9fWnuOf6UKmaAFJwOaguYVKmrDEL/wDqqCRsH2oauONzMurcGqLQ5etiSHdk9s1VuYOa4a1BbnfRqdDP2etG3b71YdB6VCxzzjj0xXL7OzOpSI3IDVXmTcc/jViVM/MtQsvHqaiVPubU3Yrsu4VXktw/3h0q135wCPemtjH9awlTT0Z1RkzNms9yn6+lQpZK/wB4Vq42/Sq0wx0/OuaVFI6ozb0KVwixqVVagltvOm+nX6VYvuQcfeA9KrpJuUbjj+lZOKudEb2OS8aootJ0YK3yN8p718h/FnxpH4TsNQVlZWQ/e9D6e1fSn7RviZvCGhrcxtna4JHcjPIr84v+CgHxgXQbO4tNLm3T6ydww2fLJPP9a0oUfaVOU6pVOSnzHzL+1p8Y5vin4xls7eSQWdn8pBbgkdcfr+VfP/jjxDH5C20K7IbcZ2rxuNdd4z1hrKy+8rE52jPzMx6k15H4kv8A7VNIqn5lOee9fd5fh1GKSPj8fiG27mOknnl2bnknNCxqtozL/Gcc1NHF+7Tyxg980so4x1XBx6Zr2YyPEkr6may7LaQH+Hjjmn6IvmGRWbvu/CnW4/0Vx/ebB4pumI0FyzN90nABrS5jymgIR9iYEbcnrU2iJ5kMiv8AlT5ofMt1Ofukcexpuk5fUmjA5BJGKzexpYngXZcKOAFOBz2rbsXWW1UMM7ScVl37LHJHJjGV59akJeRFaNmXcMnisrmrXY+94WttW1GS8gVlWLhywwS2DjmqsET6lEpwJJImBO3nvVm+v4vD3mabGudzfPJjqSPWtX4eaXDeeIobNcr56MGLevXg1+adLn3T0Ot8N27RRRybo/3LblYHqK6fTtSXxGbpfMVgQRjPANcH4R8Twt4nm0tWb7PGjBie7CrvgDUP7N8SXMPzkSv5i56d65JRSZJU8S6rNZpHJn94vyEH2rz/AMWQ/wBtauLnb5UsfVs4O7sa9E+Idqp19ZGUxW1wM4J6NnBrzzxVpd1FHceWdzRqGA7uorpohocb4je48m6vFT99CNs6Af6wdA1e5f8ABIT4mRz/ABy1rS5fla6scrk8uAw7e1fOup+MtQ06dZI/33OySN16rXpP7DGoL4Y/at0rUtjW0M0Jj+T+LcV4qsRD927nTTiz9fNOVmtsNzgc+9SDax+8RTLUqLZWBO3H50gkBlbHQ14sRxL1oQDz34FWoztOfas+1k+Q7j3q5A2wj6VpEC5HJmMUjyZUL096ZEGJwOnUUtwdkPQ9aoZFNLtO3GQOpNIBhfWnNh0+tRRtgHH/AOup9ShWRmX5V/TpVvTpPLAqFJwafHyP5VIzWhl2n5fzrRgk+b261hw3IjVQc8d60Ib8GP5fStA5TSWQM2c1IbjjNUbR9x+Y/lUsjbMf3aq5XKh73Qjzms2417Fx5YWrU0e9s/garS6QsmWHWmmaRhEpan4hW3gY71UqOctXC678Yhpcj79gVMnOetaXjTSbiMSYZsN2r5R/bK8P/EDT/h7qmr+FV+0TWkbMsSkFm4zwK9XDYP2+kQcYxXMz1vxp+1RY6HehXvI42PzYLdav+FP2pdO1idB50PUA/N1r8EfFH7dfxE1/xZ9l1y4aGa0m2MmwxkYPQivePgd+1Nda2kUlzqaxzRnaU37ckV1Yjhqoo8x2YbEUZaH7reEvHlnqkaNDMnzDOK6y219S3+sFfln8IP2u9U8NRIwvlnTPAfLV714a/bxzaW6zw/vZsbnDfSvJWEq0XZo2qZcq2sD7ig1wOPvfN2q5a6h5h/rXy9Z/tjaUyRbbiNZGHR2wQa7TwP8AtPaX4hMai6XOdrc7ea6qd+pw1shrcrkkfQenz7TjP5VqW8wI+9j2rzPRfiVY3Mw8u8hb5c48wZFbCfEixknVI7iNj67q7orQ+br5ZW5rcrO8SXNSecNtcpYeM4LqQKJlOecA1fXxDCP+Wi4+tacr6Hm1MDUi7NGtdL58O0964fxZ4d+ZnVT6nA6V0w11ZXG1lwadceXdwnvWcqfMrM1w/PRd2eSS2XlzNSLZjdx/KtfxjbLpWpt0VWPFZCaiitgGvPlTs7M+lpzc4qSFeHYvzLWRqtorxtwPetO51QMTj9aoSN9ofacc1NkaanJ6lpu0Exrk1iXlncxRsRG2fpXpaaLARuZfwqHU7K3jg2hB06mjlK5zxq/vLy2LbY29agsvF9xb/wCshb6iut8SKjSNGqrj1ArjtR87TmZlI2jpkZrGWh2UZX0Oo0jxULmMfu2U+lO1PxS0Q+XcK8yvfjBcaJdkeSH2n+Fauaf8bNP8RM0V2GhcDrt6VmpRZ2csux0et/FiTw1B5jxsygfWqfgr44WXxE1b7GsLRyqeSe9Uzb6f4jX9zIs6fWpvCXw7h0LWftFrCkbsQSwHNZya2KUktWemW2krZ42nrzXUaMqoq7S2cc1m6DpU+pQquFbAxwK9B+GXw3nvJzJdRusangnvV4ei5PQ8zGY2FODc2dF4B01jY+YV2hv1rognlNWjHpK2NqsaAKq1XMW417tOnbQ+ExGK9rNyJLdt2M1eg52+1UYkzIv61dgHP0rtpJpnBU7lpTg0uPl600Dp+VOPC11IyGnOKMYWnA7TTWP40wGlt6/y4qJ12mpehzxUchBNBUSFpMA+9QS4Y9OcVLKRnOKgbqaiR0RKkoBZqhb5c5q0x2kg1UvDn7tc1SPU6qepBPJt6VC7fL2p0koQfjULuOzH6Yrmmd0Ysa20MaCcJUc5OM+9NL7ivtXNLudEYjpHypHpVa5baDT5XyDzVW8k46/hWFQ6KcdStLJhjg59c1SuLpYbeVsrtAzyelNubkxz9/mNcD8dviPB4A8N3Ek0gh3IeTXJzHfCNz58/bU/aNs/BlveLdSSSR+S2FPVD2P071+VnxQ8fN4n1G51u6kM8e8rCWP3Rzg16h+2t+0fP8UPHdxp8MzmAsRLID8wUE8H/Cvk34reO/OLWEL/ALv7o2j0r6LKcG3Zs4MyxShGxh+JvFzalqa3CnKKxCc9Oa5bUofM1Pcoyrc8npTxM0uxf7ucjFXIEyA3Xbxz619dTjyqyPkak3OQ2ysfMZuN21WPT2qvc2uI1xjlcitzwzZ7lm3AsShxWXrD+VdRLjtitIvWxm42RTu9MNvOkeR8yh+nXIqvqNt9nlb1wMcVuXrLfTWzqo2+Vt46ACs3VgXjlk2r93Aqoy1M5R01JdIk+1Q7t275dpxVZG/s7W45N3DnHHam+DpmWZ7dv4gMVcubPzZQGXp6dqUtxx1Ra1eLMKN94RtigN5ca/MVyOmKchL2YD8gnGKM87WG7b0OKgs++/8AhH/sfnyXTNNtJyx9+lMupZtHtrWS3YifGVbOGA9c10mqQfariSNclcjIX27Vy1y8l/q6xsvEblSP7q4r8zjK59zYzNI1yTTdWuLr5UeSJkYkdT616F8PrrzrKxvyyyCQCOTjndmvM9Rs31TVmhj/AHbbsZNdhpmoDwl4Gki275Le43qVPYVFSKeovI6b4pD+0Zo7VVy3zMrZxwe1cHq2oTxWXkrGy3EKNlzzuGBn8K7CRG8Stp8kblpAfMzn+E4rmfjdaz+DI7juyoHjPseCKugtbE7aHhGqa1Je65IrhVZCSUH8Y6cV67+ytpk1rrVrfMriS0ukcB+wzz9K8VSzk1jxalxCy7pJlPlnqAetfXHwa8OtbNGjKq+aobIGQTjvW2NkoxsdlPY/STw/qX9o6LZzf89I1Lfl1q6c5+XGK4T4Ea7/AGp4Bst25njjCkk9wMV3VsQxCnn6V4LWpPUmtZMHPf3q9Cxk+9xVBI9kn41btTuY+1UBdVWJXb6VLKrFOfSnWrqRz97tT/lkU8VXMVEoF/Liz3qjBftLcsvHy+natO8G6BlXrWLZ6W1pqEjMxYNQ7FGxEN0fqakQGEdG9aYg2KODjpUznzAoFFrjFRw57dfzqeSNo0ZlPTmmw225Oyn1qe1Xb8rVS1LiS6TebxhgVataPnHes1YVI4+X04q5YFlI+bIz0q0gZY+z7qI4WRqtKNx+tTC3G2nyoylUsY2r6THqNqysoyR1x0ryrxtof/CN3DrjdDKCrgjII/GvbLiLZEflrzX4p2HnDcULBa7sDiHTmjqwslU91n5R/wDBRD/gmfomra7eeLfDdrHDeThppI1barnk5wO9fm7qdtr3wr8XXEb2slusUhJUg/LX79fE63SG4LSwLNHgqYyM8V8z/EX9izwz8YLzUJp5JLW8kJRY0gXLEjj8M1+kYfFRq0Vc5MRg503zRPhP4LftTLJDHb30ypNnuvSvfNH+NK6lbQfvkVGUEY5x9a8L/aB/4Jj/ABA+G2mavr1nF51jYyiJNhxLIO2F78V4PYfETxZ8N9LuE1S01KM2xCr5qFSQDXPUwNOrrEnD5xOhJRmfoFa/GnbI3mSSM0YG0HoK6zwz8bbmV/LW68uSNfMC78bu9fDvgn9pex8VQx28t0Y5mwGBbBNerW/iWax8NR3MUoNw/Hytztrza2V8rPssvz6nUSTPsLwv+01qlncqv9pupxgJu5Nd54S/au1HUdbg33kiMG2kBuw9q+HfDHi+WLRPtUkrNNvwOeRXQaf4uaF47hbiQSSIcHd06dK8+WEcXofRwqYeortI/RrQf2pbjRtdH+ltIrKCqP3NeraL+0vNcWsZljZWb73qfoK/Lnwz8c7q01e3hmk85lwgUnrz1NfQVt+0iqtpsit91grjjn6Uo03HVmFbLMJWs+U+/vDHxqj1O6VW3KGHG4Yr0rQPEceowDa+QffrXxV4A+JcOv2cd2rNGg5xnua9x+G3jbFkm24Xy2PGT0NacqaPl864egoc1JWPUPiJpB1TTZJIx86ruWvKdI1xku5IZjskU45717Zo96uq6MoO0sVxk1534p+Ec+q+Zdr+5mydoA6152IovdHyOFqqnJ05mXJdCQ9cipIZsOrKR+Fcg2tXWh6i1ndI2Yzt3YwGrRj1xJXUKw+ua81tI9ZR5tjqTdgR1S1Iq8X4dKj0+7aRAT+FN1WMyDKn8KXtCfZanIa3Yt5jN+Vc9fWXmowYV21zYee2f51RuNBEmeF/KuapUOinFI831PwRDcvu2qc9eKy2+FsEspbao3eleoSeHsHp+FLD4d8wYxtrz58x3QqWPO9G+HLWU37iRl5zwa9K8BeGJreZWuDv56E1ZsNFVJBhcN2rrPB3huS/vVTvmrw8ZuRjiq0VBtnqHwo8JQCzExiVww4JFejW9rHbR7UVV+grH8E6UdG0iOHjKjnFbgFfW4WlywVz8vx2IdSs3fQjmXchrPmTA/wrSk5GKpOmS1dPKjmjKxFEuT0q1EMLioo1AapRyPT+tax0FPUl69qkBzUIOVpVNVzk2HMwY01ztPWkJ3du9I55xRzAB4FQyNk1JJ0qGTdmq5i4xGONoJqB2B74706VsioZsD61LkbxiQ3LYFVZsN1q1O2Vw1UpG3N1/CuebO6nG5FKuR61XZNp4qwW2qc1WnmG33rmkd1O/UhklyeO/BFQNKVTPGaWR8NzVZ5/n9FxXJKR104jnvOMmqk0/mO3t+tF1Lvj+WqtzcfZ4st97HauacjrhGxQ8QanDZQszMqhPmyeK/Of/gp5+2bFpUMui202JIyQCjAkn0+lfSH7df7Vem/BT4e3jXE8a30kTCFGfa3+Nfib8afixe+O/E19rl6zf6QxeKFjnbk9ea6sBhHVnzPYqvVVGHmZHj3xu1sstxI2by+3OxJ+bB9a8m1C/a4vZZHYbWOQc1Y8T+Kf7avvmaRmdcA+lZ/2X/R9rZ3D1r7nC4dU42PjcXiHUdzQ0qFbsruUcZINX0tVFgxK87uKpaImEjH3uoPtXQW9tui28bc7vrxXRJ2ZzRjc0vBFmpL5KDMZHPuK4vxNGYLp93y7eP1rstFt2iQNu2sy/d9Qc1y/jmFpWG1cgryfcGlGXvjqR90d4bsxcaBIzY3Rpxx159ap39rv0xvl+beD+FXfCLNLpM3+yhJH0PFJMPNijVsr5i4+labO5m0uU5nT3Nn4jjXkbXAIPoa6S8j26k67WVXBIFc/rEDW2uN6gjJHeugWdrqdmIz5a8H61U+5nHTQbEd8ciqp2bQACKtQWivCvzY2jHFVbRjb2twrffYEj2NP0y5K2a/N8x5P1rOxofplLZeWl1dZXgHaFHOelcdLpDQq10zMJJCf0r07XPDrJHO+dsaqeB1z/kVxt7YNdwrtVv3ZPbrmvyyMrH3Hocb4b0yS616aaT5VUHaT65qxcarHZW8ltMrNI5LKeo25zWtDpxeb5VaPaeecZFTwaDHeXTMyqwVc59KpyDqVrbVJtIl0m8tSrRj5GT1WoP2ltOPiLSZrmOTkRhCO4yO/5VLbwmwvIYnBki3FD/s81g/FLXH8L2bteMv2O8UrKW/hbtWlFvn0BrW55D+z3p82t/FxdPkRjbI33vfFfdnwx8LIlk3Rdq/Lx3r51/Zj+HNvday2tw/6u4645wR3/GvrLwjaJDp6pt2nsTUY6tdnXT2PWv2cNTEWiTQq2VjbgV6zY3u75f4uoIrw74K3H9j3dxH8yiR85PavYrWdVRWB6ivNuJ7m1DOztzVq2YK+c1lwXO8qNtaEfzgbcD1pcwcps2bbpOvvV+KHj/erKsjsjU+orRtpdqdd1WpCHTWS5LdapyWqrcKP8mtR1Mq4HHGahktstux92kNEQtMr7daa1vsHy9qsq204qTG5Sy7aCuZohhfIA74q1awhieKqum35tverEFxwOMVcWVYsCJkOf4asae4AWmQzeYnTH1qWCDDZ7H0Fap6kmjEMj1/pUoXmqsX7lc1aSTjigxkD/dP5Vz3irSo7q2YNXQyrvI5qnqln5sLD270uazNMPU5ZXPmX4y6V/Z11uVFKknHFeXYEj3CyJIkm0jcvG8V9D/GLwjJIm7hhzj2rw3xNDcacrLGMtnNfWZPjvstn0kacasEcDf6BqOpruaGSW3jlBfzMssgz6eteU/tNfso+F/2gdQjm1SRNG+zp5aJFHt81R7+uMjPvX0Ddarda3YiHyz8q/MF4JPSuU1PS7jxFeR2NvHteHJfdyx+lfXKvTcTnqcPxrO7Pib9s7/glZ4DPhTR9V+Eq6hp+p2MGy+triQv9qcfxrwcd/wA6+RNa8GfEr4FalJHrun6rHbqm9WmifY6DuDiv2k03wPLIum21vbrJfW7H58/67n+mKb8e/hL/AMNKi10PXLa1soVT7GTCBuiU8Ekn86wqVrPTVHLDh902uR2PyZ+Hn7SWn3GlLp9xCI59uSQcE5rutG+IMOuhfs88awwjk564r0r9sX/glr4f8A6/b2/w/k1DWr4AtMYwDtA9R2HTk+lfGHirw94m+EfiL7PercQx7irZ9jg/ypckKh2L61h1eeqPqHSdbaa9S6jZdnfnpXovhjxurad+5mWTyiMBx0NfNHw9+KcN7EtuDGu0DLHJya9I0Dxba+HJVkt5RcK3zOrDjNefXw562Fx8tNT6t8H/ABtk0rwvEUuvJumPK7v5Cvbvg/8AtFrbzW2bpdi8uhb5ix68V8FWfxC/tXUPOT90pOFG7gdOK9I8H+JY9F1GNpi+66GQ27+VeW6clI+ko4iFaHJNH6z/AAa+NkeokeYy8qGB3ZByK940bxBZazZKysrbsZPYV+YngP4+f8I74et47cxs0iqPUp25PrXvHwz/AGkmttKWN5mkf72GbGR2xTlZbnyuccHvEfvaGjPqnxd4R0nXI2DRx7vVcZzXlXir4OyWepGSy8wqzZ9hVfwn8Yl1do5PNUbuSN1d5p/j63vyqyNH+NcVTC06iPnHluLwfuvU4i90a60OBGkXPHbtT7G9+2LtZdpxXpl1bWOtxKo8pmx1xms+8+GKD54mCljniuCrgpQ2ehzfXEtKmjOBksNv51CNOBP3a7hfA8ka/d3c00/D6aX7q7foK45UJGqxdO17nE/2avzcde4oXTHUfd+Ud67y1+GkxPTdn1FbWm/DTj94PzFTHBykzOpmdOCvc4Pw/wCGjeyLu4UH0r0bwN4DWzvVmKttXkHFbGj+BILZlYjp1HSuit7VbVNq8KK9PDYJQd5HgZhmzqLlgTwoIhx+NSrLzUKtkU7divT9D5uXmSsMg1CyZantLhajkbJ71QlEazbWpyHcKjOKM9+lCkVyk2cUZ461GGyOacG4o5hco4KTQ5+X3pvmYPWkL4HPrVcwJXButQSH5jUzncM1C3vxRzG0YkE3yCoJTntU8z7T61WlbNZylY6acSrcFuahI4yamkbah+tV5TuJIrncmdtOJCzbfr61Tup8fjVic7x1xVOU9f8AZ7muepI7KaK9xMUX1rPuJizbcHaasXMvmS8HjFVZp1hI3NXDUmejTjYaY9o+Vu9edftB/HXR/gv4LvtT1e5jt47OMyHccFvQCtb4s/FCz+Hnh251K6nWG3t42d2ZsBQBk5r8SP8AgpV/wUEv/wBpz4hTaRos0i+GNPbazqcNduO+c/drqwOFdeWmw6tRU1zzOC/bk/bT1D9qD4r3F6zNHplrO/2a3ZuoBIDE/SvnDxr48k8Q3nzbVWMYOD1xTPGGteS0iopjk7k9hXDS33m+Y+cD0z1r7jB4GEVoj5XMMxlJ2NjTJft+phm+7u611F3pn2cKu7O7HTtXIeEJc3UbdmYEg969DvYd99CwXAVASc9eK9CpGz0PLpyco3ZU0qER3O3HG3rjrXT6bbqLBOfbmsO1nC3jPtAB+6K2DJ5eh+Zg5DAdelc1R6nVTiaOlafuEMZHOCMnvXKeNLDByuWXO0kDoa7TwZfb7ZR8rMgYDPNYev3CwztE+G8zJJI781NNtTLqJcmhzPhNWbzo13YWM5HrzUN/LI9yuOygD2ra8K2AtbOZiw3SuYwD0xmqeuwtavIseNytjd3Irfm1ucnLoY/iLSpBdrIyncxAPHWtRYW0/TGdvvzYQZqbym1K+tW6lowD7Y61YudPbULxJP8AllD0A/nRKXRiUTJ1pvIulDceYoUEd6hvdWhs3WNW27Rjp1qTXJGurot8v7sFV55Ncnq+qLHc7V2ttGCfU1pCncwqTsftN4vhSCxuNpG7B3Anqcdq5mw0bfpLNJndIcoPau41zQzdw3Uzbssw+U9/pWLNo+54PvK0fIHqK/Ib2PvFLQ4mLTFiW6WRBujRiBisHTrmSzikz8pA5BHUV1/iy0kt/wDU/eLYI9RXFeIbjyrtiuY2kwVUnp64qkzSOpBczx2eorNPlY5N2PY8Yry74xPe+LlW2uFZoWlG7aOuen9a9K8YpH9mhZWLxphiue9cv4X01vE/jPzMM8KPjYP4cdM11UvdXMbRie2fs2+CIdF8L28Masp2jaOma9o0SxxerG2VBHHPeuY+F3hxY9KiOWXaNwH92u0s4mhvAyrlm6Yrza9Rylc2i0jf0S4bStVjXI+Yjp3r1HSNU+1x8lemOK8rih+0hccc8n3rq/CV80BWIvkg9zzis+hG7PSdObfGd3UDitbT23D/AGumK5XS7r+63tW/p10c/wC0tZ8xXQ3IWYKNoPvV6ybzFxnbWfZz4Tlv1q5aSct7n8qpMOhqR/c7fnUmdydOKrRDKjrVuNcRrmtLitYZ5G5v/r00qVIqdoM/N78VPFbcZoKuVBErdRSrbeWV9/SrMlpk7u3tQtuU+lGqCMhsHyy89DV6N1OM9x+VV2U4/WmF9rd+1XzA9djRXIHyndUqNkYPWqUNxtepjPn1p3M5RZY37G/vCnSPvk+b7tVzPhelSx3AdKCHF7nM+PtAXU7f3weteCfEfwJ9juJJFO1celfS2qWguYGDfexXmvxF8P8A2i0kCgbj0q6NaVOaaPay7ENe6z5f1OJtJnZmbaM9h1rmLjWBomqNfmby9w+TI5Nex+I/hyzOW3Db1bj7teV/E7weiypGsgkSM9emK+uwuMUobn22BcZ6GN4V+KV9a+OrWRnDW6HcqhPfOTXoPiT4px6880mn2K215INjvHwSOhNeH6ldKmsR/ZTIzw/w16Po3j+PX9LsbFbcQzRth2UBWf2zXdGtJ6XO+pho3Tseg6Z+zxqWt6C1xZXkaPfIIrmRlzIiHqBx3rhvj/8A8EzPhhrvgyXR7y3jfWLhDMuoSAjyfy98V7T8LvibetfW9jbWzL9n2l8nKbO+a9iHgbRviGi6peQuzRoVC/wgfToa9HDK+258vmWJnCVqvweR/OH+1b+y5rH7KvxAubS3na70wSExTRxsu8D/AOtXP/DXxVN4hjWKaZv3fYnBz71+7P7UH7EPh34s6LqF/q1sIdPt1YQqAAW4J6+lfh/+1H8BL74Z/FbUL7wfbXF1oavucxnciEfewfb6V1S1Vpbnm+z19pQ1XU9N8HxRtZRrtP7o8uTXpmiRHVrKFjIvl26gBj0WvmPwD8ZFtLSOK5ZlkXh0I5zXpHhX4wG5lW1Wb9zMeB/dFeXWou57uDxSWh9C6B4guY2WGG4VhG2QR046V6n4c8f3P2JZJpts3ZSMflXzf4c8SJZhZFWQJgEEtXWH416WZo7eWaNZxgLk9a450ZNH2ODxEfZ3Z9jfC74qzXbWsRVmkj6qmT+de0WHxM8vTfMZmTttB5z9K+Cvgp+0bcfCvWrm5jW3vEusiISNuK5rudD/AGkrybxXbvI37uYlhAzDaCe9efLDyjqFfCRxD2Vj7t+Hvxda7vYY42YBRkhuuM17z4c1wanaqxxjHB9a/P8A8C/FiTXdS2zXEds3mBfkGD0r6Y+CXxuttYvxp6TrM0OAXZv0rnlK2jPzzijIrR56UdUe/pCrr8wGKlit1DVR0nUFvoA3qK0rduT0qbXPzCpzRbRJB8n8quRqrDpVeIACpVk4raKPPqXLCfKf609TuqJX+X+lPWTtitEznaZJu2U3zMGmvJxUbSUczDl7kzSgj/69JvzVbzcUqS/8BNTzhyE55NPJAFQeZn+Kl3DvVcwOmSlsGlDZqISY/wAKa8uB9TT5gjFk7NgUyRvmH6iowxHegvk0+YtQJA/y1HK4J/3fWmyGo5GyKnmNIxGyNVV3GOv51LO2RVeYAke3Ss5SZ1QiRSOADn1qvNtx/SppnCHNZd7qIjOKxlOx20ot7Drh9vP6VnXV0WAx680lxqDNLx9OtVZ59kec/M3rXHUqHoU6dtyC8uFQHPy+9cl408Yx+G9NuLyaSOOC1QyyO5wABya1td1uGzgkkmfYYxuPP86/JX/gqt/wVO/4SrWb74e+Db7bbwrJFqV7HJ989Cin+dYYfDTxE+SJ3OpGlHmkcn/wVO/4KYXXxf1O78H+FbqSHQLZil7cRtj7S3QqMdq/PXUvEktpJujx5aDLcdKr+K/GfmzMyZiBbhc/ex3P1rjdY8SzaxMys22P0H51+g5bgVTgkkfI5lmPM2XtT8QLrMjtITvYEZPaseOFtrKfXBqJZV3bW9eCO1aNvCJQq7v9YBg+pr3uVRWh845ubuy74XiMV1D2XeDXqNzlrSNl2gmPjHU8V5poo+zX6RFQ205PtXpkcWzTYJeG2p1B6Vz19ztw8bKxhJMTfqPm3dDXTW8ZutPkiA3LgEY7YrntMg337SZz2+tdHp8xgt7ja37zZnrXHOR0QJ/h/dtHfSKAcM2BkdKg8aWrPrCBF3OrMCR0xTfCGqtbXK5HzSMd3tV3XJ11Cdki2q2/JI71jK6lc0v7iMLULgWd3bwKw3N8xwO9M1mDMk8jK2GXcPepZtLJ1tWbaduQOetbGt6XJdW1qqqqyMmCvpW3MtDnaZjeGZSmjefIBvUbEBqvrOuf2dYSbiqyMO3BxVto1tp/JXmOE/NzwTWHrFl9uu98jZbHC/3RWkbX1JbdjD1HU3kt3mGQzKQlQ6P4JuNXtPOaFdrH5S38Xqabrk/zeTGFIj5J9KngttSvoFZZJAoGFAboK9CMbLQ4KkruzP3b8RaGpsm2qVdnx+Ncs2l+ZDcBsqyHGfevR9TbzdQ8nBZUyAPU1g6j4Yjs4mZty7skj1r8XcW3ofcxqWWp5D4gt2t5ZZJmCjBP0rx3xBd/2n4qkkYny4x8p969b+IepC0guIm+Q7WUhuoHNeCa5r32W8+7tjfhjnvXRTpPc7qOpa8f6mbWwlbcF3gImD+Nd58AvAELWy3DFmadt/uDXnHg6ZfiD4khs12lYXHyNySK+lfhN4Z+wyrEY/LWMHbxjFTiKnLHlR1WO/8ABFothbMq5bcefY10y2oEKlhhgeKw9AtJIb9mTO1ucHoMV1aSbouAP8K81EkemR4Z1+XaPmAq1Jq7WgWRY8r0bHaoo1NpODtG16lmAggYbeHyuT3q3sK+p2vhHW1vrFGDiur066Yg/kK8l+HV/wCU8sTZBRuM+lelaXeMYx39PeuZ6Gp1VvNsRc8GtixlWRfwrmtPu/N+Uk/T0rb0iQKh3frTjIDchyUC/wB3mrlup8sZOQ3Ws+ymVnBz+FaUD5VV/I4reJMiyyfJ26dKltNxXmmxjOO/4VNDGCua0t2JHqu7ovtihoefmWpYk3bfWpHTIp6kc2pSnhypxx64qpL8w9P8a1HtTtzVWaz+XcufpWcjanJFON2QdeKmjnZR1OPemyrgbcc0ka/L7+hpRN7Jotrzx61JGPLP3ahVTgYznoKHZgen1NaJmLjrYkl3TOVH5VzXirT2w3y5BroUm2zbs9qoa5fRyll/iokrlUZShM8t8T6ELq1faPnIIrwrxj4fkW/vmkhaRVBGfevpi+037Rv2/lXnfjzwjJ9iunX5WZSBx1NbYfEODsfXZbj+V2PjOXWv+Eb1yZ5YxIcnHFdZ8L9R+036NGscksnO3GWJ7CuY+JWjt4d8RSefGx3MxJPQ/SrPw38Sw+C9etbyI7WV/MUsPlz719Rg8RdK59Z70oXR9SfDnV49HuJriWGSFpFwV28A4717t8B9XiOlNazXSsZhvVD1AP8A+uvDfC2tnxv4VuLuQeZJIob92MK2elVYvisfhxaMlxHNbXvEMDNnLluhr6DD1lB3ex83j8u+tU5Q2keh/tnfFuG7srb4f+H41n1XWgFnuUIK2yZAOce1eIfF7/gnxovgr4Aa1axwx63NdWskomit87GI6ceua9I+GHgSzsfEVtr2ozfbNY1JhFt35CgmvUPGHxQttP8AEFr4HtSsd1qsRMe3k46EV1ylGacp/I8XD062BnCnR1trK5/Pz+1L/wAE+fEXwusm1aEyLK4+0vAkJXy1JI9a8f8AD91r3gERXN9pt0qOMLNsO1vpX7s/t2fs9WWifDSHT0efUfEetzLDtRsqkeRnj6CuG8cf8E39Dv8A9nCxurix+z6xbxq4hB+UZGdvT865KftI3g9bH0k5YDEwjiIS5XJ29fP0PyesP2iYdS0xbeabyjGB8ueaZ/wndv4g+Zflk6Bi2K9a/aB/4Jd6oNbe60FvJkdTJLED8sZ6180+NPhF4v8AhCWW+tJPs0f/AC1HzYHqcVvTjTkY4mrisLGzXMu6PVtL8WXmlwxlL1ZVibcoV92013Hgj4mazdX8ckcibsbckfcPrXz/APDT4nLp11EkjxqrNl2ZPu/nXqXh2+fxBrbX8LrDpfAd1PH1xXPiMOystzvmerPpr4Z/EDVNOsJrq81NpoQwJQHG5j719JfsyeMLfQ/E1pqFxfC4Fw6ApGfuMe2a/Pey+JFw5On2N0DY78SPJnaMcZ/Gvob4MeOLrSLfT5GkUmPa6vDxvPuK8LFYe2rPoqlaGIpOKP2a+HuvjUdEgdd21kBGTXV2l0GPrXzN+yh8ZR418OQMzFfJRVbJ68c19CaTqUc6BlbO70ry1LU/F84y+VGtJNHTW03y81MG4rNt7reauRSZXrj8a6Iyuj5irTsWS/y8VKr5/KoI36VJ5mOxzWnMYNCyvjnrUJmyMUk0mKglbJ4NS5FRpk28EULJk8fzquGwvX8qA+DU8xXsy0r5/CnK/FVxJz7VJ5mB/s1SZLptE6y+ppDJxwah83NOV9wzT5mJQHb/AJaPOCflUZcAVDJPj86OZlxjcsFzio2kwvNMe5+XqKrTX6BfmYClzGkabexYd1C8jk9Kz7y+EB+Zvwqvc6z5gKx87eKqPGZDvkNZTqI7aOHtrIbdakzhjnC1lXN1uk4+9Ums6jDDEyhhu/Wsq0mZ5P6E9a4K1TWyPXo0klct+WYTuZqyNe8VQ6LBJJcMFEYyF/vVX8VeJobO2aNpN0mcdcCvzp/4K1f8FRLX9nzw5ceF/Dt7bXvjC8i8vap3fYwf4m54IzxVYbDzrTUYlVKkacOabOW/4LG/8FYYfC+lXnw/8G3P/E6uGMV7cwTcWkeCCMj+L8eK/H3XfE+1nkaRpZpGLM7HLSEnkmq3jH4gXXiTV7vUL+4e81C8laaeVm+aR2OSf1rl5ZZp38xj94V95leVxpRSZ8dmWaObtEt3OpyX87O2falSUTdFAyaqQxYI/wBk9zVu0XJX5frX0CiloeBKo5PUic+XJt+7zxW94cjDyQbj/H0rBvZGNx689q6DwxCz3cKr97dkc1UtiqOsjWsrcnXVIHPmYNejajGtlosYAA4wePWuG8MxNJ4v8qQf8tRn2r0PxUuy2AVVdeBxx7V59Z6pHqYePutmLo8cZuG3L8qjcAO9aNpIDJOx+UMPSqVlixgeRup4GaW4dpUXyQzM2BgdzXG1qbXsi9paLcTeZGu0L8pA7V02geEBaXl1qd4DFZW6ffYfKX9B6mk8G+AptEMNxrUclrayEOqH5Xm+g6kVu+K5dS+I3iCz0mzVrPTrNg5ixhY0HJdj6/Ws5ayGtInOan4fxqAuFhby9odnxwM9hT9Tn+ypxh5pUwP9gV3Xgjwj/wALh8dNbwmSPw9pMZ82eT5VkZersePlFcJ4r8Y2MOv3un2fl3lvHMy+eDgED0qo66EabnD6w/k3yxB+vLe9Q6m/2bSppFGC55PoK2riDS7ueWTzWt5m42vyufY1R8QaRNf2cdvGpZZDhitdMGroxl1OFjkF5fYjbhjyMV00dtJBDGsaSuwUbiOma3NL+CU1hZrcNGVjdsA7huP0rbXTZrCJY1KqoyAI/mx9TnrXb7RbI5fZvdn7j3umW4iMuAGXkknjNcZ8RNehstFuC86qxBCkjr9K+f8ARf26bi+kkt9YjMTTcCRRhV/+vUXjT43WnjeFYrW6VlhPzEt9/ivyujRVz7KWFqQepzXxW8W/bBcFpN0mMDPXg14T8StZkt7XOGaSQgRKDyTXU/F3xIsjrKJgj5yq+teeeFYbj4qfEmwsVDNHZsHfPfmuqpFQhzHpYWJ7p+zD8PWs72G6miZZbjA3Nxtyc8V9OeG9L+yzncRuHQ561y3gPw/b6XZwL/dAA46YFdxawGSPcnDLxyetfOzbk7s6pM2tLmw+WVs4xgVuWEiqMMM8cY7Vz9tK6pGdp962NO+dFYfeJqYqxnI0TDvtsfxDnPpUcjb1IfovpU6PvByML3NNaBWn2M2Vbnmr6GZk6ZdNpXiVW3YjlHA969L0TUfMCtu3DGRXn2t2CwRLNwrRsCpI/Cui8Oaq0kUe3btIArkqKzN4yud/pt9+8K/jW3Z6jhfmb8K4+wvmSUNj5exrbtrwEr82ahMtnW6Re7k5xn+VbljLulXuMVyFhcDLMCcnpXS6RcYjDH+LjNdNMmVzoLR8qDj61YgjGc5XmquncQ/rVyKIYz/k1ttqYyLESbjkY9qnjG8496ggYh8e1Wo1J6mmncxkxDHyfSopLXeduPyq5HHvPK9KkaL2p8pj7XlMefTmA4qOGzYdV/Str7NuK8fjTXtNmeKn2ZtHFaamaLT5eMfSmzQ7UPHNaRtMDjOaa9vuHv3quQFWMS5tmZDhT9a5jX90E+OnHeu6kh2RY5rgPGRYX7Lz060pqyO3D1OZ2KMdx5bctnNVdYtYdRiZWwOKYtztHb5aSWdZU4bmsEzri3F3R4Z8cvgrDr8L3FvAH8hSWz/F/nFfL/iywk017iG4b7OIiSMjt2r9BL+0jv7d4/l9/evB/j3+z3b+LrGeW2UrdBScKcButenhcXyaM+zyXN4u1OqeV/Br47ap4J0dZGlj+yLmOJHGQT2PtXtX9nf8NGana6sZltbfTVUFQudxxyfpnNfLb+G9Q8NW8ml3R8iGMl8sDziux+EPjPWNBguI01F47NQdwD4DjsBX1WDxUXFX2Poq2Bcn7WhufVCarH8PNLuJDtZiQLeZ+eenHpWJ8OfFa2vi6TVr63mm1yRSLaY8iIEdB6V5ro/xG1L4j6fZaOxjX7KSxlJ98/jXYX3iCPSoV+zySyXFuvz7Bwx9jXbOq21y7GEcvi4OFVas7zwzYzeMPjXa6jqVydQazXI8z7kXXgfnXvGqwWetzbVW3+y26guSQQT6Yr5p8G6zPpIt1RTJcXxL7OQynrya6jw7qGryavfWsUg+zEZkZ3+6SM8V2YesoqzV7nz2bZM5zUoS5VFHn/xx0d9U+JUq6ZBGtsu7e0cY2t9a+evjt+zlp/ibTrqFbO1YRoWl81QDjnOK+n9e0u5stSUrMvkQ7pHx0YZ5ya8r+Injmx8RXMiQ26xqvyupP+tHesnLufW4GjzUo03qrH5u6z/wTY1r9oPxbqFn4Ht4LPU9Ngaf7MW2mdVzyOec8V88xf8ACSfCXxldeDtcjuNLuLeTy7mO4G0o319Pp61+1/7N/g6x1P8Aaj8L6lp6/YVto2jnVfvTjHIPqK5D/goF+xx8O/2ivjx4h07VLO10HV5IjJa3MCFGLheWcr1GOa66MnKF2fnWeYOOGx7jR00v+J+a+g6pbvbw2FrJbXiyYd27MRx14rsvBepX2neJYw9+0MEiqAEcsqY68V5D8Rvgt8QP2Xr68udW0u6k8MxXDQJqkULNAcMcfNgYyBXSeBvGqeMNMW50WSTdDjzc9q5cXhb6nTl+bcrs9z9PP2EPjjNcXy6f5sao0pAB4LAYwa+/vCGpG4totnfmvxF/Z/8AjLL4V8Q2N9ueS4R/Lbb8oz9Pxr9Qv2W/2iR8QLFUZvLmjjUGIHP5V8fi8PKlO/QWdUY14+0hufV2n3Qbvn3rThkytcj4b1tZYVLHae2a37e8Yt94e3NTSqpn51isO1KxrwTYWnmaqSXGFoFxu+6f1rbmPPdN3J5Z8nFQSSVG8uRTDJx8ufyqXI0jT0JhLgUvmZPX8KgEvPejcNtHNcr2ZYEtOEh3c1WEmDSiXmq5g9mXEk/wpytiqe9fWnGfb/FVKRDpE8kyhTVSef5ty0ksyj+Kq01zjpUyma06I2+vZTGdoXNZvkSu26RvvdqsXN7tVi2BWTdav87YYkAflWFStY9CjRZoCSO0TrjFZereJAFKryfWsnV9ZZQdvU+9ZP8AbEKsxmbaT1rmlVb0R306CXvMtS3jzuzM3Q9axfEPjaPRopG85V2qSc9hWd4m8cQxI+JFjjTqc449a/Mz/gq9/wAFgtO+GNlc+DfANyl14kkV4ZrhMMlmDxknu3tWmGwdSvU5KerHWxFOjDnqbHVf8FWP+Cwem/AfSLrwf4Pnju/Fl1HkzIdy2We5Pr7V+L3izxrrfxO8T32sarfT319fSGWe4mYszsfrWbr+q33jXX7jUNSupru6unMk08jFmdjzVuCFYowqHjvX6FgMtp4WnaO/VnwuYZjPET8ig1p5T7W5bqTStF8uCueOKtXSqCdvXPNNjh3Lk5r1o7HjSWpXgt2/+tVgjavPapEAi5qOddiH1bvWm5ny2RRADzjqea67wji0nhmfnaciuXs7bzZVxnrXU6ZE0VzDGvt1qqj0sa4ZNu53fhrRZNW8QNdKu0FwzewrofEECzSeW0m3DZBPGRWd4Yum0bfNxuZfX2pp1JtY1BpJD90ZAB4ry6kr6nvcqjCwwRRSz+Wz5VeSQOK63wr4w0vwZKq2umpe3i/8trr5liP+yvT8642K6UXBbb8v86sRlWDOi4kb1PWudmPN9522m6neeLPEH2+7uGeSI4y5+VF68CvZrX4YXA+Hvn27KupeJsqAT80MAP3iewPNee/s7+EI5/EdsmoxyXUb/vJIx3A6Cuk/aW8aSfDm0a3s5I31DUFyUVyfsqdAtc+sp2R0aKN5GH8XPivpvwp+Ecnw78OyRzXV5Lv1bUkHzSjORCrddoPX1rxfTLJbeLzGQ7RyPVjWRJfXF/rBa4LSeZyW6ljmu/8ADngHUvGMUcOl25Yr9+R+FX3rq5eVHGpObbOTudBe6mUSN5Ql5JP8Iru9J+H0Wq+HoZ/tErR2v8TjaX9hWy/w00fwLbn7Xff2xqijd5cLZjj+prjfHnxEk0CyG1i90/yxRR9IvTitI62sHLZXNq4lmslW2tba4mjH3pXxt57ACr9ta2tvCqy2LedjLqrcL6VJ8HvCuranZx6heTSSNcKNscgJVPovc12Gs7dAnEcWn2se75me5mAeQ+uOeKTqqLsw5HJXR6X4v8NbnaQFcJnK1xsurLok0itI0ft05r2fxjo32W0uGVexP4182fGDWv7PvBuYqy8sT35r4TCLmlY/QJO6M7xd4+kma48yQSBQQi57/Wve/wBhf4ZSXHh5dZvI9tzekshYfdXIxg18r6JbyfEH4haVpNuu/wC2Tgvjuuea/R74QeGF0XRba1WLyYbaNUUAYAwKWaS5VyIKUep3Fjpot1jUBmGMc9jXSaTEpURt19awrSciPbxkHitO2u/MjA2/MOtfPsp6nQeWhG7JO3gCr2muq/MvbtWTYTZG76A1pQKqzDqNw59KRma8BywXcWB7UzUoWRVaPHyHn1xUUIwq9asz3O6P7vQdKrpYhkeplb7TJDu+bbjB9areBdTaCNUk+8pIwD2qL7T5FzgH5W61l395/wAI9qnmL8yTHr6GuerG5rTPVLPUwIVP5D0rY0643rx83GTXB+HtXW9t48yDc3Wuq0K62llUjngVzQ7GzWh2mlS+VGu7GDyOa6TTbjy4RtbNcXb3SxKg38+npXQ6TqSmVfm+XvW8XoT0Or0+/eMfMx29K3LFt4+9xXPWLedHnOea3dOXCL/KtomdS1jTt1zVuD5m21VtF3McZq5Am5sY6V0U0efUZPHHuGal2bhz3FEQwKmCEDOM11KmjjlKxD5RB+nvQkf+TVoLnrR5QIo9mZ+0Kxj3NUclqVJ4/Cr6wZb+VEsLY5H5Gq9mVGskZE0fDZrhvG1ipumZe4r0S7j2H8K53xHpa3Fs2fp0rnrUtLHpYWt7x5jNZYyvbuao3cfkn73T0rcvo1hnkT+6fTrWXfQgbvlG01wyjY9yLbMOe5aN9oZm3Vm6mO5bPtW1e23l/MtZt1a+aQxG5envU67HRDTY84+JvwpsvH8O5wsUqjIZRivmbxx8M9V8Ia6xjaf7N5uGZT8pX6V9oXGltHCx429frXL67pEF3uWSFZGkBHK5AruwuMnTep9RlWeTw/uy1R886P8AEu1sblbWNo/tHl7PkGPLOPvZ9a29H8X3GlPErXDeWzjCjncAc7ql8ffs27L+TULOHLvyQvBNeeWNrrHg3U2/tdJmhzmMgHgehr6ajjYyR9th8ZhsQuaD1PqLwx8QPD9pHHLNffvSMxtnv6Crtrrc7RXWoyzNZwTKFDfwn0NfLekeOrO91X7MwWNF+eIsfTk/1rqG+ON54l1Wz0ne0sSgAxxn5eDxmvSp1tNSamXx5uZa3PUNW166XTprqDUDNCrbXVuEcD0rz660Gb4h+JXn023WNbdCwKkBCBzj3qovxEik1GbS9RWGC3swxIBwpPp6VyVz46uNe1aGx8Ps2lW8ZJf5vvfT2rXnTVztjRcY2ie8+DBJ4K0fUPElhMllrFn8kKuBt3EAY964Lx1HceKTdeKNSaTUte1T/Rz5X3YwRtJPpXL6Z451TX4I9JlddtrISrZwZWzxmuj8LXcuna08MlwYY7gZKLyM1vTrJNHyeYYSMpOctWafiHS3+KH7NNr4M8VTWP8AZ2oBYGtzbgu6Ln58/wB73Nfl1+01+xZ4j+CfjXVNY+HtvrEnhm3kI2N1UgnOCOo46V+s+n64uqTCGaCPfaxGK3IH3QerZ9areOfAOh+K/Bf2XZ9l+ztshDsC0znnewHbOa9KjUjPRnwuLwThN+bPx7+E/wC0dHrskFu8LWuoQ5VwXwzOPavtb9iv9r2fw14pijvJhbyH92eQAf1rzX9rP/glpqDz3XiLwvpfl6o2ZFjt1Obhuuce+f0r5a0XVfFvwb8bWNj4w0+/0z9+FDTwtHt7ZGeteZmWBjODsZ0a1SD5aux/Qv8ABP42yeM7VLmOXfHnAw33q988Oawt1Zq38Tdc9q/PH9hXxJJc+ErCZZGurV4VKOp+4DjFfdHw88QQ32nR/vFyMfL3r4KMXCVjjzOjCWsTv0uGYcMfwqUXGFrNW4Cxj6VIkyj5vWuqMmfPexL3nAiml8VX8wGn+cAOKrmM/Z2JVYijfg1F5/rT87hRzBykgkyPxpTK3c1AZAh+lJJcUczDlJWmAP0oNxg//XqqZAWPOailuhnHf2o5jRUyea7Cnryao3uo7BuP6VBeXW1dw6rWHqOss7EdsdKzlUsdVKii/qGrrs69e1YOoatsBXLKKq6hrUdv96QbuoBrl9d8WR+Xu3DjriuWU7s9CnTsauteIFtlZt+W9z0rhvFXjhdPjeSSTbwSu48D3NZ3iTxbus5JFZVVeme9fmJ/wVc/4Kof8Iil58P/AATerJrUhMV/fRtn7KpByqkH73T6V6GBwc68+SBji8VCjDmkO/4Kuf8ABXFfDpvPAfgK9M2rMDFf6hBL8tr1BRcfxfyr8tbiS41y8kuLqWaaeZjI8sjZZ2PXJNVFV9SvJLi4ZpZpGLOzHLOx5JP1rXtrVnjXB6Hn2r9CweX08NDlhv1Z8DjswniJ3lsJbW+5lY/KvfAqy8Yzx8uOlPVPm29F7ipEtvMPstd0bLc827ZBFB5gHvUc0OwgAcVpw6eQucbeKqTW0nmVcLMmUWitMoB56AVWl/en+lbUHhafU4t0a/r1rSsfBsOlW5uL2aNG/hTu1bq1iORt2MPSNP3TL8p9c12WlaYomSZhz2BFVLBYGTzPuKh4461Leai8cWQ5X0xXJWld2R34WCjqzdj1USGRW4DDaParemxqkDc7S1YOjTiRSerZ6mtg3AEO1fvE5JrhqJrRHb7S+oQqIbg5+baeM1raOFuplVV3TM3AHas+CyaVWZfvbehruvhZosWjQS6hJH5lwo/dqw6mspWsOlC8rns3wV+Kmkfs6+EtRuNR09dQ8QahDstg5B8g9m/DNeK6/BdeNNZvNQvjI73J3FnycH0H5113hzwxN4r1pbqaRiV+aRpOFT6Vd8Ya7pfhi28m1aOW8wf3hOVT6VlzdEdEop6s47wz8NNP0147i/WRUk5RAuZH/wAK7RNL1LWka201HsbGNciOFvnI9yK870rUNQ169mkM8jRx53uw4/OqN54y1hI5IbC4mhhLFW28bq1jGTMvdSskbniHR7mxDLatFAN2JHllBJNaXwm+GelalrDX2oTLqE1v+8ldP9Wg9ya5fSvD2pa5eq0yM42gKTk5Nd9epH4D8OJaquGlG6aMKd0vtinUqOOgvZpl7x34hvNTZbXw+rRxE7BJFwqj/e6VyU3ws8Yak/mJHG3qXm8xz7nbnFdT4X+GfiX44zxx2Tvo+i2eGupUBCxr1x6ZIr1h9G1jQLG3s/DMmn6XYW4KGSc5lu24+c/571wVMQoHRGjzbHpHj0Ri2dpGPl7eStfG/wC0TqMNtPM+flX7h9q+mPin44hg02fdL2JYD+GviP42+IpvFvjS10mxZpJr6ZYUx2ycV4uW4d83MfWVp8kT3L/gn/4GTXL+68TXMbKkY8u2Ld+cEj8q+7/h+WXT0Ut82cfN2rwj4FfD6P4beCND0eFVVYYEMhAzubqf1Ne+aFJ9mjRV29BjFeNmM+eq2tjWnflOjggCRtu2nnjNWYYyCuWOehqBiDCjfdfpS2978ob+Lo3vXlSKaNTT7sxt8v8ACcEZrZsmLr1+oNc1p0uJ/lzyckGt2CTKbs89Tj0qSGjch/fKrbjx+tPuGZom7bevvVXT7sBVKt8vpWhs81RwPm4qlsZyMi6BfY3cdRT9X0j+3dLUKu2RRmp9QtvLLbh8q9MUywvFtX+8dvTB71nKJSZm+B9YaO8e3k27om2kHtXpGiTt5q9Pl9K8p8QW40HV/tSBtshywFdh4O8TtdRKMn5jXPKFtUdHNdHpltefOhzyetbFnequGB/CuP067/eA/wCTW5aSKm3/AGjk0bBHzPQPD+oZRdvRhzmux02VZI1xuzXnmi3PlwRuDxXceGrxbiGtYy7mdaOh0Fsm1lx/EavRJwfr1qjbPuC471oW78YrtpHl1ty1E4ytWMZPsetV9vQ981Yhfaf5V3UzgqEscWfX6GpBECKRXL/7NWI1ynvXRGNzkkMWAbd1DR7kqdV45+lKV3AbeK09mY8+plXFpvjOePwrK1XTt8f+NdPJAWFVZ7FZQV2/jWM6Nzto4izPJ/EnhaQuzom7nJPpXMX2nNGNrBlPvXtt7oKvG3y8NXLa34GS53Mq9j1rhq4V7nv4XMovSR5TLbB3ZWGRVO5t1B+Xn+ldPrXh9tPkdduAP1rGks2Dkr8v1HWuGVOzse1CSeqMSa283O75V9qytRjjtdwCbm/hOOTXS3VrvOMEcVnz6MrKMfeznnvSWhtGVtzEsrGMpunj+92NY/i74X6Z44tvLuYduRgEcV2b6ZtjO4fjUbWiyEEY+mK1jUaNKWIqU5c1Nnzp43/Y33p5+nzN5kIbYBjof8mvPLT4K6l4Gv5GaOaGaNt6vndvIr7WgtFmj929qr6n4Ns9TjxcRxyZ65Wu+jmE49T38NxFWh7sz4l/4Rb7XFJfXEjzXDsWkQ+5psug2ujRedArQTqQyqT94ntX11q/wR0HUWx9mUE9cVyniT9lnT9Vl3QoyfL8oyevavSp5ovtHr0+JIyVmfOtnPCIo59qrcMdzNn0rs9J1e1vIFa3iVbhUwMHJau+u/2OrqaSPy4VKhccMTuzXWfD79kdbBk861VCvBJJzj862lmcbXRz1syw7V2zyOw1CKe4hWETeczbG+p612+l+Bb6+lR2tXkWNAp3Dgd817V4W/Zl0vSbwytbQs6tuyOa7aw+G9jEAFj2Z9B1qI5vKLPFxWZUH8J4JD4F1ZLmOeV5GWJSI1AyB9K87/aV/ZS8I/H/AMJSWOs6X5mocOs6rtkBHQg19pXXg6EWm1YR8ox061xvifwUskp/0dNxGDkVvLNJTjueBXxMZs+YP2VPhr/wprwvBoE0MyR242ROxySo6ZIr6k+HxeG3Xy2J7g9a5SXwIUu1Yxqqqf4RXXeC7b+ztyDKjj3rxK2rucsqnMtT0zS7zzrdCTyw5+tXkkyfpWNpRCxZNals3T3qFe550o63LsEhI56+/apELE/Wq8Rw9WlOCKs55Dhhfwo38U0tk9eaje4Cmgz5SUy7Rz196guLjYv3s+2agu7vCde/51l3+rCM8GjmNY07l271AxJwccVmyayEY7mOaytS1piuNx+X3rD1fxTHawsxkG6pcjpp0zd1HxAxzg/LnpjrXPa54kjhib95tboBnpXJa98SVIZIXZm9h0Ncfrfi6Vow0rBc9SfWolc6qdPudZrvizerbW+Y8Ak1xev+LEtxIsswVlUtt6hjWPJ4juNUR13bFjHcbc18X/8ABS7/AIKF6T+z54NuvDmhXwvPG16pjjSLBFkpyN7+/oOtb4PCTrTUIrcnFYqFGHNI5n/gp/8A8FQJfhVpN14S8K3kDeIryPy5mjJP2ND3443V+T9/c3XiXWbi9vJZJbm6kaWSVjkuxOSTVvWtd1Dxx4huNQ1O6e7vb6QvPLK2WkY+9P8AI+ysqKu3acN71+kZfgYYanyx37n57mGOniJ3ew6ztFii3ctL29qvWluwj3fhUMKllO1frmr1sm9QG/8A113bHn7jYrct9PWrVvB5YOePSphaeUmRwPemr8z4/hFZuRpCL6lqy/e/LtyvqadJp/2ib5Y/u+3Sp9IT7XepGnrgjHWul8Q2cOhWQ28sVy/tSjOzNOW61OTbXW0ceXboGm6ZPaq/2aS7YzXUhJ68mq/25BeFlUDnqe1TLI15drzurVz7ExjfQniVpW2jhccYq5BpM1/OvHynjrSSBraI46461a0KJp513MdufWsZNvU2px6Gl/YbaTYK7R7d4wOetLpy4+Zj82eK2Uh/ti0aANzGPkNQ+HfCV5f3WxYm6+lcrkup0ypu6sXtGQlw52t6Ke9eieGdJuJwryIVi4PT+Vcbp2lto11lgMqcDIzg12Fh4hmMY3SMsapgKfWueR1UY2GeM/G0tgzW9q3kwqMEL1rlo9Om17UIZE3Sq3HPQe5rc8P+GX8Ra4JJI/MhZ+cjjFd89rYaK32fT4I57heSgHFHOo6Ir2bk9Tj7nR5rDSY7W0s5GQkb2xwxpmmeDRZXiyXRhaQniMkBRWp458X6rYQhZYzHGekcaY21jfDvwt4q8c6/Gui6bPqVxI2AgQsF9zU87tdhyxTsj07w1oOnaJ/pl5NDFIke5Y05Cjt+NaHgz4Y3/wASdVbVtRtm0Xwva5Mt/cYWWceiA+vrXoHw2/Zcsfhfdf218SLqKa4ZBLFpxl24bsMf41e8aalffFTUbaFo47PR7clYbG3YBFHbNcVStbU1jHmehzFx45uLsyaF4btvsPhm3UFd0e571/UnvzVu38CQanEJdYuJ2uG+4gbaI1+mK66w8KW3h6yZ1kTeoCu45CAdAKhe9lc5WAMuThpBywrzKlVN6HZTjZHyP8WPjWnkXYEhO4Hdz1rkP2PfBTfEf4qSeILzm308nyM8hmx/SvEtb8VX3iS9jt8v++cIoB5yTX2x+yp8PofCHhiwt9v7zbvfjqa9bFU44ajpuzWjiPrFTyR9NfDu0WZY5GG7avU9q9I0iNirE/LtAxXD/D/y7ZGGfvDIIPArvbGbbbrn0HTvXw9bVtntx0NhWCIyHq3Sn2TqGw38HT3qoLncdpXn19Ksp8+ePunqa45FSNKD5nXjaV5IrThky2A3J6gVkWUhaPIZQ3v3qwlywfI6r94VmSbccrIqkHjuBW1ZXgRlIPbj2rnLK4Vm9N/ftWgzrJb/ALv7woizOS1NPUWMi9Dg+nesi73RR7cFWU/nWhZ7sJ5mdx5x2qa90R7hGk5IA4Aqt0Bi3RXU9NKSqHbkD2rE0DWJtI1JYZCy+W3UdxW6mnsk542fjWB4lt5IblXT7ynJ+lTy30Kiz1LQ9Z+1wxkMwrrdHvvmRX53dya8j8K+Jdyxpk5XjJr0LQ7mSba+7/VisXFo2PRtKucheuB+VdVoN80I+V2Kj0rgtH1hXgVe4HJrr/Cd4so+b5vXFSN3a1PQtHvhPEp+7xWtazbfzrmdLuhF/u46VuW14MgHIrspSsebiKZrRzg/e4qaKXBXndWakqlc1btWzEPrXoU5XehwVKehoxS5PYfhV2GRV61nRycAVaiZQgzya7qZ59SJcQh6mCfP+FQ2oG1quRRZXNdUY6HDJWZGId5qOW0w1WiKjZd38qJQEpWKbQqRyMVC+nLMnQVoPACORUbQlTx9eKz5C41X0Oc1fwXFdK26JWz3xXEeJfh4Y9zRpu4yAK9aG6Q98d6r3lh5in5d3FcdTCqR6OFzOpTdmfOt74duLK6OUYAc9KgS38xjuRfyr2/VvBkWo7tyY965XV/hVGSfLPOc15lTDSifT4fNKdRWlued/wBkK/X7uelRTeHsPuUdOgFdu3w5mj/i3VYT4dyFvmcbQOaw9jJnR9agnozgU0vf94bW77atWvhl7lcFfl9TXdW/gaO3JLZPbkVJ/wAI8sONq7QPTvVRptB9ci9jlNO8E20Ts7HJbnNatpodrFIP3Ct7mtVtM2r8v6ikW2ZF7fhT1J9s2WLfTLVY12qqfhTn0iFsMoA9SOKhjgkk4HQegq1bWzKcH9aSOeUn3HRaRHj5R161cj05YU45+opsMbRr96pvtPlD72a2ic0pSexSvLVn/wBkelYWr6Z54Octk9TXTXNwrAjqccVjaidi/jya6Ex05s5htLEBYEKc/rTtP05Imyq7Q3Un1q5qEKrubOe4PXFR2D/aE2nPy8HPehnQpaXNnTn2Kqj8zWnbDABz17Vm2UG75l9BgVpRkgAZ/WpMZstwPsPzfrU7TY5OBx61RSTafmP0qvd6mkKNvb6DNVdmPLc0JL5VP3s+lZ97q8cII3fN14NYeq+JVg+XOB7Vy2seMlVmKsBjjmp5rGsKJ02seJ9hba3b8q5nVvFTKOvXnIOK5y/8USTyttOFxzWLeau07fe68DNZOpdnXGika+r+MiGO1m3N3BrA1XU7jVI9w3bc9QajlvYx8uAx7nuTRNq/lRbFUqT19qS1NNEY8WnMbh8tvcncBnpUWqQxRWW652qh6DuCKTxF4li8P2c08kiRrt3F2IFfnT/wUN/4KnjwzY33hnwNOs98rGO7v433Lb9RhfevQwuFnWlyxRy4jFRpx5pM6j/gpL/wVA034HWsvhXwlNDqHiqZCkjRsDHYcdWx/FzwK/JPxF4k1Lxzr91qWqXk13e3UhkmnlcszMTzyas619s1nWZtRup5Lq5uHMsssp3PISckn8aSC1Nwm6RVj7Zx1r73L8DTw8LR36s+GzDHTxE9diGCzVlGNuVHGPSrccablDAH3p+naPdX8oS3t7ibnB2oTXWWnwI8Rz6V9ukhtbS1zwbi5jiJ/AnNelzJHlyucvDb7gu1Nyk1etotjrkdDwK6jSvBum2IVbzWrOHb97ygZMflUzaH4ZV2K6teybSTkW3B/WolNGkYt6nOah8xX+6R27UlvGHXaa6CWPQQCFkvp2XsVCU6HVbC1ZfJsfm/hMjZzWfMa8re5FoVithC1xsZn6ACl1R5tWgfzgIl7Fj1qbUNc1C6CrH5cK542pzUE2kYt/Mvrh13dOOtHMVY5xdIWJixZW57Vc0e3UXAKxlm9uavWltaXFxtj8ybnFdNZ6c1hEscMccbNznHIqpTtoNRvqLofgpNZsmkm/cr6ucVb0/wPax3ixw3CuueQoNVr5bhU2rIzcckV0fgPSLiaIsRhhwBjrXHWqyjG9zroQTexuaTY6XoiIHj3uwwSfWvRtDsrGXQg1naxbn+UnHzCub0D4evdTJJOu7BDHjpXbadpf8AZRXy/wB2qj06V5rrXPQUDg9S8ESTamzNH5MMbZO7itTT/DOlxxM09xuVfnJVela3ibV4bm4NuvzE9W67jWx4V+HrarpUjTQ7LdhlmxVyqtLUcYnOyx28q/6Pv2gfLjgVlqi2eqNIZGV25yvUV2erXWn6dOttHESyjChO/tXR+HPCOj6RZLquqW67Mbo7b+ORu1Qq3UtxZB4RtLPxRpAj1e3X7FDgi4eMCRz6Af1r03wP8c774Q6XLb+FdE03Q9PVf3l7Ig85l9uM5rg9W8YQW8sep6y0Om2MQzHZqo3kdqz9E1LxF+0temHTNOk0vw9bymNZHjK7wOM9OfxrGd2rvYnlS0LeufEe8+NHi/zobWW8ZmOZrls89z9K6/QNHk0O2keSQsp+UheMn29q6Dwz8EovAWkyRW8iyfKFllIAb6CrC+HZbpEtbNGe8mBHzA7Yl/xrz6lVN2idUIox7S6FzfpapG3BByTkMfT616FpnwyF9ZrNf3kdo7fciUfdHvR4f8IR/DLShdXMbXl9MMRKR0J9BVyNYdXTzNS/4+M/dMm1UHoK45VLvQ1Xkfj/APs8+B/+Ey8cQ3Dxs1vaOGB9+tfeHwysfLto227VyFwvavnL9mPwT/wjejjzP9ZIcvgdzX1b8O9NSCJVC/M1etm2I5p+Q8vo8kPM9S8E2y5R/wCHuPQ13NhIECtxgDFcf4NdYk4APGK67TmLRsyqpDHoe9fJ1dWetzF9SMbR83P5VNApaHb6dT61DApS6LfdLckYqflPmAHPAArmkDkW9Pl8wEcAL61c3BoSvG4HnHesuxdobplLYDDpitAqqZb7vbA9ayY7l6F2jVem1f8APNadvcgKvow6jtWNYThs9drcEnvWhbv+6GV+goE7m5bN9tPXaF4A9a1rW78u3MTqOnFc3p95JF8wx9MVr2s3nnc2Pm/WqWpNipcw+TO2/cu48Vl67Y+YPm+72NdFdW/nBW+97GsfV4XYsuR8vaqA45Jm0G+GZP3bHI9q9L8F+I2ubPzFfcMda818Q2zSWzhuq9MCneAvGf2G5FrMSFXj60cvUfMe7+H9VMkh+bCg/nXe6RqCxRo0bdR+deW6Bfwm2Rl+ZWANdFouu7L2OMs23PGaylGxvCXQ9a0LWGaVS7fL0zmuq0/UlkTO7PPevMLS9eFF2twK6HQ9fXaNzZ+naiOm4VKakro9AS8BVcd+tXbKZk/iz+Nc3peoLMnGa14L3K88fSu2jLqebWpG9BMpPzHFXopVK8ZOKwbO53J3rRtbgFvavUo1Lo8urS1NeGbHtVuKVscVkRXOGGOuatRz5auyMjgqUzTR84Df/rpRxnNVYZwSOamWZW68Y4rQ5ZU7Ejncpx+FNjGRzTTMByDSxyeacdKiTRHKyTYuOv4UjrgdKI1wc0/O4ZpElae38wHGPyqhdaaGHvWrIDVeSPfzWNSmmb06jTMK50wiqslo0QPat+aLclU7q0JUmueVHU9GnXb3MNg2/wBqjULj/GtCW05aqZh2n5l71zSpo76dTTQryQqx/wDrVXuLPn5ePerTx89Kq3E3ljvWEqaOqE2QoskL+3arSXKpyzfpWXLqe1jVeXWc+1TGFjWSbNy5mVl4bjPaqdzertKisuTVm2fKwrPutVYE4cda0sgjFm1PeOB8vPHes+4ud4Od30zVWPW8L8x3Buajm1RXHynbz61RUYkjzMQ3zKKIJ4Y03e9Zmo6jmT5WyMYIFRWt7GGw/fpzUs0sdNa6zHsVgpKnpzUk+rswC/l9Kwk1SG3i+VkUDmsbVfGixNhWZeetARp3Z0moeJvs7su/kdMnrXN+IfGnlnllXj161y+q+J5LiZtrNuPf0rEuLqS7nXczMe3pilzGippG/feKfPB2sWb61lzzyScvxkZ5NVxZsoPc+3anSLgtub5ugJNYyuzVWRI08YB3EKuKptIs7gRkbeeMUl3aBYF3N0681iX3iCKyhKx53fwtnrUId+pqzmK2DPIyJjnn71ct47+Jmn+FNGmvry6gs7W2UtLPKwVFQDJOa4r4xfHjSfhf4autU1zUI7aOFC4UuNzY7Adc1+Vn7c/7aviL9pHU5rMX0mieD1OBBFLh7tc9W78+lerl2BlXnbp3PNxmOjSV+p3X7fX/AAVNuvirrd14K+Ht3t0+RjDdamM/vh3WP0B6Z718s+DfAFxrej61CYpJpJIjI7EbiHHPX35NcbZ6ho2m6kkmnWtxcMv8UzcfUCvcv2cPGKzardW7Ku7UoWiKkfKSeOK+1hhYUIKNM+Tq4qdWV5nisHh+NrbbcSbZB/CF6e1XJNTsdKu4lhtY5lXgyTKcg/TOK0PFOgy6JrsyMGUJKRk9MZprabb6tH91VmH8PY/Su+FTS558qepS1LxJqj/LHdbLc/dES7B+lEsKavpn74u1yvOT3FPGntp/mQzRsv8Ad9qbby+VOd7cDgY71blfVBGnYowQeV8rYx9atQOIm+ULt6fWt7S/CMXiKN5YyFZOCD2pW8CLYSZmmVlXoq1PtY7M2VNowjaS3YLxxt6cd61NF8H319txCV9GfpV59WNpbeRGiwpnlgOTWnpVwtrp8jecUeToztkn6VlKq1sX7NPcdF4WsLELFfa5BbyDkqqliD7VoyaR4Pez/wBK1fU7qRRj5YcL+dcDrjtNqrENvOcjNdV4b8JzapZIjKv7zqanmsryY1FXsjU0LwZ4ZvLjdZ32qsN38US4/OuouPh2Jo99vcRlVXrIdp/+vV7SbSx8FeHkhht1nnbqwHepv7Pu9Tt42kbZk5CDtWEq2t7m0aGhy8HgJpbtRHIJWH3iPu16d8O/h7ny13feGW9qr6F4WMTo0YVpG4wO1et+DPCj6ZpqtL/rZAOnpXl4zFN6I9DD0bK5iw+H1TdFDu2qcBvWsjXn/sseU7N6ECu51fUzGXt7WD94vtgZ+tc9LaQ2O681Py2mP3Yv8a56dTTU6JROZ03RFBW4kj8uPOQW+81dgnjFW0mPTI1ZmmOFEY/ma5fUop/EtwqxttWTso4jFeufCzwFZ+CPD51LUF3zBcwrIOnvVVKndi9DBsPBFv4VlhvL6ESXCjdHGT39TUOueKbPTlFxexx3l9McWttF82D2zWt4he68ez/Z7W2mHmcs7AgH2FdR4Y+H+m/B2zXUNSgW81y8H+iQP8zJ747VMavcJd1ucv4Q/Z+k8VzLrfjJpE09sPHZgAPJ6DHpXvWh+JYNC8Pw2OjaPDplrgBVKZk2j/GuR8E63qt7qMkmqWv+swIiVzt+g7V6l4e06PTla6uofL3Lne38I9a5cTir6II09bsi0KGbxCiy3ljFawY4LDB+pqKWS2tb1poYVWG34UjjzMdyaml8Tw6pPKlsD9ljHzyE5rC10yeKUEdkTHYQjGfutK1ef7Rt2R0RhbVlDxt8RbGz8y4aKS6viAojTkR+wrzbWNWuPFl158ck0O3IMa/wexru7pLTR4JDdSRsF42RqAWb0JrJm1OZ9v2HT4416uFjz16ZropWtYUo2W58q/DTw/HujWONVVOcDivcPCkeB02lQBxXn3gvS47ZMpj0J9a9I0C2WGNNpPbJB6mjFVLs746aHeeErdli43bm6V2+jwMgXKqQOjE1yfhaLFsjL6dCOc12Wigm3XcG6n8a8mpua8xbMJEhk54Pyn+9VrAAU/KPWoiv2j5fut2z3qQDfFkg52kYx1rnkGpD9y49WznPtVrUI2uLELGWHpj+dUsbpeRhux9quQHzFxu+ZeorOT6FITRFlt5Gjkcu5HAPaui0n5AM/Q+1ZlhCrzdt3qa2bJ9qbQvzf3vSoRUixDbia5V+ynGK0/s5hT5fvfeFZthORPzlh/e9a1oR8mNx6fgKuJJZspQF/efnVPVYlBLDHzDFT7PKKjduDevakvLMSp65/SqJ6nLanp6upUbWB5riPENhJpt150MeGB5r0jVLT7OXVVB9DXN67aC7j2/dOMc1W244mp8N/Gi3dn+8mAMfGDXqeiRHVLPzYj86jIA7V8xPFdeFr7zI5P3X8VetfCL4urI0dvJ8objiqlEV2nc9i8PeJHVTDOu1ycVv6dqCocLXFX7mWNbiFg3fitPw9qwu7Y53KwOOT1rKVM7qcro9N8PauCArSY211VlqW6LC/ga8u0/UPI27W7etdLoHiLzYwGP4mnTlZ2ZFSnc9Aspt6nJJ9a0rSTaQp69a5LS9dVDt3qVzW/ZapHIcht3HQdq9CjM8yrRZtxSlG+WrMc3Pv6VkRXqmMYqdL9WPpXXGqefKi2a0d0sbZqZdQOe1Y/2pXTgnNSC4xGtX7VmLoLqa8N3vOferMFwA/Wsa3nA681dhmwfarjU7nHVo2NZTuX5acgx8tV4p8r8vFPMuO/Na8yOP2buSMcDmonTKrg0ocgev1phbn6UOQRjYbKilMVBL0NTSEEVBJJtX7tZyN4FOaBSDVGeHaelaE3aqVzwhrlqRPQoyZQmTAPpWfeugXa1aVyflrG1Y/L71xyZ6dGNzD1QMrZT8qybq4MX1PY1o39xuzt3DB/KsbUX2E/KzEjt2rO56CQlxqTRjHf0qnNfNM5aPvxVe9kO1m6kD8azRqLwDg49jRzByM1J7nyvvtjHpWZe6zJs3Rnv3qtcayHT5g3TnmsnUNVAX5Tjvz2ouiuWxqvrp+zszHDcnFYl94xaFvlb5geRnpWDqevSRzHDblx2rLk1X7S7ELz3bNHMaRi+p1UvjKR8L3xniqrX812+S3y+9YcX3+ck465rQi37NvZhRzIC7ChL7tzbferMIjiI2v8q+tZqSOLfC+vNK93sjbdt6dTQBo3V8sUZKk/41TfV1twGkw3fpzWTd66loo8zcy9Rg9awdZ8VEQmWaVbe0iBYtIwUAdyTUsnmRveIvFgwyxmNt3TPYV8//ALUX7YHhn4C+HZpbzUI0ulH7uFCGkkPoBXgX7aH/AAU+sfBhvfD3gX/iZ6ureVJe5/cRcc4P8RFfnR4x8YeIviV4tk1DXtQur65kY5MrZCHPYdvwr18vymdV889Inl4zMI01yx3PQv2pP22vEXxn1pmVWt7KN227/mcgnv2FeLsjam5ufMaY4JYMf6V1134ZL2allVvMX5geprJt/DX2J22xtt/unjFfY4WnTpR5Yo+ZxE5zleRQ0vQlmbzBCRu9Oleg+BvK0vU7W4hk8t4WGVxiub02KQXIj7Z6A9K7DTdPgtotyozOwwGHatK0rmdOGppeM/Dy3WoySLtlhuPnXPOAa52fwfHkSWrEMvVfeukhRri32iTC4wBTLeyvPOMexiFPBUZrjjVaO6NONjlL/Tbi4Ux3ELeYBwzLWf8A8Io0G2SVHVP7xXivVtO0W6vcfbF/dKcDK84rpl8Jrr1glnZy2c7DgJIu0j8a1WKaF9Xj1PEdG13+wp9sK7i3UkcGugsb618Q/KVZZM/METrXo8X7Mep3TmaO2t229URwSfpWj4L/AGV/GnifXfI0Hw/cM6kbpJ1wq+9OdeDWu5Hs7HnP/Cs9OvoC0kk0AbncRUlp8JtGnKquqM3l8BWU819Lj9lXVvCOn+Z4umtIZkGfJt8MzD8O9ZFl4AP9ostr4ba3t0+7NOgJkHriuOWKt1Kjh76nitj8CI7t1aJTOg43bea6fRvhy+mwpH5ThV77TxXrp0+/0u1K6fYSH1IjxmpNJ0fVL6J2vF8lk6LjrXLPFt9Top4W2p5rpvw9RHG5XfJyMiryeGGikbzl+UdAK9Cj0K6KbypznhdtSWvh2W7u42aHMeRvJXpXLLFN7nXCijP8AeDVZftMkYWGPlVPUmuhvNQvJ5lht41UHo3pXSWnh5LmxjjSfy4wcE4xmr994ftvDttGYg00jcGTHJNckq13dm/JZWODvdIvNIiFxcI0xkHyIP5msW28Kw6jf/aNWuljj+9sHRfqa9MubebVo1j8mTys4LEZxWppfwW0vW41m1K4RYIzuKx9Wx2q44ixnKOhyPw38MWviXUiul2vnpGdquycH6V6defDCYp5mtRx2lrFhYomO53PqQKuW3i618OWKaX4U0uNZ87fOYAAn1zWb4l8Z2/hu3nm1rUzqGsyoUjt4zlUPsKl3bM7s2NDuPDXhORrm+uNs0eBbQqgZnPbirjaZp+prLrF1CokxuSWY5fJ7L6V5r8L9DuNa11dc8RLJZ7M/ZLViRvHqa9WsrCPxFdrNqTQ2um2xBWNBzIfSuetUa0uVCKbuR+EdEl1S4+3N+4sbcEs7j5n9hTvE3ii88ZXMWn2aeRYq+Hkx98DjFbHiLUI7/SiZNthpNtjGBgyVyc/iJdSMZtf3dmr7I1HDM3auWV5PyOiEVuzW8f3Fr4M0ay02zXb5xDSYHUdya559Vv41k8oBFkGFOMADua3PihYw6dPDcXUnlrDEAFJ5Y8d68/8ZfEy31PSPs9quzyxhmz972FdVCnJ7IiVRLQlS4XxLr62Ucvmyx/cGPlJ7sa9Q8H6QukaX5EcMc0itmWUr99v/rV5z8JdNkPhmfXo7fLTjyYievBxVrxn8RLjQzaW1veNBtQlyDy7E8n9K9bD0Ujgr1W9EeC6OucBVzztNd94XRvMRew/I1xuiIsT/wCyeMnvXd+G7dt8eDtCj5vpXj1pXPaR6D4UjJiU9OoxjrXZafGFRQmdwHOa5PwrGyhF6r1yK7iyg3Jn5enIzXDJC5hsS7n3K3sc96dNIqD5voBSpHsuPlywz3HApkrFg2MZzxxXPI1iVU+aRs8t2GKsWEmyZ1P4mq4GDhm2tnk1NCQZfw5NZM0NKDzNwP8AD61qadcZHzbunT1rOswuPlYttqzpRyjY+Zs0itzXsWDPgYbmtOIM4+UcdTjtWXaDnjC+o9a1oACgZTQiS1CTIwbG4dxU0kPmj5Tt9vWq8Rwueq8ZxU0DbpCuCoXpmtBehn38LRysvbGQa5PX3ZJPuf8AAvSu9ni805Zfmx0rmPFFgkikbSrduKqQbI4rVrKO/sWjZdwbrmuStdUuPB+qiRQ3l7gF46V2d9C6z7V+6vGKytUtY71fLkQBmGBntWkWTI9O+HPxhXUbRY7iRQwGAK7zT9WWeLzI5FxjJA618ph7jwbqiliTCxBzmvXfAvi8XdqjQyqzY5BPNU431NISs7ntWjXnnQq25vat/T9TwQleY6X4v+xYZmbDHAA7V2Gla/GSrc7uKwcdTr5r6ne6ZrDWxUHucfSuj0rW97BVbFedWutJK3zfgRWzYauIZFw23njmrjdClFNanpVtfbyOTnFaVrcYGPzzXD6X4hdnXJWti11lZX/2q2UzklRfQ6uK6VvlB/8ArVL9qwAO3eudt9UUTfeX6Zq7Dras+0lVH1raNQ45UGdBp0gZ8Vo2/wAp61h6fP5jBlPFaCzsf4q6oyR59am72NqGQLHzUyvke2OlZMV5tizVmPUBW0ZI4JUXcug5SmGTYvNVDecfeIqKS/2/xZp+0SEqLuXTKrfdqG6OFqomodf4aWS8wv8AeqHURaotMWZg44+tVLiQd/wpZbncM/d44qpcXXHTNc9Souh2UqbIpzlaxtRjLO3atC7nL1l38jJGzfxetcMpHqUVYy57fymbPOayb+Dcvy/xccit1l82M7mx61QnhCA7W3YHBrM6+buc3O6xRNx9aw7+23Ethulb2qzRwhvXqfasGfVI2Lc5HuaC02c/euQSSxCr1rD1nVEjX74LdMe1bWtJ9oDeW2M+neuZm0Vp7pmbO1hj6GgsyZFkuCw5IboamtNGZQrLn/aNbUOnJZgfNuxTjdxxH7oxQPmIba1+zR/vMHJ71aaSKELubbWXrWuxxsg/unisPXvE3n3Hlxtt45ANHMkTzHSXOswQnZJIOvTFYut+KI2UpHwF9q4nxB44t9FVpbq5X93yVY8n6185/Hv9t6HQftFno/8ApF0VKkhuENVGMpuyMKlZI9w+Mf7QuifCXSpLvUrqFWVSVi3fOcDoBXw/8df2vfEP7RPnWNvM+maLICqxRH5pB/tH8OlebeKPHus/E2aefUrqaSaY4AY7gnPavQfhT8ILaLwjcXE6ySMFJQjt/nmvUoYWNO0p7nHUrN7Hz43w0/tG+mzvXaSS2O9VB4UTT9VjXyvOVgCSV4NfR2nfDZv9MuFjDRtkAk1zKfC6TU74/umKp/dWveo4pWszy61G+p5DrWnKbgSRrtKDhccAU7TvFK208cN1plteQ9yy7ePqK9MvPhNqlxNth0+ZvmxuC9RRq/wcu7q1REsZ1nb5fu45rojXj1Zyyo3OR0/RfCviaZmXSbizbHzNDJkCu48Afs8eGvFMDNceKIdHgVchbkbSTVPw/wDDDWPC7fPasu7qSM1pap4a/tCLbKJAh7dOaxnX10ZpCiktTB8WfBeHQ55FsNV02+VmwkiShSR9KXRPB95psm7/AEdcd9wYP+NQ6z8M7x5EaOT90ozweVp48JX0thFbw3MnzNg/N0FT7RNWuVyjtaFxf6zBZtDErOQu8NkLWrP8Ko9NuU36tBJN1Aic8Vv6T8M7TRtNVvtjXUm3L4U5U+mam0zw22ks81rZz3EjnAyMmo9t2L5Sn4a+FM82oLdf2tfR+Vz5KMfnNelWHirxXcRR2drJNptsOGkDnc3uTWl4G+G+taoY5rhVtYSAcsMED0r0DT9Fs9MjRTG17OvGAOlc9TEFxpnO+HvC2pXs6zTXckzfe3SEnJrcljlf5Zgm6M8t6/hXW6R4Xm1SBQtv9mHf1rqdD+EFokDT3Duz4/j6E1xVK2psopI8mlmW7kWPY8jYzhVwtVpvA9xqzMUTyV6nI616l4ptNO0Nf3cKbicZWsO4mTXoVSBjHu447CuaVZs6IxSRw9t4Smaf7Lu2rnDKBk1pS+FrfTn8uNWdscj0+tdBa6ZHpMrR27eZJjl2bk0W2lTTuWmbaW+6vrWfO2a3SMKx8DPLKJLhlVScqvYVvWugWqy7p5k2J3/hUVJqWnzWdqv3VDdcnJxWYdHk1e1Md1cNHb5yQp5NOOpmyxca7pcZa3tgJuCPMP3QKwNQSbVFMdrIyswwHx8qD6VujQdNjt9rblhiHC4+99a634X+CR47ulENufJh9tqDHqa0itTOTstTza2stUt4FsdJtpry8uflMxBAT1NdR4e+E+i/CkRalrcy6tq7DeYnIIRjzgCu++InibSfhZF/Zehx/wBoa3ccTSD7sWfftivOL+K2064NxqEklzqUh8zH3lj9a2crIw+ILe8k8Y60b6W0a0hXgK/BPsBXQCxe+uo7i43q0bfu4Bwu3saw7rxjbWcNu1upmmHdh8q1FZeL9Q8TX+6NdrMdm49IxXHUk29DppxJPiBf3Ot3KwtIGt4Ru8pOmfQ1Hbp/ZmoaazeWvzB3X+FPrXSaF4IS1DTyOZlZd0srn5SfavG/2hPiknhyY6bpHz3E74eQfNtHtW2FoyqPlSFUqRgja/aU+IC+M/EMem2civJ1YxHIRfU15WmqR6v4tsdDs3Z23bZj1WJe5PvUFxr/APwhHhqa7mzNrOqfJAh5YA9Kv/CXwfdaZrC/aFjOqalztJ+5nqT9BX0VHCxjE8qpXbdj3zTNb03wv4FZp5lWysYSsOTjcfWvn6f4veH7fUbm41S4LT3b7kDfwoOmPzNdP8Yde/tu2n8MQ3CfZ9JTzLmVCPmbuM/hXydqPh+6+I2vX01qSbe0k8lWZuG+ldmGwvNucFbENbH03o8Kyt2GP6V3HhiDe2cc59K5DQbfDsx+VecV3vhO1Lj5W+Ydc+9fH1Nj6yOjO28OWe2CMjrnpXYaXFstx6dRiue0O32Iv8Sj0HJro9PLDav90HIPeuUknWBh16Z+bNVrmPYxZQAuMVedN0Zbd7EetQyWm4bssx+vFY1FdG0ZGSjK0uFb5sde4pdzW8vUc9z3p7Luueeqii4dSF/TNczVjWJf064YIenYcd607CL7Pv8ATgg1g2t0Y3CkD1AFdBYXCsi7QTkZINItOxoWD7Tn9a2LcYiXb35PrWZZyCST7q88H2rRtQVl28/X0oJLUMoR1Xn6VYjCuwYsNwPNRxQqXyw+6MCnBlRz8p4q4gPl4Yt2xWZqcCzru7L1NaccxbHON3BqC7h8ssc/ge9XInY5PUdNjkk3oq1zet2DCUsqgd+a7C6j2X6ru+Rs5qrqOnx3C9sVPMLU8/1TTI9UtSsw5B4NcuNQvvBV35iMxj/uj0r0q/0DazLHuKnnNY+ueEv7RtJFZPlIwD3FbRkNLU1vBPxQt9dWJGkKtnJDY4r2vwpq1rdWifvFbgZINfHWs6DN4cvi1vIy7efrXW/C74+to94lvd7irHH0quZM2g2fWllOqzfK3yk8VqI8jSCTPygV5Z4f+JMOtxxtC/B7CuusvEe9QvmE+wo5U9jZSO+0zUdoG7dn1rcsdRLBcNtPp6V53Y+ImO3nGOv0rb0nXFZt2fY5pcpSlc7eO8KH7341Ygmdpw27PvXJjWWiXOeCasw667DCscexotYOVM9L0rWFVFVmPvWp/awEQ+b5frXmdhqUiSKwkb0xmugsdVARdzbs9cmtY1GtDjqYVN3O1tdWWVRtY1bj1FQPvfnXJ2moqqZDZx6d6sDVAU9PxrT2zRyzwd9jpPtYdc1Xe62nk81h/wBrlPbH60DVWkJ/oazlXuSsG0bS3olJAqQTt/DWPaXGTuqws+FzuzUqsyZYcvPJuXBP1qvI+Miq5uWDEg//AFqjeWQdWqblRptE8a5BZqoX6qvPb61V1HWTApG7bzXP6z4n2Bv3hyOOtTKxtGLuaGo6hHDleee9ZF3qiwRMzNgVgav4vDLtzhvrXP33iKSZyok/DNHKzTY1tf1KKQN/t8Vzsw8yRvm+X+dV7m/3li7t7Vm3+uLbx535o5WaKRoMqQHc7HHWs+/1O3AO371crqvjgpuXd9K5/UPGuYz8zdfWjlKudjqniSO2biQDHtXO3/jHzj97HWuS1DxkseRuLFvU1nQG+1q5C26SMsjAfQE0crJc0tWbOreMluJMBmLjj64rndX8XTRR3FxF8rIh69zXqWk/BuCPR2abasrAtvK5wfrXnfi/wj9gsL5UVpNqnnH60SptGPtkz5N+KvxI1fxDeTmaZgqsRsGeevWvL5PDsck0ssiFppRuyfevWNa8PrfardLJt5c5OPesXXvD8dmgReuODXfRtFaHPI838JeFGuNS8mSP5jJwPUV9MeD/AAzb2/gG68mP5hDtC46mvK/gzoa3nxEPmDcFOBu7819NaR4MFvoEqhlVCDwtbVpO9jM8T0/QVtdJbzF2tISAoFWvAdjNoCTrJaxOtxkKWXOK6zUtEWxTB+ZVbv2rbsPDsL6X5jEcjr6Uo1GTKOhwb+K7vTrj7OyW0fZSIxxXLeKdXurSYbpFZtwIKjqK6LxXo0NxqEshlbK5CYNYuj+D/wDhINaVZJJNo4HcV2Ql7t2cso66GdqlzO6wSzKpBHAAqhNpjX027yofLAz06V66vwxhvLeOOFV2x8Et2rR/4UXbPp3yypGzfe9RWcqyRSjoeC23wol1a8eSKbMbH5kByDXTeFf2bLzU3b7KsULMcFpTgCvV/C/gLTfCaNIZl2xn5snr+FVfF3xGaVha6bCdq5zInBNZ/WG9i1SfQw/DX7LlrpN0v9oavC27l44znmu3t9C8M+Co1gsLdrqboS68fWuH021vr0s8bTCSQ/eYk4rqPCPw01LVrxZJLlliH3ix5olW7j9ibmmaIt+2dyiPqVB6fhXU2Hg3TdMjikVszSdsZqbT/Ddj4etdok/fuMbmPT3rntbvr20u2W3k81sfez8orklWb1KjT1sdYNZt9ItGXaiso4dlHJrkPFPxp0+Jfs6zGS5HVVHArnvEV1qyoIZrgSl+Sq9hWfoPwfmlnN7KVjEh3Dd1NZc19zaMEtyiviC88XeKGgmb7Pbgb89OKvSXUwmaDTbdmVflZ2NdBa/B+W5dbqKVX5+bd1Arf0/QIdNt2WTyx6nP3qOZPcqTXQ4q0+1WdwilEZlHzEnjNdAjq9t50vzSKMgL2qTUbeMyeXHCuc5yKbb2zNKirs4GMDqPrS5iWYd/PqOrXK+XthVTgbu4rWstBjWBXmYKq8t7/StC4todLha4vGU+WPlUVzg8W2+uXrRpHK8R46YCVcZXdg6F/wAP+Xruu/6VGlppcDcs3WQCtzxz8YF0jQJLHRxHpdtH8pmyEOPWuT8R+PNL0u1b92zG3T5Ix/G3qa8fv7PUPi/4j8u/kkt9M35ADlS/oPpXdTj3OaWup2HhPxxN4l8RyxaapmhhObq/mOQR32+pqx4k8WW93qRs9NkjnkkYiRifujPOTWP4qvbHwrYR6JpkixSMu0GMcucdOKv+DfhvHpohup9sMkqgFQOrHqTUVLK7HFNsu3ehz6lewWtup8pV3SyflxXoGkeEItNtrG1topDPcSBCoH3ye/4Ctbw1YWiCPy4vkjADkj/WGrfjjxVb+DbX+2GbbNariFV7HtWFGMqkrI0qTUI6nHftVfEdfhH4KksbeSOW7ePbIAf9Wa+StK1ya9mjWQtc315L5sjNz5SZzgU/9pL4o6h8XfidDpStI0ZkBlZDyxJ6E16N4c8BaX4ems/tEeLiYLDuA+4uMkmvpadCNGCPHlWcmXfDPw3s7+5k8QapiTyUxaQMeSR/ERWBp+pXWlDVNYZWF9I/2eyUNnOfQV6ZqMdu4+xW6SP9qZY1kYfcUcHH1zXMeItb0/SviFZ2y2Z+y6XHu5HHmcgN9a3oybdjlqStqeEfF3xdc+ErNtPjkzrGpHdeNnrntWz4K8JNb6DAllaqz+Wpn28YYiq3xG8LQ+Lfi/PMo8xreNWZexdj0FekaX4M1jSbKOPTrfchUGQAdGr2qdlBHmybvdmvo0XOB19a9C8HwMTt7Dr9a4fQ4i04bheOleg+FYPKkjJHygZzX53UPu1LU7PSYlijDfNxkcVs2KEyKxC7cDp2rI0lt8YDDjtzWxaMRxjapGelcrEX2GyDnjvih1V4/wDeOBg01HMi/MxY/wAxRC28t/s9KykaLQy7m3aCYM34e9RvGsr/ADL8x7itK8txu/2cc571TMe2Vh7cVzyNYsgUKGUt27etdBoMizoFzg1jCAlVOFH1rQ0mXyXyMMc81BZ1Gn2mAfX19K0olXftPX6Vk6Tcebj728Hkdq2I285c/wARaqSAm2Hbwc07Zv27Wwe+e9SRNuPbdjH0oQKylf4vpVWJRGkgjuOc5AxTr0i4h2r8vvTgg8r/AOt0qENuZgVOPX1oK3MLU7CR2Y8Bh6VkLe+VeJDKPmboR0FdZcQbwVK9RXP6vZGOdW2fdHGBUtAt9SR4fLXr/wDXqNtMWabPy7T2qxZzLepyu0qNuDRNEFDZ+X0pxYHN+JfAlnqkLDbtPYgV5j4w+HIsy0kcbqw4BUcCvapkb+Fs5rP1WCOQ7Hj3K3Vqd9Rps8R8OeM9V8G3W3znKqQMZ6ivWfA/x1hutqzSMrY24PrWJ4g+F9rqgeSPAJyQPeuB1fwhcaJPtj3D5u46VtCRXNc+o9D8Wx3BEgnVt4z97pXV6V4hwo/ebl618g+G/iRqGizRRtlVVsYYcGvVPDHxgSSQLcHb06dBXRGMZFe0tufRmn6xHMuGZtpHWrq6mkRGxgRXlGk/EyyvIv3dxGWxwAa3dN8YR3AVXePdnJ5xSlTZcaiZ6ImuyMflbbtrV07XWuxt3cj3rz2LxLDcoCsi47YPWrmn+Iltn3D+dRytGnMj1Cz1pbcDLcip4vFKvJtBNecReMSzdVAHqaafFfl3O4SDb25rOSYaHrUF4Z0Lb/lPSrFvqUcZwzdOuK8ztfHGE/1yrn/aqaPx5Hb5PmKc+9Y2k2RKzPUBqMbRfK1EmspGv3h+deXz/ESED/XKv0as+7+KENsPmkX6lquMWZSjE9XufEvlrgN0rM1Px8IY2Xd82MZBryLW/i/H92OQM3setc1qfxLmuS21T9c9K1UWZuyPVtZ8f5Xc0ma5TV/iAsuUUnPrXBXHiZr0bpJeF7E9axNa+IENgNu5MjjOehoUCb9j0P8AtsyuWlkwOxJ6VX1HX40YKp3Mw6ivMdO8bvrM5VZFWMdya0NV8eaX4UsiyzrdXmRxndirtYR0niHxI2lW+6ZiqsPkFcRrHj6SSNh5g2+ua5DX/iHda1cvJLJuGfkGeFrjdb8WGBD+8+9weaTt0N4xO01jxzHCG3NubHFcnqnj9pIW8uQ7a5e91aTUIztfGagtdNaRfvfL6Gs+YrlJ7vxZda5fQW8bYLOFye3NfXHwl8L29r4Tt0uFX7UsY2sMZr5K8NwC28V2P7sMgmXcPXmvsvwrPCsVmFX5CAMD0rWLTPPxknFWOmh0+E6Z+/Zti8ADvXmvxD0dLPRb6Rm8tPLbHPWvXtdtI2lgtbFGdXUFj1xXE/tI+HIbbwRtVT5jJgn61vKN1qcNOep8Tjwtb3V5IG+8XLEivP8Ax8m+8aCFfljypyOlfRmgeEbOOG4E6NvKk7j2rx9PCEPjH4izWcat5XmFSfWqpdzsvcx/2c/DElt4mkvLxlaLHynFe9SXNwtoI44wqsDnPpVvwv8ACPTfDOl7LSTzpEI4/umr4tlgLm4wqx8HNFSV2GhwPiLTCLL7q7nPJpthcvp/hO4t2j8yeQYQjtXaTnStUhzuXavygism91PRdBRlmk3egB5qeewn2PLpPCU2oSATRNuZuMDrXd+E/hP/AGdYi4k/cSAg4YfMa1NL8QWGqS+ZYQ5EPUVoahe6l4qkV1jMNvHwdnepliJPQjkW5G95pOiRsrq0kmM8jqa4PxX4zn1DUWh0+OWMNzuIrtD4QS6u1keZtqno3rWnF4Bt3mWR1G/pz0IrP2j6hGKR5VY6dqmpT7ZWTY3DHHWuw0j4eWkFqjFdr9Ccda6x/A62TrJNGqR5+Xtmr1yLWG18u3tZJpsZBHaj2nQ03Oej8M2+gwM81xHEvXBHJ+lY954/huJ2stNSRpF4aTGAa6RPhrrXijUVknjZYB0U1df4Jx6W+4TLDn7wIwaXtEgSXU4eUyGdRKzSP1ODTrzTdY1ODyrcrDE38RHIrs7zwhbWs6+TIrt0Zietaml+DZr6PCsRGo6LWaqXK0SOB0Hwm9iwVm+03P8AebnmtPWDcQQRreNgKeEjFd/pvhK1i+Zm2eWcFugNZHiifT7C6YIqzSJycHOavXcz9ornNabNd3L7YdsMZXJ3Ck1WJbNPOnJbby2TgVT1/wAVCV2W3kEcmQNu3kmq0+kXGpqp1S4ZbaMbio43e1Ci2JszLjxL588jQ7VjU4U1NpGpp5m5FLIvzPIfWoVsLXU5t0KNDaKcDdxuxWtNrel6LpElvaqrLglwfvUcreiK5rHJ+K9SuNeuvNeRobeMkJ/t1y41vUJL77FpEJmbozn7o9TmtjxB4r021gZrqRY4f7oOcCvI/ir+0ha+GrgWPh+E3F1NiOPyxnaT0/GvQw2GbOapWSOo8carpvhGxabxFqMStzsgRgXmI9vSsfTNYufGOkLqyp5MLrssoIj8zDpkivMvDH7OOu+Odf8A+Em+IGqeTbwvvS1R/mCjnBFe6+EJ7W/8m18Pw+XZ26ja7rndj0FdlaMYKyMYzbepq/CT4SW2hWa6nqkv2rUMk4bpAD2FeiWWlLrOvRr5f2eGJQxLc7veszw1dRxRAylWnyQsQ6s3qaml8Sx+Hbe4urnzJLx/lVB/ICvNleT1NoysdDquvW+meVDgN5KmQ44H414V8aPiW/iLUpTFcKqRIRsB4Ldq7Dx1ryeCPB91eXkm26vBuCtywB6LivH9IvbPStPnvtQVN105fyyfmyeletgaHKuaxw4ipdnM+DvA6eCL2XWLxzc3lxIZIlbuT0r0/wAD6ddeI/s+7d50kmWDH7uf8K5rwd4Q1bx74jjmjhaaMr8iDoozxXuGk/Df/hDrBLqRmWbYWcORx04xXdUnfQ5UktTUtfC9rp/lStIWW0h3McdT3xXz/wDE/wAY2f2oSWqSG4uLkYUj73zYA/rX0p8ZPEFlpHw/tY7Yql/PCFlUDs2Bmvm/4m+Gk1Dxx4bsNNzIscimdgOp6gH6murCxV7s5ajvsL4K+Gtw+p/brqPMiD7RIW/i9Pyr2b4c63baNpswuLE3DTMHDc8Dp/Sug8F/D0eLfDlxFHGEuWH3fQLjIBrR8J/Du40aGa3mTfsYFc9QDnivRhNHI1c8T0G03XGQRnPINegaFDtj5+9gZB71xfhqLyrjAX8x39a7XQt0p6d+Ce5r4Go9NT7dLU6nRGwVYcMwxjHetgSNsG714FZOnRZx/Dg5rYjXzkbI+noK45M0LEL+WTu+gx0qWLaVPY4x0qNGUFd3HHWpVO7ocjNYuQDbiBtpyw3Nx06VVkt22s3fOMnvWgP3h7N8uTVd3C5VlPrUFRIVt/OQt6dulOs4tszr6YP1qxb4JLZ+Y9jUyFWP3fmPPvU3Rqrl/TLlYV/i5rbt28xAQ20DrWDax7lPPOO3atbSF/dfMe/509Bmkg8vap/i71YSJsht33TimfZ/PjG0+mKngY7m3Lhh2ph6jhblTnPy46YqG6iMacdD29KnLNnheCcU15CGO3tQBTwsZVs8+4qG+to7gFu+OParLDzSyle/WoZItytgnb0FJk26mSbE2rs2/NR3CtOm75cLV2a2Kyf7PcGmfZiG28bcZqSkZ27yxuPzKTnA7UwbZvlb5VJxkitVrJWUdNzelVLnTi5PtSKuZcmlMWbBC4PAqldaRDcRtDNGrM3tWqYZI3ZmBPepICs1yu7bnvVKTQnE4DxB8JzcJ51u23j7vpXG6r4e1DSASFckHnA617tcxZbavOKoX1lHMPLkhVl9cVvGpYXOeK2PiltOK7lmVk9DXTaN8VZ441XzmkbryentXQax8NNP1VZNirGxHWuN1r4N3Ns7NZzYC8gA9a6Y1hWR2EPxU1CCZWj+VQM49K6jS/jHM0CiSQZ757V4nDaa5o3ySxNLGBknFSHxDNE6rLC+MZ6VftEx2Z9C2fxfsrhBG0nzEdulTR/Em2kba0jADp6GvnrTPFcbZ2syNnAzWpD4qVl2tdKp9M0tGS7o90X4hKysyyBVHHNVZPiG11JtjY5HevIE1rzITtulY55GaSz8YIsjKbgbk4NHL5FI9am8XThtxkzn0NQ3niF5k3OzAfWvNYfFKkc3DD+lRjxVJ5nEu5T6mpdwPQLrxNHbJu3e3NUL/wCJQii2xp5jNxXIS61HcoBJN+FVxqscUgKkN+GakVrm1d+LL7UnKjdGg9qz2Vm3NPITuP3c1XGrSOzAAbfUChZXuU+6xz3qHUsNQZYe8Kw7IdyZ464qnctlssfmqf8As5nxzxTGjjXP8RX1FYyqG0Y2MxpjMxDK20cCsrW9EW4JkypA6AHvW9co0x/dr9feiz0J1G6TGD29KylWSLOY0/Q9wDN91etacsMLWm5MK3TNbt9ZW6WhCkKcdMVyWqJIxMaMVXPGK5/aczLK8Gpx6fr1vIzFvLkU8d+RX2V8NtTtr/QrO4RfMSVAc+hr4vutAksbd7zy2cRKXz6VY/Yq/wCCkNv41+Jlx4KvNLmhmt5PJgYsCGwSCxFenhacpK8eh4+YPY/RDwpcNDd+ZlSG4x6CuJ/aN1tVKRqn2jzvlwo4StLTry4t52jjR9h/iIxnPpVXxtpcdhpDSNm4uZgQoY5xXX9mx58dJXPEPGD2+haCzRQmS7mXaoAzjNeeeE/CiaHHdXkigXEzFl45ya9H1XSryyv2MhV1bgqefyrOezsUZt3+uPRT61mpWVkdkZHO+E9Z1L+0GZ4Wkjz8i471uarYX2tWbRttjkk4OB0qxC7aHtm8kKrDGGHSrF5dC608usqxsxJO444qtw5zg4/h5J9s8r7QzYbJQHiuw074I6Lq1gJr+QQ7euT1qnZ+K7fQA0kNqbudmwTjjFb1kjeLNKZruYWsL87AefpVOK6kuRzC+C9P0WaSLTZvOUN/D/I1tadYX0Uf2eOHyo25L1Fcz6D4JkTbdIjSHGWbPNaC/GrS/DamR4f7SkXG1UPy1jyahzvZGlpHw4urhlY20kityWxxWxB4S/swbriHzG6KgPNcXqnx08T+LGVdNkg0e2x8i7cmoYfGPiNoWjkuB9oxzct3P0qZR7Exv1O41qGO4s9klmsKAY3SHpXPt4j0/wAGtJNcXNvIuMABgxrC1HTdWvo/+JjqUky3A/hbCiiw+Femx7Zmje4PXDNuArP2bZqpJI17L4uajq8yppMKybj94r0pdRbVdTlke+ZfXA4ArQ8P6ZHoE6/Y7ZY1xkhhV3XNN+0w+Y6/L95hnFHshe0sYekeH45B5wYyH+6O9alxd3FhYB7eNY2zgKx+8fSotM1qOOdVskVSgxz0FPvL+1u45UvLpEKDJI4C1UKJM6hyuttql5Oy3t6se45EEOOR+FRzaauiWsc/ks27qZD0HrWP41+Jmh/DqfzNCtZNa1SUfMzNuWP61wOu/EbXtZ3ahrd1Fp8cmf3AfCqK6IUJPcz9pfY7i58caPaXzEafJNOpzGQvBNYfiv4u27hm1KMoYz+7iRfvfXFeZeKfjVHocG+zU3DqvDAZzXmHi/4sXaW66lqk0luzZKRHAwPpXVTw7loZyqJas9a8T/Hy7vnWOG2hs4FbHA+bHtXL+IPinHaaTfXA86GFVzLLIcFh7V5f4c8bTeL5muF/0eGNs/MMtIPatbUtRsvFt1AuorPFYQndJE3HnH3r0KODUdWcs8U3ojHt/HGq/EJXisLGRbHBH2qXO1R61H4T8VeG/hdqU03l/wBtao3+rdxuVG7kU3x58bBeqvh/QY47DTozsYoACT061m+GPhPNHLDCStxfXzAp1YoueTXVKKitdDGM23od3pdrqnxY123Tz5JpJmDtBENqqvX5j6V7X4OtF0aVNJ02AyXMKfvJR0U+grO8G/DuHwFZ29tp5aXULsbZpdvQ47H0rVv9XHgq2mstNX7Zrl0PLe6z8sRPYCvIqS5nyxO6CaV2WElXQvEscEMLXWoSfe2tkR/WupvNFtbFludVlSFbf95k9z2ArlPBvhWT4NeEpNY8SXi3N7MzTyEtyAegNcr+0B8YV8SW3hyy0qRpPtyLLM6n7gPrToYe8jOtWsjI+KvjP/hJPFD2ci/aFA3Jjpntn6VyWg+HLnxnqdvDcRyR2qzbQR0Yg12vgL4cLq+vrLK7yedKASQWLjv9BXv/AIb+Dul6d4gt7eCFfLQeY3y/KhIr0pVVTVkcNr6lr4V+B7HwD4VMj28clw6BlOOT9KoeK7K81bZK0a/Z2lBbOOPavUF0b7dZw20cSjsHb0FYnxLs18PaRIqx7tgM0jfhxis6d27sJStseR+MjJ4l8WLbxwYihh8wjrgLwP5Vtfsz/BH/AIWF4u1GaeGNp7WMzIhHQgcYqvompw2aQ6h5MjzX0JUgnoK+jv2PvAoGvya55Mkdv5QRwPu16EaltDnqXtqeW6L4SuPBnxP1Dw/MZI5pkFzbgE5AOM167pPwdu9bh+0XC+XKQFPH3sDrXV/Hz9n2TV/idoPjSzZoVs4vIlEY/wBaCe9ereG9At77TY5Wk8pmUHa3atIz6GEvI/Kvw+nmP/s4zjvXWaTGIQDxtznGOlc7o6qG3KvtkV0FiFl27vWvjZyufZROpsE2qrY3Gta2PHy7gW4+lZWmKCoH6VqWM2S3+ycVyyuWWow38XzVKIdkf3vvdKiaXJ2hfxp8T7yqg5KjNYgPhlCdqcSpbB596ZKWkGCPl9qaynzF5x60bgmStCsaq2ckmrESbUBwG/pUbRfLhmCqBUkbgjy9wb+lS4mkZFpI2VFZT93r71ehRio2ttzz9Kr2SYYq1aVvkgNt4qTWJc07dIi7myynFaI+V8c5H61lWEhSVh+NaEJVjuLZPpVJlPYmQ7zu2kfU0NtkUjpmlT5kz+VRKjAsrcsKpXJsOljVcfxVDMPm3Bce1SeV8+Od3tTmCuvzDJ+tANGfIimYMQenNOkhWQdlH86nmh3K27C5PHtUUkLNhdoNZyCxGbFUO4H8KhmsssxBw3p61YKMOi/MDzQY8lWP3vbtU7llKSzxHziqEul7jx8p963o7dTJ83pUd1bhl6bu3pRygZARiqrwNvf1pWtEcfPtPpU09k2z5fvelQxxO6/NkNVamb3Klxp8athV6+lULzRZmTdG359q22Vo1+YDj2qB3yAc8GqUmBgy6fJnayhtvXiqt1olrOv7yFd2OuK6YDdGw6/Wq8sAYEeX+lUqjRexxN34DsZ922EAt3rLvfhBbztvWRlbOeO1eiPZLMnIw1RTadhVGTg8VSrMaPNLj4UyJjypm9cg0lt8MmTO5uercfer0VdIaL+FiFp7xbF/1faq+sMrlR54/gWQt8rNt+lMXwxJnlWXHvXdzyqi7W+X61UmtVnYnd2wDU+3kHKjmrbwjs+ZmzmrEPh5Y1/h+U1sJaeQvLBue1TQxMo2hd2aiVRsfKjOgsIkX7vHvSuI4VwBmtq30hrj25xg1et/AyN975fp3rKUxpHJz+Yw2ouN3pTrfw9Ney7c44zXYt4U+zzLtjXHTrVl9Ojhhb93t2+lZyqNbF2OVXwwlkFy2T3x3qtqFsLbPKtxiunuLF5FJCHaRxzWLNpNxc3O1V3DFY6sZzZspNQnVdg68D1rQ0v4ePd3G5lX1xjpXU+GPAF1dXcbeWSueTivTNB+G6wxq21t306VSaBnDeGvhPb6jYSR3MOYWjIbI68V+Z/xJ+H9/wDAP9q7XPEejTfYbeC6IiJPQkj+Vfs5p3hoWumtGy7VZevevzM/bu+A918QvilrFno9vJcMsgunVDtbA+8fcCvosqbs0jxcfa2p9r/sh/HmPxH8OrW38TeIre61uQKYoywVse4rtPHXibZDJNIrLG3ywk9WPtX59fsheDYfEeuL4kuL6Z10tBbWkJbAMq8EkZ6V9r/CvxZH440gPrUkbJpbkoSANxHQCtK9NrY8+nLW7MrxBJfJaApD++k5Uv1ANZJ0O30SwW4mnLXjHdjHQ10fj3xf9ruZL918q1jysa4xkV4z4p+I82oX/l2aNJk885xXLGMmdXMi9q3iHVP7XkNzIrR5+VCeBVpI31mSOR5NpI5UdK4q61K91Gdo5A23ucVLf+K206zEcEm1gMEg81pqkB0/iXx0ug6YLSzjVZo+shA5rhh8WL6W7ZZJJI1PHB4NY19fz37vO0m7d1Gan8OxWepaxFFdMEjJGM+lUrsDodK8O2uv3gluJJroscgbsgV1Npo1ppMW6FVji6NvPWltvGeh+ELZks7dJXYbMkZxVjw7qNlqrb7xVFuCXOegqZRe5pY0bO6t7q5i8tRJsGG2/wANdvothZ3mnRrIvmSAlufvYrxfWP2j9J0e6uodJs4mMJ2s23G41mWX7QdxPdmTb5MgXhQetKPNcyke9X+m2c9uw8+NVjOQh5Oap2WrxxX3kxskMcYySx4FeMQ+N77xjcbFuTYovLN/eNbsU1tY6fuku/tjN95Ubk+taRoN6kc1jvLr4nG6vms9Ph+3XCnAlU8A1FfanNJJt1jUlt49uSiHofSvOl8fR21zu0mJbPBKk9z6mo9VvtF8L2n9veJtUM0Z+byQ4Ab8K6IYczlM7NfE1xqKPY6DD9ok5UTNwsY9657xtLZ+E9GEniDxDDdXA628R4X2NeL/ABV/bv8AtVo2neDbe3sbVxtMq/ePvmvnfxX481TUryaa8v5pZJedzN0Nd9PASerMnWR9GeOf2mLPwuJodBt7dZJF+aR+teaDxZJ4vuxdeJL+WRZTu8tW2oorwfVPEsdk+ZL5prjOSAapy+MtW1yGZZrhlgUYSu2OXnNLFJbHrPir9onR/DOpzWOlxrM2dqsxyBiuHOu3XxF1qS51ebzIojmNAcqorgY/DAuovOYP5gOScdasa9rz6FpKw2ztGG+Ut3NdtPBxS0OGpiXLc7bxn8W20FY7XRlQvEAMg9+ldjqd1dWHw1huUdr6+mi8yRSD8pPYV5v+zl8OIfFWt3txeTKLW3XezuMlj14r33wr4Bm8UNs03zJraT5WOPlUD0NRiJRplYeMp6nH/BX4UNdJJeXsTNM43gEfdJ9Pevob4V/DmbSIG1CSER4QBfMHzY9a2PA3gCHw9psYuFVGtx1Yc49aua/q83ju7Wx0+OS1tbYZd1Ujf7fjXg18Q6krHs0aKpob4q8bR6bYR2eisJtUuG2yTEZ2eyn86SzfT/hpYf2rMyyaoVGI3OWDHvj86o2ukxeBZ7m6ZYZrlMmGI/8ALM+p965JPFdvc3N1qWsSxiOA4hg/jdjgZ+gpUqLY51Ecd8c/Hms/ETxFDp4lY294+2RVPpzzXo3w9+ETautnNthYRWwQknJjAAx+Nc98L/AV14p8ZfbpoB9jEhkgMi8DPVq+itGsLXQvA9xBZxj7ZLIFBHf6V11JJJRRxve434TeAjHPDJH5apCdkmB1969f8NeCJtZlZY8qM/M+OoFaPwK8EQTaPbpeReWzcuQvUcV3GoadF4e1FreMMsM52xsfQ1hZvVmMpW0OZ8T+T4TslMcYlaNVQEcAk15j8T7S61a1lG2RlkQmRh/COwrtPjdZ6hpl9baPar5jNGZsjnB6iu5+HXwHuPG2gNHukVoYUckjIzsyf1NdNGDMZS5dWeBeA/g+178OmubhWhOmkHDdWGa+qf2Q/DDXngC8so922RdwVuDtFYuufAa+OkGzt1aNbhUcqV+8QMkV7H+z78LZvAbyW53NBNApjkYfxdxXXGLb2OepVTVzoNc0P+0fAS2qRsu2MHA7YNY0ng6fUYoTAW2RoFx3r2nRPBHlaQFZVZ2yDkdiaP8AhAltX3RqPnAyAOmK7VgqktUcccXGOjPwx0i4ZJ+PlXGPrXTaeVWNCPv4rkdH3LKd+SMHGPWuo0i5XZtKkMPumvhpI+6jc67SWD26L/F3rUtGjKMm4Fm/SsewnZbcMFPA/OrVrPghm+UNzXPY0vqbVudvDc9hS2zLJMeikDFVF1JYIgnXnOaaJQrbwdq1HKw6mi825doXpznPWqS3RMzK2cqc0GdWX5W3d6JplWIN3b9Kjl7ApGnbz/aFO5v0qURLGqsO5/KqOi3KyS7GPy9veteOzDP975WHrUtFRkT2j7ui7vUmtTT18pmX7wPSsu3YW421tac4ktk2ruwanlNosswwbXzt/HFWUhWL5uvNOt4vPg6YagWpQ7f4etHLrc0vfccrrG3zd+g9Kevzjdtx/WojGqJtzls5FTQzFPvfeIqgbDyWZtytg96a8OTmnPuK7vu+1Oiix944XqKmQr3KboyA7lz3pqyMF3be9aDRiMH+Kqk7mJSSpxnFZu5S1IwVlgPYtUM0IhTcNzMvWpt+0r8p5705oTI+5TkYwaPMu3UiQ+dF8vytjio2gYnBbmpnj2q21arby4/2qTY7IRYdtyV9KlMHHKjHrUcCZm/2j+tTchm+Ysaq4uVEUtgvl9Nw9KrnR1aP7uAa1LdscN/F09qc8as/Bp3DlMNdAVDwx/E05tJwdox7VcniZJNuDmmrFufd6daz9pYr2ae5QbRmjH97FVLmzZzjp6cV0Cusa5xj60rqrn7oZvTFT7QfIjnF05pIvm3Cql8Ps5EaruIHFdYlusy7cYx19qiudGWWPhV+X170+ZlctjkG8Ptex+ZJ9aYNEX5sK3y+1dYbIRJjC59O1Q28O9+F2+ox1qLsdjnbPw2sknzqRzwa2LXRo4yG8tQPpWgbNk6LgUQB0Vvlz9anmYEcekwj7qEleeKmVVfA8s/X1qzaS7T83y7v1qzGkdwiqv8AFSuw5TJfZEflXP1qGW1MnH8J7Ct+bw3Jfhdowq9+9aOh+AGuZcbWbP5UuboBxcekTXFyqrG231Fdb4U+Hhv3+aPaPU9677w98K2WVN6bV9RXdaR4Fi0+JflWpb7EOSON8M/DKCyiVmUbu/Fa93oEdvGNqcLXYLpQjG0Lx0rP1ez2r7elVHuyIy1OVu7dVtWXIHHSvg/9qX4ba58Q/wBouO18L30Oj/aIvKub12ULErHDbs9sZNfempadJKD5S7mboD2r5h+JH7PNl8a/2wPC/guSRrfTLqKS/wBbdZvJzCGGMN1B7cYr6TJFzSsePnUuWFzwX9nn4U2fgH4hah8O7rVrP7XpbyTx36sDHdsFJ4PT0/OuTj+MvjXwTPfXUjiHQ7e+e2WVo8LuJ7dj1rvv+Ci37NHgX4VfGqG6+HfieK6tVtyZLeK8LywTA4O5s9OP0rivGPiO9m/YJ/sPVLO3mvpNW+0Q3Ib5gqsDknvXvVsOlKzPFo1m1c9O8E/FTWvippkOjz28aq4Vhc8Avn2/Guq8Hfs/3Xh/Wfn/ANIjkbdk9z6V4d8LbbTfgTZeD/Fur+LxNY6wyRz2pbcbcHHUexr9MtC0rwjN4N03WdJ1Sy1CO4jWUspBwCAf61z08G22zoniErHy74w+HFtpdoftEK2jL8xO3G6vnb4ga1Zvd3kdmCpjB+bPSvor9vL4g25gk/smWONXUru3ZYV8KaL4guNV8aSWk9w7RyHDNnvXPWo2eh0U6l0dzocs+s6ZH+8MYU9fWtjS5lsLkyT/ADLH0Nc1farHZwNa2sir5Pf1NZNp4ynvCbWWb93/AHvepp0rm17Hox1yTUJ0jg2/vD19BVDxj49vtPjbTtPui8SjEjr69xWY2vQeGdK4fdPdphXHVBXMW9+0KyxGT5m53N1aiVO4SlZCXniD+y5FbcrSNy2eprqvDetafqOkrcS27rcbh8x6Vxt3okOoXsDL80in5xmvR4L3TfCXgmSOSGG4aQcMRylONOxGvU0Y9TttTgI+1WtvxtCmQKxNVZNP1Kzu47fTZFZiuX/eA4H1rwbxTYW2ta2k32yRf3m4KjEFea09Z+J0fhLTJJFuroSsu0MX5OBXbTw9zKUz2q41/Q/hros1/wCJNSMcqtlIUOfMr5/+JXxTT4p63PcRs8Olx5EUbHqK8v8AE3xNufFetNJqUk80Kn92jHIrB1bxtdX18tvCotYl6YGM16VHBpanLUrdDoNc1j7IW+yjayAj6CuS1vVLq9H+ukk9lrZ0+ym1i3YzeYzdj0FR/wBlRwztGrYZeK7o2W5xzk2cvGpS9CupMh55ragE8aKJR94/KBXQ6V4Tt0DXU6iTadpYnvVjUtM+2lI7KPzCvV/7oqXVVzF05WMyzmnSJkZfkxwSO9V9d8Jw3n2cMWmMnAVOqn3rWsfDepXF00Cx/K4ypr174P8A7Kd5q1xBczswjYhn3DlRWNbFRpq46eFlNlX9nr4DX2o2sdrHHJHb3RA3Dr2yTX114V8CaV8NNBtbO0Tc/wDHvO3ee9XPA/w0tvAXhuGa1wqscK7nk468U5YI/EesNcXVwokztSPOMAelfP4jEyqO57NGjGCsZ2teZ4q1NorO33fNg44VB9e9adpo3/CM2f2dbURSMpbe7/6xj/hWqniHT9JHkWsMcM0K44GS5965jxJdyRRtLfXm6ZiWQN8qjPQfhWFOD3NpVFscZ8SHj8O2MjTt50kx3FVOa5T4P/Be88aeMLXXNWl8zS3ZiIBgM6DoK6jWbRdbFvAsLXbRg75FP3ye2K9I+HvhWWzt7aNWEOwAImPuetdftOWNjjnrudF4f+HtrduWhgjhskyVjHVAOP1rY8PaaL4n7PalRHJ5QJPTnqKj8U6vJpNr9ltZEjDrg4HzZ969Y+CXw+jm022uJ2bzlUO67f4cdaz5mzGTO20rwstnoUdvC/k3Ri3cdSevWsnwnpl98SfGcekp5v2yNtwkIyqKPX3ru/DnhS48QGOSEN8p2BiPup0P41678MvhvZ/DjQbvUpbeMSZaXzdvzAV106PNuc86jWnU8t8LfCGx03x3qd5rqyXTxwi2tgxxltvpXtn7OngWLRvAMkb2/wA0zsCTzkdK4Twbo2ofGPx+19MFhtbMt5a7cb89K+h/Cugx6BpEVuo2qqgH616ODpuUvI4MXUajbqcxqXhGz05VYRR+ZwAWXoOhrf03whDDBC3kj5SGBHal1jRftWpwyMfujGMdea6O0h2QKp/hGK9vD4VSlseZWrNRGwW2xfbtUhiUVIBz7UpXJr3qdFJWPPlM/jy8Df8ABVfxj4dYrqOk6ZqkbcsP9W34V614W/4LAeHbq4hGseG9QseAC0LLIoP6V8DpEdueORjFQyW6yD5weeK8arkGDn9n7j2KedYiHW5+q3hL/gqd8KdWULcanfWKsAuJ4eB+RNdp4X/b++Fvieby4fFWmovRRKdufTJNfjqNPULtPOKYLfZIduRzk151ThPDv4ZNHfT4kqfaifuro3xi8LeIbeNrHxBo10rY5juFOP1roTdh4y0M0N0jcjY4NfglZ6hc2j4jnuIfTbIa6HTPjF4q0CSP7Jr+qQhQAClw+B+tefU4Rafuz/A7YcRQ6o/dGFbhQVU7ePXkVVN3cJJtk6Z4I71+M/h39sP4naB+8tfGGqqAc4aUt/Ouv0b/AIKafF3SY41fXPtSxn5fNgDE1yT4VrrZo2jn1F7n612+vyq4Jj4XgkcVvaX4lIA3My7DnFflDo3/AAV4+JFir/arTS7tWOTlSv8AKuz8Of8ABaLXLchtQ8M6fI2cM0crDj2rkqcN4pdDop51QfU/UvS/ElveLtz82epFa2n3EYnZS21exNfnT4T/AOC3/hUvF/aXhnULc/xNCwbn8q9C8Pf8FmPhRfQq91capbyN1V4j8v4159TJcVDeDOynmlGW0kfeVneR+SArbiOhFTPFIEDqd26vk/wX/wAFTPhRrTxraeKLGLzBgiZiOfyr0zwx+3b8O9emWGz8aaLJIo5VpwuM/U1zvAVIu0ov7jqjjIPZnsn2cyjlctSx/ulOVPFc/o/xx8O6/aLcWeqafdZHBS5Uit7TPFMGpwvsaORcA5Dg9aiWHtuaRxCa0J7eL7UB/D61Yddjbdox61Tm1GOBfMUgQqOTnkU211OOfcyzCTbz1xis3RSK9qnsXJLHI3bunamS2rMpBX5WqNtdhkk8tl6jPB61YM5lVNv3WHHNZ+ziHtGtyp/ZbBj6L0FJsaEZx+Z6VZMMgXO7j61DLcKp2N1YdfSolRitio1naxDcqssY+U/h3qs9sjS4Aq7HKoBGeP5U2IRyPg9PWsJU10OiM9Cr9n8uTpxTZE2N8rZ9avrYqT8v3fUmo201VO4H5ulZ2saRkmVhOsiqrLg9M07zUQbcjNTNaqf/ANdV5bRWZufu1OpStcVpt3Ta2OM0yRfMHy8HGTimiBYyPm+92zUkVo0hyud3Q1maFa5G5QFBPvUkc4H3flb3qd7Rt/pTV047wzDPPGKnmAjELebuXP4U2WaR8YU/L3q+lqYR04p4tt+35dq9TSuyrmYT5vVdvvUtlaxryzbs9DWnHo6T4Wpk0FTwgPHpQFysbCParZzxmo40E52iPH0rUi0P5/4vyrd0TwkLhlwjbvTFGwtjlofDZujGNrHbwK6DSvBTBlXy/ocV3WgeB8t909ccDpXYaV4LjhKs4G3qfekZSqJHnej+AZAd2xmz0GOldt4Y8C+XHHuUKPpXY6do8Nqvyr0HcVdWLHRfbpS5bs55V2ZthoCWaDhc9+KmawVyPk49q0hBuHPpQYtoq1Ex9oZstqqDmsPXkQxsuPxxXSXSgtXOeI4pCuQO/aplob09Wc5qieVayMrbdo6mvmbxZ8GtJ+Nfxrkk1rxcfDaeHVF5bG3bZNqyk/PAzAglegweOa+j/Eazf2bMI/lfaQDXgXwT/Zf8K/HH4532sX2tWth4m8D6jHdRWxCyNciTBCODj5CV719Hw2uaozys+uqRyn7cHw2+Cfj/AOFFx4g0WSHwRrnhe2klktYCF+1SBSQrqDzkgdR3rx3/AIJ8/suJ+3Z+yt4/8Xa9qcyDwrbSJpllGTGnmqhdncehwK9F/wCCtHin4Wan8WRHpumx6X48mj8nU02jyQnbHQEn2rE/ZVvL/wCDH7BHxChtdD16O08Sq0ba1YqTbpyAWbHTHIOK+slKDq2Z8zHm9kmnY+G/D/h5fFU8dvqDTzQpIV5f5Ew2OB2r2b4IfFX/AIU14kvLOTxBqE2khNqW6zs6L9B2xXFfC74USpr/AM18ZLFYy6zr9xs8/nXmnxL1KTwP4yuJods6SSMCw+7gGsauiujvpJNe8e2fFf43L4t8QLHarNJayNgOzetc94es7O11K6eQBWxkE9a2/hR4d0Pxx4dsrq4mWGXZl1VgSK2NZ8A2+jRNcTj/AEdgcE9cVwezcmd8bJHNzXmnsq+WyszferP8KaNF4m8UyElfsunxNNMR0wK4f4oeI9P8JX7fZbkSw/7LfdJq/wCE/ivZ+F/h7qUcciyXGroEd88qp5xXR9XaiEaqbNEa9/a11c3DSHDMREnYLVFLPUdbuRtk2rGfvE421w998QF03T0WHYGztGDkmtTSvGl5qFn5jBV2rjA71SoO2xnKqmeg+F5LPSPMY3L3Ey53jOea5r4hfF66lia3hmWOMnBB6gVykXjP+y7edXO2RwTkmvPNX119a1v92zN7k8GtaWF1uzOpiLbHZ2vjB4UuAv7ySTgMDytcj4l1a+1e6+zySO4j55PSnov9nRbndgW5qumprPIWWNmbua74w5djnlUvuQ29u8kqwyNmRhwfSrMXhGQSedI2QvT3qewtvNlEh/dsOeavPqTzxrCGDYOSQOBWnM0Yy1ItPF2V2szRxt74rc03w5bOyMzM23BJFJpcBuozM+AqnbW1Z2Ufmqn3lPXtgVjOZUYrclGnW15ttrWNZE7n0NdD4b8BxrEIwyRtMdvSotE8OhBst9rM/I213vwu8OkXUyX23KpuJYcJiuGrVaVkzaFO+rOg+HnwLbSUW8uIw8DDKylOFr1zwDpmt+I4fJ0/T1WziOyW47svtXMeCtVk8Q2x060ka4toyCSvR8V6f4Z8U3UJWwhdbNQCCijA/wD115dSUnudV+VWQzxX4tt7Ke30u3BmmtwFkJORHWFJcNpkxzH5tw3IfHArpvC/wya9v7maOOW4uZnwgcfMzV2Wrfs+x/D7wJHqmrXB+1XRJFuOuPSojG7M5VEtDzex0BrWOKeSMzXF1hgerDNU7vwxH4g8Wrpt4rTKmXc4yye1emeEdQs1stQm+z7obODy4sN8yk+prj/BKOv224bmSRzhum4dq0k7bArvcwYvBaafq6/ZRHHHAcKCeTXeQyLb20bKsnmKAuV6IazbLSTLNH5WZLl8lsj7o717l+zh+zLdeOmt5pxJGrHe24cPg8Vk7y0IqSSV2cx8Gfgnd+LNV/tLU4W8lDuQueg9TX1X8KfgwzzeS0a+WEVy69NvpVxPhh5UkGjWisyspjnZB/I16v4O8JyeE9Kh0+BvMkkXDMR90e9dlChrqcNWtoUdL8K6bo6rZ6bD95g0jA/nWd8bNbmggsdNs1Y/amVXjU9Rmuyt7C38PW8txu2xr1z/ABnvWJ4T0OPxN4vbVJNzRx/LED0XrzXo8unKjmjJX5mb/wAJfBMfhbw1Eij942XkJHUnrXcQQ+bGvp1qnap5WxFBX2rUgXAr3cvw+yPHxVZydxs9n56D61YVQq0Yor6KnRjHVHnuTYUUUV1cpJ/CusJBz271IseSOFPqc9KeqqyfNjPoaf5IWAj8q5TZRuyFItjdM+tAiGN2MetTFAHxnoOfemySY9KSKcSE26lt35Cm/Z8LnirD8D5lpu3NMxI4vlOM/N7VKwZxjPy0LheRzSgZGe1Typlc0kHlf7Py4x9aaLfbk9RUhRscZ20bWxxS5BqoyF7VXG7AzQunx5ydvzccVLgkjPO6lZWAHYZpumhe2d7Ipx6X9lbcjspznjjNSBZF+ZJpI2bksrkVeiXcxyMg0MgjLbh8vQAVnKjFvU2jWmtmTaT4017QpVWz1rVIU64S5dV/nXdeGv2xvif4HEIsPGmvL5fIVpi6jHQc152YvNyvTAyBUYgdCwDcfSuepgKU/iivuOinjqsdmz6S8Kf8Fd/jJ4YsvLm1K31GPIGZ4skivSvCH/Bc7xdahU1fw3aXXQO8UhTP4V8TCFY12HPIz0pjsqKMjC9T71x1Mlwst4HVDN68dmfpBoX/AAXU0SG2jkvNAvoH3YYI24GvSPAn/BZ7wD4muFM15caeP7s44BxX5GzQwvJtC7d3IwalSzVYzhV+bqR1rz6vDGFa0ujup8Q1U/eSP3S8Bf8ABRb4deL4Y2/4SzSY2bqJJgn869I8O/tH+E/FQX7LrWkXDZ2qI7hW3frX880atEi7WaNvXJrU0rxVrmhyrJY6ndQshyCkpXmvLrcKP7EvvPUpcQUn8SP6MrDxPa34zDdWzjHzEMDz7VPb64iNtlXy1PTjkj1r+fbw1+1l8SPCN2sll4q1aMxkMoMu4Z+hr1LRP+Crnxe0uLdca3BfBVCbZYVyQPoOteZV4XxC+GzO2nnWHfU/cJfEVu6qIvnIPIxyBUlzdRzAMzbFb1Ffkb8M/wDguR4g8Nzr/bmkQ3aYALRfI3Fe4+Bf+C7Pw51WVY9a0/WbFiMbzHvUH8DXnVMgxcfs3OynmmHe0j76to8yttk3Cp1gDSZ2446jvXzx8KP+Ci/wn+Jkka2fiyzjkmP+rnJibH4ivZ9J+Mmh6paH7HqWn3EbY2bbgHOfWvNqYGrF2lFnbHFQeqZ0ENqsswG38TVqKwaFvujaT1NVrXWo7yLdAYW2cnDggVZt9SW6lCl1JQZOG61zyw7T1NliEySewYRFs7vao41KFeM+1WhDsj3hl56Av1qvca1awsv7xQ44wPWsZUHuio1ojjIFbDL+lTxRKx/vZ6U3TbuG9Tc+N3161rwWsZMeyNvm96XsGae1Q3T9Ea72kL/9etbTPC7SSACNuvJrd8N6C00MbIm1jxjdmu38P+Dpgm4oOOc5puiZyxKWhyuifDrzDu2f/WrrtJ8GLbqv7vnHXFdJp2jSIoO1RWpDprKnTn1ojROSpitTBstBW3X7uO9aEVgu3HNaZ05m7inx24Uc4P0qvZnNKtcpw2ee2BUy26qP734VbOFXtUTbc8UuVIz9o2QyJsH19Krz8nFW2Rie2OnWoJYdx96iS00NKcl1KNym1C2M1k6tErx84+lbV0PJT5iK5fXr3KNtJ+U8e9c9TQ7qN3scL8ZbyTTPBWoTW8gSaKJmXjJ+6e1eJfsQ6hoepaZcfFDQ8zeJtOQ2fiCCUuUvUzmMlcYyoDYI9a2/2vPjfd/DjwtNcabBDf3y5VLdzjzcg15X8Bo9Q1f9nK61vSY7LQdflV7jV7Rp9nngkkDHfpj2r3Mlq+zvM4M0p+091mT8eb/wb8ate1fxNe6HawalqkwAdT8ygA4xn3r1L9nDxLH8NP8AgmT8V/DeoT2twsFvcnT40YMxEwAC9eWzzXxJ42+I2palL9tSzmsbW3BI2H5GI619I+F/g5pPxE/4JJ+M/GVlqU0es2MzaglxC54kiK7UYdCDnoa+iwtebqc0dzxcRQiqaTPi34a3d94Z0YWN07WvkRGTyn4IJrsP2jPhl4V8R/st2d14cRrzxhqEmZLePDMpxkkADNeO6/8AGXUPGvg6STUoRaas9tHmdVC7sDB9ucCvbv8AgjfqMeo/td6e/ia4sZPD8NrJJI92R5asAcDnjNdmIi2k0PDtJHg/wLsNY+FOiz3urszbl/1THGCOte5/GX9vP4V3/wCzBcWbXtlH4wSEJBbxAli3oTivLv2nvFEeo/FPxtDppRdNk1Oc2hC4AjyRxXxXfeC5PEHiqbbGZLrediDuK2wtCM3eZGIxLhH3Ts9f+KX9t2N1dTeWskg+RSfl+grrvh3oup+M/h7I0ixwMuGBJx+VeP3fw0u9U1CE3E32eGFx5gLYwR7V7b4W8f8Ahnwd8PtVm1TUWT7LCI7OJQf3rdK9Sph1ypQOCnim5NyZRt9ItNG1S0gkuBNeXDBVi68+tdN4x0258O2EdmzLaO+C0jHGAa8R0r9oDR7HxHb6hdRyy+Qd0QA6HtS/FH48X3xElS+kmZYV+VIxxge9Cwc29g+v01HRnoPj3xDptvBHb2M/2l41Adm7nvXO2GsQ2dx5mVZsYAzXl8fi95bhfmb5uoFaT66EjDbtsmehNbLCOKscssdzO56LqGt/2xaNDuKtjt2p+ivHpGnYaTe2ckmuK0fxzBYvtlZWaTjNdj4Cht/Ft6Yy6bXICru5Yms5UnFanRTrxkyee8lYqYdxR/vHsBWzodnNJOFh/etjPsRXe6l8NrPwdoKReVbz3Vwob727aPT61n6F4cCxPNbI25flYj+GuSVRHVGJSsra6nmWOJTx/ABmum8MeGLmFJJLwGPfwMmt7wRot1uWzt9NlmuJPmWRoid344r0bwf+yh4o1aSS91K1uI4NwfawIUCuGpWR0Rich4Tsm0R4dqLtZuC3Ue9dn4X8OXPjDxGttEZBb5w8gH3/AGr1r4VfscWetX8s2tX0kdvjagGRg+lfUfgr9i7wf4R+H8flXm/UNvmg9z14NcE+Z7GrqRR85eA/gzqWhsVtV+yfMBnIJxXsuj/BBo9GaWG2ZriQgeYw7nvXq3wX+HOj36s11JHtVjEVZvn4rp/EPiXQvAmuQx/aFk06z52Abi59DXPKjJq7MalfXQz/AAf8Df8AhX3w1OtaoyySQruHQOxx157CvmLx58Rrv4jeM7mZbqSa2gYwxRr92JR3Ir1/4q/FvWvj74ibTdHaSHR4xhkjbBAPXIpLb4HaV4WsFt7FElu5Il81h/ASa1jTsjOnLW8jxCPw+2k6e8ccs0rXjHbFnBOe5rovC2hpLp3lzYg8kDeW4zjrXph/Z3vNc8S2YtoZJFtQPMkUffY+la/iP9mnUJ9bi0u3jM99fMFRU58scZLD8aUqbbujf28diD9lf4Ij4t+L2lmhMNnbN8z4x8tfaWgeALHwnZrpOkoqyMuDIv8AyzFUPgh8Cbf4FeA/s4/fXk2JJmPdsdK7TTNQtfDGjteXHzXc53MuOcnoK6MPh1HSR5uIxDk7xMw6RF4RnSGFWuL27wuM/dOOTXUaJpTaNpytM3mTY+ZjVXw5o322/k1CTd5s3zYP8A9K5/4/fH7w3+z74Pn1jxDfQ2drAC3zsF3Y5/KvQpU/tM46km3yrc3PFWktq9o0IZVXI+X+8a1vC2gLpGnRR7VVlAzgcE1+N/7bX/BenVf+Ett4PhrdRw2YyZbmWHdvcY2lQe3WvnHxR/wXQ/aMvtYWaz8dyW9soDFI7KEA49sV108NLm5uUmpdx5Uz+jiGPDZbH5dauRuBX873wy/4OCf2gPD1vJNceK9P1NQxYx6jpcTK2T0DAZr0Hw3/AMHNfxm03UoZNQ8P+EdSs5M/u1tZIpDyOchumOK9rC1lT0cTz6mHl3P3jVwaWvyr+GH/AAc++DLq3iXxn4D8QabMwOZLArKhxjoGIPr3r6y/Zx/4LCfAf9prUF0/Q/GUOn6owBFnqsLWbnPYM/yN9A2favSp4ylJ8qf3nNKjNbn1FRVHTtftNWgWW1ube5jbkNFIHU/iOKvA7hXZGSexkfwveVsb5ueKWPeXHy/L3HrQzfN8v6VIjZRst2wMVz6o3Ww0MEbnjtj1psiknvTouV2/ex0pwCk8dO9IWpGxwefTv2oHB9akKKfp60bNpz2pmb3I8ZXptP8AKnLLhacVU0w24bpT6B5oXzN3finKck89qje3I6U0oyL3o5RMkaYqKmys6bc4qm8TY61IoYqPl20WEXIYvLVsfrQ4Mq+o9zUSHaMe3epVbZG3pjFIvcjePy3+X5uaFQgEj/8AXTioAUbhnHzYprSlWA/WkMXClg2M9ulNmiEi4bbt6D2qdAxRe3FNMIce38qUtgK/2VQc8YxxUZi2lgB8vY1dltgVRd2Ock+1M8sbmYHKqeOaT2NIorPFuC+lO/1QyozxzzUqOxPTvTpPlccd+RU2K1REZ/lHy8dOlIIAGzxirES59gfWhoUYjc3GOlZuKuEZPqVbmy89Ru8vrzio00yGP+Fd3rWh5KkfKe3NRNAsg+XjFTyj9oUltDCGaJ5N/sxGK1tE8f8AiLQlWO01jVbdV5Cx3TqAfzqqyMGG2lZGG7d8tZyoQlui44ipHWLO98O/tf8AxQ8JlVtPGniGJMYx9rZl/Wuu0j/go78ZNHdmh8Yak/OAHk3cV4lBpTTjPzsc8Vo6d4fkL7h5nHBFc08uw0t4I6YZhiFtI+g7L/grP8brKRfL8QRzKqgBZIt3Ndn4U/4LB/F6weFryPSboswDb4iM88V836T4PWIq0kbKqnO4962f+EVhd9rXQjUjccfyFYSyXCtfAjdZpiF9o+w9M/4LbeOtHHmXXh3S7mKNcMqSlWJ/I113hX/g4F19LmMSeCbeTZ1BuMZ/SvhCw02O03bSZT0AYCkNvIZW/cxozHkqK5ZcOYZ7I6FnFZdT9OPD3/Bx+vhG9H274d3V0pAyIrxMD6cV6Zov/B0j8P7WxVbz4c+KIXK7m8uSN1H8q/H37KzTfMqhceg5oukhlEcfzEdeFHH1rF8M4bzKecTe5+3Xw6/4OaPgv4ouI11bRPEmh7s7mmhVlH5GvRdG/wCDh39nHVLdpG1y9t1QkYksmB/nX4AtGrKyiNp+cAKBWjDZ20gWWa0Y7R/qxjIrGXClB/DJlLOP5on9C/hz/guH+zv4li8xfG1hbLJ9zz18vd9c9K6/wz/wVL+BXjEqLH4i+Gd0hA2y3aR9/c1/NndixhmKLb72YYzgcVktodtcyKY7fawPXbzXJLg1NXVR/caxzqmt4fif1FWX7cPwn1G4aOPx74VkePjC6lFn+dR6/wDt0/C/w1YNdXnizQ44UyWZbtGwB34Nfy9v4Xt4Jw6LIsg+8VYhv51YnS8jZV8y48s/d+c/41zT4Lq/ZqfgaxzzD9Ys/o01f/gsf+zzpMkkbePdPlZOWEYLY+lT+Bf+CuHwG+IeoC3sPHWlrJnpcuIc/wDfVfzgOn2YbtsjNJwc9qo3cDXSsI4zGTwaJcGyentPwLjn+HX2H95/Vha/GPw14tsY5dL1fTb6OYfKYJ0k/kawvEuuwwo38S44I4FfzGeE/jJ4u+GUkc2h+JtY0ySE5VYrttoI9q9m0z/gsD8aotEi0288SfaoI8J5jwjzCOn3q8nE8H4uLummd+G4hwtrao/Rr9tHx9DrPjT7LHdPHJbsAy8ZI9RWtoXwT1/4qfs76z4x0XXrfRrfw9AIpIZn2C+2Lkgnoa8F/ZT8a+EfDWlR+K/jVrEmoXGvWrTaZBEnmZeQfKrseFI46nnNXv8Agp7Z337EXwG0eTWNVuF0/wAXWzXOjWtvOVXDYceaoOGxlea0weTzhaD1KxOaQndpnM6t4o1b4j/DGx0u3jt7afVG8tVZAuCSehrvPB37WPh/9jX9jHx78MfF32i1GtwtJbZAZJ3OMhfQ5HevhD4L/tEa98StImv7i8khh06Em2MJOUZRxwPXFfpD48+C3gX9pT/ghdrfiXVYbNPGFvEGN7KA1ykglUDrzghulelHAzp1VGX9I46mNhOnc+Tfhu/hn46/DRZI5IZTdWTCzjQYIkU4wx9a8C+GX7Q2ufs+ePptEvIWhMl8sIDDJA8zbn9a9v8AiT8C7X/gnV8HNGm0+7fxRZ67oq3sF1bsP9HmdMsDjPQnP4V8h/s4/tHeG9F+JOoan460y416W+l2wuZR/opLZ3YPWvYjh1NSaV0jjliGuVXsz9Zv+Cn/AOwt4Z/Zy8HfDvxR4ZinuI/FljuvWdy/mTbFbcD0GQ3T2r82PjSNP+Fehza1DayQ6izlI8DKrnua/SH9rf4r+Orv9g34d6n4k0u3k8B6eI207VIpDLO2RhBJngZAFfnt+2Jrul+I/wBniOSxi8ya8vBJ54X5YwOMZ96xw8v3qS0RNaT9m7s+bdJ8cXniG9ka6uHb7Q+5vm60/wAcaqk9gtuW3BG4Gc4ri7C5bTxxUt3fyXi5YtX1UaKvdHzkqzasLawLNdrkDHpWvqswjRUX/VgdM1iWBP2leeetT6lN584VTWnLdmSlZWNbT7qO3HmMM49qoarrzXNzwcc02/BhtEUN82M8VmiNs5brVU6aerCUnayL8eqshVt3Nauj+Or3RbuOSCZo3B42nFc7EuH/AJVYhiyN3HtU1KKaCFSS2Por9nb9p2xfx9Z2vjR7iTT5SI1lBz5ZPQnPpX66fsZfsafDTx14ft/FFvrWn6nas6vNBwQF96/A+wjjEqySN93oB2r6G/ZC/ai8RfBq1v5IdWvLfTYkxHbLcFUZvXGa8TGYNbo9bDYyVuVn7+6lefD0+JLfR9D8G6fJawgRm7jtlHI4zurs7j4Y6R4FEV1fw/2hZzLlIVQMMdeBXwx+xj+19b/tIfD1V0u+t9L1XToALi3mkHmTtjqP8969/wBL+J/jy98KWtpeaDeadNbKDDcNlluCTwBXkSp23R2e0b2Z6d4n0Kx8V2lnLpPhyK1hhlJX9z8zke1bfgr4Tajq0yyf2RJB5J3tJNwrj0xXjXjD43/F/wACwae114fiieSQfZ8KV3DIxxjvXs+mfEH4+fEnw9apH4b0XSFlQFpJJyXYY9McVnyxvqNzlbQ27f8AZ/Xw/PcalrN1pej6by4beFkB7V5jd+DtL8eeJro+G7a41CIPsV3AKyP3bPoK7nQP2JNd+KbLcfEbxFe3jRsSlmkxWFSTkDjsPevbfh78CdD8B2cNnBJEkdvjYqAKT9TQ6aeiI9py6s8R+G/7J3/CDPeag7Msl025kj/5aEDoB6CvRfh5+z1/akxu9Yij3byYokGBt7Zr1O8uNBtFe4udQtYYdPJbaJRgcc5rm9G+NEPxR1WTTfDihrOFilxeqfljx1xT9hBbk/WJvZDNXTSfAsTQWNms10VwFij3EE9MntWJ8B/hddeC7/UPEOtyRzaleEvgfN5KEkhQT7Vvax4l/sqaPTdDjW+uo22TSEdCO7Gi1e+uJlbUGDyc+XDH0J9ahx1KveJvXOsLdyLMzM5Y5WLPT3NJoXhCXV9QN1fZCZ+WEn9TWl4e8JhCtxcYMjYIx29q3wPLPy89hxXRTw7kryOWVbl0iJiPS7cszLGijqTivwf/AODgn9ryf4rfHz/hEvD2rXT6HoEbW17HE+2KSfIJBPciv3L8SabGLV7vUJlFrbqZHDnCqAD1Nfy5ft3+Mp/Ef7UvxCmsomax/wCEhu/shz8pi34TB78Ywa9bC0byUWtEYwkknK+p49qGoSaYPvJJtUqSSTjNY9vqjKHDSb2boB6elWPsEzHa8y4b5nDHPNV3tFW4yhzjqMV7Uaa6nNKoy5a3jQhVUfu2Gcc4FTW96zTMPMLKBxjt9KrQTGOPOdvPekubhmTgflWns0Ze0Nm28WSRyRpKyzLGeATzj0pH1dPMEvnSxPu42OysDnrwaxJisxCgsOME+9MEwslXLM5B4BrN0ItDVVo9o+EH7X3xM/Z+8RW+reEfHnibR5rVlIgh1GXyJQDna6ElWU9wRX6KfB7/AIOgvHGheE47fxR8O9N8Q6hHgfa7TUvsYYY53KUYE+4xX5JWt7IY2VV3BueT93Nallepa2yxyP8Ad6c1Ps5L4R+0Utz5sV+fqO4p6SAEiomdmxx+VO5IG013MxLCkM/owoO3bjPPpUfzBVx/EelC/e6D35rMfKTKFyfTFHl/SovPU8ZxS+eEOD39aqJEkSpHhmPX+lKkTOAw+lEUwXt1qdHDEYHFUKJAQVJ9PpSHAqxKwJ+VVqGVdzcipHEiZTQDQnyk1YtgCv41QokZiyR3DCm7JCw29quFAw47UscO3+LtQWU2fY3O4DPGKeRvPtTxDgleq5oWHcPlU1FgGkkAY/KhAcep7Gnsm3n8qbG+9/7tIAVXBbcPl7D0pYpArFec+9Pl5gwWbk0KPly3b86llJjAmTnpSlNilh2FPEYx7Uxo9sbGpKuRsxk6enak8pifenxQlXJqSC3MrfNSt0J5tdSNVaIdOKBJv49a27WwjezCtyGOM1LD4XVpMKpPHU0co3Ix1ti2zZ827rjtV6LQfOA37gwP51eh0k28nlj5WPStLTbXzrjy2VmYelLkDmKunaOwgwUb5TxxWgmiTHYYxtJ7etWb/dawKY3ZcHBGOlJBqpYqOflH3qpRQ9SRluZYvLbaNvYmpI7qBYfLkVWZeDj1qvBrHkTNuxIp9uadcXEdyBt3bmOcAVS7Bdk0dwsR+X5V7ECrFin2t2ctgHr71n3OpMIvL2hVXtjOaht9aYz+WqmjlFzWNeWRTlY+Nv8AeqK4UwbWZlUt1AFU5NaVZfm4x1zRc6qqhXVQ+f0o5R3uaUCiKLzFZdxGPpVaG5mTLZXcWJ470zTdUjkkUPtx7nGK2FubVFG7yY2z8uT96s3B9C1JWMv7WsMuCqrI3JqxHMX/AIvm5xtFdF8P4/D934s+0600cdnaKZGUtjzT2FZOoX1tfardT2e2O3ZyyrngA9qFFjlYpx2ildwkJkY/NRfxeWfvfN2HtVuyj/tC3Z4/LQL79ayNeZrVvmmWT0A7VWpGg24uZJojHhV7Y71AI5ItoGTgdQOagGtqh+ZR8o9KmHiSMR5VVX3qdQ9ShcWLM5DsWZjmt/4V/C6/+K/xG0PwzY201xeaveR20UUK5dyzAVUOsx3Em3ZubHBr7/8A+DfL9kPTf2g/2hNe8Ta7qT6LZeC7Vbm0utyoRc7uGV24wozkVyYqo1GyNqMVzXZ9PfHT9ivxxqnw98K/CfXtK8J6Vot8trZm8gk23wTbxIoPV92MgH3xxXxR/wAHBfwr1b9mT4ieE/CvibxZdeNLSDRCujNeyZmsY12qIyFAGBxzjJxX3b8MLOX/AIKn/wDBSLxdp9h8QpLzwd8I5UNjq8EaLJdX6sFbymChdq4PTPQ1+Tv/AAXL1u3t/wBvfxHon/CV3njCLw6wtWvLiUzYkyS6AnoAew715WFot1lHsdtaouRvqcx/wSr8Oap8RP2ofCvg6OK+WLxRfRWoIj+VFLDc2COQBk19t/8ABZ/4J/Eb9iT47y+BPBFvrureDvHmnJPDbWsckw3IMSqQq4zkZ4HQ1g/8E3NPt/CPgXwh8cvDEFzrB8ATr9vsLWz8y4ijAUTEEADhSTzXtn7Vf/BZ+6/aZ/bd8G6j8K4Zk0Hw7beTdyXtoN1zu/1g2t6bscd6zxlSmqjlbVFUYzcUk9D5r0DWF+E37HGr33iqNp9STT2s7ey1P5TbuyEFVVuQRzXwb8APh3pvxA+MGl6bqUwitNUnMZ2yBdmTxz7V9u/8Ft/hjJpnhHS/HFxrH+keKtRbOlHhoflz5hAwMGvzm069urC6huLaSSGaEhlZSRtPYg13ZdTc6TkupOMqKM4wfQ/c74O/tHaf4F/4JR/E74b/ABT0HWta0bwnB9k0i9jtWkUmUsIW3YwAjAHPYV+f3i7wOfE/7JC3NrMskKQmdVBywAYjmv1L/wCDd/4yaJ+29+xb40+FvjSxjuNWhtWieS6UMLiJ0KK4Pt+fFfOPj3/gl74i/Z5+CnjOwttU0a+uLfVZrSHTWuF8yeIthSo4/IV5NT91U13udCmpwsj8hng27uD170jqVC16N+0L8FPEvwP+JN1o/ijQbzQbw4kjinj2rIh5BXsR9K4b7Jw2ecc4r6qlJSimeDUjyuxQV/Jbdmnacv2u/DHOBRNb7l4qXToPsw3e3WtEZ9STUZ98rDHAqkz8cVHcz75W5NNV8Dua2jGyGyQBg3WrFtG0rZyenWq5nwvrxVqwuuFWhi2HWLG3uyrHO7ge1dAL9bPTltEb5mbcWrNeJWCsuBTo1+1Xe0nJTrk1zVKaZpGbietfs4fG7U/gz8TtP1S3laRrchjGz7UOOma/QyH/AIOG9Q8eafp+g69o1vBBbOqRNA5ABHAYn261+XfhjybzWY0kG5m+Xk4xVXXIW0nxZPCIzhW+TngD1rhrYOE2dlOu0fshrv8AwW8tI9LhbUPL1hLMbYWSQ5h9CfUiofDH/BxL4ltJLWGbT0bR7fdtkUkTsM8deK/JrwlcSXl3HbTbpIWbJ29Pxrdi1G7u5Lizgg2wJlAxPb2ryqmWxO2OI0P1q1//AIL13HxAmjtdPs7pbf5QbmSb5gx64ArUX/gqRrmuXtvpza41pYhhH5yt0yeST9M1+V/hu6bwjoiKWijY88kck0tz8XLvTtbSRmAhblhv4z61x/2fNP3TeniI9Uf0UfCb4U6X4q8BWHiK18RT+KlvEE03kz+b6EqQP617D4Z8I6xqFrG2mWP9i6e2CYlGxpBjFfhz/wAE9f8Agqz4k/Z28Sw20F411oszbfsjgHzc4BwT06V+737Jv7WHh39qPwDa6lpksMd80KvcWbN+8hP09KmNFqahLRmdao1G62NzwN8M5tFEs1wvzyfMERup9zXSaD4NGnXb3E0nmzyev/LMegrbWRIBnIGBnk9K+Iv+Ck3/AAXS+Fn7BEbaJa3EfjLx1MpMek2EwMdr2DTyDIT6DmvSpYFJe+efLESk/dPs3xR4p03wToN1qGqXlrp9haxmWa4nkEccSAZJJJxxX56ftF/8HFHwz8C6tc6R8PoW8ZahC/l/a23RWSnOCc43MB6jjjrX44/tm/8ABY74wftq+N5v7Z1q4h0Od/LGhWZ8mygiJ6Y6ufVmJrw/xv4kh8IrD9jgAkVA20SDaxP+FdXsG3ZaBG0VrqfoP+1R/wAF6viH8ZdP1Pw/e6hBptlJvikg0hPLWRSOAXOW6Hkd6/PbUfFuo3/iF57qTdDIeNxJ2jsK5e/vptcb7YIZFDMdzI3ylhUzXkmsM7N8vQMfTFdmGoqGpnUrXN+x1ZtUikMm2PDEAgdR2pujag2oG6iwQsbYB9Kt6etjb6QCz7pGAxjrVDTLn7DcyKvzI3fFd8Vqc9yy0J82Mf6wZyRVhV2n5FXpjFV4r7dIQy/N2PpVu3njjbaGVm7+1acoMQ2i54GG/lWdPpxectyy5z+Na0gMudvQc5qBLpYyx+9RYnXqU1sWjGfMZX9MVVmM0krfvcfWrk+qBkZmHzZxms+7v4i4+5nvzTUQ6njKP+73FfmYcUJIcV3Xxo+D958FPH+p+G9Yga11bSbh7a6t3+9C6nBH/wBeuLMPPy5I61MZKWqCSs7MjS4LN1wVGc+tEbZB5689etSSW22DIUVGbXJ3L+VILjejcevenBsnntTktWbHAFAtG/u000DCK4+fGOKlL7hn8KrBGV/pUqtvqjMlEnydak3qExu5qvI+zpxUMk/FMS0LeVUUqtxVH7Tj+KpUnBFIfmaEc+wfLUiXXPIFZ3neYOKIpGB60ApdzWDqfvfhTvNC5xVCCZl+9zT2lJ59+lTZF300LTRhj2+YU1IeTVdZdrZ71YF1kdflpWEgRS5ORt5qwqR7ePvVXSXc3Bz7mnIAD796Vg5ibZG680x4vk+XmlUeWmetWtPtBcRbs5x2otfcor2+nNcDhTuqWz02ZbjHl9OxrY06NY7hGzt28/WrM92o1MyZG30x1qrWJKd7pDR6S0kX31GQPQ1b8LtctpokmX7rdSKsnUFiPK7Vb0HBqx/acdnbqG27WOcdqFYVypBeG4uZJJ413KflI9KnsPEEcU7lUG5u+OlSNcwRTfMqkOOMDirGk2djFd7pNoXrz60WANQ1WOe0CNH82M9KqzFZLdPKUbv4uKtMkN5e+YWJVTjGOMU6UQ2sxaOP5W68UuVj5ims8M3zLHh8Y4oheNHDBTvzyB3rSsLS1S28xV/eZxg96hh0+OKdmZvn3ZpBzDUhhji3SZ3seh7VDBFbiVgc/Mc5x0q9qNnHc3SlixXAxgYqS40q3kVdvzcUFc11cy9QjtdvC52nvUwsLefaOF47UTaIsSbWbC55NSHTREMiQ7QODmq6k3K39jRTby2FVeho/s+Kdc7uE4B9KSzRkaZWkYZ6DPWr+h6Q7hsycNk4I60Pcu5nXeiR31uFaTPoc8VVXRJLNzHCzNGw65rZl8OTJO8m7g8Bc8U5bGZI+CuV/SpE5Gdb6Y1hEFV2Xd1BNOj0aO8fPzFu+TUl3DcMy7irc84qeFZvLwvbnJ4qZFR01KEnh9cEFtrZxiq9x4fMK/vJEZOnTFXpTI8i7mwynr61Hckbv3j9jgY61mzTR6k3gL4c6h418R2em6cqyXWoTpbQ5baC7sFUc+pIr9xv2q/Hfw3/AOCSf/BJ3wp4Q8U/DfUta17VdJNv5kNsEgkv5FO6SW4VuzNwDnIAFfnz/wAEE/2QJ/2vv2wFa+QQaT4UH28zS2xmheVeUXHClgSGHcYBxXtf/Bff9tnxp8XP2k7D9mCW38P+J9I0uaykkurQNHP9rk2hBJyRlQwJUdc15spOVRrsdEdFY9x/4I3/ALIes6L+wJd/FDS/Gtp8LNG8cWst7qtwkG94oULBmDMcKCASCOfTFfkB4F/ZQtf2vP2vPGfh3Q/GdvqGj2E9zcrrlyh3aiiMcOAectjqfWv3H/4KXfs7y/s3/wDBF680HxF8RR4V0XTtBjs4tL021W3W9lKhlgBXBOSCCO4zmvwX/wCCfGnX2r/Hzw/pekrcC41bUIbR3hcqwjZwCpI7HNZULwjOotGVL3mk9UfvZ/wbr/C7wn8Pf2PvF3gq9k0+bxHHqF0mp2bsru0IARXP+ywz7V5D4K/YZ+C/jvQBqfw0ZdM+Klj4quEkhlUpDdwi4OYlA+UrswMjvWt/wXp/Z18VfshfADwv8VvhDqF14VuNNtItH8QR6bi3FxCekj7cbiGJBz61V/4N24bq+/Zw8RfFLxq8bWunzXF/HqNyrMyoi5bGfugEZ4615GLp1KiT87HdRlGOx+X3/BYH4xeJPjF+1rqOleINHm8PyeFUSw/s5mHlwsByygdmGCDXy9eeHWtrTeiLtHOK+gP2x/jQP2ov2mfHXjtvMlj8QaxJNau/UQA7UA9sDP415i2mqkbI679x446V9NgafJRUTysRUcqjbPtv9gbxvrmgeG9Nn+B91qVj8SJtNeA2UbDy7rAy2c9Opx714J41/ap+KV18cpLfxpca5beJBqKPcx3gZZFm3jqp4/IYrqP+CNvxaufhH/wUH8A6hMkkmm/2kllchThESY7M59ia/Wz/AILa/wDBK+z+Ofxi+HPxL8Px21vfWuq2lrq0UcAzdQeZuMhwRnauSeDxXiVqMYVp32O+nUbgkfNf/Byda6Nrv7KX7P2q3MNnH4yvYlW4dUCzyQrBg577dwFfjvc2flFwMNuGMDtX3p/wXR/aKb47fteSafHaT2vh3wbaRaNpKurLHKEUb5VHTJORx2r4dubNfPzuHA+7jrXq5ff2aOHEayOYa0YSqvYU/WX8iJY1+UkZNbUVpGJ5GboozXP6nL9puHbHGelelFXZy7Iy3j3k02Nf/wBVTTjc1NWPcfpWwtRQuDVm0Xa2V61CVw3SrFsuOefwoF1LVxGxI2n8Kt6LDtdpJOWNVIZ9/rVuGQkfKPrWbC+ps6HdRWmpK7Y3scDI6VneIPEEz+IZGmO7bwDUnkMGWTrt5qh4hjVnWQHLMOalQV7lxlob3h3xqtvA0YOD1zjnNT698QJZolgt5WXbzuXgk1x1jEySL/nNa0VqrKS3X0qZUY3NI1H0LEvia+1SWPzbiaQJ2JrsFvI9b0OHcMyQjbtHf61xNhEsd2u4dq7r4V6L/aPiCONyvklgzZPQCsatNW0NYzZ1llINBj8P2/nLH9nYSSMo+bk5xX1Z+zj/AMFOdY/Y/wDG2l69obLeLYELPaSFkF4rdV4P9K+Mb/Vf7Q8W3hhb5Y3IU5+6BVXV7xr8rJJyVb1zjFcdTCxm7s29s0j9HP21v+Djj4xftFeBrjQfDOkwfDfR7pNtxc2U5lvriMjBXzP+WYOf4efevzO8Xa7Pqksl/NcSzXDsS0krb5JCe5J5Ofeuk8Qh20SN0czb0AOT92vPNf3ID8zMg4IJ6V1UaaRzTnbYtN4vX+z/AN38l4xIdwvVao2XihlkzcM0xHChuwrFvJ8n5d3FQxXIDfN2rpVJbmPOeg+GPE+0ND5m2NkbKdua3dJlWCzkjRflk5yRzXBeF7Rp5Nwb72MV3tnCLWBV+8SM5pqmkLmui5Fxj5lzmpjJhCFXvniqaxNLImO5wa0reIoDwCR+dXEF5kMTMw3dPQUKWjudwZunNSmDy8HPy9cVFNAGTePWqTuN+RpQXQe26+31qlez/vxj5eaSOTybfK9T29KrBd1wWYNjuCelXENWRSxl7dt5wuSc1yuq3my9dVk710XiPUl06wds9unrXneo6m0025eM5PWncXKffv8AwU+8At8e5/iN8VL7wffaLq2hXUdpNcWoZ7G9ZW2GRmxt3bNpPPWvz0s5/N6/Kc+nSv1F/YA/a4+IHjH9lrxzZx2q/Efwja2Zg17wtPbL9paFl2/aUb+IqAT0JyK+EP2pPgqfhp4otdX0/Q9R0Twv4kQ3GmRXbb3RR1UnA5Hoea8PA1uT91I6q0Ob3jzN0wvPSgQKF553U9Cuz1Y+9B9APc16pyieSqDoPShuB04olGR+OeKQnAHfjvQTcglVWOf09KZsVTmrDpv5NRPBuHU1USWyCVtxwagkiyKsvDz1pANoxtqgt3KZiG6pMAdM1I8WR06e1G0AUBvoAJQD0pY5MMcc09U3ChI+f6UFaDfOcGnea1OKDNPjhyRQNDRzy3elMzKQPWpvsgJ6VYttL83rQKTKsLkMK2rK2je35HzYyTVcaQB90Vo2OkyqAdp20MI6CR6P5kO71HFCQtp8Z2tuXPT0rqvDqQrOsdz8sXcgdq1NU8N6VfL/AKIztuHU+tZl8vVHHWF2xiLMgYjtVTzzJctn7wzgV2lv8HNUMDTxiMxqMk7wK5N9IaHUpfM+VlOOKYuWxXtNfaX93IpUBsZNa1xPbz2G7cBtHHPes6/01vKYrH+Ipmn6bLJbc9SehqrBYsf2ozxqrfw9D6VDHrrSKyuPunAOaVrCSJiGB57VBFZq7mJl6GpTJ5WX7bxAvkfL/D2q++s5hjKt8x6j0qnpOjR3EUq/KGXkD1qvcaTMZf7oHamwatqblvesItzNuX09KtRSrcFuxYcHNcnDJNDIYxnNaNndyFFVudpzQyl5mveXkthHjdlR3qnp/iGSGQq33Sc5qZoZtVX5duM8imw+HYwWLMw7H2pILFfWNdhlbYrN1yeai/ttZhhXLY4xnpVpPB0bsz7ixPaqk3hVrVmYKwFPQTQRX0zvuYfKOjVftfFslofn2sqisqO0Y/uwS1NFmwGyQbmJ/OnYdzooPGUF8q5DYwc81e0ZoZkVpJflPq3WuWFn5gVQhVumB3qV/Dd0rAfMiD3qGi1ZnRa09tYgeRN5u73+7WfHqJmfYzfL6jvWfb+F2MjFpWO7oN1aGnWCWgwc7V4yamTEtwjut+5TGdvZjVrTvC1x4kube1t42aWRtqIg+Ziasz2rOI/KHDY64r6H/wCCW3wSsvij+1XpNx4g0/VtU8O6HIl1exWVuZGIDjGc8fQdTXNUnaNzeC1P1C/4J8+N/gt/wT//AOCd+n3Xj/xAvhfxXqNnNqF7aIjpdSuM7Qp24YlVHOa/Kn/gnx8K9c/be/bo8VeKfCNvqmueJk1d9X04TKZIYI/O+SSZ/ULjA4zgV99f8HDH7fem6R8PrH4M+CvBMAt9WsT/AGjqGq6Y8MkETjaggkI75bJHFcn/AMG2Pw6l+EPxF1NvDNxHqnjHXrM/bomiJ0ywtw24Eup+/uA+UHpzXnaKL8zVK+p67/wcL/sh638QP2ZvCWv618UY9Q8W+H3hgi8KSCNLe+lkGHaKEHe0gGcE7uA3rX5jfBjXtA/Ymji8Q61odxH4h03UopJbDJheJoXD8ggH149quf8ABbf41fELwB/wVx8WTa14kh17VdBuoGtBZRlbe3jCDEYTJ2kDIJySa/T3/goj+yX4B/a5/wCCNUHxStPC8en+LLPRLfV1nskxNJKEHmb8csG+Y8880VKbhFJ7GlOVyfxL/wAFh/hH/wAFMPhxoPgSzhvftWuXEMV7pNxbEmcgj5FPfJ4zXA/8FmfCnxC/4J0/sfL4f8EatZ6f8M/iBKmm3FjHAI7rTWdd5RW7q+1lPTrX59/8ELvgJ4i+L/8AwUG+Gq2dveR6fouprfXzIhxDDENxJPu2Pzr7W/4OgP2l28c/H7w78LrO6hm0vwdZDUb9EOSbybIRCM4yseD6jdU4XDRdVy3QqlZxioo/KOz0pbTT44l3eXGMdOaoXU32OeRlPynOM107R7LRWC4KgD3Ncp4tgkkhZo0+72FexGy0OJ6nq/7Mtl4rn0XUrzwDpH9ra/p+L+W3jTzJFWH5wwA54I6DrXvX7Rf/AAcI/Gj4zw+GrLVdDfwbeeHVRSYmkX7Q6YBdldR1xgjpXzJ+w9+0Vq37K3xj03xpptywuNHu45riEn5LiHcN6H6rmv3x/wCCiH/BOLw3/wAFe/2RvBGveAINA8P61qH2bUbXVngVAsD4MiOVGTxkc9wK8StBe1lzLQ7qcvdSPDf2+f2Mvh/8T/8AgiXN8ZtWsbW58fRaPBrkWtQKBLLcPKoMZ/2Tu249q/CVBJfwLK3yttG4Yr+hL/gqD4S1T4Gf8En9J/Zq+HVtqnxC8T21pbJqk+n2pufsVpHKHkchf4i2Aq8nqcV+A+s6ZJpeoTW5ikhaN2R0dCrIQcEMD0OeoPeuvAW5Tnqao5+YMsLc8MMdKx7mJUJHv6V017ZhI9pPTtWDqKHzG+XgV60Dl5epkzRKo/Wo1XgGprj5Oy1CpyK0C1iSECR/ar1vZrng9qo2x+bgVtadF5kfPepuBHb2gkfCr8x6Vrnw7NbQK5XqOc0tnpTJLG0YLbTXS6iGl09RtK9yPWi4I5z7Pthasm8slZx0PNb9zHuhO3+HrWQ67Z/m9aOokQpCsY4qaJAWyKsWlrv425zVj+zPLP60bl7DdO0afVrtUiVmkY4AFdvd6K/gXTIvmxd3C/MB1UVleD7xdDvluvlYxrwp4yaL/XLrXbySW453sSBn7o9Kzkrji7FfSxJDqTbSB5n3veto2cMQDD5tvJU1XsreOMLjG7rzUmorNdwtHGv3h2qZRKUnYveI/FlrJ4fW1it44ePvg8g15b4gvRHMyK+5fX1rqvEmjrpnh/zGf970256Vwl3LvlG/65qqcUZSdypNMwHt0qGSQKvHXvVqcq52jbt61VEHnzBF+8x7VsZnb/D+L7daxfxeX0PrXZyWrbky3PT61zfgSBtOsUBXaxrpknM0yoy/d71MjSOhc06HkfLhgavNtt9xH3mqvZyiP5evGMVYR/M+VRUldSNisihmbDdhTZ5NkK+ufSnRwky7e/UHFW7Ww+2kq3AXk1SYFZVWW0Z1bkHj3rLu7vyZWLNj0xWvcNFCdqMrKvauQ8YawbVGx1JwK0iJ26GH4z1/7XMylsqPSuRuJmLZX7p6cVPqczXJY578mtPwtoC6lYtI6SfewD60SDU+xPgv4F+IX7OSaZY+ArjWvDXxUjWVdZtnXbHMFbiIxuORszncK9u/bKuda/ai/Zv8Ox+NPh62g3VxEskXiKwmU2K3QBCho1OY9+OQQOSK9C/4LJfsA+NvjB+094a+Mnwh1L7Z4H+JUsR1O/hkxHpEgYBpWx/Cw5yD2rH+Kv7TviD4C+Pbz4B6Dotj4u8Aa3JYxSaj9iUXGpXKlXfyXIw2XGMZHWvj/bNNSvq9T0eXQ/KvVfDVx4X1mexvo3huLVtjow2kH+fI5qq4bdwO+K+1P+CumgQfFb4lr4w8LeBdW8OSaVa2+na7ataiMxSJGAsjBf4iFyW6c18Z2Fv5kfXhjkV9Fha3tIXOGtBxl5FNQSG3dulOS3BHGcCrzaWSc+9TW2n7gcjgV1GZmx2zNJ93iprnT2K/KK1ItPzJtrQtrBSqqRUiaOPFswfa6lakksf7ortP+Eft5lzjmoz4aUjgfpVcxEonBy2kkf8ADULRsq8rXoB8IKFPcnmo28Di4T/V/L2NHMCODjVieM1Yi4PIrrG+H7R52kVVuPCEydF3Y7ijmRWphxQecOB1q1FpZQruFalrobQTKxXAHqKvPpTSfdo5gZm2ujCV/wCdadrom0jaOO9WbK08k4x83uKtJKwHK4HrSuwUSv8A2WkZ+6DzV6GKOK2O0Y/pUJlLGrBZY4fbuKWpXLrqVZUkP3Mt24HStDTp2hs2Rz97GPajT2VyVz8zDIFR3CbmZec+tBWqNSy1e4Cf8fEnlt8pXdwaw9S0U/ammVvlY1YUOi7RkgdMVYN8Hh2eoxz6072DV7lP7NmLbwVYc0qafHHEXVvujpT4PkPl7st1IParRVBa4/iY009RWM2e0Z03qMtjiiDSxJ98KHbrxWjbwAvt9D19aW5H2WRtw9wQKLaAUTpn2Ihk6d/erEdojIC2C3uKZd36yl+fu9vepbW1aZsnkNjkdqkRS1HSlDM67d3oBVIRMsqhfXmuiaBWgKsVBPT3qubBUjUqvQfMB3oGMsbhbMc/Mexq/ClvebWPB7896pLHGIuw3dB6VbsFVY/k2/KehoHbsWLyOPT4lMeTng1HJbtKvy42sOSR0qSeb5du0qw5OR1p8Vrczx/KjbSeTjiqYrGNcWNvbEtIxDKeoHWprHTYZo8t97qARWrJoP22Tb8p6MMc4qf+zFjmVvlG4YGeMUcwWOdkspftmchVB+U9zWoIPPt90m7pjNaH2KKRVZvvKcD61ZislJXzPuqMnHSs3IrlOetNFBkO1m65zVq3tdshbllXgqR1rWmt/IZcbdvTgc4qSKFBLH5PzdyCOv1rGUu5pGI+LSPMtRJIhgUgAPjGK/XX/gjJoOpfsIfBDXvEGufC/wAYa5feMIkv7PVLS3jlhMEUbMqNzmPJJOSMHivi/wD4Jifsi3H7b/7SNv4fv7Oafw7oNv8A2nqkUS/NcIhG2EHsXIxz7191f8Fa/wDgq38QP2RPhw3wz0v4Nap4B0zXtIfTNM1q7uo3WNdnl4iWPPzBcdcHnpXPJ3ehdrOx+Xf/AAUk/bV8a/t6/tIajr1xayWa2zNZaXpyJuZLdHzscAHLbx3757V+y3wt/aY0H9iz/gj54f8AF3w/8Jx3GvaL4bjm1SOO3+ztaTbR5jzMwz94nj3FfmX/AMG/X7Lcf7WH7Q/ibVF1SG31TwLbf2nFYThXl1KZidpZWyGUNgEdBX2J/wAFqP23vC/7Mv8AwT41j4ReFdPb/hYPxEXyNfhljRJbAMQ07sFGMnbhVHGD7VjK6molbo/LX4O/Di9/4KEfE7xt8RvEGpr/AG5M76hqFzPKT5pbJxycqBwABjpX6PfsWf8ABbj4U6r+xDefBrxFDeaX4k0m0Ok2iSwl7XUcZUEPyMcd/WvJv+DW39nXSfiz8V/Fh120t7/TLHTyht5WDF9zAfOPTB+n0r5e/wCCzP7J8n7Hn/BSnxZ4d8H6f5eh3zxarplvB+9aBJv4FXrw+cAZPSqrWlemzana5+4H/BNj4c+CfGfwhtfiN8FtF0bR/El1aTaZc3GoiQxq6jkhVxn58ckdBX4g/t26R4vsv2zPiRD48vodX8XQ67OuoXdud0E3TZs9FCFQB2xiv2E/4JWeDNf/AOCYf/BK3xJ8RvipdSQ6hdWs2vx6ZPIVNqDGPIt9pHyyOQuR6t7V+I/xL+LGq/Gn4j+IPGetL5epeKtRn1OaPJKRNI5O0E84A4/CjB03TjY560ryucvrqNFG21VXaAOMVzfiFd9m2PTOPSunuSsh+Zh7+9c7quntKJF3f6w4B9q7DNWsT/sv6PY+MfiM2nSeQyyNvCTj5HI5xX1h8ZP+Cxv7RH7O+gSfCldSs9E8I2sCRWQt7RFuIosAgJLgZwfrXxX4Duv+EK8WfajIyyI+YyvCgj1NfvXqX/BPPwX/AMFfP+CRPhDULGxsdO8eaTp2dL1eGMLKtzGcPG7AfMj4IIOcEg9q8nFQXtrPZnXTdo3N3/g2/wD2v7z9pfwR4m0XUbUzXXhuGOS4v5o8y3bTsT8zZPQL0zX4+/8ABU3wFpPgP/go98aNM0MD+yLfxPdPHGOkbufMkUewdmA+lfrh/wAEO/hLcf8ABMT9jD4pal8TrGHwz4k02aa5uXuZFWO9ihVvJETEgsDkD6tX4j/F74gXXxj+JviTxReTNPd+JNUudSlkc/MWmlaTHrxux+FdeBpxjDlRlW0mecalb/Ix27cg4965rVYGi3cdq7DW7Ur8rHvgE9q5nUbRiGUrXoxOY5149wPtVU48ytS4gZCfSs2ZQj/L3NaRFKNySzty0o/u55rpNJs1Ubj7Vg6e5DYHriul0iFivvQ2SbGlL5DKV53GtuSPdbEHGGH5Vl2FmURCpPHJzWhczFRlsjjgVIzEmCxTMqn5c1VvdNjcBlX8fWlvw7TyberdDVmwBFsqtyR170wUehUgt5EIMa/dqS5uvMTGPm6VrWUqwQspVdz85NVbyzzIG29emOlIfKULe5kjHzVq2cqSwqr4XPcdarxWwl7ZXOOO1OKGGTrnmmTqaCja67TuUcAntVkXE8alkf5fXFZjXTSDYOMdSabc301gyozfeGcnvSHqZfjC/kuHbcMLngCuNvlWSQ5OBjmus1xxKXdj/Dx7GuRuJPNkZW5wevrWiIW5Tkygq5oESzahE2B8vrVe4h8wbQfoK0vDNgWuI2OO+M0D6nd+H/8AUjd/wEV0dqitDu+705rK0OBfs655K8ZPatuBQYyp6dMVO5aSJogixlu+OtTWSiORj2I4psSAx7fbPFSIRgN0yMAVIIfI2W3Y24GOaZ9skjjZl4HQmoZJS7Nu/h5+tRNLuZRn5W7etBRXvJfIVpM8VwHivVmu523NlV4HFdV4q1tbCz2njJwAO9ebavqRll4/ibpWhL3IjO0rGJf4zxXd+F9Kkh0pFVto64Fcz4L09b6fcW3c8A16HZiOzgWNgPl9BQ/MZ+wn/Bs/8cPEXxL+G/xK+HPiK8/trwz4bLiwivMyyRK+VK7ifu98Y4JrN8NeIp4/2u9e+Hey3fw74X8VW+p6ZviDXFpKCy4WQ8hMdV70UV8bitKjserS3P0b/aQ+H2gr8RPDMk2jabdHWLOazvhNAGW6jMefnHcjPB7V/MR+1r4UsfAH7UXj3R9LhFtp+na7dw28Q6RoJWwo9h0oor1st3OXE/AcXHEr9ulNlXy5WA7UUV7Rwk8aY2/SrqRhbfP+1iiiktwLVsg+arGn/vZcN0oopAW1UCPOOmaW3nZBt4we1FFA47kTyecoZgM57U4nyztCrtPtRRUsRPb6ZDdx/Og5Pam3GmwwI21B9zNFFK43uZ0US7M7RTLaMP19RRRViiN1KNY7lVUYFWpLdFss7ecUUUFSE0iFSrNjmpo1EhUkDk4oooKH3C7HTb8u4c4qMQKsRbHzZoooArTybRv43VLYztM4VvmGaKKALFjdMl+oGOTil1SZmviv8PpRRQBmWUKzakyt93rWp5ht2Cp8o6cUUUE9AnfzIVzjgZpu7bsx64oooCIXVsu0cY2kYxVm1gWOE4XsD+tFFBRp2MK3DKz/ADHHetK0nYRbN3yjtRRQIfCoguF2jbvHNMvLdZRuZcsF4oooEippI+0jD/Nt6e1WNv72Tvt7UUVnIoW/QZT2q9poBkV8AN04H0oornqG0D9s/wDg3H8F6boXwM8ZeJILWP8Ati8vvs8lwwG4xohKpnrjJzX50f8ABWX9qXxp+0r+1h4wtvFeqfa9P8ISTW2k2Ma7La1UDBITJyxxyTyaKKzjsVL+Iesf8Gy3w70+y/bIt9bjNwt7caFdRSfP8jr5gHIx2ryD/g5h8X3y/wDBRzxNH5x8pLCwhWPnaq7AeB68n86KKy+2vUqPxM/Qz/g26+Anh34ZfC5PEOl28y6p4ksg97LI4bccqeOMj8zX1HN+yz4J8W/8FPbvxrqmjw6jr1j4fia2kuVWRLdg+AyqRwfeiiuaP8SPqV1fofDf/B158Y/EOl2fwx+H9nqEln4a1y4kvb6CH5WuHjwEDH+6NxOMda/IfU/k1ryfvRwjYoPoBRRXpdTjj8KKM0m5ZAQvBpojW4jkLD/VjiiirYHL6hpsOs+LNPtZl/czSor7eCcmv6Zv+CHlrH4e/ZTtdCtV8uwtWaSMfxBmQE+36UUV5mL/AI0Doj8DKHwo0mx/bj+K3xd8L/E2xtfEug+GtXSw0+zmTEcEbLz9W96/Dr/go78HNA+Af7bHj7wn4Zs/sOhaPqLQ2luW3eSmAQoPoM0UUZU3yv1ZWI3XofPHiGNftbLj5Q3SsHVbVDLtxx0oor2onP0MTVrGNW4XtXN6jCqdB1NFFXHciWxNokSu/NdnpsawwLhQd2M5oopT3CJ0NqAYM7V6VHeyb1AIHeiisxlG4tkMDtt+bdjNMRFjkYACiitAEt33TLnmp7x90H+70oooJ6EUA/f7f4fSp7+JYYUZVAoooCI/R7dHZXZQzZHWq/juQ/bW6fKABx0oooDoct4ilY2IFcnN/rW/KiitYkjZW2yD2rqfAsKzzruUHb0ooqZbAdraN5TfKB+Vatk7SznceOOKKKZcdjSdcSRjsRzUlyMRj60UVEtw6mfdHbMuONwGag1KRoLdGU7TnFFFMZwfjm8kaZUP3a5DU5DHIoX0ooq47mZ3HwlsY5rKSRl+YA121qoK9M9OtFFTPc1hsf/Z"
profile="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"

try:
                with open("splash.png", "r") as img_f:
                            img_f.close()
except FileNotFoundError:
                root_splash.update()
                with open("splash.png", "wb") as img_f:
                            image_da= base64.b64decode(splash_img)
                            img_f.write(image_da)
                            ctypes.windll.kernel32.SetFileAttributesW("splash.png" , 0x02)
                            os.chmod("splash.png" , 0o4444)
background_image =ImageTk.PhotoImage(Image.open("splash.png"))
background_label = tk.Label(root_splash, image=background_image)
background_label.place(relwidth=1, relheight=1)
style=ttk.Style()

style.configure("TProgressbar",
                foreground="#lightblue",
                    background="lightblue",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    highlightcolor="lightblue",
                    anchor="center",
                    justify="center")
progress = ttk.Progressbar(root_splash,orient="horizontal", length=200, mode='determinate')
progress.pack(ipadx=20,side=tk.BOTTOM,pady=20)
sp_label=tk.Label(root_splash,text="0%",bg="white",fg="darkblue")
sp_label.pack(side=tk.BOTTOM,pady=0)
root_splash.after(1, start)

root_splash.mainloop()





    # ctypes.windll.kernel32.SetFileAttributesW("warp_setting" , 0x02)




def byte_to_base64(myb):
    return base64.b64encode(myb).decode('utf-8')
     

def generate_public_key(key_bytes):
    # Convert the private key bytes to an X25519PrivateKey object
    private_key = X25519PrivateKey.from_private_bytes(key_bytes)
    
    # Perform the scalar multiplication to get the public key
    public_key = private_key.public_key()
    
    # Serialize the public key to bytes
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )    
    return public_key_bytes



def generate_private_key():
    key = os.urandom(32)    
    # Modify random bytes using algorithm described at:
    # https://cr.yp.to/ecdh.html.
    key = list(key) # Convert bytes to list for mutable operations
    key[0] &= 248
    key[31] &= 127
    key[31] |= 64    
    return bytes(key) # Convert list back to bytes




def register_key_on_CF(pub_key):
    time.sleep(5)
    url = 'https://api.cloudflareclient.com/v0a4005/reg'
    # url = 'https://api.cloudflareclient.com/v0a2158/reg'
    # url = 'https://api.cloudflareclient.com/v0a3596/reg'

    body = {"key": pub_key,
            "install_id": "",
            "fcm_token": "",
            "warp_enabled": True,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "model": "PC",
            "locale": "en_US"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1',
               "CF-Client-Version": "a-6.30-3596"
               }

    r = requests.post(url, data=bodyString, headers=headers)
    return r




def bind_keys():
    priv_bytes = generate_private_key()
    priv_string = byte_to_base64(priv_bytes)
    
    
    
    
    pub_bytes = generate_public_key(priv_bytes)
    pub_string = byte_to_base64(pub_bytes)
    
    



    result = register_key_on_CF(pub_string)
    
    if result.status_code == 200:
        try:
            z = json.loads(result.content)
            client_id = z['config']["client_id"]      
            cid_byte = base64.b64decode(client_id)
            reserved = [int(j) for j in cid_byte]
            
            
            return '2606:4700:110:846c:e510:bfa1:ea9f:5247/128',priv_string,reserved, 'bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo='
            
        except Exception as e:
            print('Something went wronge with api')
            exit()


def free_cloudflare_account():
    with open("warp_setting" , "r") as f:
            num33=f.readlines()

    if  num33[3] =="1\n":

        
        keys=bind_keys()
        return keys
    elif  num33[3] =="2\n":
        pass
        
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("https://api.zeroteam.top/warp?format=sing-box", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("https://api.zeroteam.top/warp?format=sing-box", timeout=30)
                return response.text
    output = file_o()


       
    Address_pattern = r'"2606:4700:[0-9a-f:]+/128"'
    private_key_pattern = r'"private_key":"[0-9a-zA-Z/+]+="'
    reserved_pattern = r'"reserved":[[0-9]+(,[0-9]+){2}]'

    Address_search = re.search(Address_pattern, output)
    private_key_search = re.search(private_key_pattern, output)
    reserved_search = re.search(reserved_pattern, output)

      
    Address_key = Address_search.group(0).replace('"', '') if Address_search else None
    private_key = private_key_search.group(0).split(':')[1].replace('"', '') if private_key_search else None
    reserved = reserved_search.group(0).replace('"reserved":', '').replace('"', '') if reserved_search else None

    all_key=[Address_key , private_key , reserved, "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo="]
    return all_key

        
def fetch_config_from_api():
    with open("warp_setting" , "r") as f:
            num33=f.readlines()

    if  num33[3] =="1\n":
        print("heloo")
        
        keys=bind_keys()
        
        keys=list(keys)
        
        return {
        'PrivateKey': keys[1],
        'PublicKey':  keys[3],
        'Reserved':  keys[2],
        'Address':  keys[0]
        }
    elif  num33[3] =="1\n":
        pass

        
 
        
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("https://api.zeroteam.top/warp?format=sing-box", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("https://api.zeroteam.top/warp?format=sing-box", timeout=30)
                return response.text
            
    response = file_o()
    data = json.loads(response)
    return {
        'PrivateKey': data.get('private_key'),
        'PublicKey': data.get('peer_public_key'),
        'Reserved': ','.join([str(x) for x in data.get('reserved', [])]) if data.get('reserved') else None,
        'Address': data.get('local_address')
    }

def urlencode(string):
    
    if string is None:
        return None
    return urllib.parse.quote(string, safe='a-zA-Z0-9.~_-')

def generate_wireguard_url(config, endpoint):
    global api
    
    required_keys = ['PrivateKey', 'PublicKey' ,'Address' ]
    if not all(key in config and config[key] is not None for key in required_keys):
        print("Incomplete configuration. Missing one of the required keys or value is None.")
        return None

    
    with open("warp_setting" , "r") as f:
            num33=f.readlines()

    if  num33[3] =="2\n":
  
        encoded_addresses = [quote(address1) for address1 in (config['Address'])]
        address= ','.join(encoded_addresses)
        wireguard_urll = (
        f"wireguard://{urlencode(config['PrivateKey'])}@{endpoint}"
        f"?address={address}&"
        f"publickey={urlencode(config['PublicKey'])}"
    )
    
    
        if config.get('Reserved'):
   
                wireguard_urll += f"&reserved={urlencode(config['Reserved'])}"
    else:
        listt=config['Reserved']
        lostt2=''
        for num in range(len(listt)):
            lostt2+=str(listt[num])
            if num != len(listt)-1:
                lostt2+=','
        config['Reserved']=urlencode(lostt2)
        wireguard_urll = (
        f"wireguard://{urlencode(config['PrivateKey'])}@{endpoint}"
        f"?address=172.16.0.2/32,{urlencode(config['Address'])}&"
        f"publickey={urlencode(config['PublicKey'])}"
    )
   
        if config.get('Reserved'):
   
                wireguard_urll += f"&reserved={config['Reserved']}"	
            
    
    wireguard_urll += "#Tel= @arshiacomplus wire"

    return wireguard_urll



def which_Cpu_speed():
        global Cpu_speed
            

            
        
 
def main():
    global save_result
    global max_workers_number
    WH_ipVersion=""
    
    sorted_results=[]
    
    def main_move():
        global WH_ipVersion
        WH_ipVersion="ipv4"
        main_menu()
    def main_move_v6():
        global WH_ipVersion
        WH_ipVersion="ipv6"
        main_menu()

    def clean():
        button1.destroy()
        button.destroy()
        button3.destroy()
        t=0
        clean_result=[]
        try:
             
            with open("result.txt" ,"r") as f:
                b=f.readlines()
                bb=b[0]
        except Exception:
                    print("hello")
                    labelmain1.config(text="Finished")
                    label_best.insert(1.0, f"{t} IPs")
                    return
        

        
        try:
            bb.index("|")
        except Exception:
                print("hello")
                labelmain1.config(text="Finished")
                label_best.insert(1.0, f"{t} IPs")
                    
                return
    
        with open("warp_setting", "r") as f2:
            b2=f2.readlines()
        for i in b:
            if b2[2]=="2\n":
                            clean_result.append(",")
                            clean_result.append(str(i[:i.index("|")]))
            else:
                            clean_result.append("\n")
                            clean_result.append(str(i[:i.index("|")]))

                    

        
        with open("clean_result.txt" , "w")as f3:
            for i in clean_result:
                t+=0.5
                f3.write(i)
        with open("clean_result.csv" , "w")as f3:
            for i in clean_result:
                f3.write(i)
        labelmain1.config(text="Finished")
        label_best.insert(1.0, f"{t} IPs")
                

    def main_menu():
        global WH_ipVersion
  
        button1.destroy()
        button.destroy()
        button3.destroy()
        labelmain1.config(text="please wait ... ")
        label_best.insert(1.0, "best result: ")
        rootmain.update()

        global sorted_results
        global best_result
        with open("warp_setting" , "r") as f:
            num=f.readline()

        if  num[0] =="2":
                    Cpu_speed="1"
        elif  num[0] =="1":
                    Cpu_speed="2"

        
        
        
        if Cpu_speed == "1": max_workers_number=100
        elif Cpu_speed == "2": max_workers_number=50
        print(max_workers_number)
        def generate_ipv6():
                return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"

        def ping_ip(ip, port):
                global results
                global best_ip
                global best_result_avg

                
                
                
                icmp=pinging(ip, count=4 ,interval=1,timeout=5 ,family="ipv6")
                ping=float(icmp.avg_rtt)
                jitter=icmp.jitter
                loss_rate=icmp.packet_loss
                if ping == 0.0:
                    ping=1000
                if jitter== 0.0:
                     jitter=100
                if loss_rate==1.0:
                     loss_rate=100
                loss_rate=loss_rate*100
                if (0.5 *ping + +0.2 * jitter+ 0.3* loss_rate  ) > best_ip:
                    best_ip=(0.5 * float(icmp.avg_rtt) +0.2 *icmp.jitter + 0.3* icmp.packet_loss )
                    best_result_avg=ip
              
                results.append((ip, port, ping,loss_rate ,jitter ))
                
                


        def check_ac_v6(mn):
            global best_result
            label_best.delete(1.0,tk.END)
            best_result=mn
            for ip, port, ping, loss_rate,jitter , combined_score in sorted_results[:10]:
                table.insert("","end", values=(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%", f"{jitter:.2f}", f"{combined_score:.2f}"))

            table.pack()
            best_result = sorted_results[0] if sorted_results else None
            
            ip, port, ping, loss_rate,jitter, combined_score = best_result
            rootmain.clipboard_clear()
            rootmain.clipboard_append("["+ip+"]" +":"+str(port))
            label_best.insert(1.0,f"The best IP: [{ip}]:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}% ,{jitter} ms , score: {combined_score:.2f}" )
     
            best_result=2*[1]
            best_result[0]=f"{ip}"
            best_result[1]=878
            labelmain1.config(text="Finished")
            rootmain.update()

        def check_ac():
  
            global save_result
            global best_result
            global do_you_save
            label_best.delete(1.0,tk.END)
            table.tag_configure("oddrow", background="black")
            for j in range(len(table.get_children(""))):
                if j %2==2:
                       item=table.get_children("")[j]
                       table.item(item, tags=("oddrow" ,))
            for ip, port, ping, loss_rate,jitter, combined_score in sorted_results[:10]:
                table.insert("","end", values=(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%",f"{jitter}", f"{combined_score:.2f}"))

            table.pack()
            best_result = sorted_results[0] if sorted_results else None
            ip, port, ping, loss_rate,jitter, combined_score = best_result

            rootmain.clipboard_clear()
            rootmain.clipboard_append(ip +":"+str(port))
            try:
                    label_best.insert(1.0,f"The best IP: {ip}:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}%, {jitter} ms , score: {combined_score:.2f}")
      
            except TypeError:
                    label_best.insert(1.0,f"The best IP: {ip}:{port if port else '878'} , ping: None, packet loss: {loss_rate:.2f}%, {jitter} ms , score: {combined_score:.2f}")
               
            best_result=2*[1]
            best_result[0]=f"{ip}"
            best_result[1]=878
            do_you_save=""
            
            with open("warp_setting" , "r") as f:
                num=f.readlines()
                
                if  num[1] =="2\n":
                        do_you_save="1\n"

                elif  num[1] =="1\n":
                        do_you_save="2\n"

            print(do_you_save)
            print(best_result)
            filef=open("result.txt" , "w")
            t=0
            if do_you_save =="1\n":
                for i in save_result:
                    if t==0:
          
                        filef.write(i[1:])
                        t=1
                    else:
                        
                        filef.write(i)

            filef.close()
                     
            return best_result
        def create_ip_range(start_ip, end_ip):
            start = list(map(int, start_ip.split('.')))
            end = list(map(int, end_ip.split('.')))
            temp = start[:]
            ip_range = []

            while temp != end:
                ip_range.append('.'.join(map(str, temp)))
                temp[3] += 1
                for i2 in (3, 2, 1):
                    if temp[i2] == 256:
                        temp[i2] = 0
                        temp[i2-1] += 1
            ip_range.append(end_ip)
            return ip_range
        

        def scan_ip_port(ip, port):
            global best_result
            global sorted_results
            global results
            global save_result
            global do_you_save
           

            icmp=pinging(ip, count=2 ,interval=1,timeout=5,family="ipv4" )





            results.append((ip, port, float(icmp.avg_rtt) ,float(icmp.packet_loss),float(icmp.jitter)))



    
        labelmain1.config(text="Please wait scannig ip ...")

        rootmain.update()

        if WH_ipVersion=="ipv6":
            ports_to_check = [1074 , 864]
            

            random_ip=generate_ipv6()


            executor= ThreadPoolExecutor(max_workers=max_workers_number)
            try:
                for _  in range(101):
                    executor.submit(ping_ip, generate_ipv6(), ports_to_check[random.randint(0,1)])
            except Exception:
                print("AN Error")
            finally:
                executor.shutdown(wait=True)


            extended_results=[]
            for result in results:
                ip, port, ping , loss_rate, jitter= result
                
                if loss_rate == 0.00 and ping != 0.0 and ping < 300.00:
                    
                    try:
                        save_result.index(str(ip))
                    except Exception:
                        with open("warp_setting" , "r") as f:
                            warp111=f.readlines()
                            if warp111[2]=="2\n":
                                save_result.append(",")
                                save_result.append(str(ip))
                            else:
                                save_result.append("\n")
                                save_result.append(str(ip))

                combined_score = (0.5 * ping +0.2 *jitter + 0.3* loss_rate)
                extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))

            sorted_results=sorted(extended_results, key=lambda x: x[5])
            best_result=sorted_results[0]
            
            


            port_random = ports_to_check[random.randint(0, len(ports_to_check) - 1)]
            if best_ip:

                best_ip_mix = [1] * 2
                best_ip_mix[0] = "[" + best_result_avg + "]"
                best_ip_mix[1] = port_random
            else:

                best_ip_mix = [1] * 2
                best_ip_mix[0] = "[" + random_ip + "]"
                best_ip_mix[1] = port_random
            print(best_ip_mix)
            check_ac_v6(best_ip_mix)
        else:   
            start_ips = ["188.114.96.0", "162.159.192.0", "162.159.195.0"]
            end_ips = ["188.114.99.224", "162.159.193.224", "162.159.195.224"]
            ports = [1074, 894, 908, 878]
            
 
            # except Exception:
            #      executor_bar.shutdown(wait=True)


            for start_ip, end_ip in zip(start_ips, end_ips):
                ip_range = create_ip_range(start_ip, end_ip)
                
                executor= ThreadPoolExecutor(max_workers=max_workers_number)
                try:
                    for ip in ip_range:
                        randomp=ports[random.randint(0,3)]
          

                        executor.submit(scan_ip_port, ip, randomp)
                except Exception:
                    print("AN Error")
                finally:
                    executor.shutdown(wait=True)


                
            
            
            extended_results = []
            with open("warp_setting" , "r") as f:
                warp1111=f.readlines()
            for result in results:
                ip, port, ping , loss_rate, jitter= result
                
                if loss_rate == 0.00 and ping != 0.0 and ping < 300.00:
                    if warp1111[1]=="2\n":
                         
                        try:
                            save_result.index(str(ip))
                        except Exception:
                            with open("warp_setting" , "r") as f:
                                warp111=f.readlines()
                                if warp111[2]=="2\n":
                                    save_result.append(",")
                                    save_result.append(str(ip))
                                elif warp111[2]=="1\n":
                                    save_result.append("\n")
                                    save_result.append(str(ip))

                               
                if ping==0.0 :
                    ping=1000
                
                if  jitter==0.0:
                    
                    jitter=1000
                if loss_rate == 1.0:
                     loss_rate=100
                loss_rate=loss_rate*100
                

                combined_score = (0.5 * ping +0.2 *jitter + 0.3* loss_rate)
                extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))
                        

            sorted_results = sorted(extended_results, key=lambda x: x[5])
            if warp1111[2]=="3\n": 

                for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
                                    save_result.append("\n")
                                    save_result.append(ip+" | "+"ping: "+ str(   ping) +"packet_loss: "+ str( loss_rate)+"jitter: "+str(   jitter)) 

            best_result=sorted_results[0]
        
            while len(sorted_results) < 10:
                sorted_results.append(("No IP", None, None, 100, 1000))

            
            check_ac()

       
    
    

    rootmain= tk.Tk()

    rootmain.title("my WarpScanner")


    labelmain1=tk.Label(rootmain , font = ('arial', 11) ,  text="Click to scan ip")
    labelmain1.pack()

    

            



 
    table=ttk.Treeview(rootmain, columns=("IP" ,"Port" , "Ping (ms)" , "Packet Loss (%)" ,"Jitter (ms)", "Score" ), show='headings')


    table.heading("IP" , text="IP")
    table.heading("Port" , text="port")
    table.heading("Ping (ms)" , text="Ping (ms)")
    table.heading("Packet Loss (%)" , text="Packet Loss (%)")
    table.heading("Jitter (ms)", text="jitter (ms)")
    table.heading("Score" , text="Score")

    
    label_best=Text(rootmain , width=50,height=1)
    label_best.pack()

    
    button = tk.Button(rootmain, width=5, padx=6, pady=4, bd=1, text="ipV4")
    button.pack(fill=tk.X,side=tk.BOTTOM)
    button.bind("<Enter>", hand2)


    button1 = tk.Button(rootmain, width=5, padx=6, pady=4, bd=1, text="ipV6", command=main_move_v6)
    button1.pack(fill=tk.X,side=tk.BOTTOM)
    button1.bind("<Enter>", hand2)


    button3 = tk.Button(rootmain, width=5, padx=6, pady=4, bd=1, text="clean", command=clean)
    button3.pack(fill=tk.X,side=tk.BOTTOM)
    button3.bind("<Enter>", hand2)





    rootmain.mainloop()

    # t=False
    # if what == '1':
    #     if do_you_save=='1':
    #         if which =="1":
    #              with open('/storage/emulated/0/result.csv' , "w") as f:
    #                   for j in save_result[1:]:
    #                       if j != "\n":
    #                           f.write(j)
    #                           t=False
    #                       else:
    #                      # 	if j != save_result[len(save_result)-1]:
    #                               if t==False:
    #                                    f.write(",")
    #                               t=True
                                 
    #         else:
    #              with open('/storage/emulated/0/result.csv' , "w") as f:
    #                   for j in save_result:
    #                       f.write(j)
                       
    #         print(' saved in /storage/emulated/0/result.csv !')



def hand2(event):
     event.widget.config(cursor="hand2")
def wireguard_config():
    global Cpu_speed
    def wireguard_config_main(which_ip):
            global Cpu_speed
            global max_workers_number
            global sorted_results
            global i_ip_scan
            global best_result
    

            if i_ip_scan ==False:
                button.destroy()
            button1.destroy()
            labelmain_wire.config(text="please wait ... ")
            rootwire_confing.update()

            

            



            
            
            if Cpu_speed == "1": max_workers_number=100
            elif Cpu_speed == "2": max_workers_number=50
            def upload_to_bashupload(config_data):
                rootsub.destroy()
                @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
                def file_o():
                    files = {'file': ('output.json', config_data)}
                    try:
                        response = requests.post('https://bashupload.com/', files=files, timeout=30)
                    except Exception:
                        response = requests.post('https://bashupload.com/', files=files, timeout=50)
                    return response
    
                    
                response = file_o()

                if response.ok:
                    download_link = response.text.strip()
                    download_link_with_query = download_link[59:len(download_link)-27] + "?download=1"
                    true=""
                 
                    for i in download_link_with_query :
                        if true=="":
                            if i != "b":
                                pass
                            else:
                                true="https://"
                                true+=i
                        else:
                            
                            true+=i
                
                                 
                          
                    label_best.insert(1.0, str(true) )
                    rootwire_confing.clipboard_clear()
                    rootwire_confing.clipboard_append(str(true))
              
                else:
                    label_best.insert(1.0, "Error try again")
   
                

                
            
            def generate_ipv6():
                    return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"
            def ping_ip(ip, port):
                    global results
                    global best_ip
                    global best_result_avg

                    
                    
                    
                    icmp=pinging(ip, count=4 ,interval=1,timeout=5 ,family="ipv6")
                    ping=float(icmp.avg_rtt)
                    jitter=icmp.jitter
                    loss_rate=icmp.packet_loss
                    if ping == 0.0:
                        ping=1000
                    if jitter== 0.0:
                        jitter=100
                    if loss_rate==1.0:
                        loss_rate=100
                    loss_rate=loss_rate*100
                    if (0.5 *ping + +0.2 * jitter+ 0.3* loss_rate  ) > best_ip:
                        best_ip=(0.5 * float(icmp.avg_rtt) +0.2 *icmp.jitter + 0.3* icmp.packet_loss )
                        best_result_avg=ip
                
                    results.append((ip, port, ping,loss_rate ,jitter ))
                    
                    


            def check_ac_v6(mn, i):
                global i_ip_scan
                global is_v2ray
                global best_result
                if is_v2ray==True:
                    best_result = sorted_results[0] if sorted_results else None
                    if i_ip_scan==True:
                        ip, port, ping, loss_rate,jitter ,combined_score= best_result
                    else:
                        ip, port= best_result


                    config = fetch_config_from_api()
                    wireguard_url = generate_wireguard_url(config, f"[{ip}]"+":"+str(port))

                    rootwire_confing.clipboard_clear()
                    rootwire_confing.clipboard_append(wireguard_url)

                    label_best.insert(1.0, wireguard_url)
                    labelmain_wire.config(text="finished")

                    return





                if i_ip_scan ==False:


                    best_result=mn

                    best_result = sorted_results[0] if sorted_results else None

                    ip, port, ping, loss_rate,jitter ,combined_score= best_result

                    best_result=[0]*2
                    best_result[0]=ip
                    best_result[1]=port
                
                
                try:
                    all_key=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()
        
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()

                
                if is_sub ==True:             
                    if wire_p !=1:
                        wire_config_or = f'''

                    {{
                    "type": "wireguard",
                    "tag": "Tel=@arshiacomplus Warp-IR{wire_c}",
                    "server": "{best_result[0]}",
                    "server_port": {best_result[1]},

                    "local_address": [
                        "172.16.0.2/32",
                        "{all_key[0]}"
                    ],
                    "private_key": "{all_key[1]}",
                    "peer_public_key": "{all_key[3]}",
                    "reserved": {all_key[2]},

                    "mtu": 1280,
                    "fake_packets": "5-10"
                    }},
                    {{
                    "type": "wireguard",
                    "tag": "Tel=@arshiacomplus Warp-Main{wire_c}",
                    "detour": "Tel=@arshiacomplus Warp-IR{wire_c}",
                    "server": "{best_result[0]}",
                    "server_port": {best_result[1]},
                    
                    "local_address": [
                        "172.16.0.2/32",
                        "{all_key2[0]}"
                    ],
                    "private_key": "{all_key2[1]}",
                    "peer_public_key": "{all_key2[3]}",
                    "reserved": {all_key2[2]},

                    "mtu": 1120

                    }}

                '''
                    else:
                        wire_config_or = f'''

                    ,{{
                    "type": "wireguard",
                    "tag": "Tel=@arshiacomplus Warp-IR{wire_c}",
                    "server": "{best_result[0]}",
                    "server_port": {best_result[1]},

                    "local_address": [
                        "172.16.0.2/32",
                        "{all_key[0]}"
                    ],
                    "private_key": "{all_key[1]}",
                    "peer_public_key": "{all_key[3]}",
                    "reserved": {all_key[2]},

                    "mtu": 1280,
                    "fake_packets": "5-10"
                    }},
                    {{
                    "type": "wireguard",
                    "tag": "Tel=@arshiacomplus Warp-Main{wire_c}",
                    "detour": "Tel=@arshiacomplus Warp-IR{wire_c}",
                    "server": "{best_result[0]}",
                    "server_port": {best_result[1]},
                    
                    "local_address": [
                        "172.16.0.2/32",
                        "{all_key2[0]}"
                    ],
                    "private_key": "{all_key2[1]}",
                    "peer_public_key": "{all_key2[3]}",
                    "reserved": {all_key2[2]},

                    "mtu": 1120

                    }}

                '''

                    if i == int(how_meny.get())-1:
                        print("b")
                        upload_to_bashupload(f'''{{
                "outbounds": 
                [{wire_config_temp}
                ]
                }}
                ''')
                        
                    else:
                        print("A")
                                    
                        wire_config_temp=wire_config_temp+wire_config_or
                            
                            
                    wire_c=wire_c+1
                    wire_p=1


                if is_sub == False:
                    
                    conf=f'''
{{
        "route": {{                                                         "geoip": {{
                "path": "geo-assets\\\\sagernet-sing-geoip-geoip.db"
                }},                                                         "geosite": {{
                "path": "geo-assets\\\\sagernet-sing-geosite-geosite.db"
                }},                                                         "rules": [
                {{                                                                  "inbound": "dns-in",
                        "outbound": "dns-out"                              }},
                {{                                                                  "port": 53,
                        "outbound": "dns-out"                              }},
                {{                                                                  "clash_mode": "Direct",
                        "outbound": "direct"                               }},
                {{                                                                  "clash_mode": "Global",
                        "outbound": "select"
                }}
                ],
                "auto_detect_interface": true,
                "override_android_vpn": true                       }},
        "outbounds": [
                {{
                "type": "selector",
                "tag": "select",                                           "outbounds": [
                        "auto",
                        "IP->Iran, Telegram: @arshiacomplus",
                        "IP->Main, Telegram: @arshiacomplus"
                ],
                "default": "auto"
                }},
                {{
                "type": "urltest",
                "tag": "auto",
                "outbounds": [
                        "IP->Iran, Telegram: @arshiacomplus",
                        "IP->Main, Telegram: @arshiacomplus"
                ],
                "url": "http://cp.cloudflare.com/",
                "interval": "10m0s"
                }},
                {{
                "type": "wireguard",
                "tag": "IP->Iran, Telegram: @arshiacomplus",
                "local_address": [
                        "172.16.0.2/32",
                        "{all_key[0]}"
                ],
                "private_key": "{all_key[1]}",
                "server": "{best_result[0]}",
                "server_port": {best_result[1]},
                "peer_public_key": "{all_key[3]}",
                "reserved": {all_key[2]},
                "mtu": 1280,
                "fake_packets": "5-10"
                }},
                {{
                "type": "wireguard",
                "tag": "IP->Main, Telegram: @arshiacomplus",
                "detour": "IP->Iran, Telegram: @arshiacomplus",
                "local_address": [
                        "172.16.0.2/32",
                        "{all_key2[0]}"
                ],
                "private_key": "{all_key2[1]}",
                "server": "{best_result[0]}",
                "server_port": {best_result[1]},
                "peer_public_key": "{all_key[3]}",
                "reserved": {all_key2[2]},
                "mtu": 1280,
                "fake_packets": "5-10"
                }},
                {{
                "type": "dns",
                "tag": "dns-out"
                }},
                {{
                "type": "direct",
                "tag": "direct"
                }},
                {{
                "type": "direct",
                "tag": "bypass"
                }},
                {{
                "type": "block",
                "tag": "block"
                }}
        ]
        }}
'''
                    label_best.insert(1.0 ,conf)
                    rootwire_confing.clipboard_clear()
                    rootwire_confing.clipboard_append(conf)

                    labelmain_wire.config(text="finished")

            def check_ac(i):
                
                global i_ip_scan
                global is_sub
                global best_result
                global wire_c
                global wire_p
                global wire_config_or
                global wire_config_temp
                global save_result
                global is_v2ray

                if is_v2ray==True:
              

                    ip, port= best_result
                    
                    config = fetch_config_from_api()
                    wireguard_url = generate_wireguard_url(config, f"{ip}"+":"+str(port))

                    rootwire_confing.clipboard_clear()
                    rootwire_confing.clipboard_append(wireguard_url)


                    label_best.insert(1.0, wireguard_url)
                    labelmain_wire.config(text="finished")

                    return



                if i_ip_scan == False:
                    best_result = sorted_results[0] if sorted_results else None
                    
                    ip, port, ping, loss_rate,jitter, combined_score = best_result

                    best_result=[0]*2
                    best_result[0]=f"{ip}"
                    best_result[1]=port
                

                try:
                    all_key=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()
        
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()

                
                if is_sub ==True:
                    if wire_p==0:
         
                        time.sleep(8)

                        
                        

                        if wire_p !=1:
                            all_key=free_cloudflare_account()
                            all_key2=free_cloudflare_account()
                            wire_config_or = f'''

                        {{
                        "type": "wireguard",
                        "tag": "Tel=@arshiacomplus Warp-IR1",
                        "local_address": [
                            "172.16.0.2/32",
                            "{all_key[0]}"
                        ],
                        "private_key": "{all_key[1]}",
                        "peer_public_key": "{all_key[3]}",
                        "server": "{best_result[0]}",
                        "server_port": {best_result[1]},
                        "reserved": {all_key[2]},

                        "mtu": 1280,
                        "fake_packets":"1-3",
                        "fake_packets_size":"10-30",
                        "fake_packets_delay":"10-30",
                        "fake_packets_mode":"m4"
                        }},
                        {{
                        "type": "wireguard",
                        "tag": "Tel=@arshiacomplus Warp-Main1",
                        "detour": "Tel=@arshiacomplus Warp-IR1",
                        "local_address": [
                            "172.16.0.2/32",
                            "{all_key2[0]}"
                        ],
                        "private_key": "{all_key2[1]}",
                        "server": "{best_result[0]}",
                        "server_port": {best_result[1]},
                        "peer_public_key": "{all_key2[3]}",
                        "reserved": {all_key2[2]},
                        "mtu": 1330,
                        "fake_packets_mode":"m4"
                    
                        }}

                    '''
                        else:
                            all_key=free_cloudflare_account()
                            all_key2=free_cloudflare_account()
                            wire_config_or = f'''

                        ,{{
                        "type": "wireguard",
                        "tag": "Tel=@arshiacomplus Warp-IR1",
                        "local_address": [
                            "172.16.0.2/32",
                            "{all_key[0]}"
                        ],
                        "private_key": "{all_key[1]}",
                        "peer_public_key": "{all_key[3]}",
                        "server": "{best_result[0]}",
                        "server_port": {best_result[1]},
                        "reserved": {all_key[2]},

                        "mtu": 1280,
                        "fake_packets":"1-3",
                        "fake_packets_size":"10-30",
                        "fake_packets_delay":"10-30",
                        "fake_packets_mode":"m4"
                        }},
                        {{
                        "type": "wireguard",
                        "tag": "Tel=@arshiacomplus Warp-Main1",
                        "detour": "Tel=@arshiacomplus Warp-IR1",
                        "local_address": [
                            "172.16.0.2/32",
                            "{all_key2[0]}"
                        ],
                        "private_key": "{all_key2[1]}",
                        "server": "{best_result[0]}",
                        "server_port": {best_result[1]},
                        "peer_public_key": "{all_key2[3]}",
                        "reserved": {all_key2[2]},
                        "mtu": 1330,
                        "fake_packets_mode":"m4"
                    
                        }}

                    '''

                    if i == int(how_meny.get())-1:
                        print("b")
                        upload_to_bashupload(f'''{{
                "outbounds": 
                [{wire_config_temp}
                ]
                }}
                ''')
                        
                    else:
                        print("A")
                                    
                        wire_config_temp=wire_config_temp+wire_config_or
                            
                            
                    wire_c=wire_c+1
                    wire_p=1


                if is_sub == False:

                    conf=f'''
{{
  "outbounds": 
  [

    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-IR1",
    "local_address": [
        "172.16.0.2/32",
        "{all_key[0]}"
    ],
    "private_key": "{all_key[1]}",
    "peer_public_key": "{all_key[3]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "reserved": {all_key[2]},

    "mtu": 1280,
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"
    }},
    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-Main1",
    "detour": "Tel=@arshiacomplus Warp-IR1",
    "local_address": [
        "172.16.0.2/32",
        "{all_key2[0]}"
    ],
    "private_key": "{all_key2[1]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "peer_public_key": "{all_key2[3]}",
    "reserved": {all_key2[2]},
    "mtu": 1330,
    "fake_packets_mode":"m4"
 
    }}
  ]
}}
'''
                    print("a")

                    label_best.insert(1.0 ,conf)
                    rootwire_confing.clipboard_clear()
                    rootwire_confing.clipboard_append(f"{conf}")

                    labelmain_wire.config(text="finished")


            def create_ip_range(start_ip, end_ip):
                start = list(map(int, start_ip.split('.')))
                end = list(map(int, end_ip.split('.')))
                temp = start[:]
                ip_range = []

                while temp != end:
                    ip_range.append('.'.join(map(str, temp)))
                    temp[3] += 1
                    for i2 in (3, 2, 1):
                        if temp[i2] == 256:
                            temp[i2] = 0
                            temp[i2-1] += 1
                ip_range.append(end_ip)
                return ip_range
            def scan_ip_port(ip, port):
                global best_result
                global sorted_results
                global results
                
            
                icmp=pinging(ip, count=2 ,interval=1,timeout=5,family="ipv4" )


                results.append((ip, port, float(icmp.avg_rtt) ,icmp.packet_loss,icmp.jitter))
                
            if i_ip_scan==True:
                def submit():
                    global best_result
                    best_result=[1]*2
                    best_result_temp=str(ip_entry.get())
                    best_result[0]=best_result_temp[:best_result_temp.index(":")]
                    best_result[1]=best_result_temp[best_result_temp.index(":")+1:]


                    rootip.destroy(),check_ac("")



                

                rootip=tk.Tk()
                rootip.title("main activity ")
                rootip.geometry("+200+200")

                style3 = ttk.Style(rootip)
                style3.configure("TButton",      
                    foreground="black",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    highlightcolor="lightblue",
                    font=("Helvetica", 10, "bold"),
                    anchor="center",
                    justify="center")
                
                style2 = ttk.Style(rootip)
                style2.configure("TLabel",
         
                    foreground="#3d7e7d",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    highlightcolor="lightblue",
                    font=("Helvetica", 10),
                    anchor="center",
                    justify="center",
                )

                style = ttk.Style(rootip)
                style.configure("TEntry",
         
                    foreground="#3d7e7d",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    highlightcolor="lightblue",
                    font=("Helvetica", 10),
                    anchor="center",
                    justify="center",
                    )
    
    
                label_ff=ttk.Label(rootip, text="Enter an ipv4")
                label_ff.pack(fill=tk.X)

                

                
                ip_entry=ttk.Entry(rootip)
                ip_entry.pack( padx=10, pady=10,fill=tk.X)
                rootip.after(0,focus(ip_entry))

                submitb=ttk.Button(rootip, text="submit", command=submit)
                submitb.pack(fill=tk.X,padx=11, pady=4)
                submitb.bind("<Enter>", hand2)


                rootip.mainloop()
                

            else:
                if which_ip=="ipv6":


                    ports_to_check = [1074 , 864]
                    

                    random_ip=generate_ipv6()
                    
                    executor= ThreadPoolExecutor(max_workers=max_workers_number)
                    try:
                            for _  in range(101):
                                executor.submit(ping_ip, generate_ipv6(), ports_to_check[random.randint(0,1)])
                    except Exception:
                            print("AN Error")
                    finally:
                            executor.shutdown(wait=True)

                    extended_results=[]
                    for result in results:
                        ip, port, ping , loss_rate, jitter= result
                        
                        if loss_rate == 0.00 and ping != 0.0 and ping < 300.00:
                            
                            try:
                                save_result.index(str(ip))
                            except Exception:
                                with open("warp_setting" , "r") as f:
                                    warp111=f.readlines()
                                    if warp111[2]=="2\n":
                                        save_result.append(",")
                                        save_result.append(str(ip))
                                    else:
                                        save_result.append("\n")
                                        save_result.append(str(ip))

                        combined_score = (0.5 * ping +0.2 *jitter + 0.3* loss_rate)
                        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))

                    sorted_results=sorted(extended_results, key=lambda x: x[5])
                    best_result=sorted_results[0]



                    


                    port_random = ports_to_check[random.randint(0, len(ports_to_check) - 1)]
       
                    if best_ip:

                        best_ip_mix = [1] * 2
                        best_ip_mix[0] = best_result_avg
                        best_ip_mix[1] = port_random
                        

                    else:

                        best_ip_mix = [1] * 2
                        best_ip_mix[0] = random_ip 
                        best_ip_mix[1] = port_random


                    
                    if is_sub ==True and  wire_p !=1:
                        def submit():
                            for i in range(int(how_meny.get())):


                                check_ac_v6(best_ip_mix, i)

                        rootsub= tk.Tk()
                        rootsub.title("how_many")
                        rootsub.geometry("+200+200")

                        rootsub.configure(bg="#414141",fg="#f0f0f0")
                        style3 = ttk.Style(rootip)
                        style3.configure("TButton",      
                            foreground="black",
                            highlightthickness=20,
                            highlightbackground="lightblue",
                            highlightcolor="lightblue",
                            font=("Helvetica", 10, "bold"),
                            anchor="center",
                            justify="center")
                        
                        style2 = ttk.Style(rootip)
                        style2.configure("TLabel",
                
                            foreground="#3d7e7d",
                            highlightthickness=20,
                            highlightbackground="lightblue",
                            highlightcolor="lightblue",
                            font=("Helvetica", 10),
                            anchor="center",
                            justify="center",
                        )

                        style = ttk.Style(rootip)
                        style.configure("TEntry",
                
                            foreground="#3d7e7d",
                            highlightthickness=20,
                            highlightbackground="lightblue",
                            highlightcolor="lightblue",
                            font=("Helvetica", 10),
                            anchor="center",
                            justify="center",
                            )
                        label_ff=ttk.Label(rootsub, text="How meny")
                        label_ff.pack(fill=tk.X)

                        
                        how_meny=ttk.Entry(rootsub)
                        how_meny.pack( padx=10, pady=10,fill=tk.X)

                        submitbb=ttk.Button(rootsub, text="submit", command=submit)
                        submitbb.pack(padx=11, pady=4,fill=tk.X)
                        submitbb.bind("<Enter>", hand2)


                        rootsub.mainloop()
                    else:

                        check_ac_v6(best_ip_mix ,"")
                else:


                    start_ips = ["188.114.96.0", "162.159.192.0", "162.159.195.0"]
                    end_ips = ["188.114.99.224", "162.159.193.224", "162.159.195.224"]
                    ports = [1074, 894, 908, 878]
                    
                    

                    for start_ip, end_ip in zip(start_ips, end_ips):
                        ip_range = create_ip_range(start_ip, end_ip)
                        
                        executor= ThreadPoolExecutor(max_workers=max_workers_number)
                        try:
                            for ip in ip_range:
                                randomp=ports[random.randint(0,3)]

                                executor.submit(scan_ip_port, ip, randomp)
                        except Exception:
                            print("AN Error")
                        finally:
                            executor.shutdown(wait=True)
                        

                    extended_results = []
            
                    for result in results:
                        ip, port, ping , loss_rate, jitter= result
                        
                        if loss_rate == 0.00 and ping != 0.0 and ping < 500.00:
                            
                            try:
                                save_result.index(str(ip))
                            except Exception:
                                save_result.append("\n")
                                save_result.append(str(ip))
                        if ping==0.0 :
                            ping=1000
                        
                        if  jitter==0.0:
                            
                            jitter=1000
                        if loss_rate == 1.0:
                            loss_rate=100
                        loss_rate=loss_rate*100

                        combined_score = combined_score = (0.5 * ping +0.2 *jitter + 0.3* loss_rate)
                        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))
                                

                    

                    sorted_results = sorted(extended_results, key=lambda x: x[5])
                    best_result=sorted_results[0]
                
                    while len(sorted_results) < 10:
                        sorted_results.append(("No IP", None, None, 100, 1000))

                    if is_sub ==True and  wire_p !=1:
                        def submit():
                            for i in range(int(how_meny.get())):


                                check_ac(i)

                        rootsub= tk.Tk()
                        rootsub.title("how_many")
                        rootsub.geometry("+200+200")

                        style3 = ttk.Style(rootsub)
                        style3.configure("TButton",      
                            foreground="black",
                            highlightthickness=20,
                            highlightbackground="lightblue",
                            highlightcolor="lightblue",
                            font=("Helvetica", 10, "bold"),
                            anchor="center",
                            justify="center")
                        
                        style2 = ttk.Style(rootsub)
                        style2.configure("TLabel",
                
                            foreground="#3d7e7d",
                            highlightthickness=20,
                            highlightbackground="lightblue",
                            highlightcolor="lightblue",
                            font=("Helvetica", 10),
                            anchor="center",
                            justify="center",
                        )

                        style = ttk.Style(rootsub)
                        style.configure("TEntry",
                
                            foreground="#3d7e7d",
                            highlightthickness=20,
                            highlightbackground="lightblue",
                            highlightcolor="lightblue",
                            font=("Helvetica", 10),
                            anchor="center",
                            justify="center",
                            )
                
            

                        label_ff=ttk.Label(rootsub, text="How meny")
                        label_ff.pack(fill=tk.X)
                        
                        how_meny=ttk.Entry(rootsub)
                        how_meny.pack( padx=10, pady=10,fill=tk.X)

                        submitbb=ttk.Button(rootsub, text="submit", command=submit)
                        submitbb.pack(fill=tk.X)

                        rootsub.mainloop()
                    else:
                        check_ac("")

                    


    with open("warp_setting" , "r") as f:
            num=f.readline()

            if  num[0] =="2":
                        Cpu_speed="1"
            elif  num[0] =="1":
                        Cpu_speed="2"

                     

    def main_move():
        wireguard_config_main("ipv4")
    def main_move_v6():
        wireguard_config_main("ipv6")


    

    # rootwhich_Vip=tk.Tk()
    # rootwhich_Vip.title("main activity ")

    


    # rootwhich_Vip.mainloop()

    rootwire_confing=tk.Tk()
    rootwire_confing.title("Wire_config")
    rootwire_confing.geometry("+200+200")



    labelmain_wire=tk.Label(rootwire_confing , font = ('arial', 11) ,  text="Click to Make wire_config")
    labelmain_wire.pack(fill=tk.X)


    
    label_best=Text(rootwire_confing, width=50,height=5)
    label_best.pack(fill=tk.X)


    if i_ip_scan ==True:
         

        button1 = tk.Button(rootwire_confing, width=5, padx=6, pady=4, bd=1, text="start", command=main_move,fg="#f0f0f0", bg="#414141")
        button1.pack(fill=tk.X,side=tk.BOTTOM)
        button1.bind("<Enter>", hand2)

        

    else:
        button = tk.Button(rootwire_confing, width=5, padx=6, pady=4, bd=1, text="ipV4", command=main_move,fg="#f0f0f0", bg="#414141")
        button.pack(fill=tk.X,side=tk.BOTTOM)
        button.bind("<Enter>", hand2)


        button1 = tk.Button(rootwire_confing, width=5, padx=6, pady=4, bd=1, text="ipV6", command=main_move_v6,fg="#f0f0f0", bg="#414141")
        button1.pack(fill=tk.X,side=tk.BOTTOM)
        button1.bind("<Enter>", hand2)
    

    rootwire_confing.mainloop()
def wireguard_config_without():
    global i_ip_scan
    global is_sub
    global is_v2ray
    is_v2ray=False
    i_ip_scan=True
    is_sub=False
    wireguard_config()
def wireguard_config_sub():
    global is_sub
    global i_ip_scan
    global is_v2ray
    is_v2ray=False
    i_ip_scan=False
    is_sub=True
    wireguard_config()
def v2ray():
    global is_v2ray
    global i_ip_scan
    i_ip_scan=False
    is_v2ray=True
    wireguard_config()
def v2ray_without():
    global is_v2ray
    global i_ip_scan
    i_ip_scan=True
    is_v2ray=True
    wireguard_config()
def wireguard_config_ok():
    global i_ip_scan
    i_ip_scan=False
    wireguard_config()
def mainactivity():
    rootmainactivity=tk.Tk()
    rootmainactivity.geometry("500x500")
    rootmainactivity.geometry("+200+100")
    rootmainactivity.title("main activity ")
    rootmainactivity.config(cursor="arrow")
    rootmainactivity.resizable(False, False)
    rootmainactivity.attributes("-alpha" , 1.0)
    choose=random.randint(0,1)
    choose=1
    if choose==1:

             
        

        background_image =ImageTk.PhotoImage(Image.open("nika.png"))
        background_label = tk.Label(rootmainactivity, image=background_image)
        background_label.place(relwidth=1, relheight=1)
    else:
        
        background_image =ImageTk.PhotoImage(Image.open("mahsa.png"))
        background_label = tk.Label(rootmainactivity, image=background_image)
        background_label.place(relwidth=2, relheight=2)
    
    
    menu_image =ImageTk.PhotoImage(Image.open("profile.png"))

     
    def toggle_menu():
            if menu_frame.winfo_x() == rootmainactivity.winfo_screenwidth():

               
               


                for i in range(300, rootmainactivity.winfo_width() - menu_frame.winfo_width()):
                    
                    menu_frame.place(x=i, y=0)
                    rootmainactivity.update()
                    time.sleep(0.00001)
            else:
           
                time.sleep(0.1)
                menu_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0)

    def About():
        def Github_link(event):
            webbrowser.open_new(r"https://github.com/arshiacomplus/WarpScanner/releases")
        def Telegram_link(event):
            webbrowser.open_new(r"https://t.me/arshia_mod_fun")
        def copy_donate(event):
            root_about.clipboard_append("TKUpVDG5DqLDUSg3X1hhidRPuhm1GmqZ2G")
            trx.config(text="Copied")

        root_about=tk.Tk()
        root_about.title("About")
        root_about.config(cursor="heart")
        root_about.geometry("+200+50")
        root_about.geometry("600x600")
        style=ttk.Style(root_about)
        style.configure("Costump.TLabel",
                    font=("Helvetica", 10,"bold"),
                    anchor="center",
                    justify="center",
                    padding=50,
                    foreground="lightblue",
                    background="#ffffff",
                    highlightthickness=20,
                    highlightbackground="lightblue")
        
        style2=ttk.Style(root_about)
        style2.configure("Costum.TLabel",
                    foreground="#3d7e7d",
                    background="#ffffff",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    padding=5,
                    highlightcolor="lightblue",
                    relief="groove",
                    font=("Helvetica", 10, "bold"),
                    anchor="center",
                    justify="center")
        style3=ttk.Style(root_about)
        style3.configure("Costumpp.TLabel",
                    font=("Helvetica", 10,"bold"),
                    anchor="center",
                    justify="center",
                    padding=5,
                    foreground="lightblue",
                    background="#ffffff",
                    highlightthickness=20,
                    highlightbackground="lightblue")
        label_about=ttk.Label(root_about,style="Costum.TLabel", text="This is an Warp Scanner For win")
        label_about.pack(fill=tk.X)

        label_mew=ttk.Label(root_about,style="Costump.TLabel",text="New version V0.3.0:\nGood news:\n\nNew Api Added\n\nBetter style\n\nBad news:\n\nApi zeroteam Deleted ")
        label_mew.pack(pady=5,fill=tk.X)
        label_about1=ttk.Label(root_about,style="Costum.TLabel", text="Github Link :")
        label_about1.pack(fill=tk.X)
        link_git=tk.Label(root_about, text="Github" , fg="blue" , cursor="hand2")
        link_git.pack(fill=tk.X)
        link_git.bind("<Button-1>" ,Github_link)

        label_about2=ttk.Label(root_about,style="Costum.TLabel", text="Telegram Link :")
        label_about2.pack(fill=tk.X)
        link_tel=tk.Label(root_about, text="Telegram" , fg="blue" , cursor="hand2")
        link_tel.pack(fill=tk.X)
        link_tel.bind("<Button-1>" ,Telegram_link)

        label_about2=ttk.Label(root_about,style="Costum.TLabel", text="Donate:")
        label_about2.pack(fill=tk.X)

        trx=ttk.Label(root_about,style="Costumpp.TLabel", text="Trx/ click to copy: \n\nTKUpVDG5DqLDUSg3X1hhidRPuhm1GmqZ2G" , cursor="hand2")
        trx.pack(fill=tk.X,pady=5)
        trx.bind("<Button-1>" ,copy_donate)

        label_about2=ttk.Label(root_about,style="Costum.TLabel", text="Created by Arshiacomplus")
        label_about2.pack(side=tk.BOTTOM,fill=tk.X)

        



        root_about.mainloop()



    def Setting():
        def sumbit_f():
            Cpu_speed=''
            Do_you_save=''
        
            main_frame1.place(x=rootmainactivity.winfo_screenwidth(), y=0)
            for i in range(0, rootmainactivity.winfo_screenwidth(), 10): 
                slide_frame.place(x=i, y=0)
            if checkbox_var.get() ==1:
                Cpu_speed= "2\n"
            else:
                Cpu_speed= "1\n"

            with open("warp_setting" , "r") as f:
                warp=f.readlines()
 

            with open("warp_setting" , "w") as f:
          
                warp[0]=Cpu_speed
                print(warp)
                for i in warp:
                    f.write(str(i))

            if checkbox_var2.get() ==1:
                Do_you_save= "2\n"
            if checkbox_var2.get() ==0:
                Do_you_save= "1\n"

            with open("warp_setting" , "r") as f:
                warp1=f.readlines()
            with open("warp_setting" , "w") as f:
                warp1[1]=Do_you_save
                for i in warp1:
                    f.write(i)


            if checkbox_var3.get() ==1:
                wich_p= "2\n"
            elif checkbox_var3.get() ==0:
                wich_p= "1\n"
            else:
                wich_p="3\n"

            with open("warp_setting" , "r") as f:
                warp11=f.readlines()
            with open("warp_setting" , "w") as f:
                warp11[2]=wich_p
                for i in warp11:
                    f.write(i)
            if checkbox_var4.get() ==1:
                api= "2\n"
            if checkbox_var4.get() ==0:
                api= "1\n"

            with open("warp_setting" , "r") as f:
                warp1=f.readlines()
            with open("warp_setting" , "w") as f:
                warp1[3]=api
                for i in warp1:
                    f.write(i)



            rootmainactivity.update()
            
             
        menu_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0)
        main_frame1 = tk.Frame(rootmainactivity, bg="lightblue", bd=5)
        main_frame1.pack(side="right", fill="both", expand=False)

        # --- Create the Slide Frame (Initially Hidden) ---

        slide_frame = tk.Frame(rootmainactivity, bg="gray", bd=5)
        slide_frame.pack(side="right", fill="y", expand=False)
        slide_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0, width=150, height=rootmainactivity.winfo_screenheight())

        spu_label=ttk.Label(slide_frame,style="C.TLabel",text="Scan  speed")
        spu_label.pack(fill=tk.X)
        style=ttk.Style()
        style.configure("TCheckbutton",
                        indicatorcolor="blue",
                        indicatorsize=5,
                        padding=5)
        checkbox_var = tk.IntVar()
        with open("warp_setting" , "r") as f:
            num=f.readline()

        if  num[0] =="2":
                checkbox_var = tk.IntVar(value=1)
        elif  num[0] =="1":
                checkbox_var = tk.IntVar(value=0)

        style2=ttk.Style()
        style2.configure("C.TLabel",
                        foreground="darkgreen")
        checkbox_var = tk.IntVar()
        print(checkbox_var.get())
        checkbox1 = ttk.Checkbutton(slide_frame, text="Faster", variable=checkbox_var, onvalue=1, offvalue=0)
        checkbox1.pack(ipady=5,fill=tk.X)
        checkbox1.bind("<Enter>", hand2)

        checkbox2 = ttk.Checkbutton(slide_frame, text="Slower", variable=checkbox_var, onvalue=0, offvalue=0)
        checkbox2.pack(ipady=5,fill=tk.X)
        checkbox2.bind("<Enter>", hand2)


        save_ch=ttk.Label(slide_frame,style="C.TLabel",text="Save result")
        save_ch.pack(fill=tk.X)

        with open("warp_setting" , "r") as f:
            num=f.readlines()
            if  num[1] =="2\n":
                checkbox_var2 = tk.IntVar(value=1)
            else:
                checkbox_var2 = tk.IntVar(value=0)

        checkbox3 = ttk.Checkbutton(slide_frame, text="Yes", variable=checkbox_var2, onvalue=1, offvalue=0)
        checkbox3.pack(ipady=5,fill=tk.X)
        checkbox3.bind("<Enter>", hand2)

        checkbox4 = ttk.Checkbutton(slide_frame, text="No", variable=checkbox_var2, onvalue=0, offvalue=0)
        checkbox4.pack(ipady=5,fill=tk.X)
        checkbox4.bind("<Enter>", hand2)

        which_panel=ttk.Label(slide_frame,style="C.TLabel",text="Which panel" )
        which_panel.pack(fill=tk.X)
        checkbox_var3=tk.IntVar()
        with open("warp_setting" , "r") as f:
            num=f.readlines()
            print(num[2], "hhh")
    
            if  num[2] =="2\n":
                    checkbox_var3 = tk.IntVar(value=1)
            elif num[2] =="1\n":
                    checkbox_var3 = tk.IntVar(value=0)
            else:
                    checkbox_var3 = tk.IntVar(value=2)
            

        checkbox5 = ttk.Checkbutton(slide_frame, text="bpb", variable=checkbox_var3, onvalue=1, offvalue=0)
        checkbox5.pack(ipady=5,fill=tk.X)
        checkbox5.bind("<Enter>", hand2)

        checkbox6 = ttk.Checkbutton(slide_frame, text="vahid", variable=checkbox_var3, onvalue=0, offvalue=0)
        checkbox6.pack(ipady=5,fill=tk.X)
        checkbox6.bind("<Enter>", hand2)

        checkbox7 = ttk.Checkbutton(slide_frame, text="with score", variable=checkbox_var3, onvalue=2, offvalue=0)
        checkbox7.pack(ipady=5,fill=tk.X)
        checkbox7.bind("<Enter>", hand2)

        Wh_api=ttk.Label(slide_frame,style="C.TLabel",text="Which api")
        Wh_api.pack(fill=tk.X)
        checkbox_var4 = tk.IntVar()
        with open("warp_setting" , "r") as f:
            num33=f.readlines()

        if  num33[3] =="2\n":
                checkbox_var4 = tk.IntVar(value=1)
        elif  num33[3] =="1\n":
                checkbox_var4 = tk.IntVar(value=0)

            
  
        checkbox8 = ttk.Checkbutton(slide_frame, text="api 1/not work", variable=checkbox_var4, onvalue=1, offvalue=0)
        checkbox8.pack(ipady=5,fill=tk.X)
        checkbox8.bind("<Enter>", hand2)

        checkbox9 = ttk.Checkbutton(slide_frame, text="api 2", variable=checkbox_var4, onvalue=0, offvalue=0)
        checkbox9.pack(ipady=5,fill=tk.X)
        checkbox9.bind("<Enter>", hand2)


        submit=ttk.Button(slide_frame, text="save", command=sumbit_f)
        submit.pack(pady=5,ipady=5,fill=tk.X)
        submit.bind("<Enter>", hand2)

     
        
        for i in range(300, rootmainactivity.winfo_width()  - slide_frame.winfo_width()-150):
                    slide_frame.place(x=i, y=0)
                    rootmainactivity.update() 
                    time.sleep(0.00001) 

    def check_up():
            def Github_link():
                webbrowser.open_new(r"https://github.com/arshiacomplus/WarpScanner/releases")
            ret=Check_for_update()
            rootupdate=tk.Tk()
            rootupdate.title("Update")
            rootupdate.geometry("500x250")
            rootupdate.geometry("+200+100")

            style2=ttk.Style(rootupdate)
            style2.configure("Costum.TLabel",
                            foreground="#3d7e7d",
                            background="#ffffff",
                            highlightthickness=20,
                            highlightbackground="lightblue",
                            padding=5,
                            highlightcolor="lightblue",
                            relief="groove",
                            font=("Helvetica", 10, "bold"),
                            anchor="center",
                            justify="center")
    
            style3=ttk.Style(rootupdate)
            style3.configure("Costumpp.TLabel",
                            font=("Helvetica", 10,"bold"),
                            anchor="center",
                            justify="center",
                            padding=5,
                            foreground="lightblue",
                            background="#ffffff",
                            highlightthickness=20,
                            highlightbackground="lightblue")
                
            style = ttk.Style(rootupdate)
            style.configure("TButton",
                    
                                foreground="#3d7e7d",
                                background="lightblue",
                                highlightthickness=20,
                                highlightbackground="lightblue",
                                highlightcolor="lightblue",
                                relief="groove",
                                padding=5,
                                borderwidth=0,
                                bordercolor="lightblue",
                                font=("Helvetica", 12, "bold"),
                                anchor="center",
                                justify="center")
            rootupdate.withdraw()
            if ret[0]  == True:
                rootupdate.deiconify()



                label_up=ttk.Label(rootupdate,style="Costum.TLabel" ,text=f"New version Available {ret[1]}")
                label_up.pack(fill=tk.X)

                button_up=ttk.Button(rootupdate, text="click to update",command=Github_link)
                button_up.pack(fill=tk.X,side=tk.BOTTOM)
                button_up.bind("<Enter>", hand2)

                rootupdate.mainloop()

            else:

                rootupdate.deiconify()

                label_up=ttk.Label(rootupdate,style="Costum.TLabel", text="You have new version\n\nV0.3.0:\nGood news:\n\nNew Api Added\n\nBetter style\n\nBad news:\n\nApi zeroteam Deleted  ")
                label_up.pack(fill=tk.X)

                button_up=ttk.Button(rootupdate, text="Close" , command=rootupdate.destroy)
                button_up.pack(fill=tk.X,side=tk.BOTTOM)
                button_up.bind("<Enter>", hand2)

                rootupdate.mainloop()



        
                 
        





  






#     labelmain=tk.Label(rootmainactivity, width=50, padx=50,pady=10, fg="blue" ,text="""Hello This is my Scanner
# created by Telegram= @arshiacomplus\n""")
#     labelmain.pack()





    menu_frame = tk.Frame(rootmainactivity, bg="gray")
    menu_frame.pack(side="right", fill="y")
    menu_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0, width=150, height=rootmainactivity.winfo_screenheight())


    style = ttk.Style()
    style.configure("TButton",
         
                    foreground="#3d7e7d",
                    background="lightblue",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    highlightcolor="lightblue",
                    relief="groove",
                   
                    borderwidth=0,
                    bordercolor="lightblue",
                    font=("Helvetica", 12, "bold"),
                    anchor="center",
                    justify="center")
    
     
     
    label_pro=tk.Label(menu_frame, image=menu_image)
    label_pro.pack(pady=50)
    label_pro.config(cursor="pirate")
  
    Setting_button = ttk.Button(menu_frame,text="Setting", command=Setting)
    Setting_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    Setting_button.bind("<Enter>", hand2)


    up_button = ttk.Button(menu_frame, text="Check for update", command=check_up)
    up_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    up_button.bind("<Enter>", hand2)

    About_button = ttk.Button(menu_frame, text="About", command=About)
    About_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    About_button.bind("<Enter>", hand2)

    exit_button = ttk.Button(menu_frame, text="Exit", command=rootmainactivity.quit)
    exit_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    exit_button.bind("<Enter>", hand2)

    label_arshia= ttk.Label(menu_frame, text="Created by arshiacomplus \n                   v0.3.0", foreground="white", background="gray")
    label_arshia.pack(pady=5,ipady=5,fill=tk.BOTH)


    toggle_menu_button = ttk.Button(rootmainactivity,padding=5, text="Menu", command=lambda: toggle_menu())
    toggle_menu_button.pack(side="right", anchor="ne", padx=1, ipadx=17,pady=1)




    def check_ip6_again(event):
        label_ipv4.config(text=f"ipv4 : Checking ...")
        label_ipv6.config(text=f"ipv6 : Checking ...")
        rootmainactivity.update()
        time.sleep(2.5)

        check=  check_ipv6()
        if  check[0] == "Available":
            color1="green"
        else:
            color1="red"
        if  check[1] == "Available":
            color2="green"
        else:
            color2="red"

        label_ipv4.config(text=f"ipv4 : {check[0]}")
        label_ipv4.configure(fg=color1)
        label_ipv6.config(text=f"ipv6 : {check[1]}")
        label_ipv6.configure(fg=color2)
        rootmainactivity.update()


    style3 = ttk.Style(rootmainactivity)
    style3.configure("ip.TLabel",
                    foreground="blue",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    highlightcolor="lightblue",
                    relief="groove",
                    padding=5,
                    borderwidth=2,
                    bordercolor="lightblue",
                    font=("Helvetica", 10),
                    anchor="center",
                    justify="center")
    if  check[0] == "Available":
        color1="green"
    else:
        color1="red"
    if  check[1] == "Available":
        color2="green"
    else:
        color2="red"
 
    label_ipv4=tk.Label(rootmainactivity, text=f"ipv4 : {check[0]}"  ,fg=color1)
    label_ipv4.pack(side="top", anchor="nw")


    label_ipv6=tk.Label(rootmainactivity, text=f"ipv6 : {check[1]}",fg=color2)
    label_ipv6.pack(side="top",anchor="nw")


    
    ch_ag=ttk.Label(rootmainactivity,style="ip.TLabel",text="Check again")
    ch_ag.pack(pady=3,side="top",anchor="nw")
    ch_ag.bind("<Button-1>" ,check_ip6_again)
        
    

    button = ttk.Button(rootmainactivity,width=25, text="scan ip", command=main)
    button.pack(ipady=5,pady=10)


    button.bind("<Enter>", hand2)

    button1 = ttk.Button(rootmainactivity,width=25, text="wireguard config", command=wireguard_config_ok)
    button1.pack(ipady=5,pady=10)
    button1.bind("<Enter>", hand2)

    button2 = ttk.Button(rootmainactivity, width=25, text="config without ip scan", command=wireguard_config_without)
    button2.pack(ipady=5,pady=10)

    button2.bind("<Enter>", hand2)


    button3 = ttk.Button(rootmainactivity, width=25,text="wireguard with a sub link", command=wireguard_config_sub)
    button3.pack(ipady=5,pady=10)
    button3.bind("<Enter>", hand2)

    
    button4 = ttk.Button(rootmainactivity,width=25,  text="wireguard for v2rayN Pro", command=v2ray)
    button4.pack(ipady=5,pady=10)
    button4.bind("<Enter>", hand2)

    button5 = ttk.Button(rootmainactivity,width=25,  text="v2rayN Pro without ip scan", command=v2ray_without)
    button5.pack(ipady=5,pady=10)
    button5.bind("<Enter>", hand2)

    # button = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="WoW for v2ray or mahsaNG", command=which_Vip,fg="#f0f0f0", bg="#414141")
    # button.pack()

    # button = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="WoW for v2ray or mahsaNG in sub link", command=which_Vip,fg="#f0f0f0", bg="#414141")
    # button.pack()

    # button = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="get wireguard.conf", command=which_Vip,fg="#f0f0f0", bg="#414141")
    # button.pack()


    # button = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="info", command=which_Vip,fg="#f0f0f0", bg="#414141")
    # button.pack()

 
    rootmainactivity.mainloop()

if __name__ == "__main__":
    
    mainactivity()
