try:
    import tkinter as tk
    from tkinter import ttk,messagebox
    from tkinter import *
    from PIL import Image, ImageTk
    import os
    import ctypes
    import sys
    # import sys
    import base64
    # from playsound import playsound
    # import tksvg
    # from tksvg import *
    import urllib.request
    import urllib.parse
    from urllib.parse import quote
    from requests.exceptions import RequestException
    
    import winreg as reg

    import requests
    
    import pyperclip
    import logging
    import re
    import gc

    # import socket
    from concurrent.futures import ThreadPoolExecutor, wait
    import multiprocessing
    import threading
    import time
    from typing import List, Dict, Any, Optional, Union
    from dataclasses import dataclass, field
    from json import JSONEncoder
    import webbrowser
 
    from retrying import retry
    from requests.exceptions import ConnectionError

    import random
    # import subprocess
    import json
    # import sys
 
    from icmplib import ping as pinging
    
    import datetime
    import customtkinter as ctk
    try:
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
    

    except Exception:
        root_crypto=ctk.CTk()
        root_crypto.protocol("WM_TAKE_FOCUS")


        label_up=ctk.CTkLabel(root_crypto ,text=f"Something went Wrong with cryptography\n\n You can just sacn IP")
        label_up.pack(fill=tk.X)
        root_crypto.mainloop()
    import subprocess
    
    
 
 
except Exception as E:
    messagebox.showerror("Error", f"An error has occurred!: \n {E}")
logging.basicConfig(
    filename='xray/error_log.txt',  
    level=logging.ERROR,       
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def log_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt): 
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = log_exception

if not os.path.exists("fragment_set"):
    with open("fragment_set","w") as f:
        f.writelines(["tlshello\n","10-30\n","1-5\n","false\n","cloudflare.com\n","false\n","8\n","true"])
if not os.path.exists("warp_setting") :
    
    with open("warp_setting", "w") as f:
            f.write("1\n")
            f.write("2\n")
            f.write("2\n")
            f.write("1\n")
            f.write("1\n")
            f.write("2\n")
            f.write("5\n")
            f.write("300\n")
            f.write("1\n")
            f.write("1\n")
            f.write("1\n")
            f.write("2\n")
            f.write("2\n")
            f.write("2\n")
if not os.path.exists("xray/sub_files_name"):
    with open("xray/sub_files_name", "w") as f:
        f.write("user_confs\n")
with open("warp_setting" , "r") as f:
    warp=f.readlines()
print(warp[11])

if warp[11]=="2\n":
    ctk.set_appearance_mode("system")
elif warp[11]=="1\n":
    ctk.set_appearance_mode("dark")
else:
    ctk.set_appearance_mode("light")
    


wire_config_temp=''
wire_c=0
wire_p=0
send_msg_wait=0
results = []
sorted_results=[]
save_result=[]
save_result1=[]
best_result=[]
temp_conf=[]
WoW_v2=''
isIran=''
check="none"
temp_green_txtb=""
temp_gray_txtb=""
confss=""
sub_org=""
stoped_loop=False
wch_sel=0
count=0
on_is_green=False
is_editing=False
last_list=""
frams_in_show=[]
frams_in_ping=[]

max_workers_number=0
Cpu_speed=""
if warp[0]=="1":
    
    Cpu_speed="2"
else:
    Cpu_speed="1"
best_ip = 0
do_you_save=""
best_result_avg=""
myscannerconf=False
i_ip_scan=False
is_sub=False
is_v2ray=False
ty=False
ty2=False
check=""
concted=False

ping_range_see=int(warp[7])
header={
    "outbounds": 
        []
}
header2={
    "outbounds": 
        []
}
header_temp={
    "outbounds": 
        []
}



temp_sing_old={
  "outbounds": 
  [

    {
    "type": "wireguard",
    "tag": "",
    "local_address": [
        "172.16.0.2/32",
        ""
    ],
    "private_key": "0",
    "peer_public_key": "0",
    "server": "0",
    "server_port": 0,
    "reserved": 0,

    "mtu": 1280
    },
    {
    "type": "wireguard",
    "tag": "",
    "detour": "",
    "local_address": [
        "172.16.0.2/32",
        "0"
    ],
    "private_key": "0",
    "server": "0",
    "server_port": 0,
    "peer_public_key": "0",
    "reserved": 0,
    "mtu": 1330
 
    }
  ]
}
temp_sing_new={
  "outbounds": 
  [

    {
    "type": "wireguard",
    "tag": "",
    "local_address": [
        "172.16.0.2/32",
        ""
    ],
    "private_key": "0",
    "peer_public_key": "0",
    "server": "0",
    "server_port": 0,
    "reserved": 0,

    "mtu": 1280,
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"
    },
    {
    "type": "wireguard",
    "tag": "",
    "detour": "",
    "local_address": [
        "172.16.0.2/32",
        "0"
    ],
    "private_key": "0",
    "server": "0",
    "server_port": 0,
    "peer_public_key": "0",
    "reserved": 0,
    "mtu": 1330,
    "fake_packets_mode":"m4"
 
    }
  ]
}


try:
    os.makedirs("imgs")
except Exception:
    pass


def hand2(event):
    event.widget.configure(cursor="hand2")
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
def what_ip():
    




        
    def get_ip_details(ip_address):
        
   
        def file_o():
                    try:
                        response = requests.get(f'http://ip-api.com/json/{ip_address}',timeout=10)
                    except Exception:
                        return {'countryCode':'Non'}
                    return response.json()
                
        data = file_o()
        
        data=data['countryCode']
        
        return data


    
    try:
        ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php',timeout=15)
        ipv6=ipv6.content.decode("utf-8")
        
    except Exception:
        ipv6 = "Unavailable"
    try:
        ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php',timeout=15)
        ipv4=ipv4.content.decode("utf-8")

        
    except Exception:
        ipv4 = "Unavailable"
    if ipv4!= "Unavailable":
       
        c_ipv4= get_ip_details(ipv4)
    else:
        c_ipv4="Unavailable"

    if ipv6!= "Unavailable":
        c_ipv6= get_ip_details(ipv6)
    else:
        c_ipv6="Unavailable"

       

    return  [c_ipv4,c_ipv6]
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

    if output=="""v0.4.4
""":
        return [False, output]
    else:
        return [True, output]
def check_up():
    def go():
       
        ret = Check_for_update()
        rootupdate1 = ctk.CTk()
        rootupdate1.protocol("WM_TAKE_FOCUS")
        rootupdate1.title("Update")
    # rootupdate1.protocol("WM_DELETE_WINDOW", rootupdate1.quit)
        rootupdate1.geometry("500x250")
        rootupdate1.geometry("+200+100")
        print(ret)
        if ret[0] == True:
            label_up2 = ctk.CTkLabel(rootupdate1 ,font=("Helvetica", 12, "bold"),text=f"New version Available {ret[1]}")
            label_up2.pack(fill=tk.X)
            button_up = ctk.CTkButton(rootupdate1,font=("Helvetica", 12,"bold"), text="Click to update", command=Github_link)
            button_up.pack(fill=tk.X, side=tk.BOTTOM)
            rootupdate1.mainloop()
        else:
            rootupdate1.destroy()
       
  
        

    def go_thread():
        thread = threading.Thread(target=go)
        thread.start()

    def Github_link():
        webbrowser.open_new(r"https://github.com/arshiacomplus/WarpScanner/releases")
    go_thread()
    

    




    
def start():
    global check
    t=0
    for _  in range(4):
        if t==0.0:
              sp_label.configure(text="start ...")
              root_splash.update()
        elif t==0.2:
              pass

  

        elif t==0.4:
            sp_label.configure(text="checking setting...")
            root_splash.update()
            


            if not os.path.exists("warp_setting") :
                sp_label.configure(text="Creating WarpSetting ...")
                root_splash.update()
                with open("warp_setting", "w") as f:
                        f.write("1\n")
                        f.write("2\n")
                        f.write("2\n")
                        f.write("1\n")
                        f.write("1\n")
                        f.write("2\n")
                        f.write("5\n")
                        f.write("300\n")
                        f.write("1\n")
                        f.write("2\n")
                        f.write("1\n")
                        f.write("2\n")
                        f.write("2\n")
                        f.write("2\n")

            with open("warp_setting", "r") as fsg:
                if len(fsg.readlines())!=14:
                    with open("warp_setting", "w") as f:
                            f.write("1\n")
                            f.write("2\n")
                            f.write("2\n")
                            f.write("1\n")
                            f.write("1\n")
                            f.write("2\n")
                            f.write("5\n")
                            f.write("300\n")
                            f.write("1\n")
                            f.write("2\n")
                            f.write("1\n")
                            f.write("2\n")
                            f.write("2\n")
                            f.write("2\n")

            try:
                with open("result.txt", "r") as f:
                    f.close()

            except Exception:
                sp_label.configure(text="Creating result.txt ...")
                root_splash.update()
                with open("result.txt", "w") as f:
                        f.write('')
        elif t<=0.7:
            sp_label.configure(text="check for update ...")
            thread=threading.Thread(target=check_up)
            thread.start()
            
  
   
             

        t+=0.2
        print(t)
        progress.set( t)
        
        root_splash.update_idletasks()
        time.sleep(1)
        
    root_splash.destroy()
