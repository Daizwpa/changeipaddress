import time
import random
import os;
def callback_after(fun, sec ):
    while True:
        
        time.sleep(sec)
        fun()

def change_ipadress():
    random.seed()
    x = random.randrange(2, 244)
    print(x)
    os.system(f'netsh interface ipv4 set address name="Wi-Fi" static 192.168.1.{x} 255.255.255.0 192.168.1.1')
callback_after(change_ipadress, 45)