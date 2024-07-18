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
# from urllib.parse import quote

import requests

import re
# import socket
from concurrent.futures import ThreadPoolExecutor
import time

import webbrowser

from retrying import retry
from requests.exceptions import ConnectionError

import random
# import subprocess
# import json
# import sys

from icmplib import ping as pinging



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




try:
    with open("warp_setting", "r") as f:
        f.close()

except Exception:

    with open("warp_setting", "a") as f:
            f.write("1")
            f.write("\n")

    

    with open("warp_setting", "a") as f:
        f.write("2\n")

    with open("warp_setting", "a") as f:
        f.write("2\n")


    # ctypes.windll.kernel32.SetFileAttributesW("warp_setting" , 0x02)

def check_ipv6():
    
    try:
        ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php')
        if ipv6.status_code == 200:
            ipv6 ="Available"
    except Exception:
        ipv6 = "Unavailable"
    try:
        ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php')
        if ipv4.status_code == 200:
            ipv4= "Available"
    except Exception:
        ipv4 = "Unavailable"
    return  [ipv4,ipv6]

def free_cloudflare_account():

        
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

    if output=="""v0.1.3
""":
        return [False, output]
    else:
        return [True, output]

def which_Vip():
    def main_move():
        main("ipv4"),rootwhich_Vip.destroy()
    def main_move_v6():
        main("ipv6"),rootwhich_Vip.destroy()


    

    rootwhich_Vip=tk.Tk()
    rootwhich_Vip.title("main activity ")

    
    button = tk.Button(rootwhich_Vip, width=10, padx=11, pady=4, bd=8, text="ipV4", command=main_move,fg="#f0f0f0", bg="#414141")
    button.pack()

    button1 = tk.Button(rootwhich_Vip, width=10, padx=11, pady=4, bd=8, text="ipV6", command=main_move_v6,fg="#f0f0f0", bg="#414141")
    button1.pack()

    rootwhich_Vip.mainloop()
def which_Cpu_speed():
        global Cpu_speed
            

            
        with open("warp_setting" , "r") as f:
            num=f.readline()

        if  num[0] =="2":
                    Cpu_speed="1"
        elif  num[0] =="1":
                    Cpu_speed="2"
 
                    
             
        which_Vip()
def main(WH_ipVersion):
    global save_result
    global max_workers_number
    
    sorted_results=[]
    

    def main_menu():
        button1.destroy()
        labelmain1.config(text="please wait ... ")
        label_best.insert(1.0, "best result: ")
        rootmain.update()

        global sorted_results
        global best_result

        
        
        
        if Cpu_speed == "1": max_workers_number=100
        elif Cpu_speed == "2": max_workers_number=50
        print(max_workers_number)
        def generate_ipv6():
                return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"

        def ping_ip(ip, port):
                global results
                global best_ip
                global best_result_avg

                
                
                
                icmp=pinging("2606:4700:d0::7e9:ef1:78b2:8f59", count=4 ,interval=1,timeout=5 ,family="ipv6")
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

            label_best.insert(1.0,f"The best IP: {ip}:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}% ,{jitter} ms , score: {combined_score:.2f}" )
     
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

            filef=open("result.csv" , "w")
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
            best_result=sorted_results[0]
        
            while len(sorted_results) < 10:
                sorted_results.append(("No IP", None, None, 100, 1000))


            check_ac()

       
    
    

    rootmain= tk.Tk()
    rootmain.configure(bg="#414141")
    rootmain.title("my WarpScanner")


    labelmain1=tk.Label(rootmain , font = ('arial', 11) ,  text="Click to scan ip", fg = "#f0f0f0", bg="#414141")
    labelmain1.pack()



 
    table=ttk.Treeview(rootmain, columns=("IP" ,"Port" , "Ping (ms)" , "Packet Loss (%)" ,"Jitter (ms)", "Score" ), show='headings')


    table.heading("IP" , text="IP")
    table.heading("Port" , text="port")
    table.heading("Ping (ms)" , text="Ping (ms)")
    table.heading("Packet Loss (%)" , text="Packet Loss (%)")
    table.heading("Jitter (ms)", text="jitter (ms)")
    table.heading("Score" , text="Score")

    
    label_best=Text(rootmain , width=50,height=1, fg = "#f0f0f0", bg="#414141")
    label_best.pack()

    
    button1=tk.Button(rootmain,text="scan", command=main_menu, fg = "#f0f0f0", bg="#414141")
    button1.pack()




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




def wireguard_config():
    Cpu_speed=""
    def wireguard_config_main(which_ip):
            button1.destroy()
            labelmain_wire.config(text="please wait ... ")
            rootwire_confing.update()
            global Cpu_speed
            global max_workers_number
            global sorted_results
            global i_ip_scan

            

            



            
            
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

                    
                    
                    
                    icmp=pinging("2606:4700:d0::7e9:ef1:78b2:8f59", count=4 ,interval=1,timeout=5 ,family="ipv6")
                        
                    ping=float(icmp.avg_rtt)
                    jitter=icmp.jitter
                    loss_rate=icmp.packet_loss
                    if ping == 0.0:
                        ping=1000
                    if jitter== 0.0:
                        jitter=100
                    if loss_rate==1.0:
                        loss_rate=100
                    los=loss_rate*100
                    if (0.5 *ping + +0.2 * jitter+ 0.3* loss_rate  ) > best_ip:
                        best_ip=(0.5 * float(icmp.avg_rtt) +0.2 *icmp.jitter + 0.3* icmp.packet_loss )
                        best_result_avg=ip
                    results.append((ip, port, float(icmp.avg_rtt) ,icmp.packet_loss ,icmp.jitter,best_ip))
                    
                    


            def check_ac_v6(mn, i):
                global i_ip_scan
                
                global best_result
                if i_ip_scan ==False:


                    best_result=mn

                    best_result = sorted_results[0] if sorted_results else None

                    ip, port, ping, loss_rate,jitter ,combined_score= best_result

                    best_result=[0]*2
                    best_result[0]=f"[{ip}]"
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

                rootip.configure(bg="#414141")

                label_ff=tk.Label(rootip, text="Enter an ipv4",bg="#414141",fg="#f0f0f0")
                label_ff.pack()

                
                ip_entry=tk.Entry(rootip ,width=20, bd=8)
                ip_entry.pack( padx=10, pady=10)

                submitb=tk.Button(rootip, width=10, padx=11, pady=4, bd=8, text="submit", command=submit,fg="#f0f0f0", bg="#414141")
                submitb.pack()

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

                    sorted_results=sorted(results, key=lambda x: x[5])
                    



                    


                    port_random = ports_to_check[random.randint(0, len(ports_to_check) - 1)]
                    if best_ip:

                        best_ip_mix = [1] * 2
                        best_ip_mix[0] = "[" + best_ip + "]"
                        best_ip_mix[1] = port_random
                    else:

                        best_ip_mix = [1] * 2
                        best_ip_mix[0] = "[" + random_ip + "]"
                        best_ip_mix[1] = port_random
                    if is_sub ==True and  wire_p !=1:
                        def submit():
                            for i in range(int(how_meny.get())):


                                check_ac_v6(best_ip_mix, i)

                        rootsub= tk.Tk()
                        rootsub.title("how_many")

                        rootsub.configure(bg="#414141",fg="#f0f0f0")

                        label_ff=tk.Label(rootsub, text="How meny")
                        label_ff.pack()

                        
                        how_meny=tk.Entry(rootsub ,width=20, bd=8,bg="#414141",fg="#f0f0f0")
                        how_meny.pack( padx=10, pady=10)

                        submitbb=tk.Button(rootsub, width=10, padx=11, pady=4, bd=8, text="submit", command=submit,fg="#f0f0f0", bg="#414141")
                        submitbb.pack()

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


                        rootsub.configure(bg="#414141")

                        label_ff=tk.Label(rootsub, text="How meny",bg="#414141",fg="#f0f0f0")
                        label_ff.pack()
                        
                        how_meny=tk.Entry(rootsub ,width=20, bd=8)
                        how_meny.pack( padx=10, pady=10)

                        submitbb=tk.Button(rootsub, width=10, padx=11, pady=4, bd=8, text="submit", command=submit,fg="#f0f0f0", bg="#414141")
                        submitbb.pack()

                        rootsub.mainloop()
                    else:
                        check_ac("")

                    

        
    def which_Vip():
        def main_move():
            rootwhich_Vip.destroy(),wireguard_config_main("ipv4")
        def main_move_v6():
            rootwhich_Vip.destroy(),wireguard_config_main("ipv6")


        

        rootwhich_Vip=tk.Tk()
        rootwhich_Vip.title("main activity ")

        
        button = tk.Button(rootwhich_Vip, width=10, padx=11, pady=4, bd=8, text="ipV4", command=main_move,fg="#f0f0f0", bg="#414141")
        button.pack()

        button1 = tk.Button(rootwhich_Vip, width=10, padx=11, pady=4, bd=8, text="ipV6", command=main_move_v6,fg="#f0f0f0", bg="#414141")
        button1.pack()

        rootwhich_Vip.mainloop()
         
    def which_Cpu_speed2():
        global i_ip_scan
        global Cpu_speed
 

        if i_ip_scan == True:
            wireguard_config_main("")
            return
        else:
            
                

                
            with open("warp_setting" , "r") as f:
                num=f.readline()

            if  num[0] =="2":
                        Cpu_speed="1"
            elif  num[0] =="1":
                        Cpu_speed="2"
 
            which_Vip()

                     


    rootwire_confing=tk.Tk()
    rootwire_confing.title("Wire_config")
    rootwire_confing.configure(bg="#414141")



    labelmain_wire=tk.Label(rootwire_confing , font = ('arial', 11) ,  text="Click to Make wire_config", fg = "#f0f0f0", bg="#414141")
    labelmain_wire.pack()


    
    label_best=Text(rootwire_confing, width=50,height=5, fg = "#f0f0f0", bg="#414141")
    label_best.pack()

    
    button1=tk.Button(rootwire_confing,text="make", command=which_Cpu_speed2, fg = "#f0f0f0", bg="#414141")
    button1.pack()

    rootwire_confing.mainloop()
