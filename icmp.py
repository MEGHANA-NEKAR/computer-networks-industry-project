import subprocess
import pyfiglet

print("-" * 50)
ascii_banner = pyfiglet.figlet_format("ICMP SCANNING",font="digital")
print(ascii_banner)
for ping in range(1,5):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    #if res = 1 means destination is unreachable
    if res == 0:
        print( "ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")