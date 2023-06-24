import socket
import os

def exit():
      os.system("exit")

ports = [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5555, 5900, 8080, 8888]

def scan():
        target = str(input('\nALVO: '))
        print('                       PORTA\tESTA')
        for port in ports:
             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.6)
             code = s.connect_ex((target, port))
             if code == 0:
                   print(f"                       {port}\tAberta")
  
print('''
     ____  ____  ____  ___________ _________    _   ________  __
    / __ \/ __ \/ __ \/_  __/ ___// ____/   |  / | / / __ \ \/ /
   / /_/ / / / / /_/ / / /  \__ \/ /   / /| | /  |/ / /_/ /\  /
  / ____/ /_/ / _, _/ / /  ___/ / /___/ ___ |/ /|  / ____/ / /
 /_/    \____/_/ |_| /_/  /____/\____/_/  |_/_/ |_/_/     /_/
                 https://github.com/Ch4rse
''')

try:
      scan()
except:
    exit()
    print('[!] IP INVALIDO')