try:

    root_splash=tk.Tk()
    root_splash.title("splash")
    root_splash.resizable(False,False)
    root_splash.geometry("500x500")
    root_splash.geometry("+200+100")

    background_image =ImageTk.PhotoImage(Image.open("imgs/splash.png"))
    background_label = tk.Label(root_splash, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    progress = ctk.CTkProgressBar(root_splash,orientation="horizontal",height=20,fg_color="pink",bg_color="white", mode='determinate')
    progress.pack(ipadx=20,side=tk.BOTTOM,pady=20)
    sp_label=tk.Label(root_splash,text="0%",bg="white")
    sp_label.pack(side=tk.BOTTOM,pady=0)
    root_splash.after(1, start)

    root_splash.mainloop()

    with open("warp_setting" , "r") as f:
                num33=f.readlines()
    interval_see=num33[4]
    interval_see=int(interval_see[:interval_see.index("\n")])

    count_see=num33[5]
    count_see=int(count_see[:count_see.index("\n")])
    timeout_see=num33[6]
    timeout_see=int(timeout_see[:timeout_see.index("\n")])

    ping_range_see=num33[7]
    ping_range_see=int(ping_range_see[:ping_range_see.index("\n")])
except Exception as E:
    messagebox.showerror("Error", f"An error has occurred!: \n {E}")


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
    try:
        r = requests.post(url, data=bodyString, headers=headers)
    except Exception as E:
        return E
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

def generate_wireguard_url(configure, endpoint):

    global api
    
    required_keys = ['PrivateKey', 'PublicKey' ,'Address' ]
    if not all(key in configure and configure[key] is not None for key in required_keys):
        print("Incomplete configuration. Missing one of the required keys or value is None.")
        return None

    
    with open("warp_setting" , "r") as f:
            num33=f.readlines()
    print(num33)

    if  num33[3] =="2\n":
        encoded_addresses = [quote(address1) for address1 in (configure['Address'])]
        address= ','.join(encoded_addresses)
        if num33[9]=="2\n":
           
            wireguard_urll = (
            f"wireguard://{urlencode(configure['PrivateKey'])}@{endpoint}"
            f"?address=172.16.0.2/32,{address}&"
            f"publickey={urlencode(configure['PublicKey'])}"
        )
        
        
            if configure.get('Reserved'):
    
                    wireguard_urll += f"&reserved={urlencode(configure['Reserved'])}"
        else:
            wireguard_urll = ("```configure\n"
        f"wireguard://{urlencode(configure['PrivateKey'])}@{endpoint}"
        f"?wnoise=quic&address=172.16.0.2/32,{address}&keepalive=10&wpayloadsize=1-8&"
        f"publickey={urlencode(configure['PublicKey'])}&wnoisedelay=1-3&wnoisecount=15&mtu=1330"
    )
            if configure.get('Reserved'):
    
                    wireguard_urll += f"&reserved={urlencode(configure['Reserved'])}"
                
        
     
    else:
        listt=configure['Reserved']
        lostt2=''
        for num in range(len(listt)):
            lostt2+=str(listt[num])
            if num != len(listt)-1:
                lostt2+=','
        configure['Reserved']=urlencode(lostt2)

        

        if num33[9]=="2\n":
           
            wireguard_urll = (
            f"wireguard://{urlencode(configure['PrivateKey'])}@{endpoint}"
            f"?address=172.16.0.2/32,{configure['Address']}&"
            f"publickey={urlencode(configure['PublicKey'])}"
        )
        
        
            if configure.get('Reserved'):
    
                    wireguard_urll += f"&reserved={configure['Reserved']}"
        else:
            wireguard_urll = (
        f"wireguard://{urlencode(configure['PrivateKey'])}@{endpoint}"
        f"?wnoise=quic&address=172.16.0.2/32,{configure['Address']}&keepalive=10&wpayloadsize=1-8&"
        f"publickey={urlencode(configure['PublicKey'])}&wnoisedelay=1-3&wnoisecount=15&mtu=1330"
    )
            if configure.get('Reserved'):
    
                    wireguard_urll += f"&reserved={configure['Reserved']}"
        
    wireguard_urll += "#Tel= @arshiacomplus wire"

    return wireguard_urll



def which_Cpu_speed():
        global Cpu_speed
            


def mainactivity():
    def remove_empty_strings(input_list):
        return [item for item in input_list if item and item != "\n" ]
    
    def clear_widgets(parent:ctk.CTk):
       
                
        for widget in parent.winfo_children():
            widget.destroy()
            rootmainactivity.update_idletasks(
        )
            
       
        return
       
       

    ###########                             config parse                            ###########
    def parse_configs(conifg:str,num=0):
        global is_editing
        DEFAULT_PORT = 443
        DEFAULT_SECURITY = "auto"
        DEFAULT_LEVEL = 8
        DEFAULT_NETWORK = "tcp"
        TLS = "tls"
        REALITY = "reality"
        HTTP = "http"
      
        with open("fragment_set", "r") as f:
            list_freg=f.readlines()
            list_freg=remove_empty_strings(list_freg)
            list_freg=[line.strip() for line in list_freg]
        PACKETS=list_freg[0]
        LENGTH=list_freg[1]
        INTERVAL=list_freg[2]
        if list_freg[3]=="false":
            FAKEHOST_ENABLE=False
        else:
            FAKEHOST_ENABLE=True
            HOST1_DOMAIN=list_freg[4]
            HOST2_DOMAIN=list_freg[4]
        if list_freg[5]=="false":
            MUX_ENABLE=False
        else:
            MUX_ENABLE=True
        CONCURRENCY=int(list_freg[6])
        if list_freg[7]=="false":
            FRAGMENT=False
        else:
            FRAGMENT=True
        
        is_warp=False
        conifg=urllib.parse.unquote(conifg)
        
        


        class V2rayConfig:
            def __init__(self, remarks: Optional[str] = None, stats: Optional[Any] = None, log: 'LogBean' = None,
                        policy: Optional['PolicyBean'] = None, inbounds: List['InboundBean'] = None,
                        outbounds: List['OutboundBean'] = None, dns: 'DnsBean' = None, routing: 'RoutingBean' = None,
                        api: Optional[Any] = None, transport: Optional[Any] = None, reverse: Optional[Any] = None,
                        fakedns: Optional[Any] = None, browserForwarder: Optional[Any] = None,
                        observatory: Optional[Any] = None, burstObservatory: Optional[Any] = None):
                self.remarks = remarks
                self.stats = stats
                self.log = log
                self.policy = policy
                self.inbounds = inbounds if inbounds is not None else None
                self.outbounds = outbounds if outbounds is not None else None
                self.dns = dns
                self.routing = routing
                self.api = api
                self.transport = transport
                self.reverse = reverse
                self.fakedns = fakedns
                self.browserForwarder = browserForwarder
                self.observatory = observatory
                self.burstObservatory = burstObservatory

            class LogBean:
                def __init__(self, access: str, error: str, loglevel: Optional[str] = None, dnsLog: Optional[bool] = None):
                    self.access = access
                    self.error = error
                    self.loglevel = loglevel
                    self.dnsLog = dnsLog

            class InboundBean:
                def __init__(self, tag: str, port: int, protocol: str, listen: Optional[str] = None, settings: Optional[Any] = None,
                            sniffing: Optional['V2rayConfig.InboundBean.SniffingBean'] = None, streamSettings: Optional[Any] = None, allocate: Optional[Any] = None):
                    self.tag = tag
                    self.port = port
                    self.protocol = protocol
                    self.listen = listen
                    self.settings = settings
                    self.sniffing = sniffing
                    self.streamSettings = streamSettings
                    self.allocate = allocate

                class InSettingsBean:
                    def __init__(self, auth: Optional[str] = None, udp: Optional[bool] = None,allowTransparent: Optional[bool] = None, userLevel: Optional[int] = None,
                                address: Optional[str] = None, port: Optional[int] = None, network: Optional[str] = None):
                        self.auth = auth
                        self.udp = udp
                        self.userLevel = userLevel
                        self.address = address
                        self.port = port
                        self.network = network
                        self.allowTransparent=allowTransparent

                class SniffingBean:
                    def __init__(self, enabled: bool, destOverride: List[str], metadataOnly: Optional[bool] = None, routeOnly: Optional[bool] = None):
                        self.enabled = enabled
                        self.destOverride = destOverride
                        self.metadataOnly = metadataOnly
                        self.routeOnly = routeOnly
            @dataclass
            class OutboundBean:
            
                def __init__(self, tag: str = "proxy", protocol: str = "", settings: Optional['V2rayConfig.OutboundBean.OutSettingsBean'] = None, 
                            streamSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean'] = None, proxySettings: Optional[Any] = None,
                            sendThrough: Optional[str] = None, mux: 'V2rayConfig.OutboundBean.MuxBean' = None):
                    self.tag = tag
                    self.protocol = protocol
                    self.settings = settings
                    self.streamSettings = streamSettings
                    self.proxySettings = proxySettings
                    self.sendThrough = sendThrough
                    self.mux = mux if mux is not None else self.MuxBean(False)

                class BeforeFrgSettings:
                    def __init__(self,tag:Optional[str] = None,protocol:Optional[str]="freedom",settings:Optional['V2rayConfig.OutboundBean.OutSettingsBean.FragmentBean']=None,streamSettings:Optional['V2rayConfig.OutboundBean.StreamSettingsBean'] = None) :
                        self.tag=tag
                        self.protocol=protocol
                        self.settings=settings
                        self.streamSettings=streamSettings


                class OutSettingsBean:
                    def __init__(self, vnext: Optional[List['V2rayConfig.OutboundBean.OutSettingsBean.VnextBean']] = None, 
                                fragment: Optional['V2rayConfig.OutboundBean.OutSettingsBean.FragmentBean'] = None, 
                                noises: Optional[List['V2rayConfig.OutboundBean.OutSettingsBean.NoiseBean']] = None,
                                servers: Optional[List['V2rayConfig.OutboundBean.OutSettingsBean.ServersBean']] = None, 
                                response: Optional['V2rayConfig.OutboundBean.OutSettingsBean.Response'] = None, 
                                network: Optional[str] = None, address: Optional[Any] = None, port: Optional[int] = None,
                                domainStrategy: Optional[str] = None, redirect: Optional[str] = None, userLevel: Optional[int] = None,
                                inboundTag: Optional[str] = None, secretKey: Optional[str] = None,
                                peers: Optional[List['V2rayConfig.OutboundBean.OutSettingsBean.WireGuardBean']] = None, 
                                reserved: Optional[List[int]] = None, mtu: Optional[int] = None, obfsPassword: Optional[str] = None,
                                wnoise:Optional[str]=None,wnoisecount:Optional[str]=None,keepAlive:Optional[int]= None,wnoisedelay:Optional[str]=None,wpayloadsize:Optional[str]=None):
                        self.vnext = vnext
                        self.fragment = fragment
                        self.noises = noises
                        self.servers = servers
                        self.response = response
                        self.network = network
                        self.address = address
                        self.port = port
                        self.domainStrategy = domainStrategy
                        self.redirect = redirect
                        self.userLevel = userLevel
                        self.inboundTag = inboundTag
                        self.secretKey = secretKey
                        self.peers = peers
                        self.reserved = reserved
                        self.mtu = mtu
                        self.obfsPassword = obfsPassword
                        self.wnoise=wnoise
                        self.wnoisecount=wnoisecount
                        self.wnoisedelay=wnoisedelay
                        self.wpayloadsize=wpayloadsize
                        self.keepAlive=keepAlive

                    class VnextBean:
                        def __init__(self, address: str = "", port: int = DEFAULT_PORT, users: List['V2rayConfig.OutboundBean.OutSettingsBean.VnextBean.UsersBean'] = None):
                            self.address = address
                            self.port = port
                            self.users = users if users is not None else None

                        class UsersBean:
                            def __init__(self, id: str = "", alterId: Optional[int] = None, security: str = DEFAULT_SECURITY, 
                                        level: int = DEFAULT_LEVEL, encryption: str = "", flow: str = ""):
                                self.id = id
                                self.alterId = alterId
                                self.security = security
                                self.level = level
                                self.encryption = encryption
                                self.flow = flow

                    class FragmentBean:
                        def __init__(self, packets: Optional[str] = PACKETS, length: Optional[str] = LENGTH, interval: Optional[str] = INTERVAL,host1_domain: Optional[str] = None,host2_domain: Optional[str] = None,):
                            self.packets = packets
                            self.length = length
                            self.interval = interval
                            self.host1_domain = host1_domain
                            self.host2_domain = host2_domain

                    class NoiseBean:
                        def __init__(self, type: Optional[str] = None, packet: Optional[str] = None, delay: Optional[str] = None):
                            self.type = type
                            self.packet = packet
                            self.delay = delay

                    class ServersBean:
                        def __init__(self, address: str = "", method: Optional[str] = None, ota: bool = False, 
                                    password: Optional[str] = None, port: int = DEFAULT_PORT, level: int = DEFAULT_LEVEL,
                                    email: Optional[str] = None, flow: Optional[str] = None, ivCheck: Optional[bool] = None,
                                    users: Optional[List['V2rayConfig.OutboundBean.OutSettingsBean.ServersBean.SocksUsersBean']] = None):
                            self.address = address
                            self.method = method if users is  None else "chacha20-poly1305"
                            self.ota = ota
                            self.password = password
                            self.port = port
                            self.level = level
                            self.email = email
                            self.flow = flow
                            self.ivCheck = ivCheck
                            self.users = users if users is not None else None

                        class SocksUsersBean:
                            def __init__(self, user: str = "", passw: str = "", level: int = DEFAULT_LEVEL):
                                self.user = user
                                self.passw = passw
                                self.level = level

                    class Response:
                        def __init__(self, type: str):
                            self.type = type

                    class WireGuardBean:
                        def __init__(self, keepAlvie:int=None,publicKey: str = "", endpoint: str = ""):
                            self.publicKey = publicKey
                            self.endpoint = endpoint
                            self.keepAlvie=keepAlvie

                class StreamSettingsBean:
                    
                    def __init__(self, network: str = DEFAULT_NETWORK, security: str = "", tcpSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.TcpSettingsBean'] = None,
                                kcpSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.KcpSettingsBean'] = None, 
                                wsSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.WsSettingsBean'] = None, 
                                httpupgradeSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.HttpupgradeSettingsBean'] = None, 
                                splithttpSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.SplithttpSettingsBean'] = None, 
                                httpSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.HttpSettingsBean'] = None, 
                                tlsSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.TlsSettingsBean'] = None, 
                                quicSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.QuicSettingBean'] = None, 
                                realitySettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.TlsSettingsBean'] = None, 
                                grpcSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.GrpcSettingsBean'] = None, 
                                hy2steriaSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.Hy2steriaSettingsBean'] = None, 
                                dsSettings: Optional[Any] = None, sockopt: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.SockoptBean'] = None):
                        self.network = network
                        self.security = security
                        self.tcpSettings = tcpSettings
                        self.kcpSettings = kcpSettings
                        self.wsSettings = wsSettings
                        self.httpupgradeSettings = httpupgradeSettings
                        self.splithttpSettings = splithttpSettings
                        self.httpSettings = httpSettings
                        self.tlsSettings = tlsSettings
                        self.quicSettings = quicSettings
                        self.realitySettings = realitySettings
                        self.grpcSettings = grpcSettings
                        self.hy2steriaSettings = hy2steriaSettings
                        self.dsSettings = dsSettings
                        self.sockopt = sockopt

                    # ... (Nested classes for TcpSettingsBean, KcpSettingsBean, etc.  -  See below for these) ...

                    def populateTransportSettings(self, transport: str, headerType: Optional[str], host: Optional[str], path: Optional[str], seed: Optional[str],
                                                quicSecurity: Optional[str], key: Optional[str], mode: Optional[str], serviceName: Optional[str],
                                                authority: Optional[str]) -> str:
                        sni = ""
                        self.network = transport
                        # ... (Implementation for transport settings - see below)
                        return sni
            
                    def populateTlsSettings(self, streamSecurity: str, allowInsecure: bool, sni: str, fingerprint: Optional[str], alpns: Optional[str],
                                        publicKey: Optional[str], shortId: Optional[str], spiderX: Optional[str]):
                        self.security = streamSecurity
                        # ... (Implementation for TLS settings - see below)


                class MuxBean:
                    def __init__(self, enabled: bool, concurrency: int = 8, xudpConcurrency: int = None, xudpProxyUDP443: str = None):
                        self.enabled = enabled
                        self.concurrency = concurrency
                        self.xudpConcurrency = xudpConcurrency
                        self.xudpProxyUDP443 = xudpProxyUDP443


                class HeadersBean:
                    def __init__(self, Host: Optional[str] = None, userAgent: Optional[str] = None,
                                acceptEncoding: Optional[str] = None, Connection: Optional[str] = None,
                                Pragma: Optional[str] = None, Host_single: str = ""):  #Added Host_single for WsSettingsBean compatibility
                        self.Host = Host if Host is not None else None
                        self.userAgent = userAgent if userAgent is not None else None
                        self.acceptEncoding = acceptEncoding if acceptEncoding is not None else None
                        self.Connection = Connection if Connection is not None else None
                        self.Pragma = Pragma
                        self.Host_single = Host_single


                class RequestBean:
                    def __init__(self, path: List[str] = None, headers:Optional['V2rayConfig.OutboundBean.HeadersBean'] = None, version: Optional[str] = None,
                                method: Optional[str] = None):
                        self.path = path if path is not None else None
                        self.headers = headers if headers is not None else V2rayConfig.OutboundBean.HeadersBean()
                        self.version = version
                        self.method = method
                        
                    

                class HeaderBean:
                    def __init__(self, type: str = "none", request:Optional['V2rayConfig.OutboundBean.RequestBean'] = None, response: Any = None):
                        self.type = type
                        self.request = request
                        self.response = response


                class TcpSettingsBean:
                    def __init__(self, header: Optional['V2rayConfig.OutboundBean.HeaderBean'] = None, acceptProxyProtocol: Optional[bool] = None):
                        self.header = header if header is not None else V2rayConfig.OutboundBean.HeaderBean()
                        self.acceptProxyProtocol = acceptProxyProtocol


                class KcpSettingsBean:
                    def __init__(self, mtu: int = 1350, tti: int = 50, uplinkCapacity: int = 12, downlinkCapacity: int = 100,
                                congestion: bool = False, readBufferSize: int = 1, writeBufferSize: int = 1,
                                header: Optional['V2rayConfig.OutboundBean.HeaderBean'] = None, seed: Optional[str] = None):
                        self.mtu = mtu
                        self.tti = tti
                        self.uplinkCapacity = uplinkCapacity
                        self.downlinkCapacity = downlinkCapacity
                        self.congestion = congestion
                        self.readBufferSize = readBufferSize
                        self.writeBufferSize = writeBufferSize
                        self.header = header if header is not None else V2rayConfig.OutboundBean.HeaderBean(type="none")
                        self.seed = seed


                class WsSettingsBean:
                    def __init__(self, path: str = "", headers: Optional['V2rayConfig.OutboundBean.HeadersBean'] = None, maxEarlyData: Optional[int] = None,
                                useBrowserForwarding: Optional[bool] = None, acceptProxyProtocol: Optional[bool] = None):
                        self.path = path
                        self.headers = headers if headers is not None else V2rayConfig.OutboundBean.HeadersBean(Host_single="")
                        self.maxEarlyData = maxEarlyData
                        self.useBrowserForwarding = useBrowserForwarding
                        self.acceptProxyProtocol = acceptProxyProtocol


                class HttpupgradeSettingsBean:
                    def __init__(self, path: str = "", host: str = "", acceptProxyProtocol: Optional[bool] = None):
                        self.path = path
                        self.host = host
                        self.acceptProxyProtocol = acceptProxyProtocol


                class SplithttpSettingsBean:
                    def __init__(self, path: str = "", host: str = "", maxUploadSize: Optional[int] = None,
                                maxConcurrentUploads: Optional[int] = None):
                        self.path = path
                        self.host = host
                        self.maxUploadSize = maxUploadSize
                        self.maxConcurrentUploads = maxConcurrentUploads


                class HttpSettingsBean:
                    def __init__(self, host: List[str] = None, path: str = ""):
                        self.host = host if host is not None else None
                        self.path = path


                class SockoptBean:
                    def __init__(self, TcpNoDelay: Optional[bool] = None, tcpKeepAliveIdle: Optional[int] = None,
                                tcpFastOpen: Optional[bool] = None, tproxy: Optional[str] = None, mark: Optional[int] = None,
                                dialerProxy: Optional[str] = None):
                        self.TcpNoDelay = TcpNoDelay
                        self.tcpKeepAliveIdle = tcpKeepAliveIdle
                        self.tcpFastOpen = tcpFastOpen
                        self.tproxy = tproxy
                        self.mark = mark
                        self.dialerProxy = dialerProxy


                class TlsSettingsBean:
                    def __init__(self, allowInsecure: bool = False, serverName: str = "", alpn: Optional[List[str]] = None,
                                minVersion: Optional[str] = None, maxVersion: Optional[str] = None,
                                preferServerCipherSuites: Optional[bool] = None, cipherSuites: Optional[str] = None,
                                fingerprint: Optional[str] = None, certificates: Optional[List[Any]] = None,
                                disableSystemRoot: Optional[bool] = None, enableSessionResumption: Optional[bool] = None,
                                show: bool = False, publicKey: Optional[str] = None, shortId: Optional[str] = None,
                                spiderX: Optional[str] = None):
                        self.allowInsecure = allowInsecure
                        self.serverName = serverName
                        self.alpn = alpn
                        self.minVersion = minVersion
                        self.maxVersion = maxVersion
                        self.preferServerCipherSuites = preferServerCipherSuites
                        self.cipherSuites = cipherSuites
                        self.fingerprint = fingerprint
                        self.certificates = certificates
                        self.disableSystemRoot = disableSystemRoot
                        self.enableSessionResumption = enableSessionResumption
                        self.show = show
                        self.publicKey = publicKey
                        self.shortId = shortId
                        self.spiderX = spiderX


                class QuicSettingBean:
                    def __init__(self, security: str = "none", key: str = "", header: Optional['V2rayConfig.OutboundBean.HeaderBean'] = None):
                        self.security = security
                        self.key = key
                        self.header = header if header is not None else V2rayConfig.OutboundBean.HeaderBean(type="none")


                class GrpcSettingsBean:
                    def __init__(self, serviceName: str = "", authority: Optional[str] = None, multiMode: Optional[bool] = None,
                                idle_timeout: Optional[int] = None, health_check_timeout: Optional[int] = None):
                        self.serviceName = serviceName
                        self.authority = authority
                        self.multiMode = multiMode
                        self.idle_timeout = idle_timeout
                        self.health_check_timeout = health_check_timeout


                class Hy2CongestionBean:
                    def __init__(self, type: Optional[str] = "bbr", up_mbps: Optional[int] = None, down_mbps: Optional[int] = None):
                        self.type = type
                        self.up_mbps = up_mbps
                        self.down_mbps = down_mbps


                class Hy2steriaSettingsBean:
                    def __init__(self, password: Optional[str] = None, use_udp_extension: Optional[bool] = True,
                                congestion: Optional['V2rayConfig.OutboundBean.Hy2CongestionBean'] = None):
                        self.password = password
                        self.use_udp_extension = use_udp_extension
                        self.congestion = congestion


                def split_string_to_list(s: str) -> List[str]:
                    return [item.strip() for item in s.split(',') if item.strip()]


                def populate_transport_settings(transport: str, headerType: Optional[str], host: Optional[str], path: Optional[str],
                                                seed: Optional[str], quicSecurity: Optional[str], key: Optional[str],
                                                mode: Optional[str], serviceName: Optional[str], authority: Optional[str]) -> str:
                    
                    network = transport
                    sni = ""
                    
                    if network == "tcp":
                        tcpSetting = V2rayConfig.OutboundBean.TcpSettingsBean()
                        if headerType == HTTP:
                            tcpSetting.header.type = HTTP
                            if host or path:
                                requestObj = V2rayConfig.OutboundBean.RequestBean()
                                requestObj.headers.Host = V2rayConfig.OutboundBean.split_string_to_list(host or "")
                                requestObj.path = V2rayConfig.OutboundBean.split_string_to_list(path or "")
                                tcpSetting.header.request = requestObj
                                sni = requestObj.headers.Host[0] if requestObj.headers.Host else sni
                        else:
                            tcpSetting.header.type = "none"
                            sni = host or ""
                        tcpSettings = tcpSetting # Assuming tcpSettings is a global variable
                    
                    elif network == "kcp":
                        kcpsetting = V2rayConfig.OutboundBean.KcpSettingsBean()
                        kcpsetting.header.type = headerType or "none"
                        kcpsetting.seed = seed
                        kcpSettings = kcpsetting  # Assuming kcpSettings is a global variable
                    
                    elif network == "ws":
                        wssetting = V2rayConfig.OutboundBean.WsSettingsBean()
                        wssetting.headers.Host_single = host or ""
                        sni = wssetting.headers.Host_single
                        wssetting.path = path or "/"
                        wsSettings = wssetting  # Assuming wsSettings is a global variable

                    elif network == "httpupgrade":
                        httpupgradeSetting = V2rayConfig.OutboundBean.HttpupgradeSettingsBean()
                        httpupgradeSetting.host = host or ""
                        sni = httpupgradeSetting.host
                        httpupgradeSetting.path = path or "/"
                        httpupgradeSettings = httpupgradeSetting # Assuming httpupgradeSettings is a global variable

                    elif network == "splithttp":
                        splithttpSetting = V2rayConfig.OutboundBean.SplithttpSettingsBean()
                        splithttpSetting.host = host or ""
                        sni = splithttpSetting.host
                        splithttpSetting.path = path or "/"
                        splithttpSettings = splithttpSetting # Assuming splithttpSettings is a global variable

                    elif network in ["h2", "http"]:
                        network = "h2"
                        h2Setting = V2rayConfig.OutboundBean.HttpSettingsBean()
                        h2Setting.host = V2rayConfig.OutboundBean.split_string_to_list(host or "")
                        sni = h2Setting.host[0] if h2Setting.host else sni
                        h2Setting.path = path or "/"
                        httpSettings = h2Setting # Assuming httpSettings is a global variable

                    elif network == "quic":
                        quicsetting =V2rayConfig.OutboundBean.QuicSettingBean()
                        quicsetting.security = quicSecurity or "none"
                        quicsetting.key = key or ""
                        quicsetting.header.type = headerType or "none"
                        quicSettings = quicsetting # Assuming quicSettings is a global variable

                    elif network == "grpc":
                        grpcSetting = V2rayConfig.OutboundBean.GrpcSettingsBean()
                        grpcSetting.multiMode = mode == False
                        grpcSetting.serviceName = serviceName or ""
                        grpcSetting.authority = authority or ""
                        grpcSetting.idle_timeout = 60
                        grpcSetting.health_check_timeout = 20
                        sni = authority or ""
                        grpcSettings = grpcSetting # Assuming grpcSettings is a global variable

                    return sni


                def populate_tls_settings(streamSecurity: str, allowInsecure: bool, sni: str, fingerprint: Optional[str],
                                        alpns: Optional[str], publicKey: Optional[str], shortId: Optional[str],
                                        spiderX: Optional[str]):
                    security = streamSecurity
                    tlsSetting = V2rayConfig.OutboundBean.TlsSettingsBean(
                        allowInsecure=allowInsecure,
                        serverName=sni,
                        fingerprint=fingerprint,
                        alpn=V2rayConfig.OutboundBean.split_string_to_list(alpns or "") if alpns else None,
                        publicKey=publicKey,
                        shortId=shortId,
                        spiderX=spiderX
                    )
                    if security == TLS:
                        tlsSettings = tlsSetting # Assuming tlsSettings is a global variable
                        realitySettings = None # Assuming realitySettings is a global variable
                    elif security == REALITY:
                        tlsSettings = None # Assuming tlsSettings is a global variable
                        realitySettings = tlsSetting # Assuming realitySettings is a global variable



            class DnsBean:
                def __init__(self, servers: Optional[List[Any]] = None, hosts: Optional[Dict[str, Any]] = None, 
                            clientIp: Optional[str] = None, disableCache: Optional[bool] = None, 
                            queryStrategy: Optional[str] = None, tag: Optional[str] = None,fakedns:Optional[list]=None):
                    self.servers = servers
                    self.hosts = hosts
                    self.fakedns = fakedns
                    self.clientIp = clientIp
                    self.disableCache = disableCache
                    self.queryStrategy = queryStrategy
                    self.tag = tag
            

                class ServersBean:
                    def __init__(self, address: str = "", port: Optional[int] = None, domains: Optional[List[str]] = None, 
                                expectIPs: Optional[List[str]] = None, clientIp: Optional[str] = None):
                        self.address = address
                        self.port = port
                        self.domains = domains
                        self.expectIPs = expectIPs
                        self.clientIp = clientIp


            class RoutingBean:
                def __init__(self, domainStrategy: str, domainMatcher: Optional[str] = None, 
                            rules: List['V2rayConfig.RoutingBean.RulesBean'] = None, balancers: Optional[List[Any]] = None):
                    self.domainStrategy = domainStrategy
                    self.domainMatcher = domainMatcher
                    self.rules = rules if rules is not None else None
                    self.balancers = balancers

                class RulesBean:
                    def __init__(self, type: str = "field", ip: Optional[List[str]] = None, domain: Optional[List[str]] = None, 
                                outboundTag: str = "", balancerTag: Optional[str] = None, port: Optional[str] = None, 
                                sourcePort: Optional[str] = None, network: Optional[str] = None, source: Optional[List[str]] = None, 
                                user: Optional[List[str]] = None, inboundTag: Optional[List[str]] = None, 
                                protocol: Optional[List[str]] = None, attrs: Optional[str] = None, domainMatcher: Optional[str] = None, enabled: Optional[bool]=None,id:Optional[str]=None):
                        self.type = type
                        self.ip = ip
                        self.id=id
                        self.domain = domain
                        self.outboundTag = outboundTag
                        self.balancerTag = balancerTag
                        self.port = port
                        self.sourcePort = sourcePort
                        self.network = network
                        self.source = source
                        self.user = user
                        self.inboundTag = inboundTag
                        self.protocol = protocol
                        self.attrs = attrs
                        self.domainMatcher = domainMatcher
                        self.enabled=enabled



            class PolicyBean:
                def __init__(self, levels: Dict[str, 'V2rayConfig.PolicyBean.LevelBean'], system: Optional[Any] = None):
                    self.levels = levels
                    self.system = system

                class LevelBean:
                    def __init__(self, handshake: Optional[int] = None, connIdle: Optional[int] = None, 
                                uplinkOnly: Optional[int] = None, downlinkOnly: Optional[int] = None, 
                                statsUserUplink: Optional[bool] = None, statsUserDownlink: Optional[bool] = None, 
                                bufferSize: Optional[int] = None):
                        self.handshake = handshake
                        self.connIdle = connIdle
                        self.uplinkOnly = uplinkOnly
                        self.downlinkOnly = downlinkOnly
                        self.statsUserUplink = statsUserUplink
                        self.statsUserDownlink = statsUserDownlink
                        self.bufferSize = bufferSize


            class FakednsBean:
                def __init__(self, ipPool: str = "198.18.0.0/15", poolSize: int = 10000):
                    self.ipPool = ipPool
                    self.poolSize = poolSize


            #  Simulate the missing 'outbounds' and 'EConfigType' for the function below.  Replace with your actual data.
            outbounds = [] # Replace with your actual outbound list
            class EConfigType: # Replace with your actual EConfigType class/enum
                entries = []


            def getProxyOutbound():
                for outbound in V2rayConfig.outbounds:
                    for it in V2rayConfig.EConfigType.entries:
                        if outbound.protocol.lower() == it.name.lower():  # Case-insensitive comparison
                            return outbound

        
        
            def to_dict(self):
                result = {}
                for key, value in self.__dict__.items():
                    if value is not None:
                        if isinstance(value, list):
                            result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value if item is not None]
                        elif hasattr(value, 'to_dict'):
                            result[key] = value.to_dict()
                        else:
                            result[key] = value
                return result


            def toPrettyPrinting(self) -> str:
                return json.dumps(self.to_dict(), indent=4, cls=MyEncoder)

            def __str__(self):
                return self.toPrettyPrinting()


        class MyEncoder(JSONEncoder):
            def default(self, o):
                if hasattr(o, 'to_dict'):
                    return o.to_dict()
                return o.__dict__

        # Add to_dict to all nested classes (example shown for LogBean)
        class V2rayConfigLogBean:
            def __init__(self, access: str, error: str, loglevel: Optional[str] = None, dnsLog: Optional[bool] = None):
                self.access = access
                self.error = error
                self.loglevel = loglevel
                self.dnsLog = dnsLog
            def to_dict(self):
                result = {}
                for key, value in self.__dict__.items():
                    if value is not None:
                        result[key] = value
                return result

        # You need to add to_dict methods to all the other classes as well (InboundBean, OutboundBean, etc.)

        # Example usage 
        def remove_nulls(data):
            if isinstance(data, dict):
                return {k: remove_nulls(v) for k, v in data.items() if v is not None}
            
            elif isinstance(data, list):
                return [remove_nulls(item) for item in data if item is not None]
            
            elif hasattr(data, '__dict__'):  # Check if it's an object with attributes
                obj_dict = data.__dict__
                cleaned_dict = {k: remove_nulls(v) for k, v in obj_dict.items() if v is not None}
                return cleaned_dict
            
            else:
                return data

        def replace_accept_encoding(d):
            # اگر نوع داده دیکشنری باشد
            if isinstance(d, dict):
                # استفاده از دیکشنری جدید برای ذخیره مقادیر تغییر یافته
                new_dict = {}
                for key, value in d.items():
                    if key == 'acceptEncoding':
                        new_dict['Accept-Encoding'] = value
                    elif key == 'passw':
                        new_dict['pass'] = value
                    
                    else:
                        new_dict[key] = replace_accept_encoding(value)  # بازگشتی برای عناصر تو در تو
                    
                return new_dict
            elif isinstance(d, list):
                # اگر نوع داده لیست باشد
                return [replace_accept_encoding(item) for item in d]
            elif hasattr(d, '__dict__'):  # Check if it's an object with attributes
                    obj_dict = d.__dict__
                    cleaned_dict = {itemk: replace_accept_encoding(itemk) for itemk,itemv in obj_dict.items()}
                    return cleaned_dict
            else:
                return d  # اگر نوع داده چیز دیگری باشد

        # conifg="vless://24f65efb-4885-4e3c-b598-f70336ce8c63@188.245.163.79:1616?encryption=none&flow=xtls-rprx-vision&security=reality&sni=refersion.com&fp=chrome&pbk=uGYj7gkQdNaabDVQZdbHeSVizGPrzj8YD5jdYm7stG0&sid=3a622700e73c6642&type=tcp&headerType=none"
        # conifg="vmess://eyJhZGQiOiIyLjE4OS41OS42IiwiYWlkIjoiMCIsImFscG4iOiIiLCJmcCI6IiIsImhvc3QiOiJvYmRpaS5jZmQiLCJpZCI6IjA1NjQxY2Y1LTU4ZDItNGJhNC1hOWYxLWIzY2RhMGIxZmIxZCIsIm5ldCI6IndzIiwicGF0aCI6Ii9saW5rd3MiLCJwb3J0IjoiNDQzIiwicHMiOiLwn4aUIEBpcmFuZnJlZXNlcnZlcvCfk6EiLCJzY3kiOiJhdXRvIiwic25pIjoib2JkaWkuY2ZkIiwidGxzIjoidGxzIiwidHlwZSI6IiIsInYiOiIyIn0="
        # conifg="trojan://blue2024@104.17.147.167:443?path=%2F%3Fed&security=tls&host=ha.lii2010.us.kg&type=ws&sni=ha.lii2010.us.kg#fa.kurd+haak1211"
        # conifg="ss://YWVzLTI1Ni1nY206TTJReE56UTNaVEV3T0RWbU4yWmlOekZsTUdFeU5Ea3daVE14WWpNMQ==@ir.npvnot.com:10096#IP+UAE+%F0%9F%87%A6%F0%9F%87%AA+50+GB+%40mtpproxy0098"
        # conifg="socks://Og==@ADDRESS:443#REMARKS"
        def delete_sharp(val:str):
                    if val==None:
                        return
                
                    if "#" in val :
                            

                            val=val.split("#")[0]
                            print(val)
                    
                    
                    return val


        if conifg.startswith("vless://") and conifg[0]!="s":
            

            ID=conifg.split("vless://")[1].split("@")[0]
            ID=delete_sharp(ID)
            ADDRESS=conifg.split("vless://")[1].split("@")[1].split(":")[0]
            
            PORT=conifg.split("vless://")[1].split("@")[1].split(":")[1]
            if "/?" in PORT :
                PORT=PORT.split("/?")[0]
            else:
                PORT=PORT.split("?")[0]
            PORT=delete_sharp(PORT)
            

            PORT=int(PORT)
            SECURITY=conifg.split("vless://")[1].split("security=")[1].split("&")[0]
            SECURITY=delete_sharp(SECURITY)
            if SECURITY=="none":
                SECURITY=""
            ALPN=None
            FP=""
            SNI=""

            SPX=""
            PBK=""
            SID=""
            HEADER_TYPE=None
            if SECURITY=="tls":
                
                try:
                    ALPN=conifg.split("vless://")[1].split("alpn=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    FP=conifg.split("vless://")[1].split("fp=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    SNI=conifg.split("vless://")[1].split("sni=")[1].split("&")[0]
                    
                except Exception:
                    pass
                
            elif SECURITY=="reality":
                try:
                    SNI=conifg.split("vless://")[1].split("sni=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    FP=conifg.split("vless://")[1].split("fp=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    ALPN=conifg.split("vless://")[1].split("alpn=")[1].split("&")[0]
            
                except Exception:
                    pass
        
                try:
                    SPX=conifg.split("vless://")[1].split("spx=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    PBK=conifg.split("vless://")[1].split("pbk=")[1].split("&")[0]
                    
                except Exception:
                    pass

                try:
                    SID=conifg.split("vless://")[1].split("sid=")[1].split("&")[0]
                    
                except Exception:
                    pass
                SPX=delete_sharp(SPX)
                PBK=delete_sharp(PBK)
                SID=delete_sharp(SID)
            ALPN=delete_sharp(ALPN)
            FP=delete_sharp(FP)
            SNI=delete_sharp(SNI)


            
                    
                

            ENCRYPTION=conifg.split("vless://")[1].split("encryption=")[1].split("&")[0]
            ENCRYPTION=delete_sharp(ENCRYPTION)
            
            TYPE=conifg.split("type=")[1].split("&")[0]
            TYPE=delete_sharp(TYPE)
            HEADER_TYPE=None
            MODE=None

            if TYPE!="ws" and TYPE!="httpupgrade" and  TYPE!="splithttp" and  TYPE!="h2" and TYPE!="grpc":
                try:
                    HEADER_TYPE=conifg.split("vless://")[1].split("headerType=")[1].split("&")[0]
                    HEADER_TYPE=delete_sharp(HEADER_TYPE)
                except Exception:
                    pass


                
                
            if TYPE=="grpc":
                MODE=conifg.split("vless://")[1].split("mode=")[1].split("&")[0]
                MODE=delete_sharp(MODE)
            
            R_HOST=None
            PATH=None
            if HEADER_TYPE!="none":
                print(HEADER_TYPE)
        
                if TYPE!="kcp" and TYPE!="quic" and TYPE!="grpc":
                    try:
                        R_HOST=conifg.split("vless://")[1].split("host=")[1].split("&")[0]
                    except Exception:
                        pass
                    
                if TYPE=="quic":
                    try:
                        R_HOST=conifg.split("vless://")[1].split("quicSecurity=")[1].split("&")[0]
                    except Exception:
                        pass
                elif TYPE=="grpc":
                    try:
                        R_HOST=conifg.split("vless://")[1].split("authority=")[1].split("&")[0]
                    except:
                        pass
                
                if TYPE!="tcp":
                    try:
                        if TYPE=="kcp":

                            PATH=conifg.split("vless://")[1].split("seed=")[1].split("&")[0]
                        elif TYPE=="ws" or  TYPE=="httpupgrade" or  TYPE=="splithttp" or  TYPE=="h2" :
                            PATH=conifg.split("vless://")[1].split("path=")[1].split("&")[0]
                        elif  TYPE=="quic":
                            PATH=conifg.split("vless://")[1].split("key=")[1].split("&")[0]
                        elif  TYPE=="grpc":
                            PATH=conifg.split("vless://")[1].split("serviceName=")[1].split("&")[0]
                    except Exception:
                        pass
                R_HOST=delete_sharp(R_HOST)
                PATH=delete_sharp(PATH)
            
            try:
                FLOW=conifg.split("vless://")[1].split("flow=")[1].split("&")[0]
            except Exception:
                try:
                    FLOW=conifg.split("vless://")[1].split("flow=")[1].split("#")[0]
                except Exception:
                    FLOW=""
            FLOW=delete_sharp(FLOW)
            try:
                REMARKS=conifg.split("#")[1]
            except Exception:
                REMARKS="None"

            
            list_of_c_type=[

            ID,
            ADDRESS,
            PORT,
            SECURITY,
            ALPN,
            FP,
            SNI,
            SPX,
            PBK,
            SID,
            ENCRYPTION,
            TYPE,
            HEADER_TYPE,
            MODE,
            R_HOST,
            PATH,
            FLOW,
            REMARKS
            ]

           
        elif conifg.startswith("vmess://"):
            
            after_vemss=conifg.split("vmess://")[1].encode('utf-8')
            after_vemss_d=base64.b64decode(after_vemss).decode("utf-8")
            after_vemss_d=json.loads(after_vemss_d)
        
            ADDRESS=after_vemss_d["add"]
            REMARKS=after_vemss_d["ps"]
            PATH=after_vemss_d["path"]
            ALTERID=after_vemss_d["aid"]
            ALPN=None
            FP=""
            SNI=""
            if after_vemss_d["tls"]!="":
                ALPN=after_vemss_d["alpn"]
                FP=after_vemss_d["fp"]
                SNI=after_vemss_d["sni"]
            R_HOST=after_vemss_d["host"]
            ID=after_vemss_d["id"]
            TYPE=after_vemss_d["net"]
            PORT=after_vemss_d["port"]
            if "/?" in PORT :
                PORT=PORT.split("/?")[0]
            else:
                PORT=PORT.split("?")[0]
            PORT=int(PORT)
            SCY=after_vemss_d["scy"]
            SECURITY=after_vemss_d["tls"]
            HEADER_TYPE=None
            if after_vemss_d["net"]!="grpc":
             
                HEADER_TYPE=after_vemss_d["type"]
            else:
                MODE=after_vemss_d["type"]
            V=after_vemss_d["v"]
        elif conifg.startswith("trojan://"):
            PASS=conifg.split("trojan://")[1].split("@")[0]
            PASS=delete_sharp(PASS)
            ID=PASS
            
            ADDRESS=conifg.split("trojan://")[1].split("@")[1].split(":")[0]
            
            PORT=conifg.split("trojan://")[1].split("@")[1].split(":")[1]
            if "/?" in PORT :
                PORT=PORT.split("/?")[0]
            else:
                PORT=PORT.split("?")[0]
            PORT=delete_sharp(PORT)
            PORT=int(PORT)
            SECURITY=conifg.split("trojan://")[1].split("security=")[1].split("&")[0]
            SECURITY=delete_sharp(SECURITY)
            if SECURITY=="none":
                SECURITY=""
            ALPN=None
            FP=""
            SNI=""

            SPX=""
            PBK=""
            SID=""
            HEADER_TYPE=None
            if SECURITY=="tls":
                
                try:
                    ALPN=conifg.split("trojan://")[1].split("alpn=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    FP=conifg.split("trojan://")[1].split("fp=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    SNI=conifg.split("trojan://")[1].split("sni=")[1].split("&")[0]
                    
                except Exception:
                    pass
                
            elif SECURITY=="reality":
                try:
                    SNI=conifg.split("trojan://")[1].split("sni=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    FP=conifg.split("trojan://")[1].split("fp=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    ALPN=conifg.split("trojan://")[1].split("alpn=")[1].split("&")[0]
            
                except Exception:
                    pass
        
                try:
                    SPX=conifg.split("trojan://")[1].split("spx=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    PBK=conifg.split("trojan://")[1].split("pbk=")[1].split("&")[0]
                    
                except Exception:
                    pass

                try:
                    SID=conifg.split("trojan://")[1].split("sid=")[1].split("&")[0]
                    
                except Exception:
                    pass
                SPX=delete_sharp(SPX)
                PBK=delete_sharp(PBK)
                SID=delete_sharp(SID)
            ALPN=delete_sharp(ALPN)
            FP=delete_sharp(FP)
            SNI=delete_sharp(SNI)


            
                    
                

        
            TYPE=conifg.split("type=")[1].split("&")[0]
            TYPE=delete_sharp(TYPE)
            
            MODE=None

            if TYPE!="ws" and TYPE!="httpupgrade" and  TYPE!="splithttp" and  TYPE!="h2":
                try:
                    HEADER_TYPE=conifg.split("trojan://")[1].split("headerType=")[1].split("&")[0]
                    HEADER_TYPE=delete_sharp(HEADER_TYPE)
                except Exception:
                    pass


                
                
            if TYPE=="grpc":
                MODE=conifg.split("trojan://")[1].split("mode=")[1].split("&")[0]
                MODE=delete_sharp(MODE)
                
            
            R_HOST=None
            PATH=None
            if HEADER_TYPE!="none":
                print(HEADER_TYPE)
        
                if TYPE!="kcp" and TYPE!="quic":
                    try:
                        R_HOST=conifg.split("trojan://")[1].split("host=")[1].split("&")[0]
                    except Exception:
                        pass
                    
                if TYPE=="quic":
                    try:
                        R_HOST=conifg.split("trojan://")[1].split("quicSecurity=")[1].split("&")[0]
                    except Exception:
                        pass
                elif TYPE=="grpc":
                    try:
                        R_HOST=conifg.split("trojan://")[1].split("authority=")[1].split("&")[0]
                    except Exception:
                        pass
                if TYPE!="tcp":
                    try:
                        if TYPE=="kcp":

                            PATH=conifg.split("trojan://")[1].split("seed=")[1].split("&")[0]
                        elif TYPE=="ws" or  TYPE=="httpupgrade" or  TYPE=="splithttp" or  TYPE=="h2" :
                            PATH=conifg.split("trojan://")[1].split("path=")[1].split("&")[0]
                        elif  TYPE=="quic":
                            PATH=conifg.split("trojan://")[1].split("key=")[1].split("&")[0]
                        elif  TYPE=="grpc":
                            PATH=conifg.split("trojan://")[1].split("serviceName=")[1].split("&")[0]
                    except Exception:
                        pass
                R_HOST=delete_sharp(R_HOST)
                PATH=delete_sharp(PATH)


            
            
            
            list_of_c_type=[

            ID,
            ADDRESS,
            PORT,
            SECURITY,
            ALPN,
            FP,
            SNI,
            SPX,
            PBK,
            SID,
        PASS,
            TYPE,
            HEADER_TYPE,
            MODE,
            R_HOST,
            PATH
            
            ]

            
            

        elif conifg.startswith("ss://"):
            METHOD=conifg.split("ss://")[1].split("@")[0]
            METHOD=METHOD.encode('utf-8')
            METHOD=base64.b64decode(METHOD).decode("utf-8")
            PASSWORD=METHOD.split(":")
            
            METHOD=PASSWORD[0]
            PASS=PASSWORD[1]
            print(METHOD)
           
            ADDRESS=conifg.split("ss://")[1].split("@")[1].split(":")[0]
            PORT=conifg.split("ss://")[1].split("@")[1].split(":")[1]
            if "/?" in PORT :
                PORT=PORT.split("/?")[0]
            else:
                PORT=PORT.split("?")[0]

            PORT=delete_sharp(PORT)
                
        elif conifg.startswith("hysteria2://") or conifg.startswith("hy2://"):
            METHOD="chacha20-poly1305"
            if conifg.startswith("hysteria2://"):
                start="hysteria2://"
            else:
                start="hy2://"
            PASS=conifg.split(start)[1].split("@")[0]
            ADDRESS=conifg.split(start)[1].split("@")[1].split(":")[0]
            SECURITY=conifg.split(start)[1].split("security=")[1].split("&")[0]
            SECURITY=delete_sharp(SECURITY)
            if SECURITY=="none":
                SECURITY=""
            obfs=conifg.split(start)[1].split("obfs=")[1].split("&")[0]
            obfs=delete_sharp(obfs)
            obfs_password=conifg.split(start)[1].split("obfs-password=")[1].split("&")[0]
            SNI=""
            INSECURE=""
            obfs_password=delete_sharp(obfs_password)
            if SECURITY=="tls":
                try:
                    SNI=conifg.split(start)[1].split("sni=")[1].split("&")[0]
                    
                except Exception:
                    pass
                try:
                    INSECURE=conifg.split(start)[1].split("insecure=")[1].split("&")[0]
                    
                except Exception:
                    pass
                SNI=delete_sharp(SNI)
                INSECURE=delete_sharp(INSECURE)
            
        elif conifg.startswith("socks://"):
            USER=""
            PASS=""
            METHOD="chacha20-poly1305"

            try:
                USER=conifg.split("socks://")[1].split("@")[0]
                USER=USER.encode('utf-8')
                USER=base64.b64decode(USER).decode("utf-8")
                PASSWORD=USER.split(":")
                USER=PASSWORD[0]
                PASS=PASSWORD[1]
            except Exception:
                pass

            ADDRESS=conifg.split("socks://")[1].split("@")[1].split(":")[0]
            PORT=conifg.split("socks://")[1].split("@")[1].split(":")[1]
            if "/?" in PORT :
                PORT=PORT.split("/?")[0]
            else:
                PORT=PORT.split("?")[0]
            PORT=delete_sharp(PORT)
        elif conifg.startswith("wireguard://"):
            WNOISE="quic"
            WNOISECOUNT="15"
            WNOISEDELAY="1-3"
            WPAYLOADSIZE="1-8"
            KEEPALIVE=5


            MTU=1300
            SECERKEY=conifg.split("wireguard://")[1].split("@")[0]

            ENDPOINT=conifg.split("wireguard://")[1].split("@")[1].split(":")[0]
            PORT=conifg.split("wireguard://")[1].split("@")[1].split(":")[1]
            if "/?" in PORT :
                PORT=PORT.split("/?")[0]
            else:
                PORT=PORT.split("?")[0]
            PORT=delete_sharp(PORT)
            ADDRESS=conifg.split("wireguard://")[1].split("address=")[1].split("&")[0]
            ADDRESS=delete_sharp(ADDRESS)
            try:
                ADDRESS=ADDRESS.split(",")
            except Exception:
                pass
            
            RESERVED=conifg.split("wireguard://")[1].split("reserved=")[1].split("&")[0]
            RESERVED=delete_sharp(RESERVED)

            RESERVED=RESERVED.split(",")
            temp=[]
            for i in RESERVED:
                temp.append(int(i))
            RESERVED=temp
            
            PBK=conifg.split("wireguard://")[1].split("publickey=")[1].split("&")[0]
            PBK=delete_sharp(PBK)

            MTU=conifg.split("wireguard://")[1].split("mtu=")[1].split("&")[0]
            MTU=delete_sharp(MTU)
            MTU=int(MTU)
            try:
                WNOISE=conifg.split("wireguard://")[1].split("wnoise=")[1].split("&")[0]
                WNOISECOUNT=conifg.split("wireguard://")[1].split("wnoisecount=")[1].split("&")[0]
                WNOISEDELAY=conifg.split("wireguard://")[1].split("wnoisedelay=")[1].split("&")[0]
                WPAYLOADSIZE=conifg.split("wireguard://")[1].split("wpayloadsize=")[1].split("&")[0]
                KEEPALIVE=conifg.split("wireguard://")[1].split("keepalive=")[1].split("&")[0]
                WNOISE=delete_sharp(WNOISE)
                WNOISECOUNT=delete_sharp(WNOISECOUNT)
                WNOISEDELAY=delete_sharp(WNOISEDELAY)
                WPAYLOADSIZE=delete_sharp(WPAYLOADSIZE)
                KEEPALIVE=delete_sharp(KEEPALIVE)
                KEEPALIVE=int(KEEPALIVE)
            except Exception:
                pass

            
                
        if not conifg.startswith("vmess://"):
            try:
                    REMARKS=conifg.split("#")[1]
            except Exception:
                    REMARKS="None" 



        PORT=int(PORT)
        try:
            if MODE=="gun":
                        MODE=False
            else:
                        MODE=True
        except Exception:
            pass

        
        


        #################                    eding configs if                 ############################
       
        def change_list_f(list_w:list,value):
           
            list_w_index_f=list_w.index(value)
            temp=list_w[0]
            list_w[0]=str(list_w[list_w_index_f])
            if list_w[0]!=temp:
                del list_w[list_w_index_f]
                list_w.append(temp)
            return list_w
        
        if is_editing==True:
            try:
                if HEADER_TYPE==None:
                        HEADER_TYPE="none"
            except Exception:
                pass
            if conifg.startswith("vless://") or conifg.startswith("vmess://") or conifg.startswith("trojan://") :
                if ALPN==None:
                    ALPN=""
                if TYPE=="grpc":
                    if MODE==False:
                        MODE="gun"
                    else:
                        MODE="multi"
            try:
                if R_HOST==None:
                    R_HOST=""
            except Exception:
                pass
           
            
                
            REMARKS_w=ctk.StringVar(value=REMARKS)

            ADDRESS_w=ctk.StringVar(value=ADDRESS)
            if conifg.startswith("wireguard://"):
                ADDRESS_w=ctk.StringVar(value=ENDPOINT)
                LOCAL_add_w=ctk.StringVar(value=ADDRESS)
            
            PORT_w=ctk.IntVar(value=PORT)

            ID_w=""
            ENCRYPTION_w=""
            ALTERID_w=""
            PASS_w=""
            R_HOST_w=""
            PATH_w=""
            SNI_w=""
            PBK_w=""
            SID_w=""
            SPX_w=""
            PASS_w=""
            USER_w=""
            SECERKEY_w=""
            RESERVED_w=""
            MTU_w=""
            KEEPALIVE_w=""
            WNOISE_w=""
            WNOISECOUNT_w=""
            WNOISEDELAY_w=""
            WPAYLOADSIZE_w=""

            FLOW_w=[""]
            SCY_w=[""]
            TYPE_w=[""]
            network_head_values=[""]
            MODE_w=[""]
            TLS_w=[""]
            FP_w=[""]
            ALPN_w=[""]
            SECURITY_w=[""]
            
            if conifg.startswith("vless://") or conifg.startswith("vmess://") or conifg.startswith("trojan://"):
                ID_w=ctk.StringVar(value=ID)
                if conifg.startswith("vless://"):
                    FLOW_w=change_list_f(["","xtls-rprx-vision","xtls-rprx-vision-udp443"],FLOW)

                    ENCRYPTION_w=ctk.StringVar(value=ENCRYPTION)
                elif conifg.startswith("vmess://"):
                    ALTERID_w=ctk.StringVar(value=ALTERID)
                    SCY_w=change_list_f(["chacha20-poly1305","aes-128-gcm","auto","none","zero"],SCY)
                elif conifg.startswith("trojan://"):
                    PASS_w=ctk.StringVar(value=PASS)
                TYPE_w=change_list_f(["tcp","kcp","ws","httpupgrade","splithttp","h2","quic","grpc"],TYPE)
    
                if TYPE=="tcp" or TYPE=="kcp" or TYPE=="quic":
                    if TYPE=="tcp":
                        network_head_values=["none","http"]
                    elif TYPE=="kcp" or TYPE=="quic":
                        network_head_values=["none","strp","utp","wechat-video","dtls","wireguard"]
                    network_head_values=change_list_f(network_head_values,HEADER_TYPE)

                elif TYPE=="grpc":
                    MODE_w=change_list_f(["gun","multi"],MODE)

                if TYPE!="tcp":
                    if TYPE!="kcp":
                        R_HOST_w=ctk.StringVar(value=R_HOST)
                    PATH_w=ctk.StringVar(value=PATH) 
                TLS_w=change_list_f(["","tls","reality"],SECURITY)

                if SECURITY!="":
                    SNI_w=ctk.StringVar(value=SNI)
                    FP_w=change_list_f(["","chrome","firefox","safari","ios","android","edge","360","qq","random","randomized"],FP)
                    if SECURITY=="tls":
                        ALPN_w=change_list_f(["","h3","h2","http/1.1","h3,h2,http/1.1","h3,h2","h2,http/1.1"],ALPN)
                    elif SECURITY=="reality":
                        PBK_w=ctk.StringVar(value=PBK)
                        SID_w=ctk.StringVar(value=SID)
                        SPX_w=ctk.StringVar(value=SPX)
            elif conifg.startswith("ss://") or conifg.startswith("socks://"):
                PASS_w=ctk.StringVar(value=PASS)
                
                
                if conifg.startswith("socks://"):
                    USER_w=ctk.StringVar(value=USER)
                else:
                    SECURITY_w=change_list_f(["aes-256-gcm","aes-128-gcm","chacha20-poly1305","chacha20-ietf-poly1305","xchacha20-poly1305","xchacha20-ietf-poly1305","none","plain","2022-blake3-aes-128-gcm","2022-blake3-aes-256-gcm","2022-blake3-chacha20-poly1305"],METHOD)
            elif conifg.startswith("wireguard://"):
                SECERKEY_w=ctk.StringVar(value=SECERKEY)
                PBK_w=ctk.StringVar(value=PBK)
                RESERVED_w=ctk.StringVar(value=RESERVED)
                MTU_w=ctk.IntVar(value=int(MTU))
                KEEPALIVE_w=ctk.IntVar(value=int(KEEPALIVE))
                WNOISE_w=ctk.StringVar(value=WNOISE)
                WNOISECOUNT_w=ctk.StringVar(value=WNOISECOUNT)
                WNOISEDELAY_w=ctk.StringVar(value=WNOISEDELAY)
                WPAYLOADSIZE_w=ctk.StringVar(value=WPAYLOADSIZE)

            
            tabview.add("edit")
            tabview.set("edit")
            tabview.tab("edit").grab_set()
            fram_top=ctk.CTkFrame(tabview.tab("edit"),height=50,border_width=1,border_color="#868686")
            fram_top.pack(fill=tk.X)
            back_arrow =ctk.CTkImage(light_image=Image.open("imgs/arrow.png"),
                                  dark_image=Image.open("imgs/arrow_light.png"),
                                size=(25,25)  )
            def exit_out():
                
                

                rootmainactivity.grab_set()
                tabview.set("configs")
                clear_widgets(tabview.tab("edit"))
                tabview.delete("edit")
                
                
            
            def restart_editing(conifg:str,num:int):
                global is_editing
                is_editing=True
                rootmainactivity.grab_set()
                tabview.set("configs")
                tabview.delete("edit")
                rootmainactivity.update()
                
                parse_configs(conifg,num)
            def save_normal_conf_form(conifg:str,num:int,remarks:ctk.CTkEntry):
                global frams_in_show
                conf=""
                def change_s_to_c(v):
                    return re.sub(r'\s+',',',v)
                def none_value(va):
                        if va=="":
                            return "none"
                        return va
                if conifg.startswith("vless://"):
                
                    tls_v=none_value(tls.get())
                    vless="vless://"+id.get()+"@"+ip_address.get()+":"+ports.get()+"?"+"security="+tls_v+"&"+"encryption="+encryption.get()+"&"+"headerType="+header_type.get()+"&"+"type="+network.get()
                    if flow.get()!="":
                        vless+="&"+"flow="+flow.get()
                    if network.get()=="grpc":
                        vless+="&"+"mode="+mode.get()
                    if network.get()!="tcp":
                        if network.get()!="kcp":
                            if r_host.get()!="":
                                print(network.get())
                                if network.get()!="quic" and network.get()!="grpc" :
                                    vless+="&"+"host="+r_host.get()
                                elif network.get()=="grpc":
                                    vless+="&"+"authority="+r_host.get()
                                else:
                                    vless+="&"+"quicSecurity="+r_host.get()
                        if network.get()=="ws" or network.get()=="h2":
                            vless+="&"+"path="+path.get()
                        elif network.get()=="quic":
                            vless+="&"+"key="+path.get()
                        elif network.get()=="kcp":
                            vless+="&"+"seed="+path.get()
                        elif network.get()=="grpc":
                            vless+="&"+"serviceName="+path.get()
                    if sni.get()!="":
                        vless+="&"+"sni="+sni.get()
                    if fp.get()!="":
                        vless+="&"+"fp="+fp.get()
                    if tls.get()=="tls":
                        if alpn.get()!="":
                            vless+="&"+"alpn="+alpn.get()

                    elif tls.get()=="reality":

                        if pbk.get()!="":
                            vless+="&"+"pbk="+pbk.get()
                        if sid.get()!="":
                            vless+="&"+"sid="+sid.get()
                        if spx.get()!="":
                            vless+="&"+"spx="+spx.get()


                    vless+="#"+remarks.get()
                    conf=vless
                
                elif conifg.startswith("vmess://"):
                    vmess={"add":"","aid":"0","alpn":"","fp":"","host":"","id":"","net":"","path":"","port":"","ps":"","scy":"","sni":"","tls":"","type":"","v":"2"}
                    vmess["add"]=ip_address.get()
                    vmess["ps"]=remarks.get()
                    if network.get()!="tcp":
                        if network.get()!="kcp":
                            vmess["host"]=r_host.get()
                        vmess["path"]=path.get()
                    vmess["aid"]=alterid.get()
                    if tls.get()!="":

                        vmess["fp"]=fp.get()
                        vmess["sni"]=sni.get()
                        if tls.get()=="tls":
                            vmess["alpn"]=alpn.get()
                    
                    
                    vmess["id"]=id.get()
                    vmess["net"]=network.get()
                    vmess["port"]=ports.get()
                    vmess["scy"]=security.get()
                    vmess["tls"]=tls.get()
                    if network.get()!="grpc":
                        vmess["type"]=header_type.get()
                    else:
                        vmess["type"]=mode.get()

                                        
                    json_string = json.dumps(vmess)

            
                    json_bytes = json_string.encode('utf-8')

               
                    vmess ="vmess://"+ base64.b64encode(json_bytes).decode('utf-8')
                    conf=vmess
                elif conifg.startswith("trojan://"):
                    tls_v=none_value(tls.get())
                    trojan="trojan://"+pass_w.get()+"@"+ip_address.get()+":"+ports.get()+"?"+"security="+tls_v+"&"+"headerType="+header_type.get()+"&"+"type="+network.get()
                    if network.get()=="grpc":
                        trojan+="&"+"mode="+mode.get()
                    if network.get()!="tcp":
                        if network.get()!="kcp":
                            if r_host.get()!="":

                                if network.get()!="quic" and network.get()!="grpc" :
                                    trojan+="&"+"host="+r_host.get()
                                elif network.get()=="grpc":
                                    trojan+="&"+"authority="+r_host.get()
                                else:
                                    trojan+="&"+"quicSecurity="+r_host.get()
                        if network.get()=="ws" or network.get()=="h2":
                            trojan+="&"+"path="+path.get()
                        elif network.get()=="quic":
                            trojan+="&"+"key="+path.get()
                        elif network.get()=="kcp":
                            trojan+="&"+"seed="+path.get()
                        elif network.get()=="grpc":
                            trojan+="&"+"serviceName="+path.get()
                    if sni.get()!="":
                        trojan+="&"+"sni="+sni.get()
                    if fp.get()!="":
                        trojan+="&"+"fp="+fp.get()
                    if tls.get()=="tls":
                        if alpn.get()!="":
                            trojan+="&"+"alpn="+alpn.get()

                    elif tls.get()=="reality":

                        if pbk.get()!="":
                            trojan+="&"+"pbk="+pbk.get()
                        if sid.get()!="":
                            trojan+="&"+"sid="+sid.get()
                        if spx.get()!="":
                            trojan+="&"+"spx="+spx.get()


                    trojan+="#"+remarks.get()
                    conf=trojan
                elif conifg.startswith("socks://"): 
                    user_pass_socks=user.get()+":"+pass_w.get()
                    user_pass_socks=user_pass_socks.encode("utf-8")
                    user_pass_decode=base64.b64encode(user_pass_socks).decode('utf-8')

                    socks="socks://"+user_pass_decode+"@"+ip_address.get()+":"+ports.get()+"#"+remarks.get()
                    conf=socks
                elif conifg.startswith("ss://"):
                    security_pass_socks=security.get()+":"+pass_w.get()
                    security_pass_socks=security_pass_socks.encode("utf-8")
                    security_pass_decode=base64.b64encode(security_pass_socks).decode('utf-8')
                    shs="ss://"+security_pass_decode+"@"+ip_address.get()+":"+ports.get()+"#"+remarks.get()
                    conf=shs
                elif conifg.startswith("wireguard://"):
                    listt=reserved.get().split(" ")
                    lostt2=''
                    for num in range(len(listt)):
                        lostt2+=str(listt[num])
                        if num != len(listt)-1:
                            lostt2+=','
                    reserved_encode=urlencode(lostt2)
                    wireguard="wireguard://"+urlencode(secrekey.get())+"@"+ip_address.get()+":"+ports.get()+"?"+"address="+urlencode(change_s_to_c(address.get()))+"&"+"publickey="+urlencode(pbk.get())+"&"+"reserved="+reserved_encode
                   
                    wireguard+="&"+"mtu="+mtu.get()
                    if keepAlive!=0:
                        wireguard+="&"+"keepalive="+keepAlive.get()
                    if wnoise!="":
                        wireguard+="&"+"wnoise="+wnoise.get()
                    if wnoisecount!="":
                        wireguard+="&"+"wnoisecount="+wnoisecount.get()
                    if wnoisedelay!="":
                        wireguard+="&"+"wnoisedelay="+wnoisedelay.get()
                    if wpayloadsize!="":
                        wireguard+="&"+"wpayloadsize="+wpayloadsize.get()
                    wireguard+="#"+remarks.get()
                    conf=wireguard

                lable=frams_in_show[num]
                lable.configure(state=tk.NORMAL)
                lable.delete(1.0,tk.END)
                remarks=re.sub(r'\n', '', remarks.get())
                lable.insert(1.0,remarks)
                lable.configure(state=tk.DISABLED)
                
                with open("xray/"+selec_sub.get(),"r",encoding="utf-8") as f:
                    sun_na=f.readlines()
                print(conf)
                conf=re.sub(r'\n', '', conf)
                sun_na[num]=conf+"\n"
                with open("xray/"+selec_sub.get(),"w",encoding="utf-8") as f:
                    f.writelines(sun_na)
                rootmainactivity.grab_set()
                tabview.set("configs")
                clear_widgets(tabview.tab("edit"))
                tabview.delete("edit")

            go_out_button=ctk.CTkButton(fram_top,command=exit_out, fg_color="transparent",hover_color="#DF9C27",width=25, image=back_arrow, text="")
            go_out_button.pack( padx=(0,10),pady=5,side=tk.RIGHT)
            
            restart_button=ctk.CTkButton(fram_top  ,fg_color="transparent",command=lambda conifg=conifg,num=num:restart_editing(conifg,num),hover_color="#DF9C27",width=25, image=update_icon, text="")
            restart_button.pack( padx=(0,330),pady=5,side=tk.RIGHT)
            
            save_button=ctk.CTkButton(fram_top  ,fg_color="transparent",command=lambda conifg=conifg, num=num:save_normal_conf_form(conifg,num,remarks),hover_color="#DF9C27",width=25, image=ip_cion, text="")
            save_button.pack( padx=(0,10),pady=5,side=tk.RIGHT)
            

            fram_in=ctk.CTkFrame(tabview.tab("edit"),height=500,width=500)
            fram_in.pack(fill=tk.BOTH,pady=(5,5))

            fram_in_in_1=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            fram_in_in_1.pack(fill=tk.X,pady=5,ipady=5,padx=5)

            remarks_la=ctk.CTkLabel(fram_in_in_1  ,  text="remarks: ")
            remarks_la.pack( padx=(20,0),side=tk.LEFT)


            remarks=ctk.CTkEntry(fram_in_in_1,textvariable=REMARKS_w, placeholder_text="remarks")
            remarks.pack(fill=tk.X,side=tk.LEFT,padx=4)





            ip_address_la=ctk.CTkLabel(fram_in_in_1 ,  text="address: ")
            ip_address_la.pack(padx=2,side=tk.LEFT)



       
            
            ip_address=ctk.CTkEntry(fram_in_in_1,textvariable=ADDRESS_w, placeholder_text="ip address(x.x.x.x)")
            ip_address.pack(fill=tk.X,side=tk.LEFT,padx=2)


            fram_in_in_2=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            fram_in_in_2.pack(fill=tk.X,pady=5,ipady=5,padx=5)

            ports_la=ctk.CTkLabel(fram_in_in_2  ,  text="port: ")
            ports_la.pack( padx=(20,0),side=tk.LEFT)

            
            ports=ctk.CTkEntry(fram_in_in_2,textvariable=PORT_w, placeholder_text="port")
            ports.pack(fill=tk.X,side=tk.LEFT,padx=4)

            def un_chnage_network(test):
                TYPE=network.get()
                if TYPE!="grpc":
                
                    try:
                        mode_la.pack_forget()
                        mode.pack_forget()
                    except Exception:
                            pass
                else:

        
                    try:
                        header_type_la.pack_forget()
                        header_type.pack_forget()
                    except Exception:
                            pass

                if TYPE=="tcp":
  
                    
                    header_type_la.pack( padx=(20,0),side=tk.LEFT)
                    if len(header_type._values)==1:
                        header_type.configure(values=["none","http"])
                        header_type.set("none")
                    header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)
                elif TYPE=="quic" or TYPE=="kcp":
                    header_type_la.pack( padx=(20,0),side=tk.LEFT)
                    if len(header_type._values)==1:
                        header_type.configure(values=["none","strp","utp","wechat-video","dtls","wireguard"])
                        header_type.set("none")
                    header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    
                    
                elif TYPE=="grpc":
                    
                    mode_la.pack( padx=(20,0),side=tk.LEFT)
                    if len(mode._values)==1:
                        mode.configure(values=["gun","multi"])
                        mode.set("gun")
                       
                    mode.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    
                else:

                    header_type_la.pack( padx=(20,0),side=tk.LEFT)
                    header_type.configure(values=[""])
                    header_type.set(" ")
                    header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)

            def un_chnage_tls(test):
                SECURITY=tls.get()

                if SECURITY=="tls":
                    try:
                        sni_la.pack_forget()
                        sni.pack_forget()
                        fram_in_in_8.pack_forget()
                        fp_la.pack_forget()
                        fp.pack_forget()
                    except Exception:
                        pass
                    try:
                        pbk_la.pack_forget()
                        pbk.pack_forget()
                        sid_la.pack_forget()
                        sid.pack_forget()
                        spx_la.pack_forget()
                        spx.pack_forget()
                    except Exception:
                        pass
                elif SECURITY=="reality":
                    try:
                        sni_la.pack_forget()
                        sni.pack_forget()
                        fram_in_in_7.pack_forget()
                        fp_la.pack_forget()
                        fp.pack_forget()
                    except Exception:
                        pass
                    try:
                        alpn_la.pack_forget()
                        alpn.pack_forget()
                    except Exception:
                        pass
                elif SECURITY=="":
                    try:
                        sni_la.pack_forget()
                        sni.pack_forget()
                        
                        fp_la.pack_forget()
                        fp.pack_forget()
                        fram_in_in_7.pack_forget()
                        fram_in_in_8.pack_forget()
                    except Exception:
                        pass
                    try:
                        alpn_la.pack_forget()
                        alpn.pack_forget()
                    except Exception:
                        pass
                            
                    try:
                        pbk_la.pack_forget()
                        pbk.pack_forget()
                        sid_la.pack_forget()
                        sid.pack_forget()
                        spx_la.pack_forget()
                        spx.pack_forget()
                    except Exception:
                        pass

                if SECURITY!="":
                    
                    
                    sni_la.pack( padx=(20,0),side=tk.LEFT)
                    
                    
                    sni.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    
                    fram_in_in_7.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                    
                    fp_la.pack( padx=(20,0),side=tk.LEFT)
                   
                    fp.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    if SECURITY=="tls":
                        if len(alpn._values)==1:
                         
                            alpn.configure(values=["","h3","h2","http/1.1","h3,h2,http/1.1","h3,h2","h2,http/1.1"])
                        alpn_la.pack( padx=(20,0),side=tk.LEFT)
                       
                        alpn.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    elif SECURITY=="reality":
                        
                        pbk_la.pack( padx=(20,0),side=tk.LEFT)
                    
                        pbk.pack(fill=tk.X,side=tk.LEFT,padx=4)
                        
                        fram_in_in_8.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                        
                        sid_la.pack( padx=(20,0),side=tk.LEFT)
                      
                        sid.pack(fill=tk.X,side=tk.LEFT,padx=4)
                        
                        spx_la.pack( padx=(20,0),side=tk.LEFT)
                      
                        spx.pack(fill=tk.X,side=tk.LEFT,padx=4)
            
                        

            fram_in_in_3=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            fram_in_in_4=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            fram_in_in_5=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            fram_in_in_6=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            fram_in_in_7=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            fram_in_in_8=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
            id=ctk.CTkEntry(master=fram_in_in_2,textvariable=ID_w, placeholder_text="id")
            flow=ctk.CTkOptionMenu(master=fram_in_in_3,values=FLOW_w,width=30)
            encryption=ctk.CTkEntry(master=fram_in_in_3, textvariable=ENCRYPTION_w,placeholder_text="encryption")
            network=ctk.CTkOptionMenu(master=fram_in_in_4,values=TYPE_w,width=30,command=un_chnage_network)
            header_type=ctk.CTkOptionMenu(master=fram_in_in_4,values=network_head_values,width=30)
            mode=ctk.CTkOptionMenu(master=fram_in_in_4,width=30,values=MODE_w)
            r_host=ctk.CTkEntry(master=fram_in_in_5,textvariable=R_HOST_w ,placeholder_text="")
            path=ctk.CTkEntry(master=fram_in_in_5,textvariable=PATH_w,placeholder_text="")
            tls=ctk.CTkOptionMenu(master=fram_in_in_6,width=3,values=TLS_w,command=un_chnage_tls)
            sni=ctk.CTkEntry(master=fram_in_in_6,textvariable=SNI_w,placeholder_text="")
            fp=ctk.CTkOptionMenu(master=fram_in_in_7,width=30,values=FP_w)
            alpn=ctk.CTkOptionMenu(master=fram_in_in_7,width=30,values=ALPN_w)
            pbk=ctk.CTkEntry(master=fram_in_in_7,placeholder_text="",textvariable=PBK_w)
            sid=ctk.CTkEntry(master=fram_in_in_8, placeholder_text="",textvariable=SID_w)
            spx=ctk.CTkEntry(master=fram_in_in_8, placeholder_text="",textvariable=SPX_w)
            alterid=ctk.CTkEntry(master=fram_in_in_3, placeholder_text="alterid",textvariable=ALTERID_w)
            security=ctk.CTkOptionMenu(master=fram_in_in_3,values=SECURITY_w,width=30)
            pass_w=ctk.CTkEntry(master=fram_in_in_2,placeholder_text="password",textvariable=PASS_w)
            user=ctk.CTkEntry(master=fram_in_in_3,placeholder_text="user",textvariable=USER_w)
            sni_la=ctk.CTkLabel(fram_in_in_6,text="SNI: ")
            fp_la=ctk.CTkLabel(fram_in_in_7,text="Fingerprint: ")
            alpn_la=ctk.CTkLabel(fram_in_in_7,text="Alpn: ")
            pbk_la=ctk.CTkLabel(fram_in_in_7,text="PublicKey: ")
            sid_la=ctk.CTkLabel(fram_in_in_8,text="ShortId: ")
            spx_la=ctk.CTkLabel(fram_in_in_8,text="SpiderX: ")
            header_type_la=ctk.CTkLabel(fram_in_in_4  ,  text="head type: ")
            mode_la=ctk.CTkLabel(fram_in_in_4  ,  text="gRPC mode: ")
            if conifg.startswith("vless://") or conifg.startswith("vmess://"):
                id_la=ctk.CTkLabel(fram_in_in_2  ,  text="id: ")
                id_la.pack(padx=2,side=tk.LEFT)
           
                id.pack(fill=tk.X,side=tk.LEFT,padx=2)
                
                if conifg.startswith("vless://") :
                    
               
               
                    fram_in_in_3.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                    flow_la=ctk.CTkLabel(fram_in_in_3  ,  text="flow: ")
                    flow_la.pack( padx=(20,0),side=tk.LEFT)
                    
                    flow.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    

                    encryption_la=ctk.CTkLabel(fram_in_in_3  ,  text="encryption: ")
                    encryption_la.pack( padx=(20,0),side=tk.LEFT)

                    
                   
                    encryption.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    


                    
                    fram_in_in_4.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                    network_la=ctk.CTkLabel(fram_in_in_4  ,  text="network: ")
                    network_la.pack( padx=(20,0),side=tk.LEFT)

                    
                    
                    network.pack(fill=tk.X,side=tk.LEFT,padx=4)

                    

                    if TYPE=="tcp" or TYPE=="kcp" or TYPE=="quic":

                      
                        header_type_la=ctk.CTkLabel(fram_in_in_4  ,  text="head type: ")
                        header_type_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    elif TYPE=="grpc":
                        mode_la=ctk.CTkLabel(fram_in_in_4  ,  text="gRPC mode: ")
                        mode_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        mode.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    else:
                        header_type_la=ctk.CTkLabel(fram_in_in_4  ,  text="head type: ")
                        header_type_la.pack( padx=(20,0),side=tk.LEFT)

                        header_type.configure(values=["-"])
                        header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    
                    
                    if TYPE!="tcp":
                        
                        fram_in_in_5.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                        if TYPE!="kcp":
                            r_host_la=ctk.CTkLabel(fram_in_in_5  ,  text="requets host: ")
                            r_host_la.pack( padx=(20,0),side=tk.LEFT)

                            
                            
                            r_host.pack(fill=tk.X,side=tk.LEFT,padx=4)

                        path_la=ctk.CTkLabel(fram_in_in_5  ,  text="path: ")
                        path_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        
                        path.pack(fill=tk.X,side=tk.LEFT,padx=4)

                    
                    fram_in_in_6.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                    tls_la=ctk.CTkLabel(fram_in_in_6  ,  text="tls: ")
                    tls_la.pack( padx=(20,0),side=tk.LEFT)
                   
                    tls.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    if SECURITY!="":
                        
                        
                        sni_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        
                        sni.pack(fill=tk.X,side=tk.LEFT,padx=4)

                        
                        fram_in_in_7.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                        
                        fp_la.pack( padx=(20,0),side=tk.LEFT)
                        
                        fp.pack(fill=tk.X,side=tk.LEFT,padx=4)
                        if SECURITY=="tls":
                            
                            alpn_la.pack( padx=(20,0),side=tk.LEFT)
                            
                            alpn.pack(fill=tk.X,side=tk.LEFT,padx=4)

                        elif SECURITY=="reality":
                           
                            pbk_la.pack( padx=(20,0),side=tk.LEFT)
                            
                            pbk.pack(fill=tk.X,side=tk.LEFT,padx=4)
                            
                            fram_in_in_8.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                            
                            sid_la.pack( padx=(20,0),side=tk.LEFT)
                            
                            sid.pack(fill=tk.X,side=tk.LEFT,padx=4)

                            
                            spx_la.pack( padx=(20,0),side=tk.LEFT)
                            
                            spx.pack(fill=tk.X,side=tk.LEFT,padx=4)
                if conifg.startswith("vmess://") :
                    
                    fram_in_in_3.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                    
                    alterid_la=ctk.CTkLabel(fram_in_in_3  ,  text="alterid: ")
                    alterid_la.pack( padx=(20,0),side=tk.LEFT)

                    
                    alterid.pack(fill=tk.X,side=tk.LEFT,padx=4)

                    security_la=ctk.CTkLabel(fram_in_in_3  ,  text="security: ")
                    security_la.pack( padx=(20,0),side=tk.LEFT)

                    
                    security.configure(values=SCY_w)
                    security.pack(fill=tk.X,side=tk.LEFT,padx=4)


                    
                    fram_in_in_4.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                    network_la=ctk.CTkLabel(fram_in_in_4  ,  text="network: ")
                    network_la.pack( padx=(20,0),side=tk.LEFT)

                    
                    
                    network.pack(fill=tk.X,side=tk.LEFT,padx=4)

                    if TYPE=="tcp" or TYPE=="kcp" or TYPE=="quic":

                      
                        header_type_la=ctk.CTkLabel(fram_in_in_4  ,  text="head type: ")
                        header_type_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    elif TYPE=="grpc":
                        mode_la=ctk.CTkLabel(fram_in_in_4  ,  text="gRPC mode: ")
                        mode_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        mode.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    else:
                        header_type_la=ctk.CTkLabel(fram_in_in_4  ,  text="head type: ")
                        header_type_la.pack( padx=(20,0),side=tk.LEFT)

                        header_type.configure(values=["-"])
                        header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)

                    if TYPE!="tcp":
                        
                        fram_in_in_5.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                        if TYPE!="kcp":
                            r_host_la=ctk.CTkLabel(fram_in_in_5  ,  text="requets host: ")
                            r_host_la.pack( padx=(20,0),side=tk.LEFT)

                            
                            
                            r_host.pack(fill=tk.X,side=tk.LEFT,padx=4)

                        path_la=ctk.CTkLabel(fram_in_in_5  ,  text="path: ")
                        path_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        
                        path.pack(fill=tk.X,side=tk.LEFT,padx=4)


                    
                    fram_in_in_6.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                    tls_la=ctk.CTkLabel(fram_in_in_6  ,  text="tls: ")
                    tls_la.pack( padx=(20,0),side=tk.LEFT)
                   
                    tls.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    if SECURITY!="":
                        
                        
                        sni_la.pack( padx=(20,0),side=tk.LEFT)

                        
                        
                        sni.pack(fill=tk.X,side=tk.LEFT,padx=4)

                        
                        fram_in_in_7.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                        
                        fp_la.pack( padx=(20,0),side=tk.LEFT)
                        
                        fp.pack(fill=tk.X,side=tk.LEFT,padx=4)
                        if SECURITY=="tls":
                            
                            alpn_la.pack( padx=(20,0),side=tk.LEFT)
                            
                            alpn.pack(fill=tk.X,side=tk.LEFT,padx=4)

                        elif SECURITY=="reality":
                           
                            pbk_la.pack( padx=(20,0),side=tk.LEFT)
                             
                            pbk.pack(fill=tk.X,side=tk.LEFT,padx=4)
                            
                            fram_in_in_8.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                            
                            sid_la.pack( padx=(20,0),side=tk.LEFT)
                            
                            sid.pack(fill=tk.X,side=tk.LEFT,padx=4)

                            
                            spx_la.pack( padx=(20,0),side=tk.LEFT)
                            
                            spx.pack(fill=tk.X,side=tk.LEFT,padx=4)
            elif conifg.startswith("trojan://"):
                pass_w_la=ctk.CTkLabel(fram_in_in_2  ,  text="password: ")
                pass_w_la.pack(padx=2,side=tk.LEFT)
                
                pass_w.pack(fill=tk.X,side=tk.LEFT,padx=2)
                

                
                fram_in_in_4.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                network_la=ctk.CTkLabel(fram_in_in_4  ,  text="network: ")
                network_la.pack( padx=(20,0),side=tk.LEFT)
                
                
                network.pack(fill=tk.X,side=tk.LEFT,padx=4)
                if TYPE=="tcp" or TYPE=="kcp" or TYPE=="quic":
    
                  
                    header_type_la=ctk.CTkLabel(fram_in_in_4  ,  text="head type: ")
                    header_type_la.pack( padx=(20,0),side=tk.LEFT)
                    
                    header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)
                elif TYPE=="grpc":
                    mode_la=ctk.CTkLabel(fram_in_in_4  ,  text="gRPC mode: ")
                    mode_la.pack( padx=(20,0),side=tk.LEFT)
                    
                    mode.pack(fill=tk.X,side=tk.LEFT,padx=4)
                else:
                    header_type_la=ctk.CTkLabel(fram_in_in_4  ,  text="head type: ")
                    header_type_la.pack( padx=(20,0),side=tk.LEFT)
                    header_type.configure(values=[""])
                    header_type.pack(fill=tk.X,side=tk.LEFT,padx=4)
                
                
                if TYPE!="tcp":
                    
                    
                    fram_in_in_5.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                    if TYPE!="kcp":
                        r_host_la=ctk.CTkLabel(fram_in_in_5  ,  text="requets host: ")
                        r_host_la.pack( padx=(20,0),side=tk.LEFT)
                        
                        
                        r_host.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    path_la=ctk.CTkLabel(fram_in_in_5  ,  text="path: ")
                    path_la.pack( padx=(20,0),side=tk.LEFT)
                    
                    
                    path.pack(fill=tk.X,side=tk.LEFT,padx=4)
                
                fram_in_in_6.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                tls_la=ctk.CTkLabel(fram_in_in_6  ,  text="tls: ")
                tls_la.pack( padx=(20,0),side=tk.LEFT)
               
                tls.pack(fill=tk.X,side=tk.LEFT,padx=4)
                if SECURITY!="":
                    
                    
                    sni_la.pack( padx=(20,0),side=tk.LEFT)
                    
                    
                    sni.pack(fill=tk.X,side=tk.LEFT,padx=4)
              
                    fram_in_in_7.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                    
                    fp_la.pack( padx=(20,0),side=tk.LEFT)
                    
                    fp.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    if SECURITY=="tls":
                        
                        alpn_la.pack( padx=(20,0),side=tk.LEFT)
                        
                        alpn.pack(fill=tk.X,side=tk.LEFT,padx=4)
                    elif SECURITY=="reality":
                       
                        pbk_la.pack( padx=(20,0),side=tk.LEFT)
                         
                        pbk.pack(fill=tk.X,side=tk.LEFT,padx=4)
                        
                        fram_in_in_8.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                        
                        sid_la.pack( padx=(20,0),side=tk.LEFT)
                        
                        sid.pack(fill=tk.X,side=tk.LEFT,padx=4)
                        
                        spx_la.pack( padx=(20,0),side=tk.LEFT)
                        
                        spx.pack(fill=tk.X,side=tk.LEFT,padx=4)
            elif conifg.startswith("ss://"):
                pass_w_la=ctk.CTkLabel(fram_in_in_2  ,  text="password: ")
                pass_w_la.pack(padx=2,side=tk.LEFT)
                
                pass_w.pack(fill=tk.X,side=tk.LEFT,padx=2)



                
                fram_in_in_3.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                security_la=ctk.CTkLabel(fram_in_in_3  ,  text="security: ")
                security_la.pack( padx=(20,0),side=tk.LEFT)
          
                security.pack(fill=tk.X,side=tk.LEFT,padx=4)


            elif conifg.startswith("socks://"):
                pass_w_la=ctk.CTkLabel(fram_in_in_2  ,  text="password: ")
                pass_w_la.pack(padx=2,side=tk.LEFT)
                
                pass_w.pack(fill=tk.X,side=tk.LEFT,padx=2)



                
                fram_in_in_3.pack(fill=tk.X,pady=5,ipady=5,padx=5)
                user_la=ctk.CTkLabel(fram_in_in_3  ,  text="user: ")
                user_la.pack( padx=(20,0),side=tk.LEFT)
                
                user.pack(fill=tk.X,side=tk.LEFT,padx=2)

            elif conifg.startswith("wireguard://"):
                secrekey_la=ctk.CTkLabel(fram_in_in_2  ,  text="secret or Private key: ")
                secrekey_la.pack(padx=2,side=tk.LEFT)
                secrekey=ctk.CTkEntry(fram_in_in_2,textvariable=SECERKEY_w, placeholder_text="secret key")
                secrekey.pack(fill=tk.X,side=tk.LEFT,padx=2)



                
                fram_in_in_3.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                pbk_la=ctk.CTkLabel(fram_in_in_3  ,  text="PublicKey: ")      
                pbk_la.pack( padx=(20,0),side=tk.LEFT)
                pbk=ctk.CTkEntry(fram_in_in_3,textvariable=PBK_w, placeholder_text="pbk")
                pbk.pack(fill=tk.X,side=tk.LEFT,padx=2)

                reserved_la=ctk.CTkLabel(fram_in_in_3  ,  text="reserved: ")
                reserved_la.pack( padx=(20,0),side=tk.LEFT)
                reserved=ctk.CTkEntry(fram_in_in_3,textvariable=RESERVED_w, placeholder_text="reserved")
                reserved.pack(fill=tk.X,side=tk.LEFT,padx=2)



                
                fram_in_in_5.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                address_la=ctk.CTkLabel(fram_in_in_5  ,  text="address: ")      
                address_la.pack( padx=(20,0),side=tk.LEFT)
                address=ctk.CTkEntry(fram_in_in_5,textvariable=LOCAL_add_w, placeholder_text="address")
                address.pack(fill=tk.X,side=tk.LEFT,padx=2)

                mtu_la=ctk.CTkLabel(fram_in_in_5  ,  text="mtu: ")
                mtu_la.pack( padx=(20,0),side=tk.LEFT)
                mtu=ctk.CTkEntry(fram_in_in_5,textvariable=MTU_w, placeholder_text="mtu")
                mtu.pack(fill=tk.X,side=tk.LEFT,padx=2)


                
                fram_in_in_6.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                keepAlive_la=ctk.CTkLabel(fram_in_in_6  ,  text="keepAlive: ")      
                keepAlive_la.pack( padx=(20,0),side=tk.LEFT)
                keepAlive=ctk.CTkEntry(fram_in_in_6,textvariable=KEEPALIVE_w, placeholder_text="keepAlive")
                keepAlive.pack(fill=tk.X,side=tk.LEFT,padx=2)

                wnoise_la=ctk.CTkLabel(fram_in_in_6  ,  text="wnoise: ")
                wnoise_la.pack( padx=(20,0),side=tk.LEFT)
                wnoise=ctk.CTkEntry(fram_in_in_6,textvariable=WNOISE_w, placeholder_text="wnoise")
                wnoise.pack(fill=tk.X,side=tk.LEFT,padx=2)

                fram_in_in_7=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
                fram_in_in_7.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                wnoisecount_la=ctk.CTkLabel(fram_in_in_7  ,  text="wnoisecount: ")      
                wnoisecount_la.pack( padx=(20,0),side=tk.LEFT)
                wnoisecount=ctk.CTkEntry(fram_in_in_7,textvariable=WNOISECOUNT_w, placeholder_text="wnoisecount")
                wnoisecount.pack(fill=tk.X,side=tk.LEFT,padx=2)

                wnoisedelay_la=ctk.CTkLabel(fram_in_in_7  ,  text="wnoisedelay: ")
                wnoisedelay_la.pack( padx=(20,0),side=tk.LEFT)
                wnoisedelay=ctk.CTkEntry(fram_in_in_7,textvariable=WNOISEDELAY_w, placeholder_text="wnoisedelay")
                wnoisedelay.pack(fill=tk.X,side=tk.LEFT,padx=2)

                
                fram_in_in_8=ctk.CTkFrame(fram_in,height=100,border_width=1,border_color="#48adfa",corner_radius=5)
                fram_in_in_8.pack(fill=tk.X,pady=5,ipady=5,padx=5)

                wpayloadsize_la=ctk.CTkLabel(fram_in_in_8  ,  text="wpayloadsize: ")      
                wpayloadsize_la.pack( padx=(20,0),side=tk.LEFT)
                wpayloadsize=ctk.CTkEntry(fram_in_in_8,textvariable=WPAYLOADSIZE_w, placeholder_text="wpayloadsize")
                wpayloadsize.pack(fill=tk.X,side=tk.LEFT,padx=2)

            is_editing=False
            return

        ##################################################################################################

        try:
                ALPN=ALPN.split(",")
        except Exception:
                pass
        
        logBean = V2rayConfigLogBean("", "", "warning")  # Make sure to adjust the imports for these
        inboundBean = V2rayConfig.InboundBean(tag="socks", port=10808, protocol="socks",listen="127.0.0.1", sniffing=V2rayConfig.InboundBean.SniffingBean(True, ["http","tls","fakedns"],routeOnly=False),settings=V2rayConfig.InboundBean.InSettingsBean(auth="noauth",udp=True,allowTransparent=False))
        inboundBean2=V2rayConfig.InboundBean(tag="http", port=10809, protocol="http",listen="127.0.0.1", sniffing=V2rayConfig.InboundBean.SniffingBean(True, ["http","tls","fakedns"],routeOnly=False),settings=V2rayConfig.InboundBean.InSettingsBean(auth="noauth",udp=True,allowTransparent=False)) 
        outboundBean=""
        routingBean=V2rayConfig.RoutingBean(domainStrategy="AsIs",rules=[V2rayConfig.RoutingBean.RulesBean(type="field",inboundTag=["api"],outboundTag="api",enabled=True),V2rayConfig.RoutingBean.RulesBean(id="5627785659655799759",type="field",port="0-65535",outboundTag="proxy",enabled=True)])
        dnsBean=V2rayConfig.DnsBean(hosts={"domain:googleapis.cn":"googleapis.com"},servers=[V2rayConfig.DnsBean.ServersBean(address="fakedns",domains=["geosite:cn","domain:ir","geosite:category-ir","geosite:private"]),"https://8.8.8.8/dns-query"],fakedns=V2rayConfig.FakednsBean(ipPool="198.18.0.0/15",poolSize=10000))
        if conifg.startswith("vless://"):
            
            
                
            header=V2rayConfig.OutboundBean.HeaderBean()
            if HEADER_TYPE=="http" and TYPE=="tcp":
                headers=V2rayConfig.OutboundBean.HeadersBean(Connection=["keep-alive"], Host=[R_HOST],Pragma="no-cache",acceptEncoding=["gzip, deflate"],userAgent=["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/53.0.2785.109 Mobile/14A456 Safari/601.1.46"])
                requests=V2rayConfig.OutboundBean.RequestBean(headers=headers,method="GET",path=PATH,version="1.1")
                header=V2rayConfig.OutboundBean.HeaderBean(type="http",request=requests)
            
            outboundBean_Stream_tcpsettings=V2rayConfig.OutboundBean.TcpSettingsBean(header=header)
            if TYPE=="kcp":
                outboundBean_Stream_kcp_settings=V2rayConfig.OutboundBean.KcpSettingsBean(congestion=False,downlinkCapacity=100,header=V2rayConfig.OutboundBean.HeaderBean(type=HEADER_TYPE),mtu=1350,readBufferSize=1,seed=PATH,tti=50,uplinkCapacity=12,writeBufferSize=1)
            elif TYPE=="ws":
                outboundBean_Stream_ws_settings=V2rayConfig.OutboundBean.WsSettingsBean(headers=V2rayConfig.OutboundBean.HeadersBean(Host=R_HOST,userAgent=None,acceptEncoding=None,Connection=None,Pragma=None,Host_single=None),path=PATH)
            elif TYPE=="httpupgrade":
                outboundBean_Stream_httpupgrade_settings=V2rayConfig.OutboundBean.HttpupgradeSettingsBean(host=R_HOST,path=PATH)
            elif TYPE=="splithttp":
                outboundBean_Stream_splithttp_settings=V2rayConfig.OutboundBean.SplithttpSettingsBean(host=R_HOST,path=PATH)
            elif TYPE=="h2":
                outboundBean_Stream_h2_settings=V2rayConfig.OutboundBean.HttpSettingsBean(host=[R_HOST],path=PATH)
            elif TYPE=="quic":
                outboundBean_Stream_quic_settings=V2rayConfig.OutboundBean.QuicSettingBean(header=V2rayConfig.OutboundBean.HeaderBean(type=HEADER_TYPE),key=PATH,security=R_HOST)
            elif TYPE=="grpc":
                outboundBean_Stream_grpc_settings=V2rayConfig.OutboundBean.GrpcSettingsBean(authority=R_HOST,multiMode=MODE,)
            
            if SECURITY!="reality":
                outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=True,alpn=ALPN,fingerprint=FP,serverName=SNI,show=False)
            else:
                outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=True,alpn=ALPN,fingerprint=FP,publicKey=PBK,serverName=SNI,shortId=SID,spiderX=SPX,show=False)
            
            if FRAGMENT==True:
                if  SECURITY=="reality" :
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                else:
                    
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                                    
            else:
                if  SECURITY=="reality" :
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,realitySettings=outboundBean_Stream_tlssettings)
                else:

                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,tlsSettings=outboundBean_Stream_tlssettings)
                                                
            outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="vless", settings=V2rayConfig.OutboundBean.OutSettingsBean(vnext=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean (address=ADDRESS, port=PORT, users=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean.UsersBean(id=ID,security="auto",level=8,encryption=ENCRYPTION,flow=FLOW,alterId=0)])]),mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),streamSettings=outboundBean_Stream_tcp)    
        elif conifg.startswith("vmess://"):
            header=V2rayConfig.OutboundBean.HeaderBean()
            if HEADER_TYPE=="http" and TYPE=="tcp":
                headers=V2rayConfig.OutboundBean.HeadersBean(Connection=["keep-alive"], Host=[R_HOST],Pragma="no-cache",acceptEncoding=["gzip, deflate"],userAgent=["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/53.0.2785.109 Mobile/14A456 Safari/601.1.46"])
                requests=V2rayConfig.OutboundBean.RequestBean(headers=headers,method="GET",path=PATH,version="1.1")
                header=V2rayConfig.OutboundBean.HeaderBean(type="http",request=requests)
            
            outboundBean_Stream_tcpsettings=V2rayConfig.OutboundBean.TcpSettingsBean(header=header)
            if TYPE=="kcp":
                outboundBean_Stream_kcp_settings=V2rayConfig.OutboundBean.KcpSettingsBean(congestion=False,downlinkCapacity=100,header=V2rayConfig.OutboundBean.HeaderBean(type=HEADER_TYPE),mtu=1350,readBufferSize=1,seed=PATH,tti=50,uplinkCapacity=12,writeBufferSize=1)
            elif TYPE=="ws":
                outboundBean_Stream_ws_settings=V2rayConfig.OutboundBean.WsSettingsBean(headers=V2rayConfig.OutboundBean.HeadersBean(Host=R_HOST,userAgent=None,Pragma=None,Host_single=None,Connection=None,acceptEncoding=None),path=PATH)
            elif TYPE=="httpupgrade":
                outboundBean_Stream_httpupgrade_settings=V2rayConfig.OutboundBean.HttpupgradeSettingsBean(host=R_HOST,path=PATH)
            elif TYPE=="splithttp":
                outboundBean_Stream_splithttp_settings=V2rayConfig.OutboundBean.SplithttpSettingsBean(host=R_HOST,path=PATH)
            elif TYPE=="h2":
                outboundBean_Stream_h2_settings=V2rayConfig.OutboundBean.HttpSettingsBean(host=[R_HOST],path=PATH)
            elif TYPE=="quic":
                outboundBean_Stream_quic_settings=V2rayConfig.OutboundBean.QuicSettingBean(header=V2rayConfig.OutboundBean.HeaderBean(type=HEADER_TYPE),key=PATH,security=R_HOST)
            elif TYPE=="grpc":
                outboundBean_Stream_grpc_settings=V2rayConfig.OutboundBean.GrpcSettingsBean(authority=R_HOST,multiMode=MODE,)
            
            if SECURITY!="reality":
                outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=True,serverName=SNI,fingerprint=FP,show=False)
            else:
                outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=True,alpn=ALPN,fingerprint=FP,serverName=SNI,show=False)
            
            if FRAGMENT==True :
                if  SECURITY=="reality" :
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                else:
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    
            else:
                if  SECURITY=="reality" :
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,realitySettings=outboundBean_Stream_tlssettings)
                else:
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,tlsSettings=outboundBean_Stream_tlssettings)
                                        
            outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="vmess", settings=V2rayConfig.OutboundBean.OutSettingsBean(vnext=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean (address=ADDRESS, port=PORT, users=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean.UsersBean(id=ID,security=SCY,level=8,encryption="",flow="",alterId=ALTERID)])]),mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),streamSettings=outboundBean_Stream_tcp)    
        elif conifg.startswith("trojan://"):
        
                
            header=V2rayConfig.OutboundBean.HeaderBean()
            if HEADER_TYPE=="http" and TYPE=="tcp":
                headers=V2rayConfig.OutboundBean.HeadersBean(Connection=["keep-alive"], Host=[R_HOST],Pragma="no-cache",acceptEncoding=["gzip, deflate"],userAgent=["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/53.0.2785.109 Mobile/14A456 Safari/601.1.46"])
                requests=V2rayConfig.OutboundBean.RequestBean(headers=headers,method="GET",path=PATH,version="1.1")
                header=V2rayConfig.OutboundBean.HeaderBean(type="http",request=requests)
            
            outboundBean_Stream_tcpsettings=V2rayConfig.OutboundBean.TcpSettingsBean(header=header)
            if TYPE=="kcp":
                outboundBean_Stream_kcp_settings=V2rayConfig.OutboundBean.KcpSettingsBean(congestion=False,downlinkCapacity=100,header=V2rayConfig.OutboundBean.HeaderBean(type=HEADER_TYPE),mtu=1350,readBufferSize=1,seed=PATH,tti=50,uplinkCapacity=12,writeBufferSize=1)
            elif TYPE=="ws":
                outboundBean_Stream_ws_settings=V2rayConfig.OutboundBean.WsSettingsBean(headers=V2rayConfig.OutboundBean.HeadersBean(Host=R_HOST,userAgent=None,acceptEncoding=None,Connection=None,Pragma=None,Host_single=None),path=PATH)
            elif TYPE=="httpupgrade":
                outboundBean_Stream_httpupgrade_settings=V2rayConfig.OutboundBean.HttpupgradeSettingsBean(host=R_HOST,path=PATH)
            elif TYPE=="splithttp":
                outboundBean_Stream_splithttp_settings=V2rayConfig.OutboundBean.SplithttpSettingsBean(host=R_HOST,path=PATH)
            elif TYPE=="h2":
                outboundBean_Stream_h2_settings=V2rayConfig.OutboundBean.HttpSettingsBean(host=[R_HOST],path=PATH)
            elif TYPE=="quic":
                outboundBean_Stream_quic_settings=V2rayConfig.OutboundBean.QuicSettingBean(header=V2rayConfig.OutboundBean.HeaderBean(type=HEADER_TYPE),key=PATH,security=R_HOST)
            elif TYPE=="grpc":
                outboundBean_Stream_grpc_settings=V2rayConfig.OutboundBean.GrpcSettingsBean(authority=R_HOST,multiMode=MODE,)
            
            if SECURITY!="reality":
                outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=True,alpn=ALPN,fingerprint=FP,serverName=SNI,show=False)
            else:
                outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=True,alpn=ALPN,fingerprint=FP,publicKey=PBK,serverName=SNI,shortId=SID,spiderX=SPX,show=False)
            
            if FRAGMENT==True:
                if  SECURITY=="reality" :
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                else:
                    
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,tlsSettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                                    
            else:
                if  SECURITY=="reality" :
                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,realitySettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,realitySettings=outboundBean_Stream_tlssettings)
                else:

                    if TYPE=="tcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="kcp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="ws":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="httpupgrade":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="splithttp":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="h2":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="quic":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,tlsSettings=outboundBean_Stream_tlssettings)
                    elif TYPE=="grpc":
                        outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,tlsSettings=outboundBean_Stream_tlssettings)
                                                
            outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="trojan" ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),streamSettings=outboundBean_Stream_tcp,settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS, port=PORT,method= "chacha20-poly1305", ota=False,level=8,password=PASS)] ))
        elif conifg.startswith("ss://"):
            sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255)
            if FRAGMENT==True:
                outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="shadowsocks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="",sockopt=sockopt) ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password=PASS)] ))
            else:
                outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="shadowsocks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="") ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean ( address=ADDRESS, port=PORT,method=METHOD, ota=False,level=8,password=PASS)] ))
        elif conifg.startswith("socks://"):
            FRAGMENT=False
            sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255)
            if FRAGMENT==False:
                if PASS=="" and USER=="":
                    outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="socks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="") ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password="")] ))
                else:
                    outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="socks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="") ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password="",users=V2rayConfig.OutboundBean.OutSettingsBean.ServersBean.SocksUsersBean(level=8,passw=PASS,user=USER))] ))
        elif conifg.startswith("wireguard://"):
            FRAGMENT=False
            is_warp=True
            dnsBean=V2rayConfig.DnsBean(hosts={"geosite:category-ads-all":"127.0.0.1","geosite:category-ads-ir":"127.0.0.1"},servers=[V2rayConfig.DnsBean.ServersBean(address="fakedns",domains=["geosite:category-ads-all","geosite:category-ads-ir"],expectIPs="geoip:ir"),"https://8.8.8.8/dns-query"],fakedns=V2rayConfig.FakednsBean(ipPool="198.18.0.0/15",poolSize=10000))

            outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="wireguard",settings=V2rayConfig.OutboundBean.OutSettingsBean(address=ADDRESS, mtu=MTU,reserved=RESERVED,secretKey=SECERKEY,wnoise=WNOISE,wnoisecount=WNOISECOUNT,wnoisedelay=WNOISEDELAY,wpayloadsize=WPAYLOADSIZE,keepAlive=KEEPALIVE,peers=[V2rayConfig.OutboundBean.OutSettingsBean.WireGuardBean(endpoint=ENDPOINT+":"+str(PORT) ,publicKey=PBK)]))

            routingBean=V2rayConfig.RoutingBean(domainStrategy="IPIfNonMatch",rules=[V2rayConfig.RoutingBean.RulesBean(type="field",inboundTag=["dns-in"],outboundTag="dns-out"),V2rayConfig.RoutingBean.RulesBean(ip=["geoip:ir","geoip:private"],outboundTag="direct",type="field"),V2rayConfig.RoutingBean.RulesBean(domain=["domain:ir", "geosite:category-ir","geosite:private"],outboundTag="direct",type="field"),V2rayConfig.RoutingBean.RulesBean(domain=["geosite:category-ads-all","geosite:category-ads-ir"],outboundTag="block",type="field")])

            inboundBean = V2rayConfig.InboundBean(tag="socks",listen="127.0.0.1",port=10808, protocol="socks", sniffing=V2rayConfig.InboundBean.SniffingBean(enabled=True, destOverride=["http","tls","fakedns"]),settings=V2rayConfig.InboundBean.InSettingsBean(auth="noauth",udp=True,userLevel=8))
            inboundBean2=V2rayConfig.InboundBean(tag="http", listen="127.0.0.1",port=10809, protocol="http",settings=V2rayConfig.InboundBean.InSettingsBean(userLevel=8)) 
            inboundBean3=V2rayConfig.InboundBean(listen="127.0.0.1",port=10853,protocol="dokodemo-door",settings=V2rayConfig.InboundBean.InSettingsBean(address="8.8.8.8", network="tcp,udp", port=53), tag="dns-in")


        end_outbound_bf_frg_set=V2rayConfig.OutboundBean.BeforeFrgSettings(tag="direct",protocol="freedom",settings={})
        end_outbound_bf_frg_set2=V2rayConfig.OutboundBean.BeforeFrgSettings(tag="block",protocol="blackhole",settings={"response":{"type":"http"}})
        if FRAGMENT==True:
            if FAKEHOST_ENABLE==True:
                frg=V2rayConfig.OutboundBean.OutSettingsBean.FragmentBean(packets=PACKETS,length=LENGTH,interval=INTERVAL,host1_domain=HOST1_DOMAIN,host2_domain=HOST2_DOMAIN)
            else:
                frg=V2rayConfig.OutboundBean.OutSettingsBean.FragmentBean(packets=PACKETS,length=LENGTH,interval=INTERVAL)
            frg_stream=V2rayConfig.OutboundBean.StreamSettingsBean(network=None,security=None,sockopt=V2rayConfig.OutboundBean.SockoptBean(TcpNoDelay=True,tcpKeepAliveIdle=100,mark=255))
            bf_frg_set=V2rayConfig.OutboundBean.BeforeFrgSettings(tag="fragment",protocol="freedom",settings=frg,streamSettings=frg_stream)


            config = V2rayConfig(log=logBean,dns=dnsBean,  inbounds=[inboundBean,inboundBean2], outbounds=[outboundBean,bf_frg_set,end_outbound_bf_frg_set,end_outbound_bf_frg_set2],remarks=REMARKS,routing=routingBean)
        else:
            if is_warp==False:
                config = V2rayConfig(log=logBean,dns=dnsBean, inbounds=[inboundBean,inboundBean2], outbounds=[outboundBean,end_outbound_bf_frg_set,end_outbound_bf_frg_set2],remarks=REMARKS,routing=routingBean)
            else:
                bf_after_warp_set=V2rayConfig.OutboundBean.BeforeFrgSettings(protocol="freedom",settings={"domainStrategy": "UseIP"},tag="direct")
                after_warp_set=V2rayConfig.OutboundBean.BeforeFrgSettings(protocol="blackhole",settings={"response":{"type": "http"}},tag="block")
                after_warp_set2=V2rayConfig.OutboundBean.BeforeFrgSettings(protocol="dns",tag="dns-out")

                config = V2rayConfig(log=logBean,stats={},dns=dnsBean, inbounds=[inboundBean,inboundBean2,inboundBean3], outbounds=[outboundBean,bf_after_warp_set,after_warp_set,after_warp_set2],remarks=REMARKS,routing=routingBean)
        data_conf=remove_nulls(config)

        data_conf=replace_accept_encoding(data_conf)

        data_conf=json.dumps(data_conf, indent=4, cls=MyEncoder)
        


        return data_conf



    ###########################################################################################

    def set_proxy(ip, port):
    # تنظیم پروکسی
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "ProxyEnable", 0, reg.REG_DWORD, 1)
        reg.SetValueEx(key, "ProxyServer", 0, reg.REG_SZ, f"{ip}:{port}")
        reg.CloseKey(key)
        print("Proxy has been set.")

    def remove_proxy():
       
            
        # حذف پروکسی
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "ProxyEnable", 0, reg.REG_DWORD, 0)
        reg.SetValueEx(key, "ProxyServer", 0, reg.REG_SZ, "")
        reg.CloseKey(key)
        print("Proxy has been removed.")
    def test_connection():
        global concted
        result = ""
      
        time.sleep(3)
        conn=concted
        concted=True

        with open("xray/"+selec_sub.get(), "r",encoding="utf-8") as f:
            conf_simple=f.readlines()
            if selec_sub.get()!="user_confs":
                conf_simple=conf_simple[:len(conf_simple)-1]
            conf_simple=remove_empty_strings(conf_simple)
        with open("xray/count", "r") as f:
            wch_sel=int(f.readline())
        with open("xray/config.json", "w") as f:
            f.write(parse_configs(conf_simple[wch_sel]))
        with open("xray/config.json" , "r") as f:
            temp3 = json.load(f)
        port=value=temp3["inbounds"][1]["port"]
        if conn==False:
            set_proxy("127.0.0.1",port )


        try:
            proxies = {
                "http": f"http://127.0.0.1:{port}"
            }
            url = "https://www.google.com/generate_204"
            headers = {"Connection": "close"}
            
            try:
                start = time.time()
                response = requests.get(url, proxies=proxies, timeout=5, headers=headers)
            except Exception:
                start = time.time()
                response = requests.get(url, proxies=proxies, timeout=15, headers=headers)
            elapsed = (time.time() - start) * 1000  # تبدیل به میلی‌ثانیه
            

            if response.status_code == 204 or (response.status_code == 200 and len(response.content) == 0):
                result = f"Connection test available, time elapsed: {int(elapsed)} ms"
            else:
                raise IOError(f"Connection test error, status code: {response.status_code}")
        except RequestException as e:
            print(f"testConnection RequestException: {e}")
            result = f"Connection test error: {str(e)}"
        except Exception as e:
            print(f"testConnection Exception: {e}")
            result = f"Connection test error: {str(e)}"
        ping_la.configure(text=result)
        ping_la.bind("<Button-1>" ,th_test_connection2)
        if conn==True:
            return
        ttemp=what_ip()
        print(ttemp)
        if ttemp:
            if ttemp[0]!="Unavailable":
                try:
                    ip_loc =ctk.CTkImage(light_image=Image.open(f"imgs/{ttemp[0].lower()}.png"),
                                    dark_image=Image.open(f"imgs/{ttemp[0].lower()}.png"),
                                    size=(25, 25))
                except Exception:
                    ip_loc=False
            else:
                try:
                    ip_loc =ctk.CTkImage(light_image=Image.open(f"imgs/{ttemp[1].lower()}.png"),
                                  dark_image=Image.open(f"imgs/{ttemp[1].lower()}.png"),
                                  size=(25, 25))
                except Exception:
                    ip_loc=False
        if ip_loc!=False:
             
            ipp_la.configure(image=ip_loc,text=" ")
            
        return result
    def th_test_connection():
        theard3=threading.Thread(target=test_connection)
        theard3.start()
    def th_test_connection2(test):
        theard3=threading.Thread(target=test_connection)
        theard3.start()
    def conc():
        global concted
        
        
        

        config_abs=os.path.abspath("xray/config.json")
        xray_abs=os.path.abspath("xray/xray.exe")
        if concted==True:
            conc_button.configure(text="stop!")
            concted=False
            ping_la.unbind("<Button-1>" )
            remove_proxy()

            subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
            subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
            ping_la.configure(text="\nclick to connect ")
            
            return
        ping_la.configure(text="wait ...")
        conc_button.configure(text="connected!")
        
        
        th_test_connection()
        def s_xray():
        # os.system(xray_abs+" run -c "+config_abs)
            subprocess.call([xray_abs, 'run', '-c' ,config_abs],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW )
        def theaerd_s_xray():
            thraaed=threading.Thread(target=s_xray)
            thraaed.start()
        theaerd_s_xray()
                
        # with open('output.log', 'w') as output_file:
        #     subprocess.Popen([xray_abs, 'run', '-c', config_abs], 
        #                     stdout=output_file,
        #                     stderr=subprocess.STDOUT,
        #                     creationflags=subprocess.CREATE_NO_WINDOW)

        
        
    def theard_conc():
        theard=threading.Thread(target=conc)
        theard.start()


    def wireguard_config_main(which_ip):
  
            
            global Cpu_speed
            global max_workers_number
            global sorted_results
            global i_ip_scan, myscannerconf
            global wire_p
            global best_result
            global best_ip_mix
            labelmain1.configure(text="\n\n\n\nwait ... ")
            



            max_workers_number=0
            
            if Cpu_speed == "1":
                max_workers_number=100
            elif Cpu_speed == "2":
                max_workers_number=50
            def upload_to_bashupload(config_data):

               
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
                    tabview.tab("main").clipboard_clear()
                    tabview.tab("main").clipboard_append(str(true))
              
                else:
                    label_best.insert(1.0, "Error try again")
   
                

                
            
            def generate_ipv6():
                    return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"
            def ping_ip(ip, port):
                    global results
                    global best_ip
                    global best_result_avg

                    
                    
                    
                    icmp=pinging(ip, count=count_see ,interval=interval_see,timeout=timeout_see,family="ipv6")
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
                global i_ip_scan,myscannerconf
                global is_v2ray
                global best_ip_mix
                global wire_config_temp
                global wire_p
                global header
                best_result[0]= best_ip_mix[0]
                if not "[" in best_ip_mix[0]:
                    best_result[0]="["+best_ip_mix[0]+"]"
                best_result[1]= best_ip_mix[1]

                
                if  myscannerconf==True:
                    all_key=["NONe" , "none" , "none" , "ghjgj"]

                    try:
                        all_key=free_cloudflare_account()
                    except Exception as E:
                        all_key=free_cloudflare_account()
                    
            
                    try:
                        all_key2=free_cloudflare_account()
                    except Exception as E:
                        all_key2=free_cloudflare_account()
                    with open("warp_setting" , "r") as f:
                        num33=f.readlines()
                    print(optionmenu_gi.get())
                    isIran="1"
                    
                    if optionmenu_gi.get()=="Iran":
                        isIran="1"
                    elif optionmenu_gi.get()=="German":
                        isIran="2"
                    Wow=""


           
        
             
                    Wow=f'''{{
            "dns": {{
                "hosts": {{
                "geosite:category-ads-all": "127.0.0.1",
                "geosite:category-ads-ir": "127.0.0.1"'''

                    
                        
                    if isIran=='1' :
                            Wow+=f'''
                }},
                "servers": [
                "https://94.140.14.14/dns-query",
                {{
                    "address": "8.8.8.8",
                    "domains": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],
                    "expectIPs": [
                    "geoip:ir"
                    ],
                    "port": 53
                }}
                ],
                "tag": "dns"
            }},
            "inbounds": [
                {{
                "port": 10808,
                "protocol": "socks",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "socks-in"
                }},
                {{
                "port": 10809,
                "protocol": "http",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "http-in"
                }},
                {{
                "listen": "127.0.0.1",
                "port": 10853,
                "protocol": "dokodemo-door",
                "settings": {{
                    "address": "1.1.1.1",
                    "network": "tcp,udp",
                    "port": 53
                }},
                "tag": "dns-in"
                }}
            ],
            "log": {{
                "loglevel": "warning"
            }},
            "outbounds": [
                {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                    "172.16.0.2/32",
                    "{all_key[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                    {{
                        "endpoint": "{best_result[0]}:{best_result[1]}",
                        "publicKey": "{all_key[3]}"
                    }}
                    ],
                    "reserved": {all_key[2]},
                    "secretKey": "{all_key[1]}"'''
                            if num33[9]=="1\n":Wow+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
                            Wow+=f'''
                }},
                "tag": "warp"
                }},
                {{
                "protocol": "dns",
                "tag": "dns-out"
                }},
                {{
                "protocol": "freedom",
                "settings": {{}},
                "tag": "direct"
                }},
                {{
                "protocol": "blackhole",
                "settings": {{
                    "response": {{
                    "type": "http"
                    }}
                }},
                "tag": "block"
                }}
            ],
            "policy": {{
                "levels": {{
                "8": {{
                    "connIdle": 300,
                    "downlinkOnly": 1,
                    "handshake": 4,
                    "uplinkOnly": 1
                }}
                }},
                "system": {{
                "statsOutboundUplink": true,
                "statsOutboundDownlink": true
                }}
            }},
            "remarks": "Tel= Arshiacomplus - Warp",
            "routing": {{
                "domainStrategy": "IPIfNonMatch",
                "rules": [
                {{
                    "inboundTag": [
                    "dns-in"
                    ],
                    "outboundTag": "dns-out",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "8.8.8.8"
                    ],
                    "outboundTag": "direct",
                    "port": "53",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "geoip:ir",
                    "geoip:private"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ads-all",
                    "geosite:category-ads-ir"'''
                    
                            Wow+='''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                },
                {
                    "network": "tcp,udp",
                    "outboundTag": "warp",
                    "type": "field"
                }
                ]
            },
            "stats": {}
            }'''
                    if isIran == '2' :
                            Wow+=f'''
                }},
                "servers": [
                "https://94.140.14.14/dns-query",
                {{
                    "address": "8.8.8.8",
                    "domains": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],                                                              "expectIPs": [                                                    "geoip:ir"
                    ],
                    "port": 53                                                    }}
                ],
                "tag": "dns"                                                  }},
            "inbounds": [
                {{
                "port": 10808,
                "protocol": "socks",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "socks-in"
                }},
                {{
                "port": 10809,
                "protocol": "http",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "http-in"
                }},
                {{
                "listen": "127.0.0.1",
                "port": 10853,
                "protocol": "dokodemo-door",
                "settings": {{
                    "address": "1.1.1.1",
                    "network": "tcp,udp",
                    "port": 53
                }},
                "tag": "dns-in"
                }}
            ],
            "log": {{
                "loglevel": "warning"
            }},
            "outbounds": [
                {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                    "172.16.0.2/32",
                    "{all_key[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                    {{
                        "endpoint": "{best_result[0]}:{best_result[1]}",
                        "publicKey": "{all_key[3]}"
                    }}
                    ],
                    "reserved": {all_key[2]},
                    "secretKey": "{all_key[1]}"
                }},
                "streamSettings": {{
                    "network": "tcp",
                    "security": "",
                    "sockopt": {{
                    "dialerProxy": "warp-ir"
                    }}
                }},
                "tag": "warp-out"
                }},
                {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                    "172.16.0.2/32",
                    "{all_key2[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                    {{
                        "endpoint": "{best_result[0]}:{best_result[1]}",
                        "publicKey": "{all_key[3]}"
                    }}
                    ],
                    "reserved": {all_key2[2]},
                    "secretKey": "{all_key2[1]}"'''
                            if num33[9]=="1\n":Wow+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
                            Wow+=f'''
                }},
                "tag": "warp-ir"
                }},
                {{
                "protocol": "dns",
                "tag": "dns-out"
                }},
                {{
                "protocol": "freedom",
                "settings": {{}},
                "tag": "direct"
                }},
                {{
                "protocol": "blackhole",
                "settings": {{
                    "response": {{
                    "type": "http"
                    }}
                }},
                "tag": "block"
                }}
            ],
            "policy": {{
                "levels": {{
                "8": {{
                    "connIdle": 300,
                    "downlinkOnly": 1,
                    "handshake": 4,
                    "uplinkOnly": 1
                }}
                }},
                "system": {{
                "statsOutboundUplink": true,
                "statsOutboundDownlink": true
                }}
            }},
            "remarks": "Tel = arshiacomplus - WoW",
            "routing": {{
                "domainStrategy": "IPIfNonMatch",
                "rules": [
                {{
                    "inboundTag": [
                    "dns-in"
                    ],
                    "outboundTag": "dns-out",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "8.8.8.8"
                    ],
                    "outboundTag": "direct",
                    "port": "53",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "geoip:ir",
                    "geoip:private"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ads-all",
                    "geosite:category-ads-ir"'''
                        
                    if isIran == '2' :
               
                        Wow+=f'''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                }},
                {{
                    "network": "tcp,udp",
                    "outboundTag": "warp-out",
                    "type": "field"
                }},
                {{
                    "network": "tcp,udp",
                    "outboundTag": "warp",
                    "type": "field"
                }}
                ]
            }},
            "stats": {{}}
            }}'''
                    with open("xray/config.json" , "w") as f:
                        f.write(Wow)
                    label_best.insert(1.0 ,Wow)
                    tabview.tab("main").clipboard_clear()
                    tabview.tab("main").clipboard_append(f"{Wow}")

                    labelmain1.configure(text="\n\n\n\nClick to scan ip")

                
                    return
                if  is_v2ray==True :

                    


                    configure = fetch_config_from_api()
                    wireguard_url = generate_wireguard_url(configure, f"[{ip}]"+":"+str(port))

                    tabview.tab("main").clipboard_clear()
                    tabview.tab("main").clipboard_append(wireguard_url)

                    label_best.insert(1.0, wireguard_url)
                    labelmain1.configure(text="\n\n\n\nClick to scan ip")

                    return
                all_key=[]
                
                try:
                    all_key=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    
                all_key2=[]
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    

                if is_sub == False  and is_v2ray==False:


                    with open("warp_setting" , "r") as f:
                        num=f.readlines()
                        
                        if  num[8] =="2\n":
                                hi_from="1"

                        elif  num[8] =="1\n":
                                hi_from="2"
                                
                    conf=""
                    if hi_from=="1":
                        conf=temp_sing_old
                    elif hi_from=="2":
                        conf=temp_sing_new
     
                    conf["outbounds"][0]['local_address'][1]=all_key[0]
                    conf["outbounds"][0]['private_key']=all_key[1]
                    conf["outbounds"][0]['reserved']=all_key[2]
                    conf["outbounds"][0]['peer_public_key']=all_key[3]
                    conf["outbounds"][0]['peer_public_key']=all_key[3]
                    conf["outbounds"][0]['server']=best_result[0]
                    conf["outbounds"][0]['server_port']=best_result[1]
                    conf["outbounds"][0]['tag']='Tel=@arshiacomplus Warp-IR'
                    conf["outbounds"][1]['local_address'][1]=all_key2[0]
                    conf["outbounds"][1]['private_key']=all_key2[1]
                    conf["outbounds"][1]['reserved']=all_key2[2]
                    conf["outbounds"][1]['peer_public_key']=all_key2[3]
                    conf["outbounds"][1]['peer_public_key']=all_key2[3]
                    conf["outbounds"][1]['server']=best_result[0]
                    conf["outbounds"][1]['server_port']=best_result[1]
                    conf["outbounds"][1]['tag']='Tel=@arshiacomplus Warp-Main'
                    conf["outbounds"][1]['detour']='Tel=@arshiacomplus Warp-IR'


                    conf=str(conf).replace("'", '"')

                    label_best.insert(1.0 ,conf)
                    tabview.tab("main").clipboard_clear()
                    tabview.tab("main").clipboard_append(f"{conf}")

                    labelmain1.configure(text="\n\n\n\nClick to scan ip")
                    return      
                if is_sub ==True  and is_v2ray==False:  
                               
                    
                    

                    with open("warp_setting" , "r") as f:
                                num=f.readlines()
                                
                                if  num[8] =="2\n":
                                        hi_from="1"
                                elif  num[8] =="1\n":
                                        hi_from="2"
                                        
                    conf=""
                    conf2=""
                    if hi_from=="1":
                        conf=temp_sing_old["outbounds"][0]
                        conf2=temp_sing_old["outbounds"][1]
                    elif hi_from=="2":
                        conf=temp_sing_new["outbounds"][0]
                        conf2=temp_sing_new["outbounds"][1]
                  
                    conf['local_address'][1]=all_key[0]
                    conf['private_key']=all_key[1]
                    conf['reserved']=all_key[2]
                    conf['peer_public_key']=all_key[3]
                    conf['peer_public_key']=all_key[3]
                    conf['server']=best_result[0]
                    conf['server_port']=best_result[1]
                    conf['tag']='Tel=@arshiacomplus Warp-IR'+str(i)
                    conf2['local_address'][1]=all_key2[0]
                    conf2['private_key']=all_key2[1]
                    conf2['reserved']=all_key2[2]
                    conf2['peer_public_key']=all_key2[3]
                    conf2['peer_public_key']=all_key2[3]
                    conf2['server']=best_result[0]
                    conf2['server_port']=best_result[1]
                    conf2['tag']='Tel=@arshiacomplus Warp-Main'+str(i)
                    conf2['detour']='Tel=@arshiacomplus Warp-IR'+str(i)
                    if wire_p==0:
                        wire_config_temp+=f"{conf}"+f",{conf2}"
                    else:
                         
                        wire_config_temp+=f",{conf}"+f",{conf2}"

                    
                    

                    print(header)

                    
               
                    
                    time.sleep(8)
                    print(i)
                    wire_p=1  




            def check_ac(i):
                
                
                global i_ip_scan,myscannerconf
                global is_sub
                global best_result
                global save_result
                global is_v2ray
                global wire_c
                global temp_conf
                global wire_config_temp

                global header
                global wire_p


                
                    
                if wire_p==0 and i_ip_scan==False:
                    ip, port, ping, loss_rate,jitter, combined_score=best_result
                    best_result=[1]*2
                    best_result[0]=ip
            
                    best_result[1]=int(port)
                else:
                    ip ,port=best_result
                all_key=["NONe" , "none" , "none" , "ghjgj"]

                try:
                    all_key=free_cloudflare_account()
                except Exception as E:
                    all_key=free_cloudflare_account()
                   
        
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    all_key2=free_cloudflare_account()

                if  myscannerconf==True:
                    with open("warp_setting" , "r") as f:
                        num33=f.readlines()
                    print(optionmenu_gi.get())
                    isIran="1"
                    
                    if optionmenu_gi.get()=="Iran":
                        isIran="1"
                    elif optionmenu_gi.get()=="German":
                        isIran="2"
                    Wow=""


           
        
             
                    Wow=f'''{{
            "dns": {{
                "hosts": {{
                "geosite:category-ads-all": "127.0.0.1",
                "geosite:category-ads-ir": "127.0.0.1"'''

                    
                        
                    if isIran=='1' :
                            Wow+=f'''
                }},
                "servers": [
                "https://94.140.14.14/dns-query",
                {{
                    "address": "8.8.8.8",
                    "domains": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],
                    "expectIPs": [
                    "geoip:ir"
                    ],
                    "port": 53
                }}
                ],
                "tag": "dns"
            }},
            "inbounds": [
                {{
                "port": 10808,
                "protocol": "socks",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "socks-in"
                }},
                {{
                "port": 10809,
                "protocol": "http",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "http-in"
                }},
                {{
                "listen": "127.0.0.1",
                "port": 10853,
                "protocol": "dokodemo-door",
                "settings": {{
                    "address": "1.1.1.1",
                    "network": "tcp,udp",
                    "port": 53
                }},
                "tag": "dns-in"
                }}
            ],
            "log": {{
                "loglevel": "warning"
            }},
            "outbounds": [
                {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                    "172.16.0.2/32",
                    "{all_key[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                    {{
                        "endpoint": "{best_result[0]}:{best_result[1]}",
                        "publicKey": "{all_key[3]}"
                    }}
                    ],
                    "reserved": {all_key[2]},
                    "secretKey": "{all_key[1]}"'''
                            if num33[9]=="1\n":Wow+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
                            Wow+=f'''
                }},
                "tag": "warp"
                }},
                {{
                "protocol": "dns",
                "tag": "dns-out"
                }},
                {{
                "protocol": "freedom",
                "settings": {{}},
                "tag": "direct"
                }},
                {{
                "protocol": "blackhole",
                "settings": {{
                    "response": {{
                    "type": "http"
                    }}
                }},
                "tag": "block"
                }}
            ],
            "policy": {{
                "levels": {{
                "8": {{
                    "connIdle": 300,
                    "downlinkOnly": 1,
                    "handshake": 4,
                    "uplinkOnly": 1
                }}
                }},
                "system": {{
                "statsOutboundUplink": true,
                "statsOutboundDownlink": true
                }}
            }},
            "remarks": "Tel= Arshiacomplus - Warp",
            "routing": {{
                "domainStrategy": "IPIfNonMatch",
                "rules": [
                {{
                    "inboundTag": [
                    "dns-in"
                    ],
                    "outboundTag": "dns-out",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "8.8.8.8"
                    ],
                    "outboundTag": "direct",
                    "port": "53",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "geoip:ir",
                    "geoip:private"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ads-all",
                    "geosite:category-ads-ir"'''
                    
                            Wow+='''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                },
                {
                    "network": "tcp,udp",
                    "outboundTag": "warp",
                    "type": "field"
                }
                ]
            },
            "stats": {}
            }'''
                    if isIran == '2' :
                            Wow+=f'''
                }},
                "servers": [
                "https://94.140.14.14/dns-query",
                {{
                    "address": "8.8.8.8",
                    "domains": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],                                                              "expectIPs": [                                                    "geoip:ir"
                    ],
                    "port": 53                                                    }}
                ],
                "tag": "dns"                                                  }},
            "inbounds": [
                {{
                "port": 10808,
                "protocol": "socks",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "socks-in"
                }},
                {{
                "port": 10809,
                "protocol": "http",
                "settings": {{
                    "auth": "noauth",
                    "udp": true,
                    "userLevel": 8
                }},
                "sniffing": {{
                    "destOverride": [
                    "http",
                    "tls"
                    ],
                    "enabled": true
                }},
                "tag": "http-in"
                }},
                {{
                "listen": "127.0.0.1",
                "port": 10853,
                "protocol": "dokodemo-door",
                "settings": {{
                    "address": "1.1.1.1",
                    "network": "tcp,udp",
                    "port": 53
                }},
                "tag": "dns-in"
                }}
            ],
            "log": {{
                "loglevel": "warning"
            }},
            "outbounds": [
                {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                    "172.16.0.2/32",
                    "{all_key[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                    {{
                        "endpoint": "{best_result[0]}:{best_result[1]}",
                        "publicKey": "{all_key[3]}"
                    }}
                    ],
                    "reserved": {all_key[2]},
                    "secretKey": "{all_key[1]}"
                }},
                "streamSettings": {{
                    "network": "tcp",
                    "security": "",
                    "sockopt": {{
                    "dialerProxy": "warp-ir"
                    }}
                }},
                "tag": "warp-out"
                }},
                {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                    "172.16.0.2/32",
                    "{all_key2[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                    {{
                        "endpoint": "{best_result[0]}:{best_result[1]}",
                        "publicKey": "{all_key[3]}"
                    }}
                    ],
                    "reserved": {all_key2[2]},
                    "secretKey": "{all_key2[1]}"'''
                            if num33[9]=="1\n":Wow+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
                            Wow+=f'''
                }},
                "tag": "warp-ir"
                }},
                {{
                "protocol": "dns",
                "tag": "dns-out"
                }},
                {{
                "protocol": "freedom",
                "settings": {{}},
                "tag": "direct"
                }},
                {{
                "protocol": "blackhole",
                "settings": {{
                    "response": {{
                    "type": "http"
                    }}
                }},
                "tag": "block"
                }}
            ],
            "policy": {{
                "levels": {{
                "8": {{
                    "connIdle": 300,
                    "downlinkOnly": 1,
                    "handshake": 4,
                    "uplinkOnly": 1
                }}
                }},
                "system": {{
                "statsOutboundUplink": true,
                "statsOutboundDownlink": true
                }}
            }},
            "remarks": "Tel = arshiacomplus - WoW",
            "routing": {{
                "domainStrategy": "IPIfNonMatch",
                "rules": [
                {{
                    "inboundTag": [
                    "dns-in"
                    ],
                    "outboundTag": "dns-out",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "8.8.8.8"
                    ],
                    "outboundTag": "direct",
                    "port": "53",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ir",
                    "domain:.ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "ip": [
                    "geoip:ir",
                    "geoip:private"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "domain": [
                    "geosite:category-ads-all",
                    "geosite:category-ads-ir"'''
                        
                    if isIran == '2' :
               
                        Wow+=f'''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                }},
                {{
                    "network": "tcp,udp",
                    "outboundTag": "warp-out",
                    "type": "field"
                }},
                {{
                    "network": "tcp,udp",
                    "outboundTag": "warp",
                    "type": "field"
                }}
                ]
            }},
            "stats": {{}}
            }}'''
                    with open("xray/config.json" , "w") as f:
                        f.write(Wow)
                    label_best.insert(1.0 ,Wow)
                    tabview.tab("main").clipboard_clear()
                    tabview.tab("main").clipboard_append(f"{Wow}")

                    labelmain1.configure(text="\n\n\n\nClick to scan ip")

                
                    return


                if is_sub == False and is_v2ray==False:
                    best_result[1]=int(best_result[1])

                    with open("warp_setting" , "r") as f:
                        num=f.readlines()
                        
                        if  num[8] =="2\n":
                                hi_from="1"

                        elif  num[8] =="1\n":
                                hi_from="2"
                                
                    conf=""
                    if hi_from=="1":
                        conf=temp_sing_old
                    elif hi_from=="2":
                        conf=temp_sing_new
     
                    conf["outbounds"][0]['local_address'][1]=all_key[0]
                    conf["outbounds"][0]['private_key']=all_key[1]
                    conf["outbounds"][0]['reserved']=all_key[2]
                    conf["outbounds"][0]['peer_public_key']=all_key[3]
                    conf["outbounds"][0]['peer_public_key']=all_key[3]
                    conf["outbounds"][0]['server']=best_result[0]
                    conf["outbounds"][0]['server_port']=best_result[1]
                    conf["outbounds"][0]['tag']='Tel=@arshiacomplus Warp-IR'
                    conf["outbounds"][1]['local_address'][1]=all_key2[0]
                    conf["outbounds"][1]['private_key']=all_key2[1]
                    conf["outbounds"][1]['reserved']=all_key2[2]
                    conf["outbounds"][1]['peer_public_key']=all_key2[3]
                    conf["outbounds"][1]['peer_public_key']=all_key2[3]
                    conf["outbounds"][1]['server']=best_result[0]
                    conf["outbounds"][1]['server_port']=best_result[1]
                    conf["outbounds"][1]['tag']='Tel=@arshiacomplus Warp-Main'
                    conf["outbounds"][1]['detour']='Tel=@arshiacomplus Warp-IR'
     

                    conf=str(conf).replace("'", '"')

                    label_best.insert(1.0 ,conf)
                    tabview.tab("main").clipboard_clear()
                    tabview.tab("main").clipboard_append(f"{conf}")

                    labelmain1.configure(text="\n\n\n\nClick to scan ip")
                    return


                if is_v2ray==True:
                    
                    

                    configure = fetch_config_from_api()
                    wireguard_url = generate_wireguard_url(configure, f"{ip}"+":"+str(port))

                    tabview.tab("main").clipboard_clear()
                    tabview.tab("main").clipboard_append(wireguard_url)


                    label_best.insert(1.0, wireguard_url)
                    labelmain1.configure(text="\n\n\n\nClick to scan ip")

                    return
                
                # ip, port, ping, loss_rate,jitter, combined_score = best_result
                # best_result=[0]*2
                # best_result[0]=f"{ip}"
                # best_result[1]=port

                   

                
                if is_sub ==True:


                    with open("warp_setting" , "r") as f:
                                num=f.readlines()
                                
                                if  num[8] =="2\n":
                                        hi_from="1"
                                elif  num[8] =="1\n":
                                        hi_from="2"
                                        
                    conf=""
                    conf2=""
                    if hi_from=="1":
                        conf=temp_sing_old["outbounds"][0]
                        conf2=temp_sing_old["outbounds"][1]
                    elif hi_from=="2":
                        conf=temp_sing_new["outbounds"][0]
                        conf2=temp_sing_new["outbounds"][1]
                  
                    conf['local_address'][1]=all_key[0]
                    conf['private_key']=all_key[1]
                    conf['reserved']=all_key[2]
                    conf['peer_public_key']=all_key[3]
                    conf['peer_public_key']=all_key[3]
                    conf['server']=best_result[0]
                    conf['server_port']=best_result[1]
                    conf['tag']='Tel=@arshiacomplus Warp-IR'+str(i)
                    conf2['local_address'][1]=all_key2[0]
                    conf2['private_key']=all_key2[1]
                    conf2['reserved']=all_key2[2]
                    conf2['peer_public_key']=all_key2[3]
                    conf2['peer_public_key']=all_key2[3]
                    conf2['server']=best_result[0]
                    conf2['server_port']=best_result[1]
                    conf2['tag']='Tel=@arshiacomplus Warp-Main'+str(i)
                    conf2['detour']='Tel=@arshiacomplus Warp-IR'+str(i)
                    if wire_p==0:
                        wire_config_temp+=f"{conf}"+f",{conf2}"
                    else:
                         
                        wire_config_temp+=f",{conf}"+f",{conf2}"

                    
                    

                    print(header)

                    
               
                    
                    time.sleep(8)
                    print(i)
                    wire_p=1                        
                    
                        

                            
                            
                    





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
                
            
                icmp=pinging(ip, count=count_see ,interval=interval_see,timeout=timeout_see,family="ipv4" )


                results.append((ip, port, float(icmp.avg_rtt) ,icmp.packet_loss,icmp.jitter))
                
            if i_ip_scan==True:
                def submit():
                    global best_result
                    best_result=[1]*2
                    best_result_temp=str(ip_entry.get())
                    best_result_temp2=str(port_entry.get())
                    best_result[0]=best_result_temp
                    best_result[1]=best_result_temp2
                    clear_widgets(rootip)

                    rootip.destroy(),check_ac("")



                

                rootip=ctk.CTk()
                rootip.protocol("WM_TAKE_FOCUS")
                rootip.title("main activity ")
                rootip.geometry("+200+200")


    
    
                label_ff=ctk.CTkLabel(rootip, text="Enter an ip/port")
                label_ff.pack(fill=tk.X)

                

                
                ip_entry=ctk.CTkEntry(rootip,placeholder_text="Just ip(v4/v6)")
                ip_entry.pack( padx=10, pady=10,fill=tk.X)
                port_entry=ctk.CTkEntry(rootip,placeholder_text="port")
                port_entry.pack( padx=10, pady=10,fill=tk.X)                
                rootip.after(0,focus(ip_entry))

                submitb=ctk.CTkButton(rootip, text="submit", command=submit)
                submitb.pack(fill=tk.X,padx=11, pady=4)
                submitb.bind("<Enter>", hand2)


                rootip.mainloop()
                

            else:
                if which_ip=="ipv6":
                    if i_ip_scan==True:
                        def submit():
                            global best_ip_mix
                            best_ip_mix=[1]*2
                            best_result_temp=str(ip_entry.get())
                            best_result_temp2=str(port_entry.get())
                            best_ip_mix[0]=best_result_temp
                            best_ip_mix[1]=best_result_temp2
                            clear_widgets(rootip)
                            rootip.destroy(),check_ac_v6("")



                        

                        rootip=ctk.CTk()
                        rootip.protocol("WM_TAKE_FOCUS")
                        rootip.title("main activity ")
                        rootip.geometry("+200+200")

            
                        label_ff=ctk.CTkLabel(rootip, text="Enter an ip/port")
                        label_ff.pack(fill=tk.X)

                        

                        
                        ip_entry=ctk.CTkEntry(rootip,placeholder_text="Just ip(v4/v6)")
                        ip_entry.pack( padx=10, pady=10,fill=tk.X)
                        port_entry=ctk.CTkEntry(rootip,placeholder_text="port")
                        port_entry.pack( padx=10, pady=10,fill=tk.X)                
                        rootip.after(0,focus(ip_entry))

                        submitb=ctk.CTkButton(rootip, text="submit", command=submit)
                        submitb.pack(fill=tk.X,padx=11, pady=4)
                        submitb.bind("<Enter>", hand2)


                        rootip.mainloop()


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
                        
                        if loss_rate == 0.00 and ping != 0.0 and ping < ping_range_see:
                            
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
                    best_result=[1]*2
                    best_result[0]=best_ip_mix[0]
                    best_result[1]=best_ip_mix[1]
                    labelmain1.configure(f"{best_result[0]}:{best_result[1]}")

                    
                    if is_sub ==True:

                            global wire_config_temp
                            global header
                     
                            wire_p =0
                            
                            for i in range(int(how_menypp.get())):


                                    check_ac_v6(best_ip_mix, i)
             
                            wire_config_temp=str(wire_config_temp).replace("'", '"')
                            
                            header["outbounds"].append(f'{wire_config_temp}')
                            
                            header=str(header).replace("'", '"')
                            header=list(header)
                            
                            header[15]=""
                            header[len(header)-3]=""
                            header="".join(header)
                            
                            upload_to_bashupload(header)
                            header=header_temp
                            wire_p=0


                    else:
                        wire_p =0
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
                    ip, port, ping, loss_rate,jitter, combined_score=best_result
                    labelmain1.configure(f"{ip}:{port}")
                
                    while len(sorted_results) < 10:
                        sorted_results.append(("No IP", None, None, 100, 1000))

                    if is_sub ==True:
                        
                            
                       
                    


                           
                            for i in range(int(how_menypp.get())):
                                        
                                        check_ac(i)
                                        time.sleep(1)
                
    
                            wire_config_temp=str(wire_config_temp).replace("'", '"')
                            
                            header["outbounds"].append(f'{wire_config_temp}')
                            
                            header=str(header).replace("'", '"')
                            header=list(header)
                            
                            header[15]=""
                            header[len(header)-3]=""
                            header="".join(header)
                            
                            upload_to_bashupload(header)
                            header=header_temp
                            wire_p=0
                    else:
                        check_ac("")
    def wireguard_config_without():
        global i_ip_scan
        global is_sub
        global is_v2ray
        global myscannerconf
        myscannerconf=False
        is_v2ray=False
        i_ip_scan=True
        is_sub=False
        wireguard_config_main(WH_ipVersion)
    def wireguard_config_sub():
        global is_sub
        global i_ip_scan
        global is_v2ray
        global myscannerconf
        myscannerconf=False
        is_v2ray=False
        i_ip_scan=False
        is_sub=True
        wireguard_config_main(WH_ipVersion)
    def v2ray():
        global is_v2ray
        global i_ip_scan
        global is_sub
        global myscannerconf
        myscannerconf=False
        i_ip_scan=False
        is_v2ray=True
        is_sub=False
        wireguard_config_main(WH_ipVersion)
    def v2ray_without():
        global is_v2ray
        global i_ip_scan
        global is_sub
        global myscannerconf
        myscannerconf=False
        i_ip_scan=True
        is_v2ray=True
        is_sub=False
        wireguard_config_main(WH_ipVersion)
    def wireguard_config_ok():
        global i_ip_scan
        global is_sub
        global is_v2ray
        global myscannerconf
        myscannerconf=False
        i_ip_scan=False
        is_sub=False
        is_v2ray=False
        wireguard_config_main(WH_ipVersion)
    def myscanner():
        global i_ip_scan
        global is_sub
        global is_v2ray
        global myscannerconf
        i_ip_scan=False
        is_sub=False
        is_v2ray=False
        myscannerconf=True
        wireguard_config_main(WH_ipVersion)
        



    def theard_wireguard_config_without():
                thread=threading.Thread(target=wireguard_config_without)
                thread.start()
    def theard_wireguard_config_sub():
                thread=threading.Thread(target=wireguard_config_sub)
                thread.start()
        
    def theard_v2ray():

                thread=threading.Thread(target=v2ray)
                thread.start()   
    def theard_v2ray_without():
                thread=threading.Thread(target=v2ray_without)
                thread.start()
    def theard_wireguard_config_ok():
                thread=threading.Thread(target=wireguard_config_ok)
                thread.start()
    def theard_myscanner():
                thread=threading.Thread(target=myscanner)
                thread.start()

        

    
    def main():
        global save_result
        global max_workers_number
        WH_ipVersion=""
        
        sorted_results=[]


        

                    

        def main_menu():
            global WH_ipVersion
            global save_result
       
            

         
            labelmain1.configure(text="\n\n\n\nplease wait ... ")
            label_best.insert(1.0, "best result: ")
            

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
            def copy_ip(text):
                global  sorted_results
                selected=table.selection()[0]
                ip = table.item(selected)['values'][0]
            
                
                print(ip)

                tabview.tab("main").clipboard_clear()
                if WH_ipVersion=="ipv4":
                    tabview.tab("main").clipboard_append(ip+":"+str(port))
                else:
                    tabview.tab("main").clipboard_append("["+ip+"]"+":"+str(port))
                
            def generate_ipv6():
                    return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"

            def ping_ip(ip, port):
                    global results
                    global best_ip
                    global best_result_avg

                    
                    
                    
                    icmp=pinging(ip, count=count_see ,interval=interval_see,timeout=timeout_see,family="ipv6")
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
                global save_result
                global do_you_save
                global sorted_results
                global save_result
                print(sorted_results)
                label_best.delete(1.0,tk.END)
                best_result=mn
                table.bind("<Double-1>", copy_ip)
                for ip, port, ping, loss_rate,jitter , combined_score in sorted_results[:10]:
                    table.insert("","end", values=(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%", f"{jitter:.2f}", f"{combined_score:.2f}"))
                   
               
                best_result = sorted_results[0] if sorted_results else None
                
                ip, port, ping, loss_rate,jitter, combined_score = best_result
                tabview.tab("main").clipboard_clear()
                tabview.tab("main").clipboard_append("["+ip+"]" +":"+str(port))
                label_best.insert(1.0,f"The best IP: [{ip}]:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}% ,{jitter} ms , score: {combined_score:.2f}" )
        
                best_result=2*[1]
                best_result[0]=f"{ip}"
                best_result[1]=878
                labelmain1.configure(text="\n\n\n\nFinished")
                

                do_you_save=""
                
                with open("warp_setting" , "r") as f:
                    num=f.readlines()
                print(do_you_save)
                print(best_result)
                os.remove("result.txt")
               
                t=0

                if num[1]=="2\n":
                    with open("result.txt", "w") as filef:
                        for i in save_result:
                            if t==0:
                
                                filef.write(i[1:])
                                t=1
                            else:
                                
                                filef.write(i)

            def check_ac():
    
                global save_result
                global best_result
                global do_you_save

            
                label_best.delete(1.0,tk.END)
                table.tag_configure("oddrow", background="black")
                # table.bind("<Button-1>", copy_ip)
                table.bind("<Double-1>", copy_ip)
                for j in range(len(table.get_children(""))):
                    if j %2==2:
                        item=table.get_children("")[j]
                        table.item(item, tags=("oddrow" ,))

            
                for ip, port, ping, loss_rate,jitter, combined_score in sorted_results[:10]:
                    table.insert("","end", values=(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%",f"{jitter}", f"{combined_score:.2f}"))
                    
                    
                    
                
              
                best_result = sorted_results[0] if sorted_results else None
                ip, port, ping, loss_rate,jitter, combined_score = best_result

                tabview.tab("main").clipboard_clear()
                tabview.tab("main").clipboard_append(ip +":"+str(port))
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
                    
             

                os.remove("result.txt")
                
                
                t=0

                if num[1]=="2\n":
                    with open("result.txt", "w") as fileff:
                        for i in save_result:
                            if t==0:
                
                                fileff.write(i[1:])
                                t=1
                            else:
                                
                                fileff.write(i)

          
                        
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
                
                icmp=pinging(ip, count=count_see ,interval=interval_see,timeout=timeout_see,family="ipv4" )
                # if icmp.avg_rtt != 0 and icmp.packet_loss!=1 and icmp.jitter!=0:
                #         print(icmp)
                #         progress2["value"] += 1
                        
                
                if icmp.is_alive:

                    results.append((ip, port, float(icmp.avg_rtt) ,float(icmp.packet_loss),float(icmp.jitter)))
                

        
            labelmain1.configure(text="\n\n\n\nPlease wait scannig ip ...")
        
            

            if WH_ipVersion=="ipv6":
                

                print("ipv6")
                
                save_result=[]
                sorted_results=[]


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
                label_best.insert(1.0, "sort result ...")

                extended_results=[]
                with open("warp_setting" , "r") as f:
                    warp1111=f.readlines()
                for result in results:
                    ip, port, ping , loss_rate, jitter= result

                    combined_score = (0.5 * ping +0.2 *jitter + 0.3* loss_rate)
                    extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))

                sorted_results=sorted(extended_results, key=lambda x: x[5])
                if warp1111[2]!="3\n":
                    for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
                    
                            if loss_rate == 0.00 and ping != 0.0 and ping < ping_range_see:

                                if warp1111[10]=="1\n":
                                    try:
                                        save_result.index(str(ip))
                                    except Exception:
                                        with open("warp_setting" , "r") as f:
                                            warp111=f.readlines()
                                            if warp1111[2]=="2\n":
                                                save_result.append(",")
                                                save_result.append(str(ip))
                                            else:
                                                save_result.append("\n")
                                                save_result.append(str(ip))
                                else:
                                    try:
                                        save_result.index(str(ip))
                                    except Exception:
                                        with open("warp_setting" , "r") as f:
                                            warp111=f.readlines()
                                            if warp1111[2]=="2\n":
                                                save_result.append(",")
                                                save_result.append(str(ip)+":"+str(port))
                                            else:
                                                save_result.append("\n")
                                                save_result.append(str(ip)+":"+str(port))
                if warp1111[2]=="3\n": 

                    for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
                        if ping <=ping_range_see:
                            if warp1111[10]=="1\n":
                                        save_result.append("\n")
                                        save_result.append(ip+" | "+"ping: "+ str(   ping) +"packet_loss: "+ str( loss_rate)+"jitter: "+str(   jitter)) 
                            else:
                                        save_result.append("\n")
                                        save_result.append(ip+":"+" | "+"ping: "+ str(   ping) +"packet_loss: "+ str( loss_rate)+"jitter: "+str(   jitter)) 

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
                return
            else:
                print("ipv4")
                save_result=[]
                
                sorted_results=[]
                start_ips=[]
                end_ips=[]
                print(warp[12])
                if warp[12]=="2\n":
                    start_ips = ["188.114.96.0", "162.159.192.0", "162.159.195.0"]
                    end_ips = ["188.114.99.224", "162.159.193.224", "162.159.195.224"]
                elif  warp[12]=="1\n":
                    start_ips=['167.82.229.0', '185.31.16.0', '146.75.31.0', '146.75.46.0', '199.232.65.0', '167.82.238.0', '167.82.231.0', '199.232.74.0', '146.75.115.0', '167.82.224.0', '146.75.25.0', '199.232.80.0']
                    end_ips=['167.82.229.255', '185.31.16.255', '146.75.31.255', '146.75.46.255', '199.232.65.255', '167.82.238.255', '167.82.231.255', '199.232.74.255', '146.75.115.255', '167.82.224.255', '146.75.25.255', '199.232.80.255']
                ports = [1074, 894, 908, 878]
                
    
                # except Exception:
                #      executor_bar.shutdown(wait=True)

                        

                for start_ip, end_ip in zip(start_ips, end_ips):
                    ip_range = create_ip_range(start_ip, end_ip)
                    
                    executor= ThreadPoolExecutor(max_workers=max_workers_number)
                    try:
                        for ip in ip_range:

                            futures=executor.submit(scan_ip_port, ip, ports[random.randint(0,3)]) 
                            
                    
        
                    except Exception as e:
                        print("AN Error", e)
                    finally:
                        executor.shutdown(wait=True)
                
                label_best.insert(1.0, "sort result ...")

                    
                
                
                
                extended_results = []
                with open("warp_setting" , "r") as f:
                    warp1111=f.readlines()
                for result in results:
                    ip, port, ping , loss_rate, jitter= result
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
                if warp1111[2]!="3\n": 
                        for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
                            if loss_rate == 0.00 and ping != 0.0 and ping < ping_range_see:
                                if warp1111[10]=="1\n":
                                    
                                    
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
                                else:
                                    try:
                                        save_result.index(str(ip))
                                    except Exception:
                                        with open("warp_setting" , "r") as f:
                                            warp111=f.readlines()
                                            if warp111[2]=="2\n":
                                                save_result.append(",")
                                                save_result.append(str(ip)+":"+str(port))
                                            else:
                                                save_result.append("\n")
                                                save_result.append(str(ip)+":"+str(port))
                if warp1111[2]=="3\n": 

                    for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
                        if ping <=ping_range_see:
                                        

                            if warp1111[10]=="1\n":
                                        save_result.append("\n")
                                        save_result.append(ip+" | "+"ping: "+ str(   ping) +"packet_loss: "+ str( loss_rate)+"jitter: "+str(   jitter)) 
                            else:
                                        save_result.append("\n")
                                        save_result.append(ip+":"+" | "+"ping: "+ str(   ping) +"packet_loss: "+ str( loss_rate)+"jitter: "+str(   jitter))             
                best_result=sorted_results[0]
            
                while len(sorted_results) < 10:
                    sorted_results.append(("No IP", None, None, 100, 1000))

                
                check_ac()
                return

        
        
        



        

                


        try:
            for w in tabview.tab("table").winfo_children():
                if "treeview" in str(w):
                    w.pack_forget()
        except Exception:
            pass
        table=ttk.Treeview(tabview.tab("table"), columns=("IP" ,"Port" , "Ping (ms)" , "Packet Loss (%)" ,"Jitter (ms)", "Score" ), show='headings')
        table.pack(side=tk.LEFT)

        

        table.heading("IP" , text="IP")
        table.heading("Port" , text="port")
        table.heading("Ping (ms)" , text="Ping (ms)")
        table.heading("Packet Loss (%)" , text="Packet Loss (%)")
        table.heading("Jitter (ms)", text="jitter (ms)")
        table.heading("Score" , text="Score")
 
        tabview.set("table")
        rootmainactivity.geometry("1200x500")

        def on_del_win():
            global concted

            if concted==False:
                 return
            remove_proxy()
            
            subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
            subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)


        rootmainactivity.protocol("WM_DELETE_WINDOW", on_del_win)
        main_menu()
    
    
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

    def main_move():
        global WH_ipVersion
        global results
        label_best.delete(1.0, "end")
        results=[]
        WH_ipVersion="ipv4"
        if radio_var.get()==2:
            
            thread=threading.Thread(target=main)
            thread.start()
        else:
            option=optionmenu.get()
            # ["wireguard configure",
            #                                                      "configure without ip scan",
            #                                                      "wireguard with a sub link",
            #                                                      "wireguard for v2rayN Pro",
            #                                                      "v2rayN Pro without ip scan"]
            # theard_wireguard_config_without
            # theard_wireguard_config_sub
            # theard_v2ray
            # theard_v2ray_without
            # theard_wireguard_config_ok
            if option=="wireguard configure":
                theard_wireguard_config_ok()
            elif option=="configure without ip scan":
                theard_wireguard_config_without()
            elif option== "wireguard with a sub link":
                theard_wireguard_config_sub()
            elif option== "wireguard for v2rayN Pro":
                theard_v2ray()
            elif option =="v2rayN Pro without ip scan":
                theard_v2ray_without()
            elif option=="v2rayN Pro and my scanner":
                theard_myscanner()
                

    def main_move_v6():
        global results
        results=[]
        label_best.delete(1.0, "end")
        global WH_ipVersion
        WH_ipVersion="ipv6"
        if radio_var.get()==2:
            thread=threading.Thread(target=main)
            thread.start()
        else:
            option=optionmenu.get()
            # ["wireguard configure",
            #                                                      "configure without ip scan",
            #                                                      "wireguard with a sub link",
            #                                                      "wireguard for v2rayN Pro",
            #                                                      "v2rayN Pro without ip scan"]
            # theard_wireguard_config_without
            # theard_wireguard_config_sub
            # theard_v2ray
            # theard_v2ray_without
            # theard_wireguard_config_ok
            if option=="wireguard configure":
                theard_wireguard_config_ok()
            elif option=="configure without ip scan":
                theard_wireguard_config_without()
            elif option== "wireguard with a sub link":
                theard_wireguard_config_sub()
            elif option== "wireguard for v2rayN Pro":
                theard_v2ray()
            elif option =="v2rayN Pro without ip scan":
                theard_v2ray_without()
            elif option=="v2rayN Pro and my scanner":
                theard_myscanner()
                
    def clean():
        t=0
        clean_result=[]
        try:
            
            with open("result.txt" ,"r") as f:
                b=f.readlines()
                bb=b[0]
        except Exception:
                    print("hello")
                    labelmain1.configure(text="\n\n\n\nFinished")
                    label_best.insert(1.0, f"{t} IPs")
                    return
        
        
        try:
            bb.index("|")
        except Exception:
                print("hello")
                labelmain1.configure(text="\n\n\n\nFinished")
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
        labelmain1.configure(text="\n\n\n\nFinished")
        label_best.insert(1.0, f"{t} IPs")
    def on_tab_change():
        selected_tab = tabview.get()
        if selected_tab == "table":
            rootmainactivity.geometry("1200x500")  # Auto size
     
        elif selected_tab == "main" or selected_tab == "vpn" or selected_tab == "configs":
            rootmainactivity.geometry("500x550")
            


        
    rootmainactivity=ctk.CTk()
    rootmainactivity.protocol("WM_TAKE_FOCUS")
    rootmainactivity.geometry("500x550")
    rootmainactivity.geometry("+200+100")
    rootmainactivity.resizable(False,False)
    rootmainactivity.title("main activity ")
   
    
    rootmainactivity.configure(cursor="arrow")

  
    rootmainactivity.attributes("-alpha" , 1.0)

    if not os.path.exists("xray"):
        label_sure=ctk.CTkLabel(rootmainactivity, text="Could not find xray folder")
        label_sure.pack(fill=tk.X, side="top")

        rootmainactivity.mainloop()
        
    def or_you_sure():
        def exit_exit():
    
            remove_proxy()
            
   
            subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
            subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
            remove_proxy()
          
            clear_widgets(rootmainactivity)
            rootmainactivity.destroy()
            clear_widgets(root_go)
            root_go.destroy()
            exit()
        def root_go_no():
            clear_widgets(root_go)
            root_go.destroy()
        root_go=ctk.CTkToplevel(rootmainactivity)
        root_go.grab_set()
        root_go.geometry("300x150")
        root_go.geometry("+250+150")
        root_go.title("warn")
        root_go.resizable(False,False)
        label_sure=ctk.CTkLabel(root_go, text="Are you sure ? you want to close the  main window?")
        label_sure.pack(fill=tk.X, side="top")
        b_sure=ctk.CTkButton(root_go, text="Yes",command=exit_exit)
        
        b_no=ctk.CTkButton(root_go, text="No", command=root_go_no)
        b_no.pack(fill=tk.X,side="bottom" ,  anchor="sw" , pady=5)
        b_sure.pack(fill=tk.X,side="bottom" , anchor="se", pady=5)

    rootmainactivity.protocol("WM_DELETE_WINDOW", or_you_sure)
    # background_image =ImageTk.PhotoImage(Image.open("imgs/warp_bk.png"))
    # background_label = tk.Label(rootmainactivity, image=background_image)
    # background_label.place(relwidth=1, relheight=1)
    tabview = ctk.CTkTabview(master=rootmainactivity,width=500, command=on_tab_change)
    
    tabview.place(relwidth=1, relheight=1)

    tabview.add("main")
    tabview.add("vpn")
# add tab at the end
    tabview.add("table")  # add tab at the end
    tabview.add("configs")
    with open("warp_setting", "r") as f:
        tep=f.readlines()
   
    if tep[13]=="2\n":
        tabview.set("main")  # set currently visible tab
    else:
        tabview.set("vpn")

    




    # choose=random.randint(0,1)

    # if choose==1:

             
        

    #     background_image =ImageTk.PhotoImage(Image.open("nika.png"))
    #     # background_label = tk.Label(rootmainactivity, image=background_image)
    #     # background_label.place(relwidth=1, relheight=1)
    # else:
        
    #     background_image =ImageTk.PhotoImage(Image.open("mahsa.png"))
    #     # background_label = tk.Label(rootmainactivity, image=background_image)
    #     # background_label.place(relwidth=2, relheight=2)
    
    
    menu_image =ctk.CTkImage(light_image=Image.open("imgs/profile.png"),
                                  dark_image=Image.open("imgs/profile.png"),
                                  size=(150, 150))

    def restart():
        os.execv(sys.executable, ['python'] + sys.argv)
     
    def toggle_menu_r():
            menu_frame.lift()
            toggle_menu_button.lift()
            if menu_frame.winfo_x() == rootmainactivity.winfo_screenwidth():

                toggle_menu_button.configure(text="close")
               


                for i in range(300, rootmainactivity.winfo_width() - menu_frame.winfo_width()):
                    
                    menu_frame.place(x=i, y=0)
                    rootmainactivity.update()
                    time.sleep(0.00001)
            else:
                toggle_menu_button.configure(text="Menu")
           
                time.sleep(0.1)
                menu_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0)

    def About():
        def Github_link(event):
            webbrowser.open_new(r"https://github.com/arshiacomplus/WarpScanner/releases")
        def Telegram_link(event):
            webbrowser.open_new(r"https://t.me/arshia_mod_fun")
        def copy_donate(event):
            root_about.clipboard_append("TKUpVDG5DqLDUSg3X1hhidRPuhm1GmqZ2G")
            trx.configure(text="Copied")

        root_about=ctk.CTkToplevel(rootmainactivity)
        root_about.protocol("WM_TAKE_FOCUS")
        root_about.title("About")
        root_about.configure(cursor="heart")
        root_about.geometry("+200+50")
        root_about.geometry("600x600")

        label_about=ctk.CTkLabel(root_about, text="This is an Warp Scanner For win")
        label_about.pack(fill=tk.X)

        label_mew=ctk.CTkLabel(root_about,text="New version v0.4.4:\nGood news:\n\nbetter Graphic\n\nfix Bugs\n\nBad news:\n\nNotihng:))")
        label_mew.pack(pady=5,fill=tk.X)
        label_about1=ctk.CTkLabel(root_about, text="Github Link :")
        label_about1.pack(fill=tk.X)
        link_git=ctk.CTkLabel(root_about, text="Github" ,  fg_color="blue" , cursor="hand2")
        link_git.pack(fill=tk.X)
        link_git.bind("<Button-1>" ,Github_link)

        label_about2=ctk.CTkLabel(root_about, text="Telegram Link :")
        label_about2.pack(fill=tk.X)
        link_tel=ctk.CTkLabel(root_about, text="Telegram" , fg_color="blue" , cursor="hand2")
        link_tel.pack(fill=tk.X)
        link_tel.bind("<Button-1>" ,Telegram_link)

        label_about2=ctk.CTkLabel(root_about, text="Donate:")
        label_about2.pack(fill=tk.X)

        trx=ctk.CTkLabel(root_about, text="Trx/ click to copy: \n\nTKUpVDG5DqLDUSg3X1hhidRPuhm1GmqZ2G" , cursor="hand2")
        trx.pack(fill=tk.X,pady=5)
        trx.bind("<Button-1>" ,copy_donate)

        label_about2=ctk.CTkLabel(root_about, text="Created by Arshiacomplus")
        label_about2.pack(side=tk.BOTTOM,fill=tk.X)

        



        root_about.mainloop()



    def Setting():
        
        
        # button_left=ctk.CTkButton(rootmainactivity,text="", width=5,image=back_arrow,bg_color="#000000",fg_color="#000000")
        # button_left.place(y=0,x=430)
        
        def faster_warn():
            
            
 

   



            error_window = ctk.CTkToplevel(rootmainactivity)
            error_window.grab_set() 
            error_window.title("Warning")
      
            error_window.geometry("300x100")
            error_window.geometry("+100+200")
 
            
            
            # warn_icon=tksvg.SvgImage(file="imgs/warn.svg")
            ctk.CTkLabel(error_window,compound="right",  text="if you have weak system , please do not use it ").pack(pady=20)
            ctk.CTkButton(error_window, text="Ok!", command=error_window.destroy).pack()
        def api_no():
      


            

            error_window =  ctk.CTkToplevel(rootmainactivity)
            error_window.grab_set() 
            error_window.title("Warning")

            error_window.geometry("300x100")
            error_window.geometry("+100+200")

            
            
            # warn_icon=tksvg.SvgImage(file="imgs/warn.svg")
            ctk.CTkLabel(error_window,compound="right", text="This api don not work , please do not use it !").pack(pady=20)
            ctk.CTkButton(error_window, text="Ok!", command=error_window.destroy).pack()
    

        def sumbit_f():
            global interval_see
            global count_see
            global timeout_see
            global ping_range_see
            labe.place_forget()
            Cpu_speed=''
            Do_you_save=''
            toggle_menu_button.configure(text="Menu")
        

            for i in range(0, rootmainactivity.winfo_screenwidth(), 10): 
                scrollable_frame.place(x=i, y=0)
            with open("warp_setting" , "r") as f:
                warp=f.readlines()
            print("hello"  ,int(checkbox_var.get()))
            if int(checkbox_var.get()) ==1:
                Cpu_speed= "2\n"
            else:
                Cpu_speed= "1\n"


            if checkbox_var2.get() ==1:
                Do_you_save= "2\n"
            if checkbox_var2.get() ==0:
                Do_you_save= "1\n"


            if checkbox_var3.get() ==1:
                wich_p= "2\n"
            elif checkbox_var3.get() ==0:
                wich_p= "1\n"
            else:
                wich_p="3\n"


            if checkbox_var4.get() ==1:
                api= "2\n"
            elif checkbox_var4.get() ==0:
                api= "1\n"
            
            if checkbox_var10.get() ==1:
                is_port= "2\n"
            elif checkbox_var10.get() ==0:
                is_port= "1\n"

            icmp_interval_get=interval.get()+"\n"

            icmp_count_get=count.get()+"\n"

            icmp_timeout_get=timeout.get()+"\n"
        
            ping_range_get=ping_range.get()+"\n"

            formsing="1\n"
            if checkbox_var8.get() ==1:
                formsing="2\n"
            else:
                formsing=="1\n"
            wh_v2="2\n"
            if checkbox_var9.get() ==1:
                wh_v2= "2\n"
            elif checkbox_var9.get() ==0:
                wh_v2= "1\n"    
            print(wh_v2 , "wwww")     
            theme=""
            if checkbox_var11.get() ==1:
                theme= "2\n"
            elif checkbox_var11.get() ==0:
                theme= "1\n"
            else:
                theme="3\n"
            cd_g="2\n"
            if checkbox_var12.get() ==1:
                cd_g= "2\n"
            elif checkbox_var12.get() ==0:
                cd_g= "1\n"

            f_tab="2\n"
            if checkbox_var15.get() ==1:
                f_tab= "2\n"
            elif checkbox_var15.get() ==0:
                f_tab= "1\n"  


            with open("warp_setting" , "w") as f:
                warp[0]= Cpu_speed
                warp[1]= Do_you_save
                warp[2]= wich_p
                warp[3]= api
                warp[4]= icmp_interval_get
                warp[5]= icmp_count_get
                warp[6]= icmp_timeout_get
                warp[7]= ping_range_get
                warp[8]= formsing
                warp[9]= wh_v2
                warp[10]= is_port
                warp[11]=theme
                warp[12]=cd_g
                warp[13]=f_tab
                f.writelines(warp)

            interval_see=warp[4]
            interval_see=int(interval_see[:interval_see.index("\n")])

            count_see=warp[5]
            count_see=int(count_see[:count_see.index("\n")])
            timeout_see=warp[6]
            timeout_see=int(timeout_see[:timeout_see.index("\n")])

            ping_range_see=warp[7]
            ping_range_see=int(ping_range_see[:ping_range_see.index("\n")])
            
            menu_frame.place_forget()
            menu_frame.pack_forget()
            clear_widgets(scrollable_frame)
            clear_widgets(slide_frame)
            scrollable_frame.place_forget()
            scrollable_frame.pack_forget()
            scrollable_frame.destroy()
   
            slide_frame.destroy()
            
            tabview.tab("main").update()

            gc.collect()
            return

     
        def event_submit_f(eee):
            sumbit_f()
            return
        
        
             
        menu_frame.place(x=tabview.tab("main").winfo_screenwidth(), y=0)
        # height_root = tabview.tab("main").winfo_screenheight()
        height_root=500

        slide_frame = ctk.CTkFrame(tabview.tab("main"), width=200, height=height_root)
        slide_frame.pack(side="right", fill="y", expand=True)
        slide_frame.place(x=tabview.tab("main").winfo_screenwidth(), y=0)


        scrollable_frame = ctk.CTkScrollableFrame(tabview.tab("main"), width=170, height=height_root)
        scrollable_frame.pack(padx=10, pady=10, fill="both")
        
        # speed_icon=tksvg.SvgImage(file="imgs/speedometer.svg")
        spu_label = ctk.CTkLabel(scrollable_frame,compound="right", text="Scan speed ")
        scrollable_frame.lift()
        back_arrow =ctk.CTkImage(light_image=Image.open("imgs/arrow.png"),
                                  dark_image=Image.open("imgs/arrow_light.png"),
                                size=(25,25)  )
        labe=ctk.CTkLabel(tabview.tab("main"),text="",image=back_arrow,fg_color="transparent", corner_radius=10)
        labe.place(y=0,x=430)
        labe.bind("<Button-1>", event_submit_f
                  )
        labe.lift()
        spu_label.pack(fill=tk.X)
      

        checkbox_var = ctk.IntVar()
        with open("warp_setting" , "r") as f:
                num=f.readlines()

        print(len(num))


        checkbox_var = ctk.IntVar()
        if  num[0] =="2\n":
                checkbox_var = ctk.IntVar(value=1)
        elif  num[0] =="1\n":
                checkbox_var = ctk.IntVar(value=0)


        
        checkbox1 = ctk.CTkCheckBox(scrollable_frame,command=faster_warn, text="Faster", variable=checkbox_var, onvalue=1, offvalue=0)
        checkbox1.pack(ipady=5,fill=tk.X)
        checkbox1.bind("<Enter>", hand2)

        checkbox2 = ctk.CTkCheckBox(scrollable_frame, text="Slower", variable=checkbox_var, onvalue=0, offvalue=0)
        checkbox2.pack(ipady=5,fill=tk.X)
        checkbox2.bind("<Enter>", hand2)



        checkbox_var12=ctk.IntVar()
        
        cd_gcore=ctk.CTkLabel(scrollable_frame,compound="right", text="which ip range")
        cd_gcore.pack(fill=tk.X)


        if  num[12] =="2\n":
            checkbox_var12 = ctk.IntVar(value=1)
        else:
            checkbox_var12 = ctk.IntVar(value=0)

        checkbox19 = ctk.CTkCheckBox(scrollable_frame, text="warp", variable=checkbox_var12, onvalue=1, offvalue=0)
        checkbox19.pack(ipady=5,fill=tk.X)
        checkbox19.bind("<Enter>", hand2)

        checkbox20 = ctk.CTkCheckBox(scrollable_frame, text="gcore", variable=checkbox_var12, onvalue=0, offvalue=0)
        checkbox20.pack(ipady=5,fill=tk.X)
        checkbox20.bind("<Enter>", hand2)



        

        # save_icon=tksvg.SvgImage(file="imgs/save.svg")

        save_ch=ctk.CTkLabel(scrollable_frame,compound="right", text="Save result ")
        save_ch.pack(fill=tk.X)


        if  num[1] =="2\n":
            checkbox_var2 = ctk.IntVar(value=1)
        else:
            checkbox_var2 = ctk.IntVar(value=0)

        checkbox3 = ctk.CTkCheckBox(scrollable_frame, text="Yes", variable=checkbox_var2, onvalue=1, offvalue=0)
        checkbox3.pack(ipady=5,fill=tk.X)
        checkbox3.bind("<Enter>", hand2)

        checkbox4 = ctk.CTkCheckBox(scrollable_frame, text="No", variable=checkbox_var2, onvalue=0, offvalue=0)
        checkbox4.pack(ipady=5,fill=tk.X)
        checkbox4.bind("<Enter>", hand2)


        # which_icon=tksvg.SvgImage(file="imgs/pannel.svg")

        which_panel=ctk.CTkLabel(scrollable_frame,compound="right",text="Which panel " )
        which_panel.pack(fill=tk.X)

        checkbox_var3=ctk.IntVar()

        print(num[2], "hhh")
    
        if  num[2] =="2\n":
                checkbox_var3 = ctk.IntVar(value=1)
        elif num[2] =="1\n":
                checkbox_var3 = ctk.IntVar(value=0)
        else:
                checkbox_var3 = ctk.IntVar(value=2)

        

        checkbox5 = ctk.CTkCheckBox(scrollable_frame, text="bpb", variable=checkbox_var3, onvalue=1, offvalue=0)
        checkbox5.pack(ipady=5,fill=tk.X)
        checkbox5.bind("<Enter>", hand2)

        checkbox6 = ctk.CTkCheckBox(scrollable_frame, text="vahid", variable=checkbox_var3, onvalue=0, offvalue=0)
        checkbox6.pack(ipady=5,fill=tk.X)
        checkbox6.bind("<Enter>", hand2)

        checkbox7 = ctk.CTkCheckBox(scrollable_frame, text="with score", variable=checkbox_var3, onvalue=2, offvalue=0)
        checkbox7.pack(ipady=5,fill=tk.X)
        checkbox7.bind("<Enter>", hand2)

        if  num[13] =="2\n":
            checkbox_var15 = ctk.IntVar(value=1)
        else:
            checkbox_var15 = ctk.IntVar(value=0)
        
        which_tab=ctk.CTkLabel(scrollable_frame,compound="right", text="first tab" )
        which_tab.pack(fill=tk.X)

        checkbox23 = ctk.CTkCheckBox(scrollable_frame, text="main", variable=checkbox_var15, onvalue=1, offvalue=0)
        checkbox23.pack(ipady=5,fill=tk.X)
        checkbox23.bind("<Enter>", hand2)

        checkbox24 = ctk.CTkCheckBox(scrollable_frame, text="vpn", variable=checkbox_var15, onvalue=0, offvalue=0)
        checkbox24.pack(ipady=5,fill=tk.X)
        checkbox24.bind("<Enter>", hand2)

        # theme_icon=tksvg.SvgImage(file="imgs/theme.svg")
        which_theme=ctk.CTkLabel(scrollable_frame,compound="right", text="theme " )
        which_theme.pack(fill=tk.X)

        checkbox_var11=ctk.IntVar()

        print(num[11], "hhh")
    
        if  num[11] =="2\n":
                checkbox_var11 = ctk.IntVar(value=1)
        elif num[11] =="1\n":
                checkbox_var11 = ctk.IntVar(value=0)
        else:
                checkbox_var11 = ctk.IntVar(value=2)

        

        checkbox16 = ctk.CTkCheckBox(scrollable_frame, text="system", variable=checkbox_var11, onvalue=1, offvalue=0)
        checkbox16.pack(ipady=5,fill=tk.X)
        checkbox16.bind("<Enter>", hand2)

        checkbox17 = ctk.CTkCheckBox(scrollable_frame, text="dark", variable=checkbox_var11, onvalue=0, offvalue=0)
        checkbox17.pack(ipady=5,fill=tk.X)
        checkbox17.bind("<Enter>", hand2)

        checkbox18 = ctk.CTkCheckBox(scrollable_frame, text="light", variable=checkbox_var11, onvalue=2, offvalue=0)
        checkbox18.pack(ipady=5,fill=tk.X)
        checkbox18.bind("<Enter>", hand2)


        checkbox_var10=ctk.IntVar()
        
        is_port_la=ctk.CTkLabel(scrollable_frame,compound="right", text="Save with port ")
        is_port_la.pack(fill=tk.X)


        if  num[10] =="2\n":
            checkbox_var10 = ctk.IntVar(value=1)
        else:
            checkbox_var10 = ctk.IntVar(value=0)

        checkbox15 = ctk.CTkCheckBox(scrollable_frame, text="Yes", variable=checkbox_var10, onvalue=1, offvalue=0)
        checkbox15.pack(ipady=5,fill=tk.X)
        checkbox15.bind("<Enter>", hand2)

        checkbox14 = ctk.CTkCheckBox(scrollable_frame, text="No", variable=checkbox_var10, onvalue=0, offvalue=0)
        checkbox14.pack(ipady=5,fill=tk.X)
        checkbox14.bind("<Enter>", hand2)

        # api_icon=tksvg.SvgImage(file="imgs/api.svg")
        Wh_api=ctk.CTkLabel(scrollable_frame,compound="right", text="Which api ")
        Wh_api.pack(fill=tk.X)
        checkbox_var4 = ctk.IntVar()
        with open("warp_setting" , "r") as f:
            num33=f.readlines()

        if  num33[3] =="2\n":
                checkbox_var4 = ctk.IntVar(value=1)
        elif  num33[3] =="1\n":
                checkbox_var4 = ctk.IntVar(value=0)

            
  
        checkbox8 = ctk.CTkCheckBox(scrollable_frame,command=api_no, text="api 1/not work", variable=checkbox_var4, onvalue=1, offvalue=0)
        checkbox8.pack(ipady=5,fill=tk.X)
        checkbox8.bind("<Enter>", hand2)

        checkbox9 = ctk.CTkCheckBox(scrollable_frame, text="api 2", variable=checkbox_var4, onvalue=0, offvalue=0)
        checkbox9.pack(ipady=5,fill=tk.X)
        checkbox9.bind("<Enter>", hand2)

        # format_icon=tksvg.SvgImage(file="imgs/format.svg")
        save_ch=ctk.CTkLabel(scrollable_frame,compound="right", text="sing-box formt ")
        save_ch.pack(fill=tk.X)

        checkbox_var8=ctk.IntVar()

        if  num[8] =="2\n":
            checkbox_var8 = ctk.IntVar(value=1)
        else:
            checkbox_var8 = ctk.IntVar(value=0)

        checkbox10 = ctk.CTkCheckBox(scrollable_frame, text="sing-box - hiddify(old)", variable=checkbox_var8, onvalue=1, offvalue=0)
        checkbox10.pack(ipady=5,fill=tk.X)
        checkbox10.bind("<Enter>", hand2)

        checkbox11 = ctk.CTkCheckBox(scrollable_frame, text="Just hiddify(New)", variable=checkbox_var8, onvalue=0, offvalue=0)
        checkbox11.pack(ipady=5,fill=tk.X)
        checkbox11.bind("<Enter>", hand2)

      
        save_ch2=ctk.CTkLabel(scrollable_frame, compound="right",text="v2ray formt ")
        save_ch2.pack(fill=tk.X)

        checkbox_var9=ctk.IntVar()

        if  num[9] =="2\n":
            checkbox_var9 = ctk.IntVar(value=1)
        else:
            checkbox_var9 = ctk.IntVar(value=0)

        checkbox12 = ctk.CTkCheckBox(scrollable_frame, text="v2rayN pro(old)", variable=checkbox_var9, onvalue=1, offvalue=0)
        checkbox12.pack(ipady=5,fill=tk.X)
        checkbox12.bind("<Enter>", hand2)

        checkbox13 = ctk.CTkCheckBox(scrollable_frame, text="v2rayN pro(New)", variable=checkbox_var9, onvalue=0, offvalue=0)
        checkbox13.pack(ipady=5,fill=tk.X)
        checkbox13.bind("<Enter>", hand2)

        # range_icon=tksvg.SvgImage(file="imgs/range.svg")
        ping_lab=ctk.CTkLabel(scrollable_frame,compound="right", text="ping range ")

        ping_lab.pack(fill=tk.X)
        with open("warp_setting" , "r") as f:
            num33=f.readlines()

        num33=num33[7]
        num33=num33[:num33.index("\n")]
        ping_range=ctk.CTkEntry(scrollable_frame,placeholder_text="50~250",width=25)
        ping_range.pack( padx=10, pady=10,fill=tk.X)

        ping_range.insert(0, num33)
