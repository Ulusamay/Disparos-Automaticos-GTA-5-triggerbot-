from pymem import *
from pymem.process import *
from time import sleep
from ahk import AHK

ahk = AHK()
try:
    pm = pymem.Pymem('GTA5.exe')
except:
    print('GTA 5 Não detectado')
print('TRIGGERBOT GTA V  <DarlanScript>')
while True:
    atirar = pm.read_long(0x1794E54E364)
    if (atirar == 377 or atirar == 377):
        ahk.click()
input('')
