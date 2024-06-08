
import urllib.parse
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
from concurrent.futures import ThreadPoolExecutor
import time
try:
	import rich
except Exception:
	os.system('pip install rich')
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich.table import Table

console = Console()
wire_config_temp=''
wire_c=1
wire_p=0
send_msg_wait=0
results = []
save_result=[]
best_result=[]

def urlencode(string):
    
    if string is None:
        return None
    return urllib.parse.quote(string, safe='a-zA-Z0-9.~_-')

def fetch_config_from_api(api_url):
    response = requests.get(api_url)
    data = response.json()
    return {
        'PrivateKey': data.get('private_key'),
        'PublicKey': data.get('peer_public_key'),
        'Reserved': ','.join([str(x) for x in data.get('reserved', [])]) if data.get('reserved') else None
    }


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
    try:
        files = {'file': ('output.json', config_data)}
        response = requests.post('https://bashupload.com/', files=files)

        if response.ok:
            download_link = response.text.strip()
            download_link_with_query = download_link[59:len(download_link)-27] + "?download=1"
            console.print(f'[green]Your link: {download_link_with_query}[/green]')
        else:
            console.print("[red]Something happened with creating the link[/red]", style="bold red")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]", style="bold red")
  
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

def scan_ip_port(ip, port, results, packet_loss):
    global best_result
    global save_result
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            start_time = time.time()
            result = s.connect_ex((ip, port))
            end_time = time.time()

            if result == 0:
                elapsed_time = (end_time - start_time) * 1000
                results.append((ip, port, elapsed_time))
                if do_you_save =='y':
                    try:
                	    save_result.index(str(ip)+',')
                    except Exception:
                        save_result.append(str(ip)+',')
                
                if elapsed_time > 1000: 
                    packet_loss[ip] = packet_loss.get(ip, 0) + 1
            else:
                console.print(f"IP: {ip} Port: {port} is not responding or closed.", style="red")
                packet_loss[ip] = packet_loss.get(ip, 0) + 1
    except Exception as e:
        console.print(f"Error scanning {ip}:{port} - {e}", style="red")
        packet_loss[ip] = packet_loss.get(ip, 0) + 1