# icmp=pinging(ip, count=count_see ,interval=interval_see,timeout=timeout_see,family="ipv4" )

        advane=ctk.CTkLabel(scrollable_frame,text="<Advance>\n")

        advane.pack(fill=tk.X)
        with open("warp_setting" , "r") as f:
            num33=f.readlines()

        num33=num33[4]
        num33=num33[:num33.index("\n")]
        # interval_icon=tksvg.SvgImage(file="imgs/interval.svg")
        icmp_interval=ctk.CTkLabel(scrollable_frame, compound="right", text="icmp_interval ")
        icmp_interval.pack(fill=tk.X)


        interval=ctk.CTkEntry(scrollable_frame,placeholder_text="1~5",width=25)
        interval.pack( padx=10, pady=10,fill=tk.X)

        interval.insert(0, num33)

        with open("warp_setting" , "r") as f:
            num33=f.readlines()

        num33=num33[5]
        num33=num33[:num33.index("\n")]
        # count_icon=tksvg.SvgImage(file="imgs/count.svg")
        icmp_count=ctk.CTkLabel(scrollable_frame,compound="right", text="icmp_ping_count ")
        icmp_count.pack(fill=tk.X)


        count=ctk.CTkEntry(scrollable_frame,placeholder_text="2~10",width=25)
        count.pack( padx=10, pady=10,fill=tk.X)

        count.insert(0, num33)



        with open("warp_setting" , "r") as f:
            num33=f.readlines()

        num33=num33[6]
        num33=num33[:num33.index("\n")]
        # timeout_icon=tksvg.SvgImage(file="imgs/timeout.svg")
        icmp_timeout=ctk.CTkLabel(scrollable_frame,compound="right", text="icmp_timeout ")
        icmp_timeout.pack(fill=tk.X)



        timeout=ctk.CTkEntry(scrollable_frame,placeholder_text="5~10",width=25)
        timeout.pack( padx=10, pady=10,fill=tk.X)

        timeout.insert(0, num33)
        
        submit=ctk.CTkButton(scrollable_frame, text="save", command=sumbit_f)
        submit.pack(pady=5,ipady=5,fill=tk.X)
        submit.bind("<Enter>", hand2)

    
        for i in range(290, rootmainactivity.winfo_width()  - scrollable_frame.winfo_width()-200):
                    scrollable_frame.place(x=i, y=0)
                    rootmainactivity.update() 
                    time.sleep(0.00001)

        

    def check_up():
            def Github_link():
                webbrowser.open_new(r"https://github.com/arshiacomplus/WarpScanner/releases")
            def on_go():
                ret=Check_for_update()
                if ret[0]  == True:
                    
                



                    label_up=ctk.CTkLabel(rootupdate , font=("Helvetica", 12, "bold"),text=f"New version Available {ret[1]}")
                    label_up.pack(fill=tk.X)

                    button_up=ctk.CTkButton(rootupdate ,font=("Helvetica", 12, "bold"), text="click to update",command=Github_link)
                    button_up.pack(fill=tk.X,side=tk.BOTTOM)
                    button_up.bind("<Enter>", hand2)

                

                else:


                    label_up=ctk.CTkLabel(rootupdate ,font=("Helvetica", 12, "bold"), text="New version v0.4.4:\nGood news:\n\nbetter Graphic\n\nfix Bugs\n\nBad news:\n\nNotihng:))")
                    label_up.pack(fill=tk.X)

                    button_up=ctk.CTkButton(rootupdate ,font=("Helvetica", 12, "bold"), text="Close" , command=rootupdate.destroy)
                    button_up.pack(fill=tk.X,side=tk.BOTTOM)
                    button_up.bind("<Enter>", hand2)
            
            rootupdate=ctk.CTk()
            rootupdate.title("Update")
            on_go()
            rootupdate.geometry("500x250")
            rootupdate.geometry("+200+100")
          
            

            rootupdate.mainloop()



        
    def theard_check_up():
            thread=threading.Thread(target=check_up)
            thread.start()
               
        





  

    def close_frame(event):
        clear_widgets(menu_frame)
        menu_frame.destroy()




