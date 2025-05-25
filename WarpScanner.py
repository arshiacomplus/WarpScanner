V=73
import urllib.request
import urllib.parse
from urllib.parse import quote
import os
try:
    import requests
except Exception:
    print("Requests module not installed. Installing now...")
    os.system('pip install requests')
try:
    import requests
except Exception:
    os.system('wget https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
try:
    import requests
except Exception:
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
from numbers import Number
import threading
from requests import RequestException
from typing import List, Dict, Any, Optional
from dataclasses import dataclass,field
from json import JSONEncoder
try:
    import yaml
except Exception:
    os.system("pip install pyyaml")
try:
    import psutil
except Exception:
    os.system("pip install psutil")
try:
    import signal
except Exception:
    os.system("pip install signal")
CONF_PATH="config.json"
DEFAULT_CONFIG={
    "core": {
      "test_url": "http://www.gstatic.com/generate_204",
      "log_level": "warning",
      "domain_strategy": "IPIFNonMatch",
      "allow_insecure_tls": False,
      "sniffing_enabled": True,
      "inbound_ports": {
        "socks": 10808,
        "http": 10809
      },
      "dns": {
        "enabled": True,
        "fake_dns_enabled": True,
        "local_port": 10853,
        "remote_server": "https://8.8.8.8/dns-query",
        "domestic_server": "1.1.1.2"
      },
      "routing_rules": {
        "proxy": "",
        "direct": "",
        "block": ""
      },
      "fragment": {
        "enabled": False,
        "packets": "tlshello",
        "length": "10-30",
        "interval": "1-5"
      },
      "fake_host": {
        "enabled": False,
        "domain": "cloudflare.com"
      },
      "mux": {
        "enabled": False,
        "concurrency": 8
      }
    },
    "warp_on_warp": {
      "enabled": False,
      "config_url": ""
    }
  }
if not  os.path.exists(CONF_PATH):

    with open(CONF_PATH, "w") as f:
        json.dump(DEFAULT_CONFIG, f, indent=2)
with open(CONF_PATH,"r") as file_client_set:
        app_conf=json.load(file_client_set)
        test_link_=app_conf["core"]["test_url"]
class ProcessManager:
    """
    Manages background processes (like Xray, Hysteria) started by the script.
    Ensures proper termination on Linux systems using SIGTERM and SIGKILL.
    """
    def __init__(self):
        self.active_processes = {}
        self.lock = threading.Lock()
        print("ProcessManager initialized.")
    def add_process(self, name: str, pid: int):
        """یک پردازش جدید را به لیست مدیریت‌شده اضافه می‌کند."""
        with self.lock:
            if name in self.active_processes:
                print(f"Warning: Process name '{name}' already exists with PID {self.active_processes[name]}. Overwriting with new PID {pid}.")
            print(f"Tracking process '{name}' with PID {pid}.")
            self.active_processes[name] = pid
    def stop_process(self, name: str):
        """یک پردازش مشخص را با نام آن متوقف می‌کند."""
        pid_to_stop = None
        with self.lock:
            if name in self.active_processes:
                pid_to_stop = self.active_processes.pop(name)
                print(f"Attempting to stop process '{name}' with PID {pid_to_stop}. Removed from tracking list.")
            else:
                print(f"Process '{name}' not found in active processes list for stopping.")
                return
        if pid_to_stop is None:
             print(f"Error: Could not retrieve PID for '{name}' despite being found initially.")
             return
        try:
            if psutil.pid_exists(pid_to_stop):
                print(f"  Sending SIGTERM (polite request) to PID {pid_to_stop}...")
                os.kill(pid_to_stop, signal.SIGTERM)
                time.sleep(1)
                if psutil.pid_exists(pid_to_stop):
                    print(f"  PID {pid_to_stop} still exists after SIGTERM. Sending SIGKILL (force kill)...")
                    os.kill(pid_to_stop, signal.SIGKILL)
                    time.sleep(0.1)
                    if psutil.pid_exists(pid_to_stop):
                        print(f"  WARNING: PID {pid_to_stop} could not be terminated even with SIGKILL!")
                    else:
                        print(f"  PID {pid_to_stop} terminated successfully by SIGKILL.")
                else:
                    print(f"  PID {pid_to_stop} terminated gracefully by SIGTERM.")
            else:
                print(f"  Process with PID {pid_to_stop} was already gone before stop attempt.")
        except (ProcessLookupError, psutil.NoSuchProcess):
            print(f"  Process with PID {pid_to_stop} disappeared during termination attempt.")
        except PermissionError:
            print(f"  ERROR: Permission denied to send signal to PID {pid_to_stop}.")
        except Exception as e:
            print(f"  ERROR: An unexpected error occurred while stopping PID {pid_to_stop}: {e}")
    def stop_all(self):
        """تمام پردازش‌های مدیریت‌شده را متوقف می‌کند."""
        print("Stopping all tracked processes...")
        names_to_stop = []
        with self.lock:
             names_to_stop = list(self.active_processes.keys())
        if not names_to_stop:
            print("No active processes were being tracked.")
            return
        print(f"Found {len(names_to_stop)} processes to stop: {names_to_stop}")
        for name in names_to_stop:
             self.stop_process(name)
        print("Finished stopping all tracked processes.")
process_manager = ProcessManager()
xray_abs="xray/xray"
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
which_v=""
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
        which_api=input_p('Which Api \n', {'1':'First api', '2' :'Second api(need vpn just for install lib)'})
        api=which_api
    else:
        which_api=api
    if which_api == '2':
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
            exit()
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
                response = urllib.request.urlopen("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30)
                return response.text
    b = file_o()
    b=b.split("\n")
    Address_key=b[0][b[0].index(":")+2:]
    private_key=b[1][b[1].index(":")+2:]
    reserved=b[2][b[2].index(":")+2:].split(" ")
    reserved.pop(3)
    reserved = [int(item) for item in reserved]
    pub_key=b[3][b[3].index(":")+2:]
    return {
        'PrivateKey': private_key,
        'PublicKey': pub_key,
        'Reserved':reserved,
        'Address': Address_key
    }
def free_cloudflare_account():
    global api
    if api=='':
        which_api=input_p('Which Api \n', {'1':'First api', '2' :'Second api(need vpn just for install lib)'})
        api=which_api
    else:
        which_api=api
    if which_api == '2':
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
            exit()
        keys=bind_keys()
        keys=list(keys)
        return keys
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
            try:
                response = urllib.request.urlopen("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30).read().decode('utf-8')
                return response
            except Exception:
                response = requests.get("http://s9.serv00.com:1074/arshiacomplus/api/wirekey", timeout=30)
                return response.text
    try:
            b = file_o()
    except ConnectionError:
            console.print("[bold red]Failed to connect to API after 6 attempts.[/bold red]")
    b=b.split("\n")
    Address_key=b[0][b[0].index(":")+2:]
    private_key=b[1][b[1].index(":")+2:]
    reserved=b[2][b[2].index(":")+2:].split(" ")
    reserved.pop(3)
    reserved = [int(item) for item in reserved]
    pub_key=b[3][b[3].index(":")+2:]
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
def scan_ip_port(ip, results :list):
    port=ports[random.randint(0,3)]
    icmp=pinging(ip, count=4, interval=1, timeout=5,privileged=False)
    if icmp.is_alive:
        results.append((ip, port, float(icmp.avg_rtt), icmp.packet_loss, icmp.jitter))
def parse_configs(conifg,num=0,cv=1,hy2_path="hy2/config.yaml",is_hy2=False): # nuitka: pragma: no cover
    @dataclass
    class ConfigParams:
        protocol: str
        address: str
        port: int
        security: Optional[str] = ""
        encryption: Optional[str] = "none"
        header_type: Optional[str] = "none"
        network: Optional[str] = "tcp"
        flow: Optional[str] = ""
        sni: Optional[str] = ""
        fp: Optional[str] = ""
        alpn: Optional[str] = None
        pbk: Optional[str] = ""
        sid: Optional[str] = ""
        spx: Optional[str] = ""
        tag: Optional[str] = ""
        id: Optional[str] = ""
        type: Optional[str] = "tcp"
        alter_id: Optional[str] = ""
        mode: Optional[str] = None
        host: Optional[str] = None
        path: Optional[str] = None
        scy: Optional[str] = ""
        socks_user: Optional[str] = ""
        ss_method: Optional[str] = "chacha20-poly1305"
        ss_password: Optional[str] = ""
        hy2_insecure: Optional[str] = "0"
        hy2_obfs_password: Optional[str] = ""
        hy2_hop_interval: Optional[str] = "30"
        hy2_pinsha256: Optional[str] = ""
        hy2_obfs: Optional[str] = ""
        wg_reserved: Optional[str] = ""
        wg_public_key: Optional[str] = ""
        wg_endpoint: Optional[str] = ""
        wg_secret_key: Optional[str] = ""
        wg_keep_alive: Optional[int] = 10
        wg_mtu: Optional[int] = 0
        wg_address: Optional[str] = ""
        wnoise: Optional[str] = "quic"
        wnoisecount: Optional[str] = "15"
        wnoisedelay: Optional[str] = "1-3"
        wpayloadsize: Optional[str] = "1-8"
        extra_params: Dict[str, Any] = field(default_factory=dict)
    def parse_configs_by_get(config: str) -> ConfigParams:
        """Parse all possible parameters from config strings"""
        try:
            config = config.strip()
            config_parts = config.split('#', 1)
            main_config = config_parts[0]
            print(config_parts)
            tag = config_parts[1] if len(config_parts) > 1 else ""
            protocol = next((p for p in ["vless", "vmess", "trojan", "hy2", "hysteria2",
                                        "ss", "socks", "wireguard"] if main_config.startswith(p)), None)
            if not protocol:
                raise ValueError("Invalid protocol")
            common_params = {"protocol": protocol, "tag": tag}
            if protocol in ["vless", "trojan"]:
                match = re.search(r'([^:]+)@([^:]+):(\d+)', main_config)
                if match:
                    common_params.update({
                        "id": match.group(1).replace("//","") if protocol != "trojan" else "",
                        "address": match.group(2),
                        "port": int(match.group(3))
                    })
            elif protocol == "wireguard":
                match = re.search(r'([^@]+)@([^:]+):(\d+)', main_config)
                if match:
                    common_params.update({
                        "wg_secret_key": match.group(1).split('wireguard://')[1],
                        "address": match.group(2),
                        "port": int(match.group(3))
                    })
            else:
                match = re.search(r'@([^:]+):(\d+)', main_config)
                if match:
                    common_params.update({
                        "address": match.group(1),
                        "port": int(match.group(2))
                    })
            protocol_handlers = {
                "vless": parse_vless,
                "vmess": parse_vmess,
                "trojan": parse_trojan,
                "hy2": parse_hysteria,
                "hysteria2": parse_hysteria,
                "ss": parse_shadowsocks,
                "socks": parse_socks,
                "wireguard": parse_wireguard
            }
            parser = protocol_handlers.get(protocol)
            if not parser:
                raise NotImplementedError(f"Unsupported protocol: {protocol}")
            return parser(main_config, common_params)
        except Exception as e:
            print(f"Error parsing config: {e}")
            return ConfigParams(protocol="", address="", port=0)
    def parse_vless(config: str, common: dict) -> ConfigParams:
        query = re.split(r"\?", config, 1)[1] if "?" in config else ""
        params = parse_query_params(query)
        host_params = {
            "tcp": params.get("host",None),
            "ws": params.get("host",None),
            "h2": params.get("host",None),
            "httpupgrade": params.get("host",None),
            "xhttp": params.get("host",None),
            "splithttp": params.get("host",None),
            "quic": params.get("quicSecurity", None),
            "grpc": params.get("authority", None)
        }
        path_params = {
            "ws": params.get("path",None),
            "h2": params.get("path",None),
            "httpupgrade": params.get("path",None),
            "splithttp": params.get("path",None),
            "xhttp": params.get("path",None),
            "kcp": params.get("seed", None),
            "grpc": params.get("serviceName",None),
            "quic": params.get("key",None)
        }
        return ConfigParams(
            **common,
            security=params.get("security", ""),
            encryption=params.get("encryption", "none"),
            type=params.get("type", "tcp"),
            host=host_params.get(params.get("type", "tcp"), None),
            path=path_params.get(params.get("type", "tcp"), None),
            flow=params.get("flow", ""),
            sni=params.get("sni", ""),
            fp=params.get("fp", ""),
            alpn=params.get("alpn", None),
            pbk=params.get("pbk", ""),
            sid=params.get("sid", ""),
            spx=params.get("spx", ""),
            mode=params.get("mode", None)
        )
    def parse_vmess(config: str, common: dict) -> ConfigParams:
        encoded_part = config.split("://")[1]
        missing_padding = len(encoded_part) % 4
        if missing_padding:
            encoded_part += '=' * (4 - missing_padding)
        decoded = base64.b64decode(encoded_part).decode("utf-8")
        vmess_data = json.loads(decoded)
        address = vmess_data.get("add", "")
        port = int(vmess_data.get("port", 0))
        tag = vmess_data.get("ps", "none")
        sec=vmess_data.get("tls", "")
        return ConfigParams(
            protocol=common.get("protocol",""),
            address=address,
            port=port,
            tag=tag,
            security=sec,
            id=vmess_data.get("id", ""),
            alter_id=int(vmess_data.get("aid", 0)),
            scy=vmess_data.get("scy", ""),
            sni=vmess_data.get("sni", ""),
            fp=vmess_data.get("fp", ""),
            type=vmess_data.get("net","tcp"),
            host=vmess_data.get("host", None),
            path=vmess_data.get("path", None),
            alpn=vmess_data.get("alpn", None),
            mode=vmess_data.get("mode", None)
        )
    def parse_trojan(config: str, common: dict) -> ConfigParams:
        query = re.split(r"\?", config, 1)[1] if "?" in config else ""
        params = parse_query_params(query)
        password = re.search(r'trojan://([^@]+)@', config).group(1) if "trojan://" in config else ""
        host_params = {
            "tcp": params.get("host",None),
            "ws": params.get("host",None),
            "h2": params.get("host",None),
            "httpupgrade": params.get("host",None),
            "xhttp": params.get("host",None),
            "splithttp": params.get("host",None),
            "quic": params.get("quicSecurity", None),
            "grpc": params.get("authority", None)
        }
        path_params = {
            "ws": params.get("path",None),
            "h2": params.get("path",None),
            "httpupgrade": params.get("path",None),
            "splithttp": params.get("path",None),
            "xhttp": params.get("path",None),
            "kcp": params.get("seed", None),
            "grpc": params.get("serviceName",None),
            "quic": params.get("key",None)
        }
        return ConfigParams(
            **common,
            security="tls",
            ss_password=password,
            sni=params.get("sni", ""),
            fp=params.get("fp", ""),
            alpn=params.get("alpn", None),
            pbk=params.get("pbk", ""),
            sid=params.get("sid", ""),
            type=params.get("type", "tcp"),
            host=host_params.get(params.get("type", "tcp"), None),
            path=path_params.get(params.get("type", "tcp"), None),
            spx=params.get("spx", ""),
            mode=params.get("mode", None)
        )
    def parse_hysteria(config: str, common: dict) -> ConfigParams:
        query = re.split(r"\?", config, 1)[1] if "?" in config else ""
        params = parse_query_params(query)
        return ConfigParams(
            **common,
            security="tls",
            hy2_insecure=params.get("insecure", "0") == "1",
            hy2_obfs_password=params.get("obfs-password", ""),
            hy2_hop_interval=int(params.get("hopInterval", 30)),
            hy2_pinsha256=params.get("pinSHA256",""),
            hy2_obfs=params.get("obfs",""),
            sni=params.get("sni", ""),
            alpn=params.get("alpn", None)
        )
    def parse_socks(config: str, common: dict) -> ConfigParams:
        auth_part = config.split("://")[1].split("@")[0]
        user_pass = base64.b64decode(auth_part).decode("utf-8").split(":")
        return ConfigParams(
            **common,
            socks_user=user_pass[0],
            ss_password=user_pass[1],
            security="none"
        )
    def parse_wireguard(config: str, common: dict) -> ConfigParams:
        query = re.split(r"\?", config, 1)[1] if "?" in config else ""
        params = parse_query_params(query)
        return ConfigParams(
            **common,
            wg_reserved=params.get("reserved", ""),
            wg_public_key=params.get("publickey", ""),
            wg_endpoint=params.get("endpoint", ""),
            wg_keep_alive=int(params.get("keepalive", 5)),
            wg_mtu=int(params.get("mtu",0)),
            wg_address=params.get("address",""),
            wnoise=params.get("wnoise", "quic"),
            wnoisecount=params.get("wnoisecount", "15"),
            wnoisedelay=params.get("wnoisedelay", "1-3"),
            wpayloadsize=params.get("wpayloadsize", "1-8")
        )
    def parse_shadowsocks(config: str, common: dict) -> ConfigParams:
        auth_part = config.split("://")[1].split("@")[0]
        method_pass = base64.b64decode(auth_part).decode("utf-8").split(":")
        return ConfigParams(
            **common,
            ss_method=method_pass[0],
            ss_password=method_pass[1],
            security="none"
        )
    def parse_query_params(query: str) -> Dict[str, str]:
        params = {}
        for pair in query.split("&"):
            if "=" in pair:
                key, value = pair.split("=", 1)
                params[key] = urllib.parse.unquote(value)
        return params
    conifg=urllib.parse.unquote(conifg)
    dict_conf=parse_configs_by_get(conifg)
    print("the cv is"+ str(cv))
    LOCAL_HOST="127.0.0."+str(cv)
    DEFAULT_PORT = 443
    DEFAULT_SECURITY = "auto"
    DEFAULT_LEVEL = 8
    DEFAULT_NETWORK = "tcp"
    TLS = "tls"
    REALITY = "reality"
    HTTP = "http"
    try:
        with open(CONF_PATH,"r") as f:
            file=json.load(f)
        core=file['core']
        warp_sets = file['warp_on_warp']
        fragment_sets=core["fragment"]
        fake_host_sets =core["fake_host"]
        mux_sets= core["mux"]
        dns_sets = core["dns"]
        routing_sets = core["routing_rules"]
        inbound_ports = core["inbound_ports"]
        PACKETS=fragment_sets["packets"]
        LENGTH=fragment_sets["length"]
        INTERVAL=fragment_sets["interval"]
        FAKEHOST_ENABLE= fake_host_sets["enabled"]
        HOST1_DOMAIN=fake_host_sets["domain"]
        HOST2_DOMAIN=HOST1_DOMAIN
        MUX_ENABLE= mux_sets["enabled"]
        CONCURRENCY=mux_sets["concurrency"]
        FRAGMENT= fragment_sets["enabled"]
        IS_WARP_ON_WARP= warp_sets["enabled"]
        WARPONWARP=urllib.parse.unquote(warp_sets["config_url"])
        ENABLELOCALDNS = dns_sets["enabled"]
        ENABLEFAKEDNS = dns_sets["fake_dns_enabled"]
        LOCALDNSPORT = dns_sets["local_port"]
        ALLOWINCREASE = core["allow_insecure_tls"]
        DOMAINSTRATEGY = core["domain_strategy"]
        CUSTOMRULES_PROXY = routing_sets["proxy"].split(",")
        CUSTOMRULES_DIRECT = routing_sets["direct"].split(",")
        CUSTOMRULES_BLOCKED = routing_sets["block"].split(",")
        SOCKS5 = inbound_ports["socks"]
        HTTP5 = inbound_ports["http"]
        REMOTEDNS = dns_sets["remote_server"]
        DOMESTICDNS = dns_sets["domestic_server"]
        LOGLEVEL = core["log_level"]
        SNIFFING = core["sniffing_enabled"]
    except Exception as E:
        print(E)
    is_warp=False
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
                            xhttpSettings: Optional['V2rayConfig.OutboundBean.StreamSettingsBean.XhttpSettingsBean']= None,
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
                            useBrowserForwarding: Optional[bool] = None, acceptProxyProtocol: Optional[bool] = None,host: Optional[str] = None,):
                    self.path = path
                    self.headers = headers if headers is not None else V2rayConfig.OutboundBean.HeadersBean(Host_single="")
                    self.maxEarlyData = maxEarlyData
                    self.useBrowserForwarding = useBrowserForwarding
                    self.acceptProxyProtocol = acceptProxyProtocol
                    self.host = host
            class HttpupgradeSettingsBean:
                def __init__(self, path: str = "", host: str = "", acceptProxyProtocol: Optional[bool] = None):
                    self.path = path
                    self.host = host
                    self.acceptProxyProtocol = acceptProxyProtocol
            class XhttpSettingsBean:
                def __init__(self,path: Optional[str] = None,host: Optional[str] = None,mode: Optional[str] = None,extra: Optional[Any] = None):
                    self.path = path
                    self.host = host
                    self.mode = mode
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
                    kcpSettings = kcpsetting
                elif network == "ws":
                    wssetting = V2rayConfig.OutboundBean.WsSettingsBean()
                    wssetting.headers.Host_single = host or ""
                    sni = wssetting.headers.Host_single
                    wssetting.path = path or "/"
                    wsSettings = wssetting
                elif network == "httpupgrade":
                    httpupgradeSetting = V2rayConfig.OutboundBean.HttpupgradeSettingsBean()
                    httpupgradeSetting.host = host or ""
                    sni = httpupgradeSetting.host
                    httpupgradeSetting.path = path or "/"
                    httpupgradeSettings = httpupgradeSetting
                elif network == "xhttp":
                    xhttpSetting = V2rayConfig.OutboundBean.XhttpSettingsBean()
                    xhttpSetting.host = host or ""
                    sni = xhttpSetting.host
                    xhttpSetting.path = path if path else "/"
                    xhttpSettings = xhttpSetting
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
                    tlsSettings = tlsSetting
                    realitySettings = None
                elif security == REALITY:
                    tlsSettings = None
                    realitySettings = tlsSetting
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
        outbounds = []
        class EConfigType:
            entries = []
        def getProxyOutbound():
            for outbound in V2rayConfig.outbounds:
                for it in V2rayConfig.EConfigType.entries:
                    if outbound.protocol.lower() == it.name.lower():
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
    def remove_nulls(data):
        if isinstance(data, dict):
            return {k: remove_nulls(v) for k, v in data.items() if v is not None}
        elif isinstance(data, list):
            return [remove_nulls(item) for item in data if item is not None]
        elif hasattr(data, '__dict__'):
            obj_dict = data.__dict__
            cleaned_dict = {k: remove_nulls(v) for k, v in obj_dict.items() if v is not None}
            return cleaned_dict
        else:
            return data
    def replace_accept_encoding(d):
        if isinstance(d, dict):
            new_dict = {}
            for key, value in d.items():
                if key == 'acceptEncoding':
                    new_dict['Accept-Encoding'] = value
                elif key == 'passw':
                    new_dict['pass'] = value
                else:
                    new_dict[key] = replace_accept_encoding(value)
            return new_dict
        elif isinstance(d, list):
            return [replace_accept_encoding(item) for item in d]
        elif hasattr(d, '__dict__'):
                obj_dict = d.__dict__
                cleaned_dict = {itemk: replace_accept_encoding(itemk) for itemk,itemv in obj_dict.items()}
                return cleaned_dict
        else:
            return d
    ID,ADDRESS,PORT,SECURITY,ALPN,FP,SNI,SPX,HEADER_TYPE,ENCRYPTION,TYPE,MODE,FLOW,ALTERID,R_HOST,PATH,SCY,PASS,SID,METHOD,OBFS_PASSWORD,INSECURE,PORTHOPINGINTERVAL,PINSHA256,OBFS,USER,WNOISE,WNOISECOUNT,WNOISEDELAY,WPAYLOADSIZE,KEEPALIVE,MTU,ENDPOINT,RESERVED,PBK,SECERKEY,REMARKS,protocol_c=(dict_conf.id, dict_conf.address,dict_conf.port,dict_conf.security,dict_conf.alpn,dict_conf.fp,dict_conf.sni,dict_conf.spx,dict_conf.header_type,dict_conf.encryption,dict_conf.type,dict_conf.mode,dict_conf.flow,dict_conf.alter_id,dict_conf.host,dict_conf.path,dict_conf.scy,dict_conf.ss_password,dict_conf.sid,dict_conf.ss_method,dict_conf.hy2_obfs_password,dict_conf.hy2_insecure,dict_conf.hy2_hop_interval,dict_conf.hy2_pinsha256,dict_conf.hy2_obfs,dict_conf.socks_user,dict_conf.wnoise,dict_conf.wnoisecount,dict_conf.wnoisedelay,dict_conf.wpayloadsize,dict_conf.wg_keep_alive,dict_conf.wg_mtu,dict_conf.address,dict_conf.wg_reserved,dict_conf.pbk,dict_conf.wg_secret_key,dict_conf.tag,dict_conf.protocol)
    if SECURITY=="none":
            SECURITY=""
    if INSECURE=="0": INSECURE=False
    else: INSECURE=True
    if RESERVED!="":
        RESERVED = list(map(int, RESERVED.split(",")))
    if MODE=="gun" and TYPE=="grpc":
        MODE=False
    elif MODE=="multi" and TYPE=="grpc":
        MODE=True
    if protocol_c=="wireguard":
        ADDRESS=dict_conf.wg_address.split(",")
        PBK=dict_conf.wg_public_key
    if IS_WARP_ON_WARP:
        warp_conf=parse_configs_by_get(WARPONWARP)
        WNOISEON,WNOISECOUNTON,WNOISEDELAYON,WPAYLOADSIZEON,KEEPALIVEON,MTUON,SECERKEYON,ENDPOINTON,PORTON,ADDRESSON,RESERVEDON,PBKON=(warp_conf.wnoise,warp_conf.wnoisecount,warp_conf.wnoisedelay,warp_conf.wpayloadsize,warp_conf.wg_keep_alive,warp_conf.wg_mtu,warp_conf.wg_secret_key,warp_conf.address,warp_conf.port,warp_conf.wg_address.split(","),warp_conf.wg_reserved,warp_conf.wg_public_key)
        if RESERVEDON!="":
            RESERVEDON = list(map(int, RESERVEDON.split(",")))
    ##################################################################################################
    def parse_yaml_hy2():
        yaml_hy2={
            'server':ADDRESS+":"+str(PORT),
            'auth':PASS,
            'transport':{
                'type':'udp',
                'udp':{
                    'hopInterval':str(PORTHOPINGINTERVAL)+'s'
            },
            }
        }
        if SECURITY=="tls":
            tlsin={'tls':{
                'insecure':INSECURE
            }
            }
            if SNI!="":
                tlsin.update({'sni':SNI})
            if PINSHA256!="":
                tlsin.update({'pinSHA256':PINSHA256})
            yaml_hy2.update(tlsin)
        if OBFS=="salamander":
            obfsin={
                'obfs':{
                    'type':'salamander',
                    'salamander':{
                        'password':OBFS_PASSWORD
                    }
                }
            }
            yaml_hy2.update(obfsin)
        nest_yaml_hy2={
            'bandwidth':{
                'up':'20 mbps',
                'down':'100 mbps'
            },
            'quic':{
                'initStreamReceiveWindow': 8388608,
                'maxStreamReceiveWindow': 8388608,
                'initConnReceiveWindow': 20971520,
                'maxConnReceiveWindow': 20971520,
                'maxIdleTimeout': '30s',
                'keepAlivePeriod': '10s',
                'disablePathMTUDiscovery': False
            },
            'fastOpen':True,
            'lazy':True,
            'socks5':{
                'listen':LOCAL_HOST+':'+str(SOCKS5+2),
            },
            'http':{
                'listen':LOCAL_HOST+':'+str(HTTP5+2)
            }
        }
        yaml_hy2.update(nest_yaml_hy2)
        return yaml_hy2
    if conifg.startswith("hy2://") or conifg.startswith("hysteria2://"):
        with open(hy2_path,'w') as f:
            yaml.dump(parse_yaml_hy2(),f)
        return parse_configs(conifg=f"socks://Og==@{LOCAL_HOST}:{str(SOCKS5+2)}#hy2",cv=cv,is_hy2=True)
    try:
            ALPN=ALPN.split(",")
    except Exception:
            pass
    logBean = V2rayConfigLogBean("", "",LOGLEVEL)  # Make sure to adjust the imports for these
    inboundBean = V2rayConfig.InboundBean(tag="socks", port=SOCKS5, protocol="socks",listen=LOCAL_HOST, sniffing=V2rayConfig.InboundBean.SniffingBean(False, [],routeOnly=False),settings=V2rayConfig.InboundBean.InSettingsBean(auth="noauth",udp=True,allowTransparent=False))
    inboundBean2=V2rayConfig.InboundBean(tag="http", listen=LOCAL_HOST,port=HTTP5, protocol="http",settings=V2rayConfig.InboundBean.InSettingsBean(userLevel=8))
    sniff_list=[]
    sniff_enable=False
    if SNIFFING:
        sniff_list+=["http","tls"]
        sniff_enable=True
    if ENABLELOCALDNS:
        if ENABLEFAKEDNS:
            inboundBean = V2rayConfig.InboundBean(tag="socks", port=SOCKS5, protocol="socks",listen=LOCAL_HOST, sniffing=V2rayConfig.InboundBean.SniffingBean(True, sniff_list+["fakedns"],routeOnly=False),settings=V2rayConfig.InboundBean.InSettingsBean(auth="noauth",udp=True,allowTransparent=False))
            inboundBean3=V2rayConfig.InboundBean(listen=LOCAL_HOST,port=LOCALDNSPORT,protocol="dokodemo-door",settings=V2rayConfig.InboundBean.InSettingsBean(address="8.8.8.8", network="tcp,udp", port=53), tag="dns-in")
        else:
            inboundBean = V2rayConfig.InboundBean(tag="socks", port=SOCKS5, protocol="socks",listen=LOCAL_HOST, sniffing=V2rayConfig.InboundBean.SniffingBean(sniff_enable,sniff_list,routeOnly=False),settings=V2rayConfig.InboundBean.InSettingsBean(auth="noauth",udp=True,allowTransparent=False))
            inboundBean3=V2rayConfig.InboundBean(listen=LOCAL_HOST,port=LOCALDNSPORT,protocol="dokodemo-door",settings=V2rayConfig.InboundBean.InSettingsBean(address="8.8.8.8", network="tcp,udp", port=53), tag="dns-in")
    outboundBean=""
    if IS_WARP_ON_WARP:
        outboundBeanwow = V2rayConfig.OutboundBean(tag="warp-out", protocol="wireguard",settings=V2rayConfig.OutboundBean.OutSettingsBean(address=ADDRESSON, mtu=MTUON,reserved=RESERVEDON,secretKey=SECERKEYON,wnoise=WNOISEON,wnoisecount=WNOISECOUNTON,wnoisedelay=WNOISEDELAYON,wpayloadsize=WPAYLOADSIZEON,keepAlive=KEEPALIVEON,peers=[V2rayConfig.OutboundBean.OutSettingsBean.WireGuardBean(endpoint=ENDPOINTON+":"+str(PORTON) ,publicKey=PBKON)]),streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="",sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="proxy")))
    rulesBean=[]
    domainrule=[]
    iprule=[]
    domaindirectdns=[]
    hostdomains={"domain:googleapis.cn":"googleapis.com"}
    if CUSTOMRULES_PROXY[0]!="":
        for i in CUSTOMRULES_PROXY:
            found_num=any(ch.isdigit() for ch in i)
            if not found_num and not "geoip" in i:
                domainrule.append(i)
            else:
                iprule.append(i)
        if domainrule!=[]:
            rulesBean.append(V2rayConfig.RoutingBean.RulesBean(type="field",domain=domainrule,outboundTag="proxy",enabled=True))
        if iprule!=[]:
            rulesBean.append(V2rayConfig.RoutingBean.RulesBean(type="field",ip=iprule,outboundTag="proxy",enabled=True))
        domainrule=[]
        iprule=[]
    if CUSTOMRULES_DIRECT[0]!="":
        for i in CUSTOMRULES_DIRECT:
            found_num=any(ch.isdigit() for ch in i)
            if not found_num and not "geoip" in i:
                domainrule.append(i)
            else:
                iprule.append(i)
            domaindirectdns.extend(domainrule)
        if domainrule!=[]:
            rulesBean.append(V2rayConfig.RoutingBean.RulesBean(type="field",domain=domainrule,outboundTag="direct",enabled=True))
        if iprule!=[]:
            rulesBean.append(V2rayConfig.RoutingBean.RulesBean(type="field",ip=iprule,outboundTag="direct",enabled=True))
        domainrule=[]
        iprule=[]
    if CUSTOMRULES_BLOCKED[0]!="":
        for i in CUSTOMRULES_BLOCKED:
            found_num=any(ch.isdigit() for ch in i)
            if not found_num and not "geoip" in i:
                domainrule.append(i)
            else:
                iprule.append(i)
            if "geosite" in i or  "domain" in i:
                hostdomains.update({f"{i}":LOCAL_HOST})
        if domainrule!=[]:
            rulesBean.append(V2rayConfig.RoutingBean.RulesBean(type="field",domain=domainrule,outboundTag="block",enabled=True))
        if iprule!=[]:
            rulesBean.append(V2rayConfig.RoutingBean.RulesBean(type="field",ip=iprule,outboundTag="block",enabled=True))
    hostdomains.update({
    "dns.pub": [
    "1.12.12.12",
    "120.53.53.53"
    ],
    "dns.alidns.com": [
    "223.5.5.5",
    "223.6.6.6",
    "2400:3200::1",
    "2400:3200:baba::1"
    ],
    "one.one.one.one": [
    "1.1.1.1",
    "1.0.0.1",
    "2606:4700:4700::1111",
    "2606:4700:4700::1001"
    ],
    "dns.google": [
    "8.8.8.8",
    "8.8.4.4",
    "2001:4860:4860::8888",
    "2001:4860:4860::8844"
    ]})
    routingBean=V2rayConfig.RoutingBean(domainStrategy=DOMAINSTRATEGY,rules=rulesBean)
    ######servers
    if not ENABLELOCALDNS:
        dnsBeanSERVERS=[REMOTEDNS]
    else:
        if not ENABLEFAKEDNS:
            dnsBeanSERVERS=[V2rayConfig.DnsBean.ServersBean(address=DOMESTICDNS,domains=["geosite:cn"]+domaindirectdns,expectIPs=["geoip:cn"],port=53),REMOTEDNS]
        else:
            dnsBeanSERVERS=[V2rayConfig.DnsBean.ServersBean(address=DOMESTICDNS,domains=["geosite:cn"]+domaindirectdns,expectIPs=["geoip:cn"],port=53),V2rayConfig.DnsBean.ServersBean(address="fakedns",domains=["geosite:cn"]+domaindirectdns),REMOTEDNS]
    dnsBean=V2rayConfig.DnsBean(hosts=hostdomains,servers=dnsBeanSERVERS,fakedns=V2rayConfig.FakednsBean(ipPool="198.18.0.0/15",poolSize=10000))
    def check_type():
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
            if R_HOST:
                ws_headers = V2rayConfig.OutboundBean.HeadersBean(Host=R_HOST)
            else:
                ws_headers=None
            outboundBean_Stream_ws_settings=V2rayConfig.OutboundBean.WsSettingsBean(headers=ws_headers,path=PATH)
        elif TYPE=="httpupgrade":
            outboundBean_Stream_httpupgrade_settings=V2rayConfig.OutboundBean.HttpupgradeSettingsBean(host=R_HOST,path=PATH)
        elif TYPE=="xhttp":
            outboundBean_Stream_xhttp_settings=V2rayConfig.OutboundBean.XhttpSettingsBean(host=R_HOST,path=PATH,mode=MODE,)
        elif TYPE=="splithttp":
            outboundBean_Stream_splithttp_settings=V2rayConfig.OutboundBean.SplithttpSettingsBean(host=R_HOST,path=PATH)
        elif TYPE=="h2":
            outboundBean_Stream_h2_settings=V2rayConfig.OutboundBean.HttpSettingsBean(host=[R_HOST],path=PATH)
        elif TYPE=="quic":
            outboundBean_Stream_quic_settings=V2rayConfig.OutboundBean.QuicSettingBean(header=V2rayConfig.OutboundBean.HeaderBean(type=HEADER_TYPE),key=PATH,security=R_HOST)
        elif TYPE=="grpc":
            outboundBean_Stream_grpc_settings=V2rayConfig.OutboundBean.GrpcSettingsBean(authority=R_HOST,serviceName=PATH,multiMode=MODE,)
        if SECURITY!="reality":
            outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=ALLOWINCREASE,alpn=ALPN,fingerprint=FP,serverName=SNI,show=False)
        else:
            outboundBean_Stream_tlssettings=V2rayConfig.OutboundBean.TlsSettingsBean(allowInsecure=ALLOWINCREASE,alpn=ALPN,fingerprint=FP,publicKey=PBK,serverName=SNI,shortId=SID,spiderX=SPX,show=False)
        if FRAGMENT:
            if  SECURITY=="reality" :
                if TYPE=="tcp":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security=SECURITY,tcpSettings=outboundBean_Stream_tcpsettings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                elif TYPE=="kcp":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="kcp",security=SECURITY,kcpSettings=outboundBean_Stream_kcp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                elif TYPE=="ws":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="ws",security=SECURITY,wsSettings=outboundBean_Stream_ws_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                elif TYPE=="httpupgrade":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpupgrade",security=SECURITY,httpupgradeSettings=outboundBean_Stream_httpupgrade_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
                elif TYPE=="xhttp":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpx",security=SECURITY,xhttpSettings=outboundBean_Stream_xhttp_settings,realitySettings=outboundBean_Stream_tlssettings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
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
                elif TYPE=="xhttp":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpx",security=SECURITY,xhttpSettings=outboundBean_Stream_xhttp_settings,sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255))
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
                elif TYPE=="xhttp":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpx",security=SECURITY,xhttpSettings=outboundBean_Stream_xhttp_settings,realitySettings=outboundBean_Stream_tlssettings)
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
                elif TYPE=="xhttp":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="httpx",security=SECURITY,xhttpSettings=outboundBean_Stream_xhttp_settings)
                elif TYPE=="splithttp":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="splithttp",security=SECURITY,splithttpSettings=outboundBean_Stream_splithttp_settings,tlsSettings=outboundBean_Stream_tlssettings)
                elif TYPE=="h2":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="h2",security=SECURITY,httpSettings=outboundBean_Stream_h2_settings,tlsSettings=outboundBean_Stream_tlssettings)
                elif TYPE=="quic":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="quic",security=SECURITY,quicSettings=outboundBean_Stream_quic_settings,tlsSettings=outboundBean_Stream_tlssettings)
                elif TYPE=="grpc":
                    outboundBean_Stream_tcp=V2rayConfig.OutboundBean.StreamSettingsBean(network="grpc",security=SECURITY,grpcSettings=outboundBean_Stream_grpc_settings,tlsSettings=outboundBean_Stream_tlssettings)
        return outboundBean_Stream_tcp
    if conifg.startswith("vless://"):
        outboundBean_Stream_tcp=check_type()
        outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="vless", settings=V2rayConfig.OutboundBean.OutSettingsBean(vnext=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean (address=ADDRESS, port=PORT, users=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean.UsersBean(id=ID,security="auto",level=8,encryption=ENCRYPTION,flow=FLOW,alterId=0)])]),mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),streamSettings=outboundBean_Stream_tcp)
    elif conifg.startswith("vmess://"):
        outboundBean_Stream_tcp=check_type()
        outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="vmess", settings=V2rayConfig.OutboundBean.OutSettingsBean(vnext=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean (address=ADDRESS, port=PORT, users=[V2rayConfig.OutboundBean.OutSettingsBean.VnextBean.UsersBean(id=ID,security=SCY,level=8,encryption="",flow="",alterId=ALTERID)])]),mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),streamSettings=outboundBean_Stream_tcp)
    elif conifg.startswith("trojan://"):
        outboundBean_Stream_tcp=check_type()
        outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="trojan" ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),streamSettings=outboundBean_Stream_tcp,settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS, port=PORT,method= "chacha20-poly1305", ota=False,level=8,password=PASS)] ))
    elif conifg.startswith("ss://"):
        sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255)
        if FRAGMENT:
            outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="shadowsocks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="",sockopt=sockopt) ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password=PASS)] ))
        else:
            outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="shadowsocks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="") ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean ( address=ADDRESS, port=PORT,method=METHOD, ota=False,level=8,password=PASS)] ))
    elif conifg.startswith("socks://"):
        if is_hy2:
            FRAGMENT=False
            IS_WARP_ON_WARP=False
            MUX_ENABLE=False
        print(FRAGMENT, is_hy2)
        sockopt=V2rayConfig.OutboundBean.SockoptBean(dialerProxy="fragment",tcpKeepAliveIdle=100,mark=255)
        if FRAGMENT==False:
            if PASS=="" and USER=="":
                outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="socks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="") ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password="")] ))
            else:
                outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="socks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="") ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password="",users=V2rayConfig.OutboundBean.OutSettingsBean.ServersBean.SocksUsersBean(level=8,passw=PASS,user=USER))] ))
        else:
            if PASS=="" and USER=="":
                outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="socks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="",sockopt=sockopt) ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password="")] ))
            else:
                outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="socks",streamSettings=V2rayConfig.OutboundBean.StreamSettingsBean(network="tcp",security="",sockopt=sockopt) ,mux=V2rayConfig.OutboundBean.MuxBean(enabled=MUX_ENABLE,concurrency=CONCURRENCY,xudpConcurrency=CONCURRENCY,xudpProxyUDP443=""),settings=V2rayConfig.OutboundBean.OutSettingsBean(servers=[V2rayConfig.OutboundBean.OutSettingsBean.ServersBean (address=ADDRESS,method=METHOD, port=PORT, ota=False,level=8,password="",users=V2rayConfig.OutboundBean.OutSettingsBean.ServersBean.SocksUsersBean(level=8,passw=PASS,user=USER))] ))
    elif conifg.startswith("wireguard://"):
        FRAGMENT=False
        is_warp=True
        outboundBean = V2rayConfig.OutboundBean(tag="proxy", protocol="wireguard",settings=V2rayConfig.OutboundBean.OutSettingsBean(address=ADDRESS, mtu=MTU,reserved=RESERVED,secretKey=SECERKEY,wnoise=WNOISE,wnoisecount=WNOISECOUNT,wnoisedelay=WNOISEDELAY,wpayloadsize=WPAYLOADSIZE,keepAlive=KEEPALIVE,peers=[V2rayConfig.OutboundBean.OutSettingsBean.WireGuardBean(endpoint=ENDPOINT+":"+str(PORT) ,publicKey=PBK)]))
    end_outbound_bf_frg_set=V2rayConfig.OutboundBean.BeforeFrgSettings(tag="direct",protocol="freedom",settings={})
    end_outbound_bf_frg_set2=V2rayConfig.OutboundBean.BeforeFrgSettings(tag="block",protocol="blackhole",settings={"response":{"type":"http"}})
    if FRAGMENT:
        if FAKEHOST_ENABLE:
            frg=V2rayConfig.OutboundBean.OutSettingsBean.FragmentBean(packets=PACKETS,length=LENGTH,interval=INTERVAL,host1_domain=HOST1_DOMAIN,host2_domain=HOST2_DOMAIN)
        else:
            frg=V2rayConfig.OutboundBean.OutSettingsBean.FragmentBean(packets=PACKETS,length=LENGTH,interval=INTERVAL)
        frg_stream=V2rayConfig.OutboundBean.StreamSettingsBean(network=None,security=None,sockopt=V2rayConfig.OutboundBean.SockoptBean(TcpNoDelay=True,tcpKeepAliveIdle=100,mark=255))
        bf_frg_set=V2rayConfig.OutboundBean.BeforeFrgSettings(tag="fragment",protocol="freedom",settings=frg,streamSettings=frg_stream)
        if ENABLELOCALDNS:
            config = V2rayConfig(log=logBean,dns=dnsBean,  inbounds=[inboundBean,inboundBean2,inboundBean3], outbounds=[outboundBean,bf_frg_set,end_outbound_bf_frg_set,end_outbound_bf_frg_set2],remarks=REMARKS,routing=routingBean)
        else:
            config = V2rayConfig(log=logBean,dns=dnsBean,  inbounds=[inboundBean,inboundBean2], outbounds=[outboundBean,bf_frg_set,end_outbound_bf_frg_set,end_outbound_bf_frg_set2],remarks=REMARKS,routing=routingBean)
    else:
        if is_warp==False:
            if IS_WARP_ON_WARP:
                if ENABLELOCALDNS:
                    config = V2rayConfig(log=logBean,dns=dnsBean, inbounds=[inboundBean,inboundBean2,inboundBean3], outbounds=[outboundBeanwow,outboundBean,end_outbound_bf_frg_set,end_outbound_bf_frg_set2],remarks=REMARKS,routing=routingBean)
                else:
                    config = V2rayConfig(log=logBean,dns=dnsBean, inbounds=[inboundBean,inboundBean2], outbounds=[outboundBeanwow,outboundBean,end_outbound_bf_frg_set,end_outbound_bf_frg_set2],remarks=REMARKS,routing=routingBean)
            else:
                config = V2rayConfig(log=logBean,dns=dnsBean, inbounds=[inboundBean,inboundBean2], outbounds=[outboundBean,end_outbound_bf_frg_set,end_outbound_bf_frg_set2],remarks=REMARKS,routing=routingBean)
        else:
            bf_after_warp_set=V2rayConfig.OutboundBean.BeforeFrgSettings(protocol="freedom",settings={"domainStrategy": "UseIP"},tag="direct")
            after_warp_set=V2rayConfig.OutboundBean.BeforeFrgSettings(protocol="blackhole",settings={"response":{"type": "http"}},tag="block")
            after_warp_set2=V2rayConfig.OutboundBean.BeforeFrgSettings(protocol="dns",tag="dns-out")
            if IS_WARP_ON_WARP:
                if ENABLELOCALDNS:
                    config = V2rayConfig(log=logBean,stats={},dns=dnsBean, inbounds=[inboundBean,inboundBean2,inboundBean3], outbounds=[outboundBeanwow,outboundBean,bf_after_warp_set,after_warp_set,after_warp_set2],remarks=REMARKS,routing=routingBean)
                else:
                    config = V2rayConfig(log=logBean,stats={},dns=dnsBean, inbounds=[inboundBean,inboundBean2], outbounds=[outboundBeanwow,outboundBean,bf_after_warp_set,after_warp_set,after_warp_set2],remarks=REMARKS,routing=routingBean)
            else:
                if ENABLELOCALDNS:
                    config = V2rayConfig(log=logBean,stats={},dns=dnsBean, inbounds=[inboundBean,inboundBean2,inboundBean3], outbounds=[outboundBean,bf_after_warp_set,after_warp_set,after_warp_set2],remarks=REMARKS,routing=routingBean)
                else:
                    config = V2rayConfig(log=logBean,stats={},dns=dnsBean, inbounds=[inboundBean,inboundBean2], outbounds=[outboundBean,bf_after_warp_set,after_warp_set,after_warp_set2],remarks=REMARKS,routing=routingBean)
    data_conf=remove_nulls(config)
    data_conf=replace_accept_encoding(data_conf)
    data_conf=json.dumps(data_conf, indent=4, cls=MyEncoder)
    return data_conf
