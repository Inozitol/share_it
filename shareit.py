import os
import sys
import hashlib
import subprocess
import urllib.request


home = os.path.expanduser("~")
sh_path = home+"/.share/"

if not os.path.exists(sh_path):
    os.mkdir(sh_path)

hash_name=hashlib.md5(sys.argv[1].encode()).hexdigest()[:10]
if not os.path.exists("/var/www/html/share/"+hash_name):
    os.symlink(os.path.abspath(sys.argv[1]),"/var/www/html/share/"+hash_name)

ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print("URL: http://"+ip+"/share/"+hash_name)