#     labelmain=tk.Label(rootmainactivity, width=50, padx=50,pady=10, fg="blue" ,text="""Hello This is my Scanner
# created by Telegram= @arshiacomplus\n""")
#     labelmain.pack()

    height_root=tabview.tab("main").winfo_screenheight()

    menu_frame = ctk.CTkFrame(tabview.tab("main"), width=150, height=height_root)
    menu_frame.pack(side="right", fill="y",padx=5, expand=True)
    menu_frame.place(x=tabview.tab("main").winfo_screenwidth(), y=0)
    
    # rootmainactivity.bind("<Button-1>", close_frame)



     
     
    label_pro= ctk.CTkLabel(menu_frame, image=menu_image)
    label_pro.pack(pady=50)
    label_pro.configure(cursor="pirate")
    # set_icon=tksvg.SvgImage(file="imgs/gear.svg")
    Setting_button = ctk.CTkButton(menu_frame,text="Setting",compound="right", command=Setting)
    Setting_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    Setting_button.bind("<Enter>", hand2)

    # up_icon=tksvg.SvgImage(file="imgs/arrow_up.svg")
    up_button = ctk.CTkButton(menu_frame, text="Check for update",compound="right", command=theard_check_up)
    up_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    up_button.bind("<Enter>", hand2)

    # about_icon=tksvg.SvgImage(file="imgs/about.svg")
    About_button = ctk.CTkButton(menu_frame, text="About",compound="right", command=About)
    About_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    About_button.bind("<Enter>", hand2)

    # exit_icon=tksvg.SvgImage(file="imgs/exit.svg")    
    exit_button = ctk.CTkButton(menu_frame, text="Exit",compound="right", command=tabview.tab("main").quit)
    exit_button.pack(pady=5,ipady=5,fill=tk.BOTH)
    exit_button.bind("<Enter>", hand2)

    label_arshia= ctk.CTkLabel(menu_frame, text="by arshiacomplus\nv0.4.4")
    label_arshia.pack(pady=5,ipady=5,fill=tk.BOTH)

    # menu_icon=tksvg.SvgImage(file="imgs/menu_button.svg")
    toggle_menu_button = ctk.CTkButton(tabview.tab("main"),height=40,width=70,compound="right", text="Menu", command=lambda: toggle_menu_r())
    toggle_menu_button.pack(side="right", anchor="ne")

    # restart_button = tctk.CTkButton(tabview.tab("main"),padding=5, text="Restart", command=lambda: restart())
    # restart_button.place(y=50,x=350,width=150)





    def theard_check_ip6_again(event):

        def check_ip6_again():
            global check
            
            
            label_ipv4.configure(text=f"ipv4 : Checking ",corner_radius=8)
            label_ipv6.configure(text=f"ipv6 : Checking ",corner_radius=8)
            tabview.tab("main").update()
            time.sleep(2.5)
            check="none"
           
    
            check=  check_ipv6()
            if  check[0] == "Available":
            
                color1="green"
            else:
 
                color1="red"
               
            if  check[1] == "Available":
       
                color2="green"
            else:
  
                color2="red"
  

            label_ipv4.configure(text=f"ipv4 : {check[0]}")
            label_ipv4.configure(fg_color=color1)
            label_ipv6.configure(text=f"ipv6 : {check[1]}")
            label_ipv6.configure(fg_color=color2)
            tabview.tab("main").update()

      
        thread=threading.Thread(target=check_ip6_again)
        thread.start()

        
    def ratio_event():
        global ty, ty2
    
        if radio_var.get()==1:
            try:
                tabview.delete("table")
            except Exception:
                pass
            label_best.configure(height=50)
            button.pack_forget()
            button1.pack_forget()
            button3.pack_forget()
            
            optionmenu.pack(fill=tk.X,anchor="center" , pady=4,)
            if ty==True:
                how_menypp.pack(fill=tk.X, anchor="center")
            if ty2==True:
                optionmenu_gi.pack()
                 
            button.pack(fill=tk.X,anchor="center", pady=4)
            button.bind("<Enter>", hand2)

            button1.pack(fill=tk.X,anchor="center",  pady=4,)
            button1.bind("<Enter>", hand2)

            button3.pack(fill=tk.X,anchor="center" , pady=4,)
            button3.bind("<Enter>", hand2)
        else:
            try:
                tabview.add("table")
            except Exception:
                pass
            label_best.configure(height=1)
            ty=False
            try:
                how_menypp.pack_info()
                
                ty=True
            except tk.TclError:
                t2=False
            if ty==True:
                how_menypp.pack_forget()
            optionmenu.pack_forget()

            ty2=False
            try:
                optionmenu_gi.pack_info()
                
                ty2=True
            except tk.TclError:
                ty2=False
            if ty2==True:
                optionmenu_gi.pack_forget()


    def need_how_meny(nn):
        if optionmenu.get()=="wireguard with a sub link":
            button.pack_forget()
            button1.pack_forget()
            button3.pack_forget()
            how_menypp.pack(fill=tk.X, anchor="center")
            button.pack(fill=tk.X,anchor="center", pady=4)
            button.bind("<Enter>", hand2)

            button1.pack(fill=tk.X,anchor="center",  pady=4,)
            button1.bind("<Enter>", hand2)

            button3.pack(fill=tk.X,anchor="center" , pady=4,)
            button3.bind("<Enter>", hand2)
        
        else:
            how_menypp.pack_forget()

        if  optionmenu.get()=="v2rayN Pro and my scanner":
            button.pack_forget()
            button1.pack_forget()
            button3.pack_forget()
            try:
                how_menypp.pack_forget()
            except Exception:
                pass
            optionmenu_gi.pack()
  

            button.pack(fill=tk.X,anchor="center", pady=4)
            button.bind("<Enter>", hand2)

            button1.pack(fill=tk.X,anchor="center",  pady=4,)
            button1.bind("<Enter>", hand2)

            button3.pack(fill=tk.X,anchor="center" , pady=4,)
            button3.bind("<Enter>", hand2)
        else:
            optionmenu_gi.pack_forget()
            
             
            
    # ch_icon=tksvg.SvgImage(file="imgs/check.svg")
    # on_ch_icon=tksvg.SvgImage(file="imgs/reception_3.svg")
    # wifi_icon=tksvg.SvgImage(file="imgs/wifi.svg")
    # wifi_off_icon=tksvg.SvgImage(file="imgs/wifi_off.svg")

    label_ipv4=ctk.CTkLabel(tabview.tab("main"), text=f"ipv4 : checking "  ,compound="right", corner_radius=8)
    label_ipv4.pack(side="top", anchor="nw",pady=2)


    label_ipv6=ctk.CTkLabel(tabview.tab("main") , text=f"ipv6 : checking ",compound="right",corner_radius=8)
    label_ipv6.pack(side="top",anchor="nw")


    
    ch_ag=ctk.CTkLabel(tabview.tab("main"),text="Check again ",compound="right", text_color="#848484",corner_radius=8)
    ch_ag.pack(pady=3,side="top",anchor="nw")
    ch_ag.bind("<Button-1>" ,theard_check_ip6_again)
    ch_ag.bind("<Enter>", hand2)

 
    theard_check_ip6_again("none")

    
    labelmain1=ctk.CTkLabel(tabview.tab("main")  ,  text="\n\n\n\nClick to scan ip")
    

    label_best=ctk.CTkTextbox(tabview.tab("main") , width=50,height=1)
    
    

    how_menypp=ctk.CTkEntry(tabview.tab("main"), placeholder_text="haw many ? (2~4)")

    
    radio_var = tk.IntVar(value=2)
    radiobutton_1 = ctk.CTkRadioButton(tabview.tab("main"), text="IP scanning ",
                                             command=ratio_event, variable= radio_var, value=2)
    
    radiobutton_2 = ctk.CTkRadioButton(tabview.tab("main"), text="Get config",
                                             command=ratio_event, variable= radio_var, value=1)
    

    
    optionmenu = ctk.CTkOptionMenu(tabview.tab("main"), values=["wireguard configure",
                                                                 "configure without ip scan",
                                                                 "wireguard with a sub link",
                                                                 "wireguard for v2rayN Pro",
                                                                 "v2rayN Pro without ip scan",
                                                                 "v2rayN Pro and my scanner"] ,
                                                                 command=need_how_meny)
    
    optionmenu_gi = ctk.CTkOptionMenu(tabview.tab("main"), values=["Iran",
                                                                 "German",],
                                                                 command=need_how_meny)

    # ip_icon=tksvg.SvgImage(file="imgs/router.svg")
    button = ctk.CTkButton(tabview.tab("main"),  width=5, compound="right",text="ipV4",command=main_move)
    


    button1 = ctk.CTkButton(tabview.tab("main"),  width=5, compound="right",text="ipV6", command=main_move_v6)
    # star_icon=tksvg.SvgImage(file="imgs/stars.svg")

    button3 = ctk.CTkButton(tabview.tab("main"),width=5,compound="right",  text="clean", command=clean)
    
    
    labelmain1.pack(fill=tk.X,anchor="center",pady=10)

    label_best.pack(fill=tk.X,anchor="center",pady=10,)


    radiobutton_1.pack(anchor="center" , pady=4,)
    radiobutton_2.pack(anchor="center" , pady=4,)
    
    button.pack(fill=tk.X,anchor="center", pady=4)
    button.bind("<Enter>", hand2)

    button1.pack(fill=tk.X,anchor="center",  pady=4,)
    button1.bind("<Enter>", hand2)

    button3.pack(fill=tk.X,anchor="center" , pady=4,)
    button3.bind("<Enter>", hand2)


    #################### vpn view
    def on_change_var(*args):
        try:
            temp3["outbounds"][1]["settings"]["wnoise"]=wnoise_e.get()
            temp3["outbounds"][1]["settings"]["wnoisecount"]=wnoisecount_e.get()
            temp3["outbounds"][1]["settings"]["wnoisedelay"]=wnoisedelay_e.get()
            temp3["outbounds"][1]["settings"]["wpayloadsize"]=wpayloadsize_e.get()
            temp3["outbounds"][1]["settings"]["keepAlive"]=keepAlive_e.get()
            temp3["outbounds"][1]["settings"]["peers"][0]["endpoint"]=endpoint_e.get()
            temp3["outbounds"][0]["settings"]["peers"][0]["endpoint"]=endpoint_e.get()
            with open("xray/config.json" , "w") as ff:
                    ff.write(json.dumps(temp3, indent=4))
        except Exception:
            return
    def is_frag_or_wire(nn):
        op=is_warp_or_not.get()
        if op!="wiregaurd config setting":

            wnoise_la.pack_forget()
            wnoise.pack_forget()
            wnoisecount_la.pack_forget()
            wnoisecount.pack_forget()

            wnoisedelay_la.pack_forget()
            wnoisedelay.pack_forget()
            wpayloadsize_la.pack_forget()
            wpayloadsize.pack_forget()

            keepAlive_la.pack_forget()
            keepAlive.pack_forget()
            endp_la.pack_forget()
            endp.pack_forget()
            try:
                interval.pack_info()
            except Exception:

         
                packets_la.pack(padx=(20,0),side=tk.LEFT)
                packets.pack(padx=(20,0),side=tk.LEFT)
                length_la.pack(padx=(20,0),side=tk.LEFT)
                length.pack(padx=(20,0),side=tk.LEFT)
                interval_la.pack(padx=(20,0),side=tk.LEFT)
                interval.pack(padx=(20,0),side=tk.LEFT)
                fakehost_la.pack(padx=(20,0),side=tk.LEFT)
                fakehost.pack(padx=(20,0),side=tk.LEFT)
                mux_la.pack(padx=(20,0),side=tk.LEFT)
                mux.pack(padx=(20,0),side=tk.LEFT)
        else:

        
            packets_la.pack_forget()
            packets.pack_forget()
            length_la.pack_forget()
            length.pack_forget()
            interval_la.pack_forget()
            interval.pack_forget()
            fakehost_la.pack_forget()
            fakehost.pack_forget()
            mux_la.pack_forget()
            mux.pack_forget()
            try:
                endp.pack_info()
            except Exception:
                wnoise_la.pack(padx=(20,0),side=tk.LEFT)
                wnoise.pack(padx=(20,0),side=tk.LEFT)
                wnoisecount_la.pack(padx=(20,0),side=tk.LEFT)
                wnoisecount.pack(padx=(20,0),side=tk.LEFT)
                wnoisedelay_la.pack(padx=(20,0),side=tk.LEFT)
                wnoisedelay.pack(padx=(20,0),side=tk.LEFT)
                wpayloadsize_la.pack(padx=(20,0),side=tk.LEFT)
                wpayloadsize.pack(padx=(20,0),side=tk.LEFT)
                keepAlive_la.pack(padx=(20,0),side=tk.LEFT)
                keepAlive.pack(padx=(20,0),side=tk.LEFT)
                endp_la.pack(padx=(20,0),side=tk.LEFT)
                endp.pack(padx=(20,0),side=tk.LEFT)
  

    def save_frag_setting(*args):
        set=[packets.get()+"\n",length.get()+"\n",interval.get()+"\n","false\n",fakehost.get()+"\n","false\n",mux.get()+"\n","true"]
    
        if fakehost_var.get()==0:
            set[3]="false\n"
        else:
            set[3]="true\n"
  
        if mux_var.get()==0:
            set[5]="false\n"
        else:
            set[5]="true\n"
        if frag_var.get()==0:
            set[7]="false\n"
        else:
            set[7]="true\n"
        with open("fragment_set", "w") as file_fragmnet_set:
            file_fragmnet_set.writelines(set)

        
                
                    
        
        

    conc_button = ctk.CTkButton(tabview.tab("vpn"),  width=100,height=100,corner_radius=50, compound="right",text="Stop",command=theard_conc)
    conc_button.pack(anchor="center", pady=(125,0))
    conc_button.bind("<Enter>", hand2)



    ping_la=ctk.CTkLabel(tabview.tab("vpn")  ,  text="\nclick to connect ")
    ping_la.pack(fill=tk.X,anchor="center",pady=(0,10))

    # ip_cion =ctk.CTkImage(light_image=Image.open("imgs/DE.png"),
    #                               dark_image=Image.open("imgs/DE.png"),
    #                               size=(25, 25))

    button_loc = ctk.CTkFrame(tabview.tab("vpn"),border_width=1,border_color="#33cccc")
    button_loc.pack(pady=5,ipady=5, fill=tk.X)

    ipp_la=ctk.CTkLabel(button_loc ,text="Loc:  " )
    ipp_la.pack(fill=tk.X,anchor="center",pady=(0,10))

        
    is_warp_or_not = ctk.CTkOptionMenu(tabview.tab("vpn"), values=["fragment setting","wiregaurd config setting"] ,
                                                                 command=is_frag_or_wire)
    
    is_warp_or_not.pack(fill=tk.X, pady=3)
    



    
    try:
        with open("xray/config.json" , "r") as f:
            temp3 = json.load(f)

        wnoise_e=ctk.StringVar(value=temp3["outbounds"][1]["settings"]["wnoise"])
        wnoisecount_e=ctk.StringVar(value=temp3["outbounds"][1]["settings"]["wnoisecount"])
        wnoisedelay_e=ctk.StringVar(value=temp3["outbounds"][1]["settings"]["wnoisedelay"])
        wpayloadsize_e=ctk.StringVar(value=temp3["outbounds"][1]["settings"]["wpayloadsize"])
        keepAlive_e=ctk.IntVar(value=temp3["outbounds"][1]["settings"]["keepAlive"])
        endpoint_e=ctk.StringVar(value=temp3["outbounds"][1]["settings"]["peers"][0]["endpoint"])

        wnoise_e.trace_add("write",on_change_var)
        wnoisecount_e.trace_add("write",on_change_var)
        wnoisedelay_e.trace_add("write",on_change_var)
        wpayloadsize_e.trace_add("write",on_change_var)
        keepAlive_e.trace_add("write",on_change_var)
        endpoint_e.trace_add("write",on_change_var)
    except Exception:
        wnoise_e=""
        wnoisecount_e=""
        wnoisedelay_e=""
        wpayloadsize_e=""
        keepAlive_e=""
        endpoint_e=""
        
    ##fragment
    set=["tlshello\n","10-30\n","1-5\n","false\n","cloudflare.com\n","false\n","8\n","true"]
    with open("fragment_set", "r") as f:
        list_freg=f.readlines()
        list_freg=remove_empty_strings(list_freg)
        list_freg=[line.strip() for line in list_freg]
    
        
    packets_var=ctk.StringVar(value=list_freg[0])
    length_var=ctk.StringVar(value=list_freg[1])
    interval_var=ctk.StringVar(value=list_freg[2])
    fakehost_var_str=ctk.StringVar(value=list_freg[4])
    mux_var_str=ctk.StringVar(value=list_freg[6])
    if list_freg[3]=="false":
        fakehost_var=ctk.IntVar(value=0)
    else:
        fakehost_var=ctk.IntVar(value=1)
    if list_freg[5]=="false":
        mux_var=ctk.IntVar(value=0)
    else:
        mux_var=ctk.IntVar(value=1)
    if list_freg[6]=="false":
        frag_var=ctk.IntVar(value=0)
    else:
        frag_var=ctk.IntVar(value=1)


    button_frame = ctk.CTkFrame(tabview.tab("vpn"),border_width=3)
    button_frame.pack(pady=5,ipady=5, fill=tk.X)

    packets_la=ctk.CTkLabel(button_frame ,  text="packets: ")
    packets_la.pack(pady=2, padx=(20,0),side=tk.LEFT)

    
    packets=ctk.CTkEntry(button_frame,textvariable=packets_var, placeholder_text="packets [tlshello, ...]")
    packets.pack(fill=tk.X,side=tk.LEFT,padx=2)
    packets_var.trace_add("write",save_frag_setting)
    

    length_la=ctk.CTkLabel(button_frame ,  text="length: ")
    length_la.pack(padx=2,side=tk.LEFT)

    
    length=ctk.CTkEntry(button_frame,textvariable=length_var, placeholder_text="length[10-30 , ...]")
    length.pack(fill=tk.X,side=tk.LEFT,padx=2)
    length_var.trace_add("write",save_frag_setting)

    button_frame2 = ctk.CTkFrame(tabview.tab("vpn"),border_width=3)
    button_frame2.pack(pady=5,ipady=5, fill=tk.X)



    interval_la=ctk.CTkLabel(button_frame2  ,  text="interval: ")
    interval_la.pack( padx=(20,0),side=tk.LEFT)

    
    interval=ctk.CTkEntry(button_frame2,textvariable=interval_var, placeholder_text="interval['1-5']")
    interval.pack(fill=tk.X,side=tk.LEFT,padx=4)
    interval_var.trace_add("write",save_frag_setting)


    fakehost_la=ctk.CTkCheckBox(button_frame2  ,variable=fakehost_var,onvalue=1,offvalue=0,  text="fakehost: ")
    fakehost_la.pack(padx=2,side=tk.LEFT)
    fakehost_var.trace_add("write",save_frag_setting)
    
    fakehost=ctk.CTkEntry(button_frame2,textvariable=fakehost_var_str, placeholder_text="fakehost[cloudflare.com]")
    fakehost.pack(fill=tk.X,side=tk.LEFT,padx=2)
    fakehost_var_str.trace_add("write",save_frag_setting)

    button_frame3 = ctk.CTkFrame(tabview.tab("vpn"),border_width=3)
    button_frame3.pack(pady=5,ipady=5, fill=tk.X)

    mux_la=ctk.CTkCheckBox(button_frame3  ,variable=mux_var,onvalue=1,offvalue=0, text="mux: ")
    mux_la.pack(padx=(20,0),side=tk.LEFT)
    mux_var.trace_add("write",save_frag_setting)

    
    mux=ctk.CTkEntry(button_frame3,textvariable=mux_var_str, placeholder_text="mux[5]")
    mux.pack(fill=tk.X,side=tk.LEFT,padx=3)
    mux_var_str.trace_add("write",save_frag_setting)

    frag_la=ctk.CTkCheckBox(button_frame3  ,variable=frag_var,onvalue=1,offvalue=0, text="fragment")
    frag_la.pack(padx=(20,0),side=tk.LEFT)
    frag_var.trace_add("write",save_frag_setting)


    # endp_la=ctk.CTkLabel(button_framee3  ,  text="endpoint: ")
    # endp_la.pack(padx=2,side=tk.LEFT)

    
    # endp=ctk.CTkEntry(button_framee3,textvariable=endpoint_e, placeholder_text="endpoint[ip:port]")
    # endp.pack(fill=tk.X,side=tk.LEFT,padx=3)


    ##############################################
    


    wnoise_la=ctk.CTkLabel(button_frame ,  text="wnoise: ")
    wnoise=ctk.CTkEntry(button_frame,textvariable=wnoise_e, placeholder_text="wnoise[quic, random]")

    

    wnoisecount_la=ctk.CTkLabel(button_frame ,  text="wnoisecount: ")
    wnoisecount=ctk.CTkEntry(button_frame,textvariable=wnoisecount_e, placeholder_text="wnoisecount[10-15]")

   



    wnoisedelay_la=ctk.CTkLabel(button_frame2  ,  text="wnoisedelay: ")
    wnoisedelay=ctk.CTkEntry(button_frame2,textvariable=wnoisedelay_e, placeholder_text="wnoisedelay['1']")




    wpayloadsize_la=ctk.CTkLabel(button_frame2  ,  text="wpayloadsize: ")
    wpayloadsize=ctk.CTkEntry(button_frame2,textvariable=wpayloadsize_e, placeholder_text="wpayloadsize['5-10']")


   

    keepAlive_la=ctk.CTkLabel(button_frame3  ,  text="keepAlive: ")
    keepAlive=ctk.CTkEntry(button_frame3,textvariable=keepAlive_e, placeholder_text="keepAlive[5]")

    endp_la=ctk.CTkLabel(button_frame3  ,  text="endpoint: ")
    endp=ctk.CTkEntry(button_frame3,textvariable=endpoint_e, placeholder_text="endpoint[ip:port]")

    #######################   configs tab      ########################
    protocl_confs=["vless://","vmess://","trojan://","wireguard://", "ss://","socks://"]

    
    def parse_sub(sub:str):
        global sub_org
        sub_org=sub
        
       
       
        
        def get_confs():
            global confss
            global sub_org
           
   
            
            
            tag=sub_org.split("/")[-1]
            sub=sub_org.strip()
            try:
                tag=sub.split("#")[1]
                tag=sub.split("#")
                sub=tag[0]
                tag=tag[1]
            except:
                pass
            if  not os.path.exists("xray/"+tag):
                
                with open("xray/sub_files_name","a") as f:
                    f.write(tag+"\n")
                with open("xray/sub_files_name","r") as f:
                    sun_nms=f.readlines()
                    sun_nms=remove_empty_strings(sun_nms)
                    sun_nms = [line.strip() for line in sun_nms]
                selec_sub.configure(values=sun_nms)
                
            
            
            
            confss= requests.get(sub,  timeout=30)
            confss=confss.text
            boolor,confss,cout_add=check_confs(confss)

            if boolor==False:
                print("rturn")
                return
            

            with open("xray/"+tag,"w",encoding="utf-8") as f:
                f.write(str(confss))
                f.write("\n"+sub)
            get_config_from_user()
            
        
        tha=threading.Thread(target=get_confs)
        tha.start()
     
        
        
        
    def show_confs(test:str):
        global wch_sel,count
        if selec_sub.get()!="user_confs":

            update_buton.pack(side=tk.LEFT,padx=(155,0))
            remov_buton.pack(side=tk.LEFT,padx=(8,0))
        elif selec_sub.get()=="user_confs":
            try:
                remov_buton.pack_forget()
                update_buton.pack_forget()
            except Exception:
                pass
            
        



       
     
        sun_nms=selec_sub._values
        
        print(sun_nms)
        tag_num=sun_nms.index(selec_sub.get())
        if tag_num!=0:
       
            tag_sel=sun_nms[tag_num]
            
            temp1=sun_nms[0]
            
            sun_nms[0]=tag_sel
            sun_nms[tag_num]=temp1

            with open("xray/sub_files_name","w") as f:
                for j in sun_nms:
                    f.write(j+"\n")
            sun_nms = [line.strip() for line in sun_nms]
            selec_sub.configure(values=sun_nms)

        path_c="xray/"+selec_sub.get()
        with open(path_c, "r",encoding="utf-8") as f:
            conf_simple=f.readlines()
            if selec_sub.get()!="user_confs":
                conf_simple=conf_simple[:len(conf_simple)-1]
            conf_simple=remove_empty_strings(conf_simple)
            
        try:
            with open("xray/count", "r") as f:
                    wch_sel=int(f.readline())
        except Exception:
            pass
    
        if wch_sel>len(conf_simple):
            print("true")
           
            
        
            with open("xray/count", "w") as f:
                    f.write(str(0))
            
            wch_sel=0
        


        def remove_frame(widget):
            try:
                widget.destroy()
            except Exception:
                pass
        def edit_config(conf,count):
            global is_editing
            is_editing=True
            
            with open("xray/"+selec_sub.get(),"r",encoding="utf-8") as f:
                sun_na=f.readlines()
            
            parse_configs(sun_na[count],count)
            # with open("xray/"+selec_sub.get(),"w",encoding="utf-8") as f:
            #     for i in sun_na:
            #         f.write(i)
        def remove_config(frame:ctk.CTkFrame,count):
            with open("xray/"+selec_sub.get(),"r",encoding="utf-8") as f:
                sun_na=f.readlines()
            del sun_na[count]
            with open("xray/"+selec_sub.get(),"w",encoding="utf-8") as f:
                f.writelines(sun_na)
            frame.pack_forget()
        def clear_frames_in_scrollable_frame():
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = []
                for widget in scrollable_frame5.winfo_children():
                    if isinstance(widget, ctk.CTkFrame):
                        futures.append(executor.submit(remove_frame, widget))
                wait(futures)
        copy_icon =ctk.CTkImage(light_image=Image.open("imgs/copy.png"),
                                   dark_image=Image.open("imgs/copy.png"),
                                   size=(25, 25))
        remove_icon =ctk.CTkImage(light_image=Image.open("imgs/remove.png"),
                                   dark_image=Image.open("imgs/remove.png"),
                                   size=(25, 25))
        edit_icon =ctk.CTkImage(light_image=Image.open("imgs/edit.png"),
                                   dark_image=Image.open("imgs/edit.png"),
                                   size=(25, 25))
        def copy_config(config):
            on_copy_root = ctk.CTkFrame(tabview.tab("configs"), width=tabview.tab("configs").winfo_screenwidth(), height=tabview.tab("configs").winfo_screenheight(),border_width=1,border_color="red",corner_radius=5)
            on_copy_root.place(x=230, y=200)
            on_copy_root.grab_set()
            
            

            def normal():
                tabview.tab("configs").clipboard_clear()
                tabview.tab("configs").clipboard_append(config)
                on_copy_root.place_forget()
                rootmainactivity.grab_set()
            def full():
                tabview.tab("configs").clipboard_clear()
                tabview.tab("configs").clipboard_append(parse_configs(config))
                on_copy_root.place_forget()
                rootmainactivity.grab_set()
            def close(close):
                on_copy_root.place_forget()
                rootmainactivity.grab_set()
            back_arrow =ctk.CTkImage(light_image=Image.open("imgs/arrow.png"),
                                  dark_image=Image.open("imgs/arrow_light.png"),
                                size=(25,25)  )
            labe=ctk.CTkButton(on_copy_root,text="",image=back_arrow,fg_color="transparent", corner_radius=10,width=5,hover_color="#DF9C27")
            labe.pack(anchor=tk.NE,side=tk.TOP,ipady=10,ipadx=10)
            labe.bind("<Button-1>", close
                    )
            # buttonctk_b=ctk.CTkButton(on_copy_root,text="",image=back_arrow).pack(anchor=tk.NE)
            button_normal=ctk.CTkButton(on_copy_root,command=normal,text="Normal").pack(pady=(5,3),padx=5)
            button_norma2=ctk.CTkButton(on_copy_root,command=full,text="Full").pack(pady=(5,10),padx=5)
            on_copy_root.lift()

            


        def show_confs_therd():
            global temp_green_txtb,stoped_loop,wch_sel,count,on_is_green,frams_in_show,frams_in_ping
            frams_in_show=[]

            count=0
            tcount=0
           

            add_add_prog=10/len(conf_simple)/10
           
            
            
            clear_frames_in_scrollable_frame()
    
            for i in conf_simple:
                i=urllib.parse.unquote(i)
                
                if not i.startswith("vmess://"):
                    i_p=i.strip().split("#")[-1]
                else:
                    after_vemss=i.split("vmess://")[1].encode('utf-8')
                    after_vemss_d=base64.b64decode(after_vemss).decode("utf-8")
                    after_vemss_d=json.loads(after_vemss_d)
                    i_p=after_vemss_d["ps"]

                frame_confs=ctk.CTkFrame(scrollable_frame5,border_width=1,height=50,corner_radius=10)
                frame_confs.pack(pady=5,ipady=5, fill=tk.X)
                
                if count==wch_sel:

                    print("green")
                    is_on2=ctk.CTkTextbox(frame_confs,width=1,height=48,fg_color="green",activate_scrollbars=False,state = "disabled",)
                    is_on2.pack(padx=(3,0),side=tk.LEFT)
                    temp_green_txtb=is_on2
                    is_on2.bind("<Enter>", hand2)
                    on_is_green=True
                    
                else:
                    is_on3=ctk.CTkTextbox(frame_confs,width=1,height=48,fg_color="gray",activate_scrollbars=False,state = "disabled",)
                    is_on3.pack(padx=(3,0),side=tk.LEFT)
                    is_on=is_on3
                    is_on3.bind("<Enter>", hand2)
                
                    
                    

                if count==wch_sel :
                    is_on=temp_green_txtb
                else:
                    is_on2=is_on3


  
                label_click_confs=ctk.CTkTextbox(frame_confs,width=100,height=48)
                label_click_confs.pack(padx=(5,5),side=tk.LEFT)
                label_click_confs.insert(1.0,i_p)
                label_click_confs.configure(state = "disabled")
                frams_in_show.append(label_click_confs)
    
                ping_label=ctk.CTkLabel(frame_confs,text="",width=10)
                ping_label.pack(side=tk.LEFT,pady=(0,25))
                frams_in_ping.append(ping_label)

                copy_button=ctk.CTkButton(frame_confs,image=copy_icon,text="",width=25,command=lambda i=i: copy_config(i),hover_color="#DF9C27",fg_color="#2b2b2b")
                copy_button.pack(fill=tk.X,side=tk.LEFT,padx=(100,0))
                
                remove_button=ctk.CTkButton(frame_confs,image=remove_icon,text="",width=25,command=lambda  count=count, frame=frame_confs: remove_config(frame,count),hover_color="#DF9C27",fg_color="#2b2b2b")
                remove_button.pack(fill=tk.X,side=tk.LEFT,padx=(20,0))

                edit_button=ctk.CTkButton(frame_confs,image=edit_icon,text="",width=25,command=lambda  count=count, frame=frame_confs: edit_config(i,count),hover_color="#DF9C27",fg_color="#2b2b2b")
                edit_button.pack(fill=tk.X,side=tk.LEFT,padx=(20,0))
                i=i.strip()
                i=re.sub(r'\n', '', i)
                
                if stoped_loop==True:
                    is_on=""
                    if  on_is_green!=True:

                        
                        print("green")
                        is_on2.configure(fg_color="green")
                        is_on2.pack(padx=(3,0),side=tk.LEFT)
                        
                        is_on2.bind("<Enter>", hand2)
                        temp_green_txtb=is_on2
                        is_on=is_on2
                        print("is_on:  ",is_on)
                        
                    elif  on_is_green==True:
                        print("gray")
                        is_on3.configure(fg_color="gray")
                        is_on3.pack(padx=(3,0),side=tk.LEFT)
                        
                        is_on3.bind("<Enter>", hand2)
                        is_on=is_on3
                    print(on_is_green)
                    stoped_loop=False
                    on_is_green=False
                    frame_confs.bind("<Button-1>", lambda e,i=i,is_on=is_on, count=count: on_conf_click(i,count,is_on))
                    break
                frame_confs.bind("<Button-1>", lambda e,i=i,is_on=is_on, count=count: on_conf_click(i,count,is_on))
                
                count+=1
                tcount+=add_add_prog
                
                progress_bar_go.set(tcount)
                wait_progress.lift()
                label_show_which.configure(text=text_update+" "+str(tcount*100//1)+" %")
                
                
            clear_widgets(wait_progress)
            wait_progress.destroy()
                
        def show_confs_int_therd():
            thea=threading.Thread(target=show_confs_therd)
            thea.start()
            
        wait_progress=ctk.CTkToplevel(tabview.tab("configs"))
        wait_progress.geometry("+200+100")
        
        wait_progress_f=ctk.CTkFrame(wait_progress,border_width=2,border_color="red")
        wait_progress_f.pack(pady=10,padx=10,ipady=5,ipadx=5)
        text_update="load configs from "+selec_sub.get()+" "
        label_show_which=ctk.CTkLabel(wait_progress_f,text=text_update)
        label_show_which.pack(padx=5,pady=5)
        progress_bar_go=ctk.CTkProgressBar(wait_progress_f,orientation="horizontal",height=20,fg_color="pink", mode='determinate')
        progress_bar_go.pack(fill=tk.X)
        def exit_thread():
            global wch_sel,count,stoped_loop,on_is_green

            with open("xray/count", "w") as f:
                    f.write(str(wch_sel-1))
            

            stoped_loop=True
            
        ctk.CTkButton(wait_progress, text="cancel", command=exit_thread).pack(padx=5,pady=5)
        show_confs_int_therd()

    def check_confs(config:str):
        config=config.splitlines()

        booltemp=False
        boolor=False
        cout_add=0
        confgis=""
        for j in config:
            
            for i in protocl_confs:

                        
                if j.startswith(i):
                    
                    booltemp=True
                    if booltemp==True and i=="ss://":
                        if j[0]!="s":
                            booltemp=False
                        
                    if booltemp==True:
                        break
                    
                    print("True")
            if booltemp==True:
                cout_add+=1
                confgis=confgis+(j+"\n")
                boolor=True
                booltemp=False
            
        return boolor,confgis,cout_add
        
    def get_config_from_user():
        global confss
        config = pyperclip.paste()
       
       
        
        if (config.startswith("http://") or config.startswith("https://"))  and confss=="":
            parse_sub(config)
            
            return
        if confss!="":
            config=confss
            confss=""
            show_confs("test")
            return
        
    

        boolor,confgis,cout_add=check_confs(config)
        confgis=str(confgis)
        if confgis[-1]=="\n":
            confgis=confgis[0:len(confgis)-1]

        if boolor==False:
            print("rturn")
            return

        with open("xray/user_confs", "r",encoding="utf-8") as f:
            confgs=f.readlines()
            confgs=remove_empty_strings(confgs)

        confs=""
        for i in confgs:
            confs+=i
        confs=(confgis+"\n"+confs)
        with open("xray/user_confs", "w",encoding="utf-8") as f:
            # shift_value = 3  
            # encryptor = SimpleEncryptor(shift_value)
            
            # original_text = "Hello, World!"
            # encrypted_text = encryptor.encrypt(original_text)
            # decrypted_text = encryptor.decrypt(encrypted_text)
            f.write(confs.strip())
            f.write("\n")
        
        
        with open("xray/count", "r") as f:
            count=int(f.readline())+cout_add
        with open("xray/count", "w") as f:
            f.write(str(count))
        

        show_confs("test")

    def parse_sub_in():
        with open("xray/"+selec_sub.get(),"r",encoding="utf-8") as f:
            sun_na=f.readlines()[-1]
        tabview.tab("configs").clipboard_clear()
        tabview.tab("configs").clipboard_append(str(sun_na))
        get_config_from_user()
        tabview.tab("configs").clipboard_clear()

    def remove_sub_in():
        os.remove("xray/"+selec_sub.get())
        with open("xray/sub_files_name","r") as f:
        
            sun_nms=f.readlines()
            del sun_nms[0]
        with open("xray/sub_files_name","w") as f:
            f.writelines(sun_nms)
        print(sun_nms)
        
        sun_nms=remove_empty_strings(sun_nms)
        sun_nms = [line.strip() for line in sun_nms]
        selec_sub.configure(values=sun_nms)
        selec_sub.set(sun_nms[0])
        

        show_confs('testttttttt')

    def th_ping_all():
        def ping_all():
            global frams_in_ping
            config_abs=os.path.abspath("xray/config_test_ping.json")
            xray_abs=os.path.abspath("xray/xray.exe")
            def s_xray():
            
                subprocess.call([xray_abs, 'run', '-c' ,config_abs],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW )
            def stop_x():
                subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.call(["taskkill" , "/F", "/IM" ,"xray.exe"],  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)

            
            with open("xray/"+selec_sub.get(),"r",encoding="utf-8") as f:
            
                sun_nms=f.readlines()
                sun_nms=remove_empty_strings(sun_nms)
            t=0
            conc_button.configure(state=tk.DISABLED)
            for i in sun_nms:
                is_wrong=False
                with open("xray/config_test_ping.json" , "w") as f:
                    try:
                        temp3 = f.write(parse_configs(i))
                    except Exception:
                        is_wrong=True
                if is_wrong==False:
                    with open("xray/config_test_ping.json" , "r") as f:
                        temp3 = json.load(f)
                    
                    port=temp3["inbounds"][1]["port"]
                    set_proxy("127.0.0.1",port)
                    th3=threading.Thread(target=s_xray)
                    th3.start()
                    time.sleep(2)
                
                    
                    print("go ping")
                    try:
                        proxies = {
                            "http": f"http://127.0.0.1:{port}"
                        }
                        url = "https://www.google.com/generate_204"
                        headers = {"Connection": "close"}
                        
                        start = time.time()
                        response = requests.get(url, proxies=proxies, timeout=10, headers=headers)
                        elapsed = (time.time() - start) * 1000  # تبدیل به میلی‌ثانیه
                        
                        if response.status_code == 204 or (response.status_code == 200 and len(response.content) == 0):
                            result = f"{int(elapsed)}"
                        else:
                            raise IOError(f"Connection test error, status code: {response.status_code}")
                    except RequestException as e:
                        print(f"testConnection RequestException: {e}")
                        result = "-1"
                    except Exception as e:
                        print(f"testConnection Exception: {e}")
                        result = "-1"
                    if result=="-1":
                        frams_in_ping[t].configure(text=result,bg_color="red")
                    else:
                        frams_in_ping[t].configure(text=result,bg_color="green")
                    
                    stop_x()
                    print("fin ping")
                    
                else:
                    frams_in_ping[t].configure(text="-1",bg_color="red")
                t+=1
            conc_button.configure(state=tk.NORMAL)
        th=threading.Thread(target=ping_all,args=())
        th.start()
        
        
        


    top_vpn_f = ctk.CTkFrame(tabview.tab("configs"),border_width=1,corner_radius=10)

    top_vpn_f.pack(pady=5,ipady=5, fill=tk.X)
    
    ip_cion =ctk.CTkImage(light_image=Image.open("imgs/save.png"),
                                   dark_image=Image.open("imgs/save.png"),
                                   size=(25, 25))

    add_icon=ctk.CTkButton(top_vpn_f,image=ip_cion,text="",width=25,command=get_config_from_user,hover_color="#DF9C27",fg_color="#2b2b2b")
    add_icon.pack(side=tk.LEFT,padx=3)


    

    update_icon =ctk.CTkImage(light_image=Image.open("imgs/update.png"),
                                   dark_image=Image.open("imgs/update.png"),
                                   size=(25, 25))
    
    remove_icon =ctk.CTkImage(light_image=Image.open("imgs/remove.png"),
                                   dark_image=Image.open("imgs/remove.png"),
                                   size=(25, 25))


    with open("xray/sub_files_name","r") as f:
        sun_nms=f.readlines()
        sun_nms=remove_empty_strings(sun_nms)
        sun_nms = [line.strip() for line in sun_nms]
    
    selec_sub=ctk.CTkOptionMenu(top_vpn_f, values=sun_nms,width=150,command=show_confs)
    selec_sub.pack(side=tk.LEFT, padx=(20,0))
    update_buton=ctk.CTkButton(top_vpn_f,image=update_icon,text="",width=25,command=parse_sub_in,hover_color="#DF9C27",fg_color="#2b2b2b")

    remov_buton=ctk.CTkButton(top_vpn_f,image=remove_icon,text="",width=25,command=remove_sub_in,hover_color="#DF9C27",fg_color="#2b2b2b")

        
    

    confs_fram = ctk.CTkFrame(tabview.tab("configs"),border_width=1,height=500,corner_radius=10)

    confs_fram.pack(pady=5,ipady=5, fill=tk.BOTH)

    ping_b=ctk.CTkButton(confs_fram,command=th_ping_all,text="ping",corner_radius=20)
    ping_b.pack(side=tk.BOTTOM)

    scrollable_frame5 = ctk.CTkScrollableFrame(confs_fram, width=490, height=500)
    scrollable_frame5.pack(padx=10, pady=10, fill="both")
    
    
        
    def on_conf_click(i,c,is_on:ctk.CTkTextbox):
        global temp_green_txtb
       
       
        
       
        is_on.configure(fg_color="green")
        

        
        
        temp_green_txtb.configure(fg_color="gray")
        temp_green_txtb=is_on
      
        
        with open("xray/count", "w") as f:
            f.write(str(c))


        

    show_confs("test")

    ###################################################################
 
    rootmainactivity.mainloop()
    

if __name__ == "__main__":
    
         
    
    mainactivity()