def goCheckWithConfig(sorted_results,config="wireguard://qJPoIYFnhd/zKuLFPf8/FUyLCbwIzUSNMKvelMlFUnM=@188.114.97.150:891?address=172.16.0.2/32,2606:4700:110:846c:e510:bfa1:ea9f:5247/128&publickey=bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=&reserved=79,60,41&mtu=1330&keepalive=10&wnoise=quic&wnoisecount=15&wnoisedelay=1-3&wpayloadsize=1-8#Tel= @arshiacomplus wire"):
    print("igo")
    oklist = []

    def go():

        http5 = int(app_conf["core"]["inbound_ports"]["http"])

        def split_list(lst, n):
            k, m = divmod(len(lst), n)
            return [
                lst[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
                for i in range(n)
            ]

        split_r = split_list(sorted_results, 20)

        def test_th(port, num=1):
            response = ""
            result = ""
            try:
                proxies = {
                    "http": f"http://127.0.0.{num}:{port}",
                    "https": f"http://127.0.0.{num}:{port}",
                }
                url = test_link_
                headers = {"Connection": "close"}
                try:
                    start = time.time()
                    response = requests.get(
                        url, proxies=proxies, timeout=5, headers=headers
                    )
                except Exception:
                    start = time.time()
                    response = requests.get(
                        url, proxies=proxies, timeout=5, headers=headers
                    )
                elapsed = (time.time() - start) * 1000  # تبدیل به میلی‌ثانیه
                if response.status_code == 204 or (
                    response.status_code == 200 and len(response.content) == 0
                ):
                    result = elapsed
                else:
                    raise IOError(
                        f"Connection test error, status code: {response.status_code}"
                    )
            except RequestException as e:
                print(f"testConnection RequestException: {e}")
                result = "Connection test error, time out !"
                try:
                    if response.status_code == 503:
                        result = "Connection test error, check your connection or ping again ..."
                except Exception:
                    pass
            except Exception as e:
                print(f"testConnection Exception: {e}")
                result = "Connection test error, time out !"
                try:
                    if response.status_code == 503:
                        result = "Connection test error, check your connection or ping again ..."
                except Exception:
                    pass
            if isinstance(result, Number):
                return True
            return False

        def goOnTheTh(whichTuple, i):
            nonlocal oklist
            global which_v
            for ip, port, ping, loss_rate, jitter, combined_score in whichTuple:
                ip = f"[{ip}]" if which_v == "2" else ip
                if loss_rate == 0.00 and ping != 0.0 and ping < 500.00:
                    ipchanged = config.split("@")[0] + f"@{ip}:{port}"
                    if "?" in config:
                        ipchanged += f"?{config.split('?')[1]}"
                    else:
                        ipchanged += f"#none"
                    with open(f"xray/config{i}.json", "w") as f:
                        json.dump(
                            json.loads(parse_configs(ipchanged, cv=i)), f, indent=4
                        )
                    xa,hy=(None,None)
                    if ipchanged.startswith("hy2://") or ipchanged.startswith(
                        "hysteria2://"
                    ):
                        hy = subprocess.Popen(
                            ["hy2/hysteria", "client", "-c", "hy2/config.yaml"],
                            stdin=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                    else:
                        with open("xray/xrayErr.log", "w") as errFile:
                            xa = subprocess.Popen(
                                ["xray/xray", "run", "-c", f"xray/config{i}.json"],
                                stdin=subprocess.DEVNULL,
                                stdout=errFile,
                                stderr=errFile
                            )
                    if test_th(http5, i):
                        print("is ok")
                        oklist.append(
                            (ip, port, ping, loss_rate, jitter, combined_score)
                        )
                    if xa:
                        xa.terminate()
                        xa.wait()
                    if hy:
                        hy.terminate()
                        hy.wait()
                    os.remove(f"xray/config{i}.json")

        def goOnEachThreadOfTuple(split_r):
            threads = []
            for i, part in enumerate(split_r, start=1):
                thread = threading.Thread(target=goOnTheTh, args=(part, i))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

        goOnEachThreadOfTuple(split_r)

    go()
    return oklist
def get_cpu_arch():
    try:
        result = subprocess.run(['uname', '-m'], stdout=subprocess.PIPE, text=True)
        arch = result.stdout.strip().lower()
        return arch
    except Exception as e:
        print(f"[ERROR] Failed to detect CPU architecture: {e}")
        return None

def ensure_folder_exists(folder):
    os.makedirs(folder, exist_ok=True)

def download_file(url, folder):
    filename = url.split('/')[-1]
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        print(f"[SKIP] File already exists: {path}")
        return path

    ensure_folder_exists(folder)
    print(f"[INFO] Downloading: {url} → {path}")
    cmd = ['wget', '-O', path, url]
    subprocess.run(cmd)
    return path

def extract_zip(zip_path, folder):
    print(f"[INFO] Extracting {zip_path} to {folder}...")
    cmd = ['unzip', '-o', zip_path, '-d', folder]
    subprocess.run(cmd)

ARCH_MAP = {
    'aarch64': {
        'xray_url': 'https://github.com/GFW-knocker/Xray-core/releases/download/v1.25.4-mahsa-r2/Xray-linux-arm64-v8a.zip ',
        'hys_url': 'https://github.com/apernet/hysteria/releases/download/app%2Fv2.6.1/hysteria-android-arm64 ',
        'xray_folder': 'xray',
        'hys_folder': 'hy2'
    },
    'armv7l': {
        'xray_url': 'https://github.com/GFW-knocker/Xray-core/releases/download/v1.25.4-mahsa-r2/Xray-linux-arm32-v7a.zip ',
        'hys_url': 'https://github.com/apernet/hysteria/releases/download/app%2Fv2.6.1/hysteria-android-armv7 ',
        'xray_folder': 'xray',
        'hys_folder': 'hy2'
    }
}

def download_cores():
    arch = get_cpu_arch()
    if not arch:
        return

    print(f"[INFO] Detected CPU architecture: {arch}")

    if arch in ARCH_MAP:
        config = ARCH_MAP[arch]

        # --- Xray ---
        xray_zip = download_file(config['xray_url'], config['xray_folder'])
        extract_zip(xray_zip, config['xray_folder'])

        # تعیین دسترسی اجرای تمام فایل‌های داخل xray
        for file in os.listdir(config['xray_folder']):
            file_path = os.path.join(config['xray_folder'], file)
            if os.path.isfile(file_path):
                os.chmod(file_path, 0o755)
                print(f"[CHMOD] +x {file_path}")

        # --- Hysteria ---
        hys_binary = download_file(config['hys_url'], config['hys_folder'])
        os.chmod(hys_binary, 0o755)
        print(f"[CHMOD] +x {hys_binary}")

        print("[SUCCESS] All files downloaded, extracted and permissions set.")
    else:
        print(f"[ERROR] Architecture '{arch}' is not supported.")
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
        if icmp.is_alive:
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
        combined_score = 0.5 * ping + 0.3 * loss_rate + 0.2 * jitter
        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))
    check_conf_ornot=input_p('Check it with config\n ', {"1": 'yes' ,"2": 'no'})
    if check_conf_ornot=="1":
        download_cores()
        confg=input("Give me a config: [Default: N]: ")
        if confg.lower()!="n":
            extended_results=goCheckWithConfig(extended_results,confg)
        else:
            extended_results=goCheckWithConfig(sorted_results=extended_results)
    # Sort the results based on ping time
    sorted_results=sorted(extended_results, key=lambda x: x[5])

    for ip, port,ping,loss_rate,jitter, combined_score  in sorted_results:
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
        if which =='3' and do_you_save=='1':
            if need_port=="2":
                save_best.append('['+ip+']'+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
            else:
                save_best.append('['+ip+']'+port+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
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
        best_ip_mix[0] = "[" + best_ip + "]"
        best_ip_mix[1] = port_random
    else:
        console.print(f"\n[bold green]Best IP : [{random_ip}]:{port_random} with ping time: {best_ping} ms[/bold green]")
        best_ip_mix[0] = "[" + random_ip + "]"
        best_ip_mix[1] = port_random
    return best_ip_mix
def main():
    global which
    global max_workers_number
    global ping_range
    global which_v
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
        combined_score = 0.5 * ping + 0.3 * loss_rate + 0.2 * jitter
        extended_results.append((ip, port, ping, loss_rate,jitter, combined_score))
    check_conf_ornot=input_p('Check it with config\n ', {"1": 'yes' ,"2": 'no'})
    if check_conf_ornot=="1":
        download_cores()
        confg=input("Give me a config: [Default: N]: ")
        if confg.lower()!="n":
            extended_results=goCheckWithConfig(extended_results,confg)
        else:
            extended_results=goCheckWithConfig(sorted_results=extended_results)
    sorted_results = sorted(extended_results, key=lambda x: x[5])
    for ip, port, ping, loss_rate,jitter, combined_score in sorted_results:
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
        if which =='3' and do_you_save=='1':
            if need_port=="2":
                save_result.append(ip+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
            else:
                save_result.append(ip+port+' | '+'ping: '+str(ping)+'packet_lose: '+str(loss_rate)+'jitter: '+str(jitter)+'\n')
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
        if what =='3' or what=='16':
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
    if what=="3" or  what=="16":
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
    if what =='5' or  what=='6' or what =='11' or  what=='12':
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
    os.system('clear')
    check_ipv=check_ipv6()
    rprint(f'ipv4 : [bold red]{check_ipv[0]}[/bold red]\nipv6 : [bold red]{check_ipv[1]}[/bold red]\n')
    options = {
        "1": "scan ip",
        "2": "wireguard for Hiddify",
        "3": "wireguard for Hiddify without ip scanning",
        "4": "wireguard for Hiddify with a sub link",
        "5": "wireguard for v2ray and mahsaNG without noise",
        "6": "wireguard for v2ray and mahsaNG without ip scanning without noise",
        "7": "WoW for v2ray or mahsaNG without noise",
        "8": "WoW for v2ray or mahsaNG in sub link without noise",
        "9": "Add/Delete shortcut",
        "10":"get wireguard.conf",
        "11":"wireguard for nikaNg and MahsaNg  with noise",
        "12":"wireguard for nikaNg and MahsaNg without ip scanning with noise",
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
            if which !="4" :
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
        api_url = 'http://s9.serv00.com:1074/arshiacomplus/api/wirekey'
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
