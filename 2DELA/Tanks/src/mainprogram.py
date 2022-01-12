
# Thanks to : https://github.com/rm-hull/luma.lcd/issues/90
# Need to go to /etc/rc.local and change: https://www.makeuseof.com/how-to-run-a-raspberry-pi-program-script-at-startup/ 1.

import time
import ip

from datetime import datetime

from luma.core.interface.serial import pcf8574
from luma.lcd.device import hd44780

interface = pcf8574(address=0x27, backlight_enabled=True)
device = hd44780(interface, width=16, height=2)
device.text = "Hello world"

try:
    while (True):

        globalIP = str(ip.getMyGlobalIp())
        localIP = str(ip.getMyLocalIp())
        # https://strftime.org/

        device.text = '\n'.join([globalIP, localIP])
        time.sleep(5)

except KeyboardInterrupt:
    pass

device.backlight(False)
device.show()