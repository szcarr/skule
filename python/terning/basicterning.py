import machine
import utime

pins = [16, 17, 18, 19, 20, 21, 22]
ledListe = []

for i in range(len(pins)):
    ledListe.append(machine.Pin(pins[i], machine.Pin.OUT))

while True:
    for i in range(len(ledListe)):
        ledListe[i].toggle()
        utime.sleep(1)