def main():
    
    console.clear()
    console.print("Please wait, scanning IP ...", style="blue")

    start_ips = ["188.114.96.0", "162.159.192.0", "162.159.195.0"]
    end_ips = ["188.114.99.224", "162.159.193.224", "162.159.195.224"]
    ports = [1074, 894, 908, 878]
    results = []
    packet_loss = {}

    for start_ip, end_ip in zip(start_ips, end_ips):
        ip_range = create_ip_range(start_ip, end_ip)
        with ThreadPoolExecutor(max_workers=500) as executor:
            for ip in ip_range:
                for port in ports:
                    executor.submit(scan_ip_port, ip, port, results, packet_loss)

    for ip in packet_loss:
        packet_loss[ip] = (packet_loss[ip] / len(ports)) * 100

    extended_results = []
    for result in results:
        ip, port, ping = result
        loss_rate = packet_loss.get(ip, 0)
        combined_score = ping + (loss_rate * 10)
        extended_results.append((ip, port, ping, loss_rate, combined_score))
    
    # Add IPs with high packet loss but no successful connections
    for ip in packet_loss:
        if ip not in [res[0] for res in extended_results]:
            loss_rate = packet_loss[ip]
            extended_results.append((ip, None, None, loss_rate, loss_rate * 10))

    sorted_results = sorted(extended_results, key=lambda x: x[4])

    # Ensure to print at least a few IPs
    while len(sorted_results) < 10:
        sorted_results.append(("No IP", None, None, 100, 1000))

    console.clear()
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("IP", style="dim", width=15)
    table.add_column("Port", justify="right")
    table.add_column("Ping (ms)", justify="right")
    table.add_column("Packet Loss (%)", justify="right")
    table.add_column("Score", justify="right")

    for ip, port, ping, loss_rate, combined_score in sorted_results[:10]:
        table.add_row(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%", f"{combined_score:.2f}")

    console.print(table)

    best_result = sorted_results[0] if sorted_results else None
    if best_result and best_result[0] != "No IP":
        ip, port, ping, loss_rate, combined_score = best_result
        try:
        	console.print(f"The best IP: {ip}:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}%, score: {combined_score:.2f}", style="green")
        except TypeError:
        	console.print(f"The best IP: {ip}:{port if port else '878'} , ping: None, packet loss: {loss_rate:.2f}%, score: {combined_score:.2f}", style="green")
        best_result=2*[1]
        best_result[0]=f"{ip}"
        best_result[1]=878
    else:
        console.print("Nothing was found", style="red")
    if what == '1':
        if do_you_save=='y':
    	    with open('result.txt' , "w") as f:
    	         for j in save_result:
    	         	f.write(j)
    	    print('saved in result.txt! ')

    return best_result


def main2():
    global best_result
    def main2_1():
        global best_result
        try:
            all_key=free_cloudflare_account()
        except Exception as E:
        	print(' Try again Error =', E)
        	exit()
        public_key=all_key[0]
        private_key=all_key[1]
        reserved=all_key[2]
        try:
            all_key2=free_cloudflare_account()
        except Exception as E:
        	print(' Try again Error =', E)
        	exit()
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
                

    
    print('\033[91m')
    if what=="3":
        main2_1()

    try:
    	best_result=main()
    except Exception:
    	print("\033[91m")
    	print('Try again and choose wire guard without ip')
    	print('\033[0m')
    	exit()
    print(f"please wait make wireguard. ")
    
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
    print(f"please wait make wireguard : {wire_c}. ")
    try:
        all_key=free_cloudflare_account()
    except Exception as E:
    		print(' Try again Error =', E)
    		exit()
    public_key=all_key[0]
    private_key=all_key[1]
    reserved=all_key[2]
    try:
        all_key2=free_cloudflare_account()
    except Exception as E:
    		print(' Try again Error =', E)
    		exit()
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
def generate_wireguard_url(config, endpoint):
    
    required_keys = ['PrivateKey', 'PublicKey']
    if not all(key in config and config[key] is not None for key in required_keys):
        print("Incomplete configuration. Missing one of the required keys or value is None.")
        return None

    
    wireguard_url = (
        f"wireguard://{urlencode(config['PrivateKey'])}@{endpoint}"
        f"?publickey={urlencode(config['PublicKey'])}"
    )
    
    
    if config.get('Reserved'):
        wireguard_url += f"&reserved={urlencode(config['Reserved'])}"
    
    wireguard_url += "#Tel= @arshiacomplus wire"

    return wireguard_url
def start_menu():
    options = {
        "1": "scan ip",
        "2": "wireguard config",
        "3": "wireguard config without ip scanning",
        "4": "wireguard with a sub link[BETA]",
        "5": "wireguard for v2ray and mahsaNG",
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
            how_many = int(Prompt.ask('How many configs do you need (2 or above)'))
            if how_many >= 2:
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
        
        do_you_save=input('\nDo you want to save in a result txt? (y/n)')
        while do_you_save!= 'y' and do_you_save!= 'n':
        	console.print("[bold red]Please enter (y/n)![/bold red]", style="red")
        	
        	do_you_save=input('\nDo you want to save in a result txt? (y/n)')
        	
        main()
    elif what=='2':
        main2()
    elif what=="3":
        main2()
    elif what=='4':
        how_many=get_number_of_configs()  

        for i in range(how_many):
            main3()
    elif what =='5':
    	api_url = 'https://api.zeroteam.top/warp?format=sing-box'
    	endpoint_ip_best_result=main()
    	endpoint_ip = str(endpoint_ip_best_result[0])+":"+str(endpoint_ip_best_result[1])
    	rprint("[bold green]Please wait, generating WireGuard URL...[/bold green]")
    	try:
    		config = fetch_config_from_api(api_url)
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
    elif what=='0':
        gojo_goodbye_animation()
        time.sleep(1)
        console.print("""
[bold magenta]Exiting... Goodbye![/bold magenta]""")
        
        
        exit()