def wireguard_config_without():
    global i_ip_scan
    global is_sub
    i_ip_scan=True
    is_sub=False
    wireguard_config()
def wireguard_config_sub():
    global is_sub
    global i_ip_scan
    i_ip_scan=False
    is_sub=True
    wireguard_config()

def mainactivity():
    rootmainactivity=tk.Tk()
    rootmainactivity.geometry("500x500")
    rootmainactivity.title("main activity ")
    rootmainactivity.resizable(False, False)
    mahsa_img="/9j/4AAQSkZJRgABAQEAYABgAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcgSlBFRyB2OTApLCBxdWFsaXR5ID0gODIK/9sAQwAGBAQFBAQGBQUFBgYGBwkOCQkICAkSDQ0KDhUSFhYVEhQUFxohHBcYHxkUFB0nHR8iIyUlJRYcKSwoJCshJCUk/9sAQwEGBgYJCAkRCQkRJBgUGCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQk/8AAEQgD9QQAAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A+qaKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFGKACiiigAooooAKKKKACijFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFGKACiiigAooooAKKKKACiiigANFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRiigAooooAKKKKACiiigAooooAKKKKACiijFABRRRQAUUUUAFFFFABRRiigAooooAKKKKACiiigAo70UUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFGKACiiigAooooAKKKKACijFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUE4FABRketJuFU9S1ex0mBp766it4153O2KVwLuR60ZHrXlGsfHzRrO9aCxt3vY1GPMU4BauX1n47a5dxFNNggsyTkORvYD+VFx8rPf80ZHrXzLF8Y/G0Eyu+oQTIDkxtAoB/EVs237Q+txD/StItZP+ubEfzouFmfQOR60ZrwST9qC2sSv9oaJNGrHGUbNdJo/7SHgjUwqyXMlo57SLwKLiser5oyK5uw+IXhbUlBt9as2z0HmAGtC68RaTZoks1/bqkjBVO8cmi4GpRTEkV0DKQQRnIp24etMBaKMiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKMii4ATgZNU9S1Sz0q0kur64jt4E+9JI2AKzvF3i/S/Bujz6pqlykUUSFgpbBc46Cvi34ifG/W/iKktvOxt7US5ihjJCquO/qaVxpHunj79pWxshJp/hCIX9yQVa6fiOI+o9a8el1nWPENy13rerT3Ujnd5bMdo+grzW3nuYhhJePY1eg1W/j5EtQzaMdD0SMKBhMYFSM4RclsV5+Nf1LH+v21FJqFzOP3tw7evzUi7HZ33iC3tUIQiSQfw54/OsSXxXeOxKrGq9hjNYavkfeBoLDpmmHKXL/AFWbUUVJwmAc8DFUNnsKeSg6kfnTQynpQLlHJNLFjy3dcejYqWXVL+dAj3tw6joC5/xqA4prFE5ZgPrRcVkep+Cv2ivFXhG2hsrsR6paRDCrMTv9vmr2H4e/tA6b4tvXGpvBpYVABE7dXJ65PbHFfJWVcblYEVFICMODjHAxRclxR+iZ1qxFk96LmNrdF3mQNlcfWrkNxHPGskbBkcAqw6EV+e1t468Q2WlS6VDqk/2OUgtEW4yCD/MD8q91/Zz+Nlxe38fhDXp1O5SbSZzgluuz/CqRm42Ppiimhw3SnVRIUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRTJZkhUs52qBkk9AKAFMigcnHavOfin8atB+G1pJE86XWq4/d2aNlue59BXkH7QH7SBglk8M+EpxvR1ae+U5KMjB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4T45eCZ/Hnw7vLKxiEuoWzLc24zyxUjcv4rn8a7rmpojg9Mj09a2pT5ZXMa0eZWPzYnge3kaKVGSRCVZWGCp9DUNfTP7SvwYKvL400KD92+PtlvGvQ/3xXzS6hfWvZjNSVzx5Rs7DKKKKokKKKKACiiigAooooAKKKKACiiigApc0lFABRRRQAUUUUAFFFFABRRRQAUUUUAFevfsw6ToWr/E21j1wRSBI2e2hlHyySjp+XWvJoIXnkSONWd3OAqjJJ+lfS/wH/Zv1yHVdO8Wa9M2nR20izw2w/1kmOQT6CgD60iiRIwiKFUDAAHQVIOBikUfKKWgAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigApGOKWobovsbyxlgpxnuaAPk/wDbO8VRT6npXhuJ8yQIbmVf7pPC18xHg12HxXutavPiBrc2vq6XzXLhkboqg4UL7Yrjz1oASiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKUUALSUGkoAmjfauKR231FS5oAKKSigAp68qQaZSg4oASiiigAooooAKKKKACiiigAooooAKcKbThQB9BfspeLRDqd/4WuJMLdp59uCf416j8R/Kvot0dHK88V8H+CfEc/hPxRp2sW/37aZXIJxuGeR+VffsEsWo2lvfRYMdzEkykdwwBH8683GU7PmPSwdS65SCF33dyKvrziokjA7VKOK4DvH0ZFGaTvSd+gh2cipIhk/SsvXNcsPDelz6pqdwkFvChY7jjdgZwPU15Z4C+J2v+OfGy6q0aaZ4Sso5Q3mcecdpCsT65Oce1dFOm3qznnVSdj3JraG6tpLeeNZY5F2urjIYV8RfH74P3Xw215r61jd9CvpM28v/PNzk+Wffg49hX20uo2UemHU5LhFsxH53nE/LtxnOfpXxP8AHz4z3XxN1NNPtR5Oh2ErGGPvK/I3t+GQPTJ9a9KimjzarTZ5JSU7rikYbSRXQYiUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH0h+x78PrLXtT1PxNqNsk8enssFsHGQJSMs31A2/ma+wURQAAOB2r51/YnwfAuuDHP9qE/+Qkr6NAoAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACkKgnkUtFAHzt+1H8Gp/FNovinRLdWv7RMXMajmSMd/civjaRSjlWBBU4IPY1+p8sayAqwBB6g18ofH79mkWYn8UeDoHkUuXurEAfIDyXTHbPagD5doqWaF4JDHIjI6nBDDBqKgAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAFpKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKXNJRQA4Egg5r7n+Bmv/APCSfCvRpi7SS2qG0kJ/vIcAf98la+Fq9V+EHxo1v4dRSabbWKajp80gkeA53Ke5UjoTWGIp88LG1CfJK59nAGlyK4/wv8VPD/ia3haSSTS7mQZ8i8GzJ46E4B5I7/hXYAKx+Ug59DXjyg46HrxqqQcnpXMeNfiR4f8AAVi9xqd2sk2CI4I+XdvSvO/iv8cb3w/fSaBoGnSteH5TNNGRyf7o7ivN9N8Itan/AISv4h3rOka70tmbLO2eAffvit6dG+sjKrVb0idAV1b4r6g3inxjcNpnheyy8VqW2iQDkDHf3qtf61c/FDUl0Dw8yaH4RtMtPcn92HVec/8A1qgtm1D4tyS3l/INC8GaWCzBTtMoXnAz1OOv5dTVSw06/wDipc3WmeHoP7I8LadG58xAQ02BkKfUn07Cu2KS3OWTutCP41/GhdWsrPwh4WupRounwJbvMDta4Krt/Lj8a8PLE8k06UnJHOM96jrqSS2OJvXUUHmny8uTTBQSSaYgNJRRQAUUUUAFFFFABRRRQAUUUUAFFLQRigBKKKKACiiigAooooAKKKKACiiigD7I/YnX/ihNbb/qKEf+Qo6+jB0r5h/Yt8QWEXh7W9EeeNL03ouVjLYLIUVcj8U/Wvp1TuAPrQAtFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAU1kDAggEHqDTqKAPmr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5NeLWg4ysz1qU1JXGBeRzivLf2ldV+w/DuGwV9jX9ym5c/eVfmP67a9VA9OtfO37Vms+brOj6MmNltA05+rnp+S1eEheoicTO0DwU0lKaSvaZ5IUUUUgCiiigAqWFsNg9DUVL0oAkmi2nI6VHU8UwI2PSzW20blPFAFaiiigAooooAcnWhhyaTNK3rQA2iiigAooooAKKKKACiiigAooooAsWVxLZ3MNzC5jlicOjg4KkHII981+mnhLXoPE3hzTtYgIMd5bpLgdiRyPwNfmIDivtv8AZG8VtrXw/k0maQvJpkuxR3CHkf1oA94ooHIooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACsfxJ4T0fxbpz6frWnwXls4OUdenuD1B+lbFFAHzhr/7Gfh+81Az6RrV5YWzHJgZRJsHoD1/OvDfjF8CdY+FLR3Lzrf6XO+yO5UYIPow/rX6A4rm/Hvgyx8c+GbvRL9QUmU7Gxko3YigD80MGkrf8b+FLzwX4kvtEvkKyWshUEj747MPqKwKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACl6UlLmmgOz+F/xBuvh/4lt7+N3a0dgtzD2kQ9ePUV9oLcQXdvDd20wmgmRZEkHRwRwfxBr8/QeRX0r+zd4/m1XT5vCV65d7NDNaux58vIyn4E5+hNcWLpXjzI7MLVtKzPbl5YD1OK+Qfj9qv9qfE3VCDlICsCj02jFfXSvsbJ7c18Q/EK8OoeNtbuj/AMtbyVv/AB41lg177Zri37iRzppKU0leiecFFFFABRRRQAUUUUALmpBcNs2nkVFRQAUUUUAFFFFABT2+7TKdnjFADaKKKACiiigAooooAKKKKACiiigAr6F/Y11p7Xx1faWZCI7u1ZwvqyHP8ia+eq9T/Zn1Q6V8YdDYDP2hntsf76kUAfoCOlFA6UUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUhHFLQaAPm39rb4US67pcXjPSYN91YJsvUUctCOQ//Aec+30r4/ZCvcV+pd1aRXdtLbTxrJDKhjdGGQykYIPtg1+fXxw+Fs/wz8Vy20YdtOuCZLWQ/wB3P3fqKAPN6KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAFrofA3iibwl4nsdVhYqIpBvweqnqK52nChx5tGNO2p942moW+q6al9auHhmi8xWXuCM18N61IZdVvHY5JmY/rX0j+z34mOoeBdTtbiTLaUrsqk8iPYT/Q180XziS8ncc7pGOfxrmoQ5ZM6K8+aKK5pKU0ldJzBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABSjpSUooASilpKACiiigAooooAKKKKACiiigArvvgQ234v+E8Zz/aCf1rga7z4Ff8AJX/Cf/YQj/rQB+jA6CikX7o+lLQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAHpXhP7XukwXfwtbUGVfOs7uHYcc4ZtpFe7HpXz5+2Tq4tfh/Z6cHAa7vUJX1VQT/ADoA+LqKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAClHWkpQcU0B6N8GvEg0TU9bspJCsWo6Rdwj08wQsy5/I/nXnbnLE+tLHO8Tbo2KtgjIPOCMH+dMJzUpW1G3cM0lFFMQUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUALSUUUAFFFFABRRRQAUUUUAFFFFABXe/Aj/ksHhP8A7CEf9a4Ku7+B1xFa/FnwtNM4RFv48sTgDrQB+jI6CikB445paACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK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SJUXBXBrgZ5vEyKY3W7UdMEGsS6huw/79X3n+91ranh2vtHPVxEduU03ttKj+Yzgj0qvNc6VGjeXEXbHGazpLOdRuKHFVT1wa64w8zzqla+lhWIJJHHtSZpKK1OYKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAClB4xSUooASiiigAooooAKKKKACiiigAooooAKKKKACiiigAqzYX02m3cV3bStFNEwdHU4Kkd6rUUAfoH8AvicnxI8FxyTSZ1GyxBcg9SccN+Neo1+fHwD+JM/w78c2sjNnT79ltrpCcDBYAN/wEnP51+gkUqSxLIjBlYAgjuDQA+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACgjNFFAFLU5LWCwuJr0xrbRxs8rSfdVQMknPtX5n+KLq1vfEWqXdgmy0mu5ZIVxjbGWJUfgMV+mWr6Xba1pd3pt4nmW13C8Eq/3kZSpH5E18OfHD4AX3w0xq1jO19o8rld+3DQkk4Deo96LAeNhsHNSLcyJ913H0NRshXrTaBptbFr+0boDHnyY/wB6n2GqXGn30V7C5E0TB1Y84IqlSilZFKpJdT0JPjb4qVQv2zGPRQM1QvvijruoAie6kOfQ4rjCaBU+ziWsRNdTbm8XanLnNw/PvWVPeS3D75ZGdvUmoTSVSilsRKpKW7JTMxHLN+dRnk0lFMgWikooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAHq+0gjIIORX3T+zH8TE8a+CU0y7n3arpQEUgY5Z4/4X/mPwr4Tr0v4C/ENfh58QLG9uXI0+5zbXQB/gbo34Ng/hQB+hNFQ211FdQpNCwkikAZXU5BHrU1ABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAARkEetYvi3w1aeK/Dt/ot4iPDdxNH8w6HHB/A1tUjDIODigD8xPFOgXXhjXr/RrxGSeymaFgw64PB/Gsevof9sPwZ/Zni+18RwRkQ6jEElIHAkXj8yK+ecUAJRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABTw5HTg+tMooA+rP2Z/jxZWunx+E/E195To220nlbjB/gJPvX1KkyuFK8hu4r8sVkZGDKSCOhr3b4WftT6/4PtodK16P+2NPiAWORziaIdgD3/GgD7borzbwZ8fvBHjGGPydUjtbh+PJuDtYV6JFdRToHidZEbkMpyDQBLRSBs8UtABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRQKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACg8iiigDzL9oPwYnjD4aanGsQe5s0N1Ecc5UZP6A1+fbDGR3BxX6l3UMc9vJFMgeN1Ksp6EEYINfm58T/Bk3gLxxq+gSq/l21w3kM/WSEnKN+KkZ98jtQBylFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABS5pKKAJEmeNgyMysOhBwa9F+HPx28W+ANQieO+lvrIECS0uHLKw9vSvNqUHBzQB99eBP2kPBHi+3iEt7/Zl6R88FxwAfZuhr1G01C1vohLazxToRndGwIr8thIykFSQR0I4r3v9knxFrF18S102XULiSzNlK5hdyVyCuDg0Afa1FItLQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUADDIrxr9oT4KJ8TdIhvdNSOPWrPhHIx5yf3SfY9K9lpNooA/NHxF8OvFHha7a21PRL6Jx0YRFlYeoIrAe2ljba8bofRhiv1Hnsra4GJYI5BjHzKDxWXL4I8NTsXl0LTnY85aBSf5UAfmTswBTSMdq/QjxX+z38P/FRaS50WK2mfjzbX9236V86/FX9lXWPCcEmp+G3l1WyU7mhx+9jH070AeAUVLPA9vK0UqNG6nBVhgio6AEooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAr2v8AZFJHxdjx/wA+M381rxSva/2Rf+SvRZ/58Zv5rQB90ClpB1NLQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFHeiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooACM0jIrLtYAg8EGlooA8o+Kf7PnhX4gwS3EdtHp2rbTsuYF2hj2Djof518YfED4aa98OdUNjrNqyAnEcwHySD1Br9JiAa85+Ovw4T4i+BL6yt4lOpQIZ7Rscl1525/2gMfjQB+eRpKnu7eS2uZIJY2SSNirKwwVI6gioTQAlFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAV7V+yMM/F2L2sZv5rXite1/sjEf8Ldjz/wA+M381oA+6BS0CigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii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qStLxFYtpuu39mQQYZ3TB9jWbQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFLijB9K7L4c/C7X/AIl6r9i0q3IjUZkuHBCIPr60AcciMzhQDknAGK+nPgL+zR/aSQ+I/GVofs7jdBYv/GCDhm/POK9B8A/sp+FPC80N9q5l1e8jIcJJ8sStnI4HX8a9xiiWJVVFCqowAOABQBl6T4T0PQolj03SrO1AXb+7iAOPyrWVFHG0D6U6igAwKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACmsM5p1BoA/PP4/6A/h/wCKmtQbNiSy+egHcNzmvN6+lv2zPCU8HiTSvEkULG2urf7PK4GcSIcjJ7fKwx9DXzVgk0AJRS4pKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKANvwl4dn8V+I7DRbY7ZbuZYw390E8mv0a8G+D9L8GaLa6XpVpFbwwoFJUDLkDqT3r4w/ZS0mLUvivaySruW2hklGR3HSvu7GKADFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAGX4i8N6b4p0ubS9WtIrq1mXDI4z+Xoa+Y/Fv7Gtx9omn8O6qpiLErFOOQPTNfWFBGaAPg7VP2WPiJYO3kWEV2o7o/WuE8R/DLxf4Th8/WdAvbOHOPMdMr+Yr9K9tVr7TLXUrZ7a8gjnhcYZJFDAj6HigD8ttpoxX2F8RP2QtP1rUpNQ8L36aYsgJe1dNyBv9n0rj7P9i3XZCBc69aRL6rGSTQB824oxX1Ev7E1zjLeKowf+vf8A+vXP+Jf2PPFWl27zaVqFtqW0Z2Y2MfpQB8+0lbviLwV4g8K3JttY0u5tXHOXQ4P41iFSKAG0UuKXaaAG0UpUikoAKKKUKT0oASineW2M9qQjBwaAEooooAKKKKAPpH9jDR2m8VapqZU7IbcID7k19h18/wD7HGgiy+H13qrAh768ZRkfwoABj86+gKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKADFGKKKAAikK564paKAM/UtA0zWYjFqNha3aEYxNGG4/GvMvFX7MPw/wDErNKlg+mzMclrRto/756V67RQB8xz/sU6e1yzQeJ50hJ+VGgBIH1zV/U/2MfDcmnqlhrN9DdjG6WTDKfXivo2jGaAPijX/wBj/wAa2LO2m3NjqC5+VQ2xiPfNcjqn7N3xK0vHmaC03/XCQPiv0E20bRQB+dUXwK+IcsgQeGbwEnHK8V1mjfsn/EPUJUW7t7OwjYZ8ySXdj2wK+6NgznFLtoA+VX/YxYeHvk8QZ1cZPKfujxwvr1714D43+GfibwBdeTrunvApPyyr8yN9DX6Ubec5rF8VeDdG8Z6XJpms2iXNu46MOVPqDQB+ZG33ptfVXjb9jJnlkuPCetIq4JW1vB1PoGHT8a8K8YfB3xr4HLNrGh3CQAkC4iAkjYA4zlc4H1xQBxVTW1u9zcRwxjc8jbVHqaa0LKcEY+vFeu/s2fDW48a+PrO+ubZ20rTGFxO5X5WYconvlsZ9s0AfZXwz8Lx+DvA2i6KsflvbWyeav/TUjL/+PE11NNVcY9qdQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAJimS20U6GOVFkRuqsoINSUUAcrqPwu8HarcNcXfh7T5JmOWfyQMmtrSNC07QrQWmmWcNpApyEhQKP0rQooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA//2Q=="
    nika_img="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"
    profile="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"
    choose=random.randint(0,1)
    if choose==1:

             
        try:
            with open("nika.png", "r") as img_f:
                img_f.close()
        except FileNotFoundError:
            with open("nika.png", "wb") as img_f:
                image_da= base64.b64decode(nika_img)
                img_f.write(image_da)
                ctypes.windll.kernel32.SetFileAttributesW("nika.png" , 0x02)
                os.chmod("nika.png" , 0o4444)

        background_image =ImageTk.PhotoImage(Image.open("nika.png"))
        background_label = tk.Label(rootmainactivity, image=background_image)
        background_label.place(relwidth=1, relheight=1)
    else:
        try:
            with open("mahsa.png", "r") as img_f:
                img_f.close()
        except FileNotFoundError:
            with open("mahsa.png", "wb") as img_f:
                image_da= base64.b64decode(mahsa_img)
                img_f.write(image_da)
                ctypes.windll.kernel32.SetFileAttributesW("mahsa.png" , 0x02)
                os.chmod("mahsa.png" , 0o4444)
        background_image =ImageTk.PhotoImage(Image.open("mahsa.png"))
        background_label = tk.Label(rootmainactivity, image=background_image)
        background_label.place(relwidth=2, relheight=2)
    
    try:
            with open("profile.png", "r") as img_f:
                img_f.close()
    except FileNotFoundError:
            with open("profile.png", "wb") as img_f:
                image_da= base64.b64decode(profile)
                img_f.write(image_da)
                ctypes.windll.kernel32.SetFileAttributesW("profile.png" , 0x02)
                os.chmod("profile.png" , 0o4444)
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
        root_about=tk.Tk()
        root_about.title("About")
        root_about.geometry("250x250")

        label_about=tk.Label(root_about, text="This is an Warp Scanner For win")
        label_about.pack()

        label_about1=tk.Label(root_about, text="Github Link :")
        label_about1.pack()
        link_git=tk.Label(root_about, text="Github" , fg="blue" , cursor="hand2")
        link_git.pack()
        link_git.bind("<Button-1>" ,Github_link)

        label_about2=tk.Label(root_about, text="Telegram Link :")
        label_about2.pack()
        link_tel=tk.Label(root_about, text="Telegram" , fg="blue" , cursor="hand2")
        link_tel.pack()
        link_tel.bind("<Button-1>" ,Telegram_link)

        label_about2=tk.Label(root_about, text="Created by Arshiacomplus", bg="red")
        label_about2.pack(side=tk.BOTTOM)

        



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
            if checkbox_var3.get() ==0:
                wich_p= "1\n"

            with open("warp_setting" , "r") as f:
                warp11=f.readlines()
            with open("warp_setting" , "w") as f:
                warp11[2]=wich_p
                for i in warp11:
                    f.write(i)

            rootmainactivity.update()
            
             
        menu_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0)
        main_frame1 = tk.Frame(rootmainactivity, bg="lightblue", bd=5)
        main_frame1.pack(side="right", fill="both", expand=False)

        # --- Create the Slide Frame (Initially Hidden) ---

        slide_frame = tk.Frame(rootmainactivity, bg="gray", bd=5)
        slide_frame.pack(side="right", fill="y", expand=False)
        slide_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0, width=150, height=rootmainactivity.winfo_screenheight())

        spu_label=ttk.Label(slide_frame,text="Scan  speed", background="gray" )
        spu_label.pack()
        checkbox_var = tk.IntVar()
        with open("warp_setting" , "r") as f:
            num=f.readline()

        if  num[0] =="2":
                checkbox_var = tk.IntVar(value=1)
        elif  num[0] =="1":
                checkbox_var = tk.IntVar(value=0)

            
        print(checkbox_var.get())
        checkbox1 = tk.Checkbutton(slide_frame, text="Faster", variable=checkbox_var, onvalue=1, offvalue=0)
        checkbox1.pack(pady=10)

        checkbox2 = tk.Checkbutton(slide_frame, text="Slower", variable=checkbox_var, onvalue=0, offvalue=0)
        checkbox2.pack(pady=10)


        save_ch=ttk.Label(slide_frame,text="Save result", background="gray" )
        save_ch.pack(pady=10)

        with open("warp_setting" , "r") as f:
            num=f.readlines()
            if  num[1] =="2\n":
                checkbox_var2 = tk.IntVar(value=1)
            else:
                checkbox_var2 = tk.IntVar(value=0)

        checkbox3 = tk.Checkbutton(slide_frame, text="Yes", variable=checkbox_var2, onvalue=1, offvalue=0)
        checkbox3.pack(pady=10)

        checkbox4 = tk.Checkbutton(slide_frame, text="No", variable=checkbox_var2, onvalue=0, offvalue=0)
        checkbox4.pack(pady=10)

        which_panel=ttk.Label(slide_frame,text="Which panel", background="gray" )
        which_panel.pack(pady=10)
        checkbox_var3=tk.IntVar()
        with open("warp_setting" , "r") as f:
            num=f.readlines()
            print(num[2], "hhh")
    
            if  num[2] =="2\n":
                    checkbox_var3 = tk.IntVar(value=1)
            else:
                    checkbox_var3 = tk.IntVar(value=0)

            

        checkbox5 = tk.Checkbutton(slide_frame, text="bpb", variable=checkbox_var3, onvalue=1, offvalue=0)
        checkbox5.pack(pady=10)

        checkbox6 = tk.Checkbutton(slide_frame, text="vahid", variable=checkbox_var3, onvalue=0, offvalue=0)
        checkbox6.pack(pady=10)

        submit=ttk.Button(slide_frame, text="save", command=sumbit_f)
        submit.pack(pady=10)

        
        for i in range(300, rootmainactivity.winfo_width()  - slide_frame.winfo_width()-150):
                    slide_frame.place(x=i, y=0)
                    rootmainactivity.update() 
                    time.sleep(0.00001) 

    def check_up():
            def Github_link():
                webbrowser.open_new(r"https://github.com/arshiacomplus/WarpScanner/releases")
            ret=Check_for_update()
            if ret[0]  == True:
                rootupdate=tk.Tk()
                rootupdate.title("Update")

                label_up=tk.Label(rootupdate, text=f"New version Available {ret[1]}")
                label_up.pack()

                button_up=tk.Button(rootupdate, text="click to update",command=Github_link)
                button_up.pack()

                rootupdate.mainloop()

            else:

                rootupdate=tk.Tk()
                rootupdate.title("Update")

                label_up=tk.Label(rootupdate, text="You have new version ")
                label_up.pack()

                button_up=tk.Button(rootupdate, text="Close" , command=rootupdate.destroy)
                button_up.pack()

                rootupdate.mainloop()



        
                 
        





  






