V=58
import urllib.request
import urllib.parse
from urllib.parse import quote
import os
try:
    import requests
except ImportError:
    print("Requests module not installed. Installing now...")
    os.system('pip install requests')
try:
    import requests
except ModuleNotFoundError:
    os.system('wget https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
try:
    import requests
except ModuleNotFoundError:
    os.system('curl -L -o requests-2.32.2.tar.gz https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
    import requests
import re
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
try:
    import rich
except Exception:
    print("Rich module not installed. Installing now...")
    os.system('pip install rich')
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich.table import Table
try:
    import retrying
except Exception:
    print("retrying module not installed. Installing now...")
    os.system('pip install retrying')
try:
    import retrying
except Exception:
    os.system("wget https://github.com/rholder/retrying/archive/refs/tags/v1.3.3.tar.gz")
    os.system("tar -zxvf v1.3.3.tar.gz")
    os.chdir("retrying-1.3.3")
    os.system("python setup.py install")
from retrying import retry
from requests.exceptions import ConnectionError

import random
import subprocess
import json
import sys
try:
    from icmplib import ping as pinging
except Exception:
    os.system('pip install icmplib')
    from icmplib import ping as pinging
try:
    from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey 
    from cryptography.hazmat.primitives import serialization
except Exception:
    try:
        print("cryptography module not installed. Installing now...")
        os.system('pkg install python3 rust binutils-is-llvm -y')
        os.system('export CXXFLAGS="-Wno-register"')
        os.system('export CFLAGS="-Wno-register"')
        os.system('python3 -m pip install cryptography ')
    except Exception:
       os.system("wget https://github.com/pyca/cryptography/archive/refs/tags/43.0.0.tar.gz")
       os.system("tar -zxvf 43.0.0.tar.gz")
       os.chdir("cryptography-43.0.0")
       os.system("pip install .")
try:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
except Exception:
 print('somthing wemt wrong with cryptography')
 
import base64
try:
    import datetime
except Exception:
    os.system('pip install datetime')
    import datetime
try:
    from alive_progress import alive_bar
except Exception:
    os.system("pip install alive_progress")
    from alive_progress import alive_bar
api=''
ports = [1074, 894, 908, 878]
console = Console()
wire_config_temp=''
wire_c=1
wire_p=0
send_msg_wait=0
results=[]
resultss=[]
save_result=[]
save_best=[]
best_result=[]
WoW_v2=''
isIran=''
max_workers_number=0
do_you_save='2'
which=''
ping_range='n'
def gt_resolution():
    return os.get_terminal_size().columns

def info():
    console.clear()
    
    table = Table(show_header=True,title="Info", header_style="bold blue")
    table.add_column("Creator", width=15)
    
    table.add_column("contact", justify="right")
    table.add_row("arshiacomplus","1 - Telegram")
    table.add_row("arshiacomplus","2 - github")
    console.print(table)
    
    print('\nEnter a Number\n')
    options2={"1" : "open Telegram Channel", "2" : "open github ", "0":"Exit"}
    for key, value in options2.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats2 = Prompt.ask("Choose an option", choices=list(options2.keys()), default="1")
    
    if whats2=='0':
        os.execv(sys.executable, ['python'] + sys.argv)
    elif whats2=='1':
        os.system("termux-open-url 'https://t.me/arshia_mod_fun'")
    elif whats2=='2'   :
        os.system("termux-open-url 'https://github.com/arshiacomplus/'")
        
def check_ipv6():
    
    try:
        ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php', timeout=15)
        if ipv6.status_code == 200:
            ipv6 ="[green]Available[/green]"
    except Exception:
        ipv6 = "Unavailable"
    try:
        ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php',timeout=15)
        if ipv4.status_code == 200:
            ipv4= "[green]Available[/green]"
    except Exception:
        ipv4 = "Unavailable"
    return  [ipv4,ipv6]

def input_p(pt ,options):
    os.system('clear')
    options.update({"0" : "Exit"})
    print(pt)
    for key, value in options.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats = Prompt.ask("Choose an option", choices=list(options.keys()), default="1")
    if whats=='0':
        os.execv(sys.executable, ['python'] + sys.argv)
    return whats
def urlencode(string):
    
    if string is None:
        return None
    return urllib.parse.quote(string, safe='a-zA-Z0-9.~_-')


def free_cloudflare_account2():
    
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("https://fscarmen.cloudflare.now.cc/wg", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("https://fscarmen.cloudflare.now.cc/wg", timeout=30)
                return response.text
            
    response = file_o()
    PublicKey=response[response.index(':')+2:response.index('\n')]
    PrivateKey=response[response.index('\n')+13:]
    reserved=[222,6,184]
    return ["2606:4700:110:8d48:52cb:c565:3a80:c416/128" , PrivateKey , reserved, PublicKey]



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
def fetch_config_from_api():
    global api
    if api=='':
        which_api=input_p('Which Api \n', {'1':'First api/Not work', '2' :'Second api'})
        api=which_api
    else:
        which_api=api
    if which_api == '2':
        
        keys=bind_keys()
        
        keys=list(keys)
        
        return {
        'PrivateKey': keys[1],
        'PublicKey':  keys[3],
        'Reserved':  keys[2],
        'Address':  keys[0]
        }
        
 
        
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
    
    
def free_cloudflare_account():
    global api
    if api=='':
        which_api=input_p('Which Api \n', {'1':'First api/Not work', '2' :'Second api'})
        api=which_api
    else:
        which_api=api
    if which_api == '2':
        keys=bind_keys()
        keys=list(keys)
        return keys
        
        
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("https://api.zeroteam.top/warp?format=sing-box", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("https://api.zeroteam.top/warp?format=sing-box", timeout=30)
                return response.text
    try:
            output = file_o()
    except ConnectionError:
            console.print("[bold red]Failed to connect to API after 6 attempts.[/bold red]")

       
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
def upload_to_bashupload(config_data):
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
        files = {'file': ('output.json', config_data)}
        try:
            response = requests.post('https://bashupload.com/', files=files, timeout=30)
        except Exception:
            response = requests.post('https://bashupload.com/', files=files, timeout=50)
        return response
    try:
        
        response = file_o()

        if response.ok:
            download_link = response.text.strip()
            download_link_with_query = download_link[59:len(download_link)-27] + "?download=1"
            console.print(f'[green]Your link: {download_link_with_query}[/green]')
        else:
            console.print("[red]Something happened with creating the link[/red]", style="bold red")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]", style="bold red")
        
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
def scan_ip_port(ip, results):
    port=ports[random.randint(0,3)]
    
    
    icmp=pinging(ip, count=4, interval=1, timeout=5,privileged=False)
    
    
    
    
    
    results.append((ip, port, float(icmp.avg_rtt), icmp.packet_loss, icmp.jitter))
    
    
    
    
            
            
        
def main_v6():
    global which
    global ping_range
    global save_best
    global resultss
    global which
    resultss=[]
    
    def generate_ipv6():
        return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"

    def ping_ip(ip, port):
        global do_you_save
        global resultss
        
        icmp=pinging(ip, count=4, interval=1, timeout=5,privileged=False, family='ipv6')

        
        resultss.append((ip, port, float(icmp.avg_rtt), icmp.packet_loss, icmp.jitter))
        
            

    console = Console()
    ports_to_check = [1074 , 864]

    random_ip=generate_ipv6()
    best_ping=1000
    best_ip=""




    table = Table(show_header=True, title="IP Scan Results", header_style="bold blue")
    table.add_column("IP", style="dim",width=15)  # Set no_wrap to False to allow text wrapping
    table.add_column("Port", justify="right")
    table.add_column("Ping (ms)", justify="right")
    table.add_column("Packet Loss (%)", justify="right")
    table.add_column("Jitter (ms)", justify="right")
    table.add_column("Score", justify="right")
    
    

    executor= ThreadPoolExecutor(max_workers=800)
    try:
        print("\033[1;35m")
        futures = [executor.submit(ping_ip, generate_ipv6(), ports_to_check[random.randint(0,1)])  for _ in range(101)]
        none=gt_resolution()
        
        bar_size=min( none-40, 20)
        if bar_size<3:
            bar_size=3
        elif bar_size>1000:
            bar_size=1000
        with alive_bar(total=len(futures), length=bar_size) as bar:  # Length is in characters
                    for future in futures:
                        time.sleep(0.01)
                        result = future.result()
                        bar()

    except Exception as E:
            rprint('[bold red]An Error: [/bold red]', E)
    finally:
            executor.shutdown(wait=True)
    print("\033[0m")
    extended_results=[]
    for result in resultss:
        ip, port, ping ,loss_rate,jitter= result
        if ping ==0.0:
            ping=1000
        if float(jitter)==0.0:
            jitter=1000
        if loss_rate ==1.0 :
            loss_rate=1000
            
        loss_rate=loss_rate*100
        if which !='3' and do_you_save=='1':
            if loss_rate == 0.0 and ping !=0.0:
                    if ping<=int(ping_range):
                        if which =="1" or which=="2" :
                            if need_port=="1":
                                if which=='2':
                                    save_best.append("\n")
                                    save_best.append('['+str(ip)+']'+":"+str(port))
                                elif which=='1':
                                    
                                    save_best.append('['+str(ip)+']'+":"+str(port)+",")
                            else:
                                if which=='2':
                                    save_best.append("\n")
                                    save_best.append('['+str(ip)+']')
                                elif which=='1':
                                    
                                    save_best.append('['+str(ip)+'],')
    
            
        combined_score = 0.5 * ping + 0.3 * loss_rate + 0.2 * jitter

        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))

    # Sort the results based on ping time
    sorted_results=sorted(extended_results, key=lambda x: x[5])
    

    for ip, port,ping,loss_rate,jitter, combined_score  in sorted_results:
        if which =='3':
            save_best.append('['+ip+']'+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
        table.add_row(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%",f"{jitter}", f"{combined_score:.2f}")
        if ping < best_ping:
            best_ping = ping
            best_ip = ip
    os.system("clear")

    console.print(table)
    port_random = ports_to_check[random.randint(0, len(ports_to_check) - 1)]
    if do_you_save=='1':
        
        if which!='2':
            save_best[len(save_best)-1]=save_best[len(save_best)-1][:len(save_best[len(save_best)-1])-1]
        with open('/storage/emulated/0/result.csv' , "w") as f:
            for j in save_best:
                f.write(j)
        print(' saved in /storage/emulated/0/result.csv !')
    best_ip_mix = [1] * 2
    if best_ip:
        console.print(f"\n[bold green]Best IP : [{best_ip}]:{port_random} with ping time: {best_ping} ms[/bold green]")
        
        if what !='2' and what!='3'and what != '4':
        
            best_ip_mix[0] = "[" + best_ip + "]"
        else:
            best_ip_mix[0] =  best_ip 
        best_ip_mix[1] = port_random
        
    else:
        console.print(f"\n[bold green]Best IP : [{random_ip}]:{port_random} with ping time: {best_ping} ms[/bold green]")
        if what !='2' and what!='3'and what != '4':
        
            best_ip_mix[0] = "[" + random_ip + "]"
        else:
            best_ip_mix[0] =  random_ip 
                 
        
        best_ip_mix[1] = port_random
    return best_ip_mix

        

def main():
    global which
    global max_workers_number
    global ping_range
    ping_range=''
    results=[]
    if do_you_save=='1':
        ping_range=input('\nping range(zero to what)[defual= n]: ')
        if ping_range=='n' or ping_range=='N':
            ping_range='300'
    if what!='0':
        which_v=input_p('Choose an ip version\n ', {"1": 'ipv4' ,
         "2": 'ipv6'})
        if which_v=="2":
            console.clear()
            
            best_result=main_v6()
            return best_result
    Cpu_speed=input_p('scan power', {"1" : "Faster" , "2" : "Slower"})
    if Cpu_speed == "1": max_workers_number=1000
    elif Cpu_speed == "2": max_workers_number=500
    
    console.clear()
    console.print("Please wait, scanning IP ...\n\n", style="blue")

    start_ips = ["188.114.96.0", "162.159.192.0", "162.159.195.0"]
    end_ips = ["188.114.99.224", "162.159.193.224", "162.159.195.224"]
    ports = [1074, 894, 908, 878]
   

    for start_ip, end_ip in zip(start_ips, end_ips):
        ip_range = create_ip_range(start_ip, end_ip)
        executor=ThreadPoolExecutor(max_workers=max_workers_number)
        print("\033[1;35m")
        try:
                
                futures = [executor.submit(scan_ip_port, ip, results) for ip in ip_range]
                none=gt_resolution()
               
                bar_size=min( none-40, 20)
                if bar_size<3:
                    bar_size=3
                elif bar_size>1000:
                    bar_size=1000
                with alive_bar(total=len(futures), length=bar_size) as bar:  # Length is in characters
                    for future in futures:
                        time.sleep(0.01)
                        result = future.result()
                        bar()
                        
                        
                    
                
        except Exception as E:
            print("Error :",E)
        finally:
            executor.shutdown(wait=True)

        print("\033[0m")
    extended_results = []
    
    for result in results:
        ip, port, ping ,loss_rate,jitter= result
        if ping ==0.0:
            ping=1000
        if float(jitter)==0.0:
            jitter=1000
        if loss_rate ==1.0 :
            loss_rate=1000
            
        loss_rate=loss_rate*100
        if which !='3' and do_you_save=='1':
            if loss_rate == 0.0 and ping !=0.0:
                if which =="1" or which=="2" :
                    if need_port=="2":
                    
                        try:
                            if ping<=int(ping_range):
                                save_result.index(str(ip))
                        except Exception:
                            if ping<=int(ping_range):
                                save_result.append("\n")
                                save_result.append(str(ip))
                    else:
                        try:
                            if ping<=int(ping_range):
                                save_result.index(str(ip)+":"+str(port))
                        except Exception:
                            if ping<=int(ping_range):
                                save_result.append("\n")
                                save_result.append(str(ip)+":"+str(port))
    
            
        combined_score = 0.5 * ping + 0.3 * loss_rate + 0.2 * jitter

        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))
       

    sorted_results = sorted(extended_results, key=lambda x: x[5])
    
    if which=='3':
        for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
            
            save_result.append(ip+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
    
    

    console.clear()
    table = Table(show_header=True,title="IP Scan Results", header_style="bold blue")
    table.add_column("IP", style="dim", width=15)
    table.add_column("Port", justify="right")
    table.add_column("Ping (ms)", justify="right")
    table.add_column("Packet Loss (%)", justify="right")
    table.add_column("Jitter (ms)", justify="right")
    table.add_column("Score", justify="right")

    for ip, port, ping, loss_rate,jitter, combined_score in sorted_results[:10]:
        table.add_row(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%",f"{jitter}", f"{combined_score:.2f}")

    console.print(table)

    best_result = sorted_results[0] if sorted_results else None
    if best_result and best_result[0] != "No IP":
        ip, port, ping, loss_rate,jitter, combined_score = best_result
        try:
            console.print(f"The best IP: {ip}:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}%, {jitter:.2f} ms ,score: {combined_score:.2f}", style="green")
        except TypeError:
            console.print(f"The best IP: {ip}:{port if port else '878'} , ping: None, packet loss: {loss_rate:.2f}% ,{jitter:.2f} ms ,  score: {combined_score:.2f}", style="green")
        best_result=2*[1]
        best_result[0]=f"{ip}"
        best_result[1]=port
    else:
        console.print("Nothing was found", style="red")
    t=False
    if what == '1':
        if do_you_save=='1':
            if which =="1":
                 
                 with open('/storage/emulated/0/result.csv' , "w") as f:
                      for j in save_result[1:]:
                          if j != "\n":
                              f.write(j)
                              t=False
                          else:
                         # 	if j != save_result[len(save_result)-1]:
                                  if t==False:
                                       f.write(",")
                                  t=True
                                 
            else:
                 with open('/storage/emulated/0/result.csv' , "w") as f:
                      for j in save_result:
                          f.write(j)
                       
            print(' saved in /storage/emulated/0/result.csv !')
            

    return best_result


def main2():
    global best_result
    
    
    def main2_2():
        global WoW_v2
        try:
           all_key3=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()

        try:
                all_key2=free_cloudflare_account()
        except Exception as E:
                print(' Try again Error =', E)
                exit()
        os.system('clear')
        print(f'Make Wireguard ')
        time.sleep(10)
        WoW_v2+=f'''
    {{
        "remarks": "Tel= arshiacomplus - WoW",
        "log": {{
            "loglevel": "warning"
        }},
        "dns": {{
            "hosts": {{
                "geosite:category-ads-all": "127.0.0.1",
                "geosite:category-ads-ir": "127.0.0.1"'''
        if polrn_block=='1' :WoW_v2+=f''',
                "geosite:category-porn": "127.0.0.1"'''
                
        WoW_v2+=f'''
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
                    "enabled": true,
                    "routeOnly": true
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
                    "enabled": true,
                    "routeOnly": true
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
        "outbounds": [
            {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                        "172.16.0.2/32",
                        "{all_key3[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                        {{
                            "endpoint": "{best_result[0]}:{best_result[1]}",
                            "publicKey": "{all_key3[3]}"
                        }}
                    ],
                    "reserved": {all_key3[2]},
                    "secretKey": "{all_key3[1]}"'''
        if what== '14':WoW_v2+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
        WoW_v2+=f'''
                }},
                "streamSettings": {{
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
                            "endpoint": "162.159.192.115:864",
                            "publicKey": "{all_key2[3]}"
                        }}
                    ],
                    "reserved": {all_key2[2]},
                    "secretKey": "{all_key2[1]}"'''
        if what== '14':WoW_v2+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
        WoW_v2+=f'''
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
        if polrn_block=='1' :WoW_v2+=f''',
                        "geosite:category-porn"'''
        WoW_v2+=f'''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                }},
                {{
                    "outboundTag": "warp-out",
                    "type": "field",
                    "network": "tcp,udp"
                }}
            ]
        }},
        "stats": {{}}
    }},
    {{
        "remarks": "Tel= arshiacomplus - Warp",
        "log": {{
            "loglevel": "warning"
        }},
        "dns": {{
            "hosts": {{
                "geosite:category-ads-all": "127.0.0.1",
                "geosite:category-ads-ir": "127.0.0.1"'''
        if polrn_block=='1' :WoW_v2+=f''',
                "geosite:category-porn": "127.0.0.1"'''
                
        WoW_v2+=f'''
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
                    "enabled": true,
                    "routeOnly": true
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
                    "enabled": true,
                    "routeOnly": true
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
        "outbounds": [
            {{
                "protocol": "wireguard",
                "settings": {{
                    "address": [
                        "172.16.0.2/32",
                        "{all_key3[0]}"
                    ],
                    "mtu": 1280,
                    "peers": [
                        {{
                            "endpoint": "{best_result[0]}:{best_result[1]}",
                            "publicKey": "{all_key3[3]}"
                        }}
                    ],
                    "reserved": {all_key3[2]},
                    "secretKey": "{all_key3[1]}"'''
        if what== '14':WoW_v2+=''',
                    "keepAlive": 10,
                    "wnoise": "quic",
                    "wnoisecount": "10-15",
                    "wpayloadsize": "1-8",
                    "wnoisedelay": "1-3"'''
        WoW_v2+=f'''
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
                        "geoip:ir"
                    ],
                    "outboundTag": "direct",
                    "type": "field"
                }},
                {{
                    "domain": [
                        "geosite:category-ads-all",
                        "geosite:category-ads-ir"'''
        if polrn_block=='1' :WoW_v2+=f''',
                        "geosite:category-porn"'''
        WoW_v2+=f'''
                    ],
                    "outboundTag": "block",
                    "type": "field"
                }},
                {{
                    "outboundTag": "warp",
                    "type": "field",
                    "network": "tcp,udp"
                }}
            ]
        }},
        "stats": {{}}
    }}'''
        if n !=how_many-1:
            WoW_v2+=','
            return 
    def main2_1():
        global best_result
        
        print()
        try:
            all_key=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        if what == '7':
            if isIran=='2' :
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()
        else:
                try:
                    all_key2=free_cloudflare_account()
                except Exception as E:
                    print(' Try again Error =', E)
                    exit()

        
        temp_ip=''
        temp_port=''
        temp_c=0
        if what =='3' and what=='16':
            print("\033[0m")
            enter_ip=input('Enter ip with port(Default =Enter( N )) : ')
            if enter_ip=='N' or  enter_ip=='n':
                best_result=["162.159.195.166" , 908]
            else:
                while enter_ip[temp_c] !=':':
                        temp_ip=temp_ip+enter_ip[temp_c]
                        temp_c=temp_c+1
                            
                        
                set_enter_ip=enter_ip.index(":")
                temp_port=enter_ip[set_enter_ip+1: ]
                    

                    
                    
                    #temp_port=temp_port+enter_ip[i]
                best_result=[temp_ip, int(temp_port)]

        Wow=''
        if what=='7' or what =='13':
             print("\033[0m")
             os.system('clear')
             
             Wow=f'''{{
  "dns": {{
    "hosts": {{
      "geosite:category-ads-all": "127.0.0.1",
      "geosite:category-ads-ir": "127.0.0.1"'''
             if polrn_block=='1' : Wow+=''',
      "geosite:category-porn": "127.0.0.1"'''
        
            
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
                 if what== '13':Wow+=''',
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
             
             if isIran=='1':
                 if polrn_block=='1':Wow+=''',
          "geosite:category-porn"'''
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
                 if what== '13':Wow+=''',
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
                 if polrn_block=='1' :Wow+=''',
          "geosite:category-porn"'''
                 Wow+='''
        ],
        "outboundTag": "block",
        "type": "field"
      },
      {
        "network": "tcp,udp",
        "outboundTag": "warp-out",
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

             print(Wow), exit()
        
        else:
            os.system('clear')
            hising=f'''
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

    "mtu": 1280'''
            if what !='15' and what !='16':hising+=f''',
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"'''
            hising+=f'''
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
    "mtu": 1330'''
            if what !='15' and  what !='16':hising+=f''',
    "fake_packets_mode":"m4"'''
            hising+=f'''
 
    }}
  ]
}}
'''
            print(hising),exit()
        if what=="3":
            exit()
                

    
    
    if what=="3":
        main2_1()
        exit()
    


    best_result=main()
    
    if what=='8' or what=='14':
        
        rprint("[bold green]Please wait, generating WireGuard URL...[/bold green]")
        for n in range(how_many):
            main2_2()
        os.system('clear')
        
        #upload_to_bashupload
        upload_to_bashupload(f'''[
{WoW_v2}
]''')
        exit()
        
    
    main2_1()

    
def main3():
    global best_result
    global wire_config_temp
    global wire_c

    global wire_p
    if wire_p==0:

         try:
             best_result=main()
         except Exception:
             print("\033[91m")
             print('Try again and choose wire guard without ip')
             print('\033[0m')
             exit()
    
    os.system('clear')
         

    if wire_p==1:
            print(f"please wait make wireguard : {wire_c-1}. ")
    
    
    print('\033[0m')

    
    

    if wire_p !=1:
        all_key=free_cloudflare_account()
        time.sleep(5)
        all_key2=free_cloudflare_account()
        time.sleep(5)
        wire_config_or = f'''

    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-IR{wire_c}",
    "local_address": [
        "172.16.0.2/32",
        "{all_key[0]}"
    ],
    "private_key": "{all_key[1]}",
    "peer_public_key": "{all_key[3]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "reserved": {all_key[2]},

    "mtu": 1280'''
        if what!='17':
            wire_config_or+=''',
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"'''
        wire_config_or+=f'''
    }},
    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-Main{wire_c}",
    "detour": "Tel=@arshiacomplus Warp-IR{wire_c}",
    "local_address": [
        "172.16.0.2/32",
        "{all_key2[0]}"
    ],
    "private_key": "{all_key2[1]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "peer_public_key": "{all_key2[3]}",
    "reserved": {all_key2[2]},
    "mtu": 1330'''
        if what!='17':
            wire_config_or+=''',
    "fake_packets_mode":"m4"'''
        wire_config_or+=f'''
    }}

'''
    else:
        all_key=free_cloudflare_account()
        time.sleep(5)
        all_key2=free_cloudflare_account()
        time.sleep(5)
        wire_config_or = f'''

    ,{{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-IR{wire_c}",
    "local_address": [
        "172.16.0.2/32",
        "{all_key[0]}"
    ],
    "private_key": "{all_key[1]}",
    "peer_public_key": "{all_key[3]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "reserved": {all_key[2]},

    "mtu": 1280'''
        if what!='17':
            wire_config_or+=''',
    "fake_packets":"1-3",
    "fake_packets_size":"10-30",
    "fake_packets_delay":"10-30",
    "fake_packets_mode":"m4"'''
        wire_config_or+=f'''
    
    }},
    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-Main{wire_c}",
    "detour": "Tel=@arshiacomplus Warp-IR{wire_c}",
    
    "local_address": [
        "172.16.0.2/32",
        "{all_key2[0]}"
    ],
    "private_key": "{all_key2[1]}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},
    "peer_public_key": "{all_key2[3]}",
    "reserved": {all_key2[2]},
    "mtu": 1330'''
        if what!='17':
            wire_config_or=wire_config_or+''',
    "fake_packets_mode":"m4"'''
        
        wire_config_or+=f'''
    }}

'''

    if i == int(how_many)-1:
        os.system('clear')
        upload_to_bashupload(f'''{{
  "outbounds": 
  [{wire_config_temp}
  ]
}}
''')
    else:
                    
        wire_config_temp=wire_config_temp+wire_config_or
            
            
    wire_c=wire_c+1
    wire_p=1
def generate_wireguard_url(config, endpoint):
    global api
    
    required_keys = ['PrivateKey', 'PublicKey' ,'Address' ]
    if not all(key in config and config[key] is not None for key in required_keys):
        print("Incomplete configuration. Missing one of the required keys or value is None.")
        return None

    
    
    if api =='1':
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
        if what =='11' or what =='12':
                    wireguard_urll = (
        f"wireguard://{urlencode(config['PrivateKey'])}@{endpoint}"
        f"?wnoise=quic&address=172.16.0.2/32,{urlencode(config['Address'])}&keepalive=5&wpayloadsize=1-8&"
        f"publickey={urlencode(config['PublicKey'])}&wnoisedelay=1-3&wnoisecount=15&mtu=1330"
    )
   #wireguard://qO6m%2BpxSH677ETSmqykciE7MQ7rp0Jw8qJHSUh7Gj3k%3D@162.159.195.166:878?wnoise=quic&address=172.16.0.2%2F32%2C2606%3A4700%3A110%3A846c%3Ae510%3Abfa1%3Aea9f%3A5247%2F128&reserved=111%2C162%2C171&keepalive=5&wpayloadsize=1-8&publickey=bmXOC%2BF1FxEMF9dyiK2H5%2F1SUtzH0JuVo51h2wPfgyo%3D&wnoisedelay=1-3&wnoisecount=15&mtu=1280#Tel%3D+%40arshiacomplus+wire
        if config.get('Reserved'):
   
                wireguard_urll += f"&reserved={config['Reserved']}"
            
    
    wireguard_urll += "#Tel= @arshiacomplus wire"

    return wireguard_urll
def start_menu():
    check_ipv=check_ipv6()
    rprint(f'ipv4 : [bold red]{check_ipv[0]}[/bold red]\nipv6 : [bold red]{check_ipv[1]}[/bold red]\n')
    
    options = {
        "1": "scan ip",
        "2": "wireguard for Hiddify",
        "3": "wireguard for Hiddify without ip scanning",
        "4": "wireguard for Hiddify with a sub link",
        "5": "wireguard for v2ray and mahsaNG",
        "6": "wireguard for v2ray and mahsaNG without ip scanning",
        "7": "WoW for v2ray or mahsaNG",
        "8": "WoW for v2ray or mahsaNG in sub link",
        "9": "Add/Delete shortcut",
        "10":"get wireguard.conf",
        "11":"wireguard for nikaNg ",
        "12":"wireguard for nikaNg without ip scanning",
        "13":"WoW with noise for Nikang or MahsaNg ",
        "14":"WoW with noise for Nikang or MahsaNg in sub link",
        "15": "wireguard for Sing-box and Hhidify | old | ",
        "16": "wireguard for Sing-box and Hiddify| old | without ip scanning",
        "17": "wireguard for Sing-box and Hiddify | old | with a sub link",
        "00" : "info",
        "0": "Exit"
    }

    rprint("[bold red]by Telegram= @arshiacomplus[/bold red]")
    for key, value in options.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    what = Prompt.ask("Choose an option", choices=list(options.keys()), default="0")
    return what
def get_number_of_configs():
    while True:
        try:
            how_many = int(Prompt.ask('\nHow many configs do you need (2 to 4): '))
            if how_many >= 2 and how_many <= 4:
                break
        except ValueError:
            console.print("[bold red]Please enter a valid number![/bold red]", style="red")
    return how_many
def gojo_goodbye_animation():
    frames  = [
        "\n\033[94m(＾-＾)ノ\033[0m",  # آبی
        "\n\033[93m(＾-＾)ノ~~~\033[0m",  # زرد
        "\n\033[92m(＾-＾)ノ~~~~~~\033[0m" , # سبزl
    ]
    
    for frame in frames:
      #  os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(1)
if __name__ == "__main__":
    os.system('clear')
    
    
    what=start_menu()


    if what =='1':
        
        do_you_save=input_p('Do you want to save in a result csv\n', {"1" : 'Yes' , "2" : "No"})
        which = 'n'
        if do_you_save=='1':
            os.system('termux-setup-storage')
            which = input_p('Do you want for bpb panel(with comma) or vahid panel(with enter) in a result csv\n ', {'1' : 'bpb panel(with comma)',
             '2' : 'vahid panel(with enter)', '3':'with score', '4':'clean'})
            if which =="1" or which=="2":
                need_port = input_p('Do you want to save port in result\n ', {'1' : 'Yes',
             '2' : 'No'})
            if which =='4':
                which = input_p('Do you want for bpb panel(with comma) or vahid panel(with enter) in a result csv\n ', {'1' : 'bpb panel(with comma)',
             '2' : 'vahid panel(with enter)'})
                with open('/storage/emulated/0/result.csv', 'r') as f:
                    b=f.readlines()
                    with open('/storage/emulated/0/clean_result.csv', 'w') as ff:
                        for j in b:
                                 if which =='1':
                                     ff.write(j[:j.index('|')-1])
                                     if j != b[len(b)-1]:
                                          ff.write(',')
                                 else:
                                     ff.write(j[:j.index('|')-1])
                                     ff.write('\n')
                                    
                print(' saved in /storage/emulated/0/clean_result.csv !')
                exit()
                            
            
       
            
        main()
    elif what=='2' or what=="3" or what =='7' or what =='13'  or what=='15' or what=="16":
    
        if what == '7' or what=='13':
            
            polrn_block= input_p('Do you want to block p@rn sites\n' , {"1": "Yes", "2": "No"})
            
            isIran =input_p('Iran or Germany\n' , {"1" : "Ip Iran[faster speed]", "2" : "Germany[slower speed]"})
            
            
        main2()
    elif what=='4' or what=='17':
        how_many=get_number_of_configs()  

        for i in range(how_many):
            main3()
    elif what =='5' or what =='6' or what=='11' or what=='12':
        
            
        api_url = 'https://api.zeroteam.top/warp?format=sing-box'
        if what=='5' or what =='11':
            endpoint_ip_best_result=main()
            endpoint_ip = str(endpoint_ip_best_result[0])+":"+str(endpoint_ip_best_result[1])
        else:
            endpoint_ip=input('Enter ip with port (defualt = n):')
            if endpoint_ip=='N' or  endpoint_ip=='n':
                endpoint_ip="162.159.195.166:878"
            else:
                temp_ip2=''
                temp_port2=''
                temp_c2=0
                while endpoint_ip[temp_c2] !=':':
                        temp_ip2=temp_ip2+endpoint_ip[temp_c2]
                        temp_c2=temp_c2+1
                            
                        
                set_enter_ip2=endpoint_ip.index(":")
                temp_port2=endpoint_ip[set_enter_ip2+1: ]
                    

                    
                    
                    #temp_port=temp_port+enter_ip[i]
                endpoint_ip=str(temp_ip2 +":" +str(temp_port2))
                
                
        rprint("[bold green]Please wait, generating WireGuard URL...[/bold green]")
        try:
            config = fetch_config_from_api()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        wireguard_url = generate_wireguard_url(config, endpoint_ip)
        if wireguard_url:
            os.system('clear')
            print(f"""


{wireguard_url}




""")
        else:
            print("Failed to generate WireGuard URL.")
    elif what == '8' or  what=='14':
        how_many=get_number_of_configs()
        polrn_block= input_p('Do you want to block p@rn sites\n' , {"1": "Yes", "2": "No"})

        
        main2()
    
    elif what == '9':

        if os.path.exists('/data/data/com.termux/files/usr/etc/bash.bashrc.bak'):
            
            Delete=input_p('Do you want to Delete short cut',{"1" : "Yes", "2" : "No"})
            if Delete=='1':
                os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
                os.rename('/data/data/com.termux/files/usr/etc/bash.bashrc.bak', '/data/data/com.termux/files/usr/etc/bash.bashrc')
                console.print("[bold red]Shortcut Deleted,  successful[/bold red]", style="red")
    
    
            exit()
        while True:
            name = input("\nEnter a shortcut name : ")
            if not name.isdigit():
                break
                
            
            else:
                console.print("\n[bold red]Please enter a name![/bold red]", style="red")
                
        with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r') as f2:
            txt= f2.read()
            with open('/data/data/com.termux/files/usr/etc/bash.bashrc.bak', 'w') as f:
                f.write(txt)
        text=f'''
{name}() {{
bash <(curl -fsSL https://raw.githubusercontent.com/arshiacomplus/WarpScanner/main/install.sh)
}}\n'''
        with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r+') as f:
               content = f.read()
               f.seek(0, 0)
               f.write(text.rstrip('\r\n') + '\n' + content)
        rprint(f"\n[bold green]Please Restart your  termux and Enter [bold red]{name}[/bold red] to run script[/bold green]")

    elif what =='10':
        endpoint_ip_best_result=main()
        endpoint_ip = str(endpoint_ip_best_result[0])+":"+str(endpoint_ip_best_result[1])
        try:
            all_key=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        name_conf=input('\nEnter a name: (defult [Enter]) : ')
        
        os.system('termux-setup-storage')
        
            
        
        if name_conf=='' :
            
            name_conf='acpwire.conf'
        path = '/storage/emulated/0/'+name_conf+".conf"
        with open(path, 'w') as f:
            f.write(f'''[Interface]
PrivateKey = {all_key[1]}
Address = 172.16.0.2/32, {all_key[0]}
DNS = 1.1.1.1, 1.0.0.1, 2606:4700:4700::1111, 2606:4700:4700::1001
MTU = 1280

[Peer]
PublicKey = {all_key[3]}
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = {endpoint_ip}''')
        rprint(f'\n[bold green]{name_conf} saved in {path}.conf[/bold green]')
    
    elif what == '00':
        info()
        
    elif what=='0':
        gojo_goodbye_animation()
        time.sleep(1)
        console.print("""
[bold magenta]Exiting... Goodbye![/bold magenta]""")
        
        
        exit()
