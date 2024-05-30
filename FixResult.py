

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
    os.system('cd requests-2.32.2')
    os.system('python setup.py install')
    import requests
import re
import socket
from concurrent.futures import ThreadPoolExecutor
import time
wire_config_temp=''
wire_c=1
wire_p=0
send_msg_wait=0
results = []
best_result=[]
#this function didn't use

def free_cloudflare_account():
        response = requests.get("https://api.zeroteam.top/warp?format=sing-box")
        output = response.text

       
        public_key_pattern = r'"2606:4700:[0-9a-f:]+/128"'
        private_key_pattern = r'"private_key":"[0-9a-zA-Z/+]+="'
        reserved_pattern = r'"reserved":[[0-9]+(,[0-9]+){2}]'

        public_key_search = re.search(public_key_pattern, output)
        private_key_search = re.search(private_key_pattern, output)
        reserved_search = re.search(reserved_pattern, output)

      
        public_key = public_key_search.group(0).replace('"', '') if public_key_search else None
        private_key = private_key_search.group(0).split(':')[1].replace('"', '') if private_key_search else None
        reserved = reserved_search.group(0).replace('"reserved":', '').replace('"', '') if reserved_search else None

        all_key=[public_key , private_key , reserved]
        return all_key
def upload_to_bashupload(config_data):
     
        files = {'file': ('output.json', config_data)}

    
        response = requests.post('https://bashupload.com/', files=files)

        if response.ok:
            
            download_link = response.text.strip()
            #[58:len(download_link)-27]
            
            download_link_with_query = download_link[59:len(download_link)-27] + "?download=1"
            print('your link : ', download_link_with_query)
        else:
            print("Something happend with create the link")
def check_ip():
    
    response = requests.get('http://ip-api.com/json/')
    if response.status_code == 200:
        ip_info = response.json()
        country = ip_info.get('countryCode')
        if country != 'IR':
            print('Discconect your VPN and try again .')
            exit()
        else:
            exit()
    print('Something has happend Try again')
    exit()
           
    
def scan_ip_port(ip, port):
   
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            start_time = time.time()
            result = s.connect_ex((ip, port))
            end_time = time.time()

            if result == 0:
                elapsed_time = (end_time - start_time) * 1000
                results.append((ip, port, elapsed_time))
           
            else:
                    print(f"IP: {ip} Port: {port} is not responding or closed.")
   
                    
            
                
    except Exception as e:
        print(f"Error scanning {ip}:{port} - {e}")

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

def main():
    print('\033[94m')
    os.system("clear")
    print("""please wait (scaning ip)      ...........
""")
    start_ip = ["188.114.96.0", "162.159.192.0","162.159.195.0"]
    end_ip = ["188.114.98.224", "162.159.193.224","162.159.195.224"]
    ports = [1074 , 894, 908 , 878]
    
    ip_range = create_ip_range(start_ip[0], end_ip[0])
    
    ip_range2 = create_ip_range(start_ip[1], end_ip[1])

    ip_range3 = create_ip_range(start_ip[2], end_ip[2])
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in ip_range:
            for port in ports:
                executor.submit(scan_ip_port, ip, port)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in ip_range2:
            for port in ports:
                executor.submit(scan_ip_port, ip, port)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in ip_range3:
            for port in ports:
                executor.submit(scan_ip_port, ip, port)
    executor.shutdown(wait=True)

    sorted_results = sorted(results, key=lambda x: x[2])
    
    os.system('clear')
    for result in sorted_results[:10]:
        print(f"IP: {result[0]}:{result[1]}, Ping: {result[2]:.2f} ms")

    
    if sorted_results:
        best_result = sorted_results[0]
        print("\033[91m")
        print(f"""
        Best ping: IP:  {best_result[0]}:{best_result[1]}
        Ping: {best_result[2]:.2f} ms""")
    if len(best_result)==0:
        print()
        os.system('clear')
        print("\033[91m")				
        print('Try again and choose wire guard without ip')
        print('\033[0m')
        exit()
    return best_result

def main2():
    global best_result
    def main2_1():
        global best_result
        all_key=free_cloudflare_account()
        public_key=all_key[0]
        private_key=all_key[1]
        reserved=all_key[2]
        
        all_key2=free_cloudflare_account()
        public_key2=all_key2[0]
        private_key2=all_key2[1]
        reserved2=all_key2[2]
        
        temp_ip=''
        temp_port=''
        temp_c=0
        if what =='3':
            print("\033[0m")
            enter_ip=input('Enter ip with port(defulte =Enter( N )) : ')
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

        
        print('\033[0m')
        os.system('clear')
        print(f'''
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
                        "{public_key}"
                ],
                "private_key": "{private_key}",
                "server": "{best_result[0]}",
                "server_port": {best_result[1]},
                "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
                "reserved": {reserved},
                "mtu": 1280,
                "fake_packets": "5-10"
                }},
                {{
                "type": "wireguard",
                "tag": "IP->Main, Telegram: @arshiacomplus",
                "detour": "IP->Iran, Telegram: @arshiacomplus",
                "local_address": [
                        "172.16.0.2/32",
                        "{public_key2}"
                ],
                "private_key": "{private_key2}",
                "server": "{best_result[0]}",
                "server_port": {best_result[1]},
                "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
                "reserved": {reserved2},
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
''')	
        if what=="3":
            exit()
                

    
    print('\033[94m')
    if what=="3":
        main2_1()


    best_result=main()
    print(f"please wait make wireguard. ")
    
    main2_1()

    
def main3():
    global best_result
    global wire_config_temp
    global wire_c
    global wire_p
    if wire_p==0:

        best_result=main()
    print('\033[91m')
    print(f"please wait make wireguard : {wire_c}. ")

    all_key=free_cloudflare_account()
    public_key=all_key[0]
    private_key=all_key[1]
    reserved=all_key[2]
    
    all_key2=free_cloudflare_account()
    public_key2=all_key2[0]
    private_key2=all_key2[1]
    reserved2=all_key2[2]
    print('\033[0m')

    os.system('clear')

    if wire_p!=1:				
        wire_config_or = f'''

    {{
    "type": "wireguard",
    "tag": "Tel=@arshiacomplus Warp-IR{wire_c}",
    "server": "{best_result[0]}",
    "server_port": {best_result[1]},

    "local_address": [
        "172.16.0.2/32",
        "{public_key}"
    ],
    "private_key": "{private_key}",
    "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
    "reserved": {reserved},

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
        "{public_key2}"
    ],
    "private_key": "{private_key2}",
    "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
    "reserved": {reserved2},

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
        "{public_key}"
    ],
    "private_key": "{private_key}",
    "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
    "reserved": {reserved},

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
        "{public_key2}"
    ],
    "private_key": "{private_key2}",
    "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
    "reserved": {reserved2},

    "mtu": 1120

    }}

'''

    if i == int(how_many)-1:
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
    
if __name__ == "__main__":
    os.system('clear')
    print("\033[91m")
    print("by Telegram= @arshiacomplus")
    print("\033[0m")
    what=input("""
 scan ip (enter 1)
 wireguard config(enter 2)
 wireguard config without ip scanning(enter 3)
 wireguard with a sub link[BETA](enter 4)
 Exit(enter 0)

>:""")
    while what!='0' and what !='1' and what !='2' and what !='3' and what!='4' and what !='5':
        what=input("""
 scan ip (enter 1)
 wireguard config(enter 2)
 wireguard config without ip scanning(enter 3)
 wireguard with a sub link[BETA](enter 4)
 Exit(enter 0)

>:""")
    if what =='1':
        main()
    elif what=='2':
        main2()
    elif what=="3":
        main2()
    elif what=='4':
        true=True
        while true==True:
            try:
                how_many=int(input('How many configs do you need(2 or above 2  ) : '))
                true=False
            except ValueError:

                true=True
    

        for i in range(how_many):
            main3()
    elif what=='0':
        exit()