#     labelmain=tk.Label(rootmainactivity, width=50, padx=50,pady=10, fg="blue" ,text="""Hello This is my Scanner
# created by Telegram= @arshiacomplus\n""")
#     labelmain.pack()




    main_frame = tk.Frame(rootmainactivity)
    main_frame.pack(side="right", fill="both",expand=False)



    menu_frame = tk.Frame(rootmainactivity, bg="gray")
    menu_frame.pack(side="right", fill="y", expand=False)
    menu_frame.place(x=rootmainactivity.winfo_screenwidth(), y=0, width=150, height=rootmainactivity.winfo_screenheight())


    style = ttk.Style()
    style.configure("TButton",
                    foreground="black",
                    background="lightblue",
                    highlightthickness=20,
                    highlightbackground="lightblue",
                    highlightcolor="lightblue",
                    relief="groove",
                    borderwidth=10,
                    bordercolor="lightblue",
                    font=("Helvetica", 12, "bold"),
                    anchor="center",
                    justify="center")
    
     
     
    label_pro=tk.Label(menu_frame, image=menu_image)
    label_pro.pack(pady=50)
  
    Setting_button = ttk.Button(menu_frame,text="Setting", command=Setting)
    Setting_button.pack()


    up_button = ttk.Button(menu_frame, text="Check for update", command=check_up)
    up_button.pack(pady=20)

    About_button = ttk.Button(menu_frame, text="About", command=About)
    About_button.pack(pady=10)

    exit_button = ttk.Button(menu_frame, text="Exit", command=rootmainactivity.quit)
    exit_button.pack(pady=10)

    label_arshia= ttk.Label(menu_frame, text="Created by arshiacomplus \n                   v0.1.3", foreground="white", background="gray")
    label_arshia.pack(pady=10)


    toggle_menu_button = ttk.Button(rootmainactivity,padding=5, text="Menu", command=lambda: toggle_menu())
    toggle_menu_button.pack(side="right", anchor="ne", padx=1, pady=1)




    

    check=  check_ipv6()
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


    button = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="scan ip", command=which_Cpu_speed,fg="#f0f0f0", bg="#414141")
    button.pack(padx=11, pady=4)

    button1 = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="wireguard config", command=wireguard_config,fg="#f0f0f0", bg="#414141")
    button1.pack(padx=11, pady=4)

    button2 = tk.Button(rootmainactivity, width=30, padx=11, pady=4, bd=8, text="wireguard config without ip scanning", command=wireguard_config_without,fg="#f0f0f0", bg="#414141")
    button2.pack(padx=11, pady=4)



    button3 = tk.Button(rootmainactivity, width=15, padx=15, pady=4, bd=8, text="wireguard with a sub link", command=wireguard_config_sub,fg="#f0f0f0", bg="#414141")
    button3.pack()

    # button = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="wireguard for v2ray and mahsaNG", command=which_Vip,fg="#f0f0f0", bg="#414141")
    # button.pack()

    # button = tk.Button(rootmainactivity, width=10, padx=11, pady=4, bd=8, text="wireguard for v2ray and mahsaNG without ip scanning", command=which_Vip,fg="#f0f0f0", bg="#414141")
    # button.pack()

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
