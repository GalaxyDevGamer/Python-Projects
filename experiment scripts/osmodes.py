import os
import ctypes
mode = ['shutdown', 'reboot', 'sleep', 'cancel']
flag = 'n'
while(flag != 'y'):
    cnt = 0
    for i in mode:
        cnt+=1
        print cnt, mode[cnt-1]
    a = input('Select mode')
    if a == 1:
        os.system('shutdown -s -f')
        break
    if a == 2:
        os.system('shutdown -r -f')
        break
    if a == 3:
        ctypes.windll.PowrProf.SetsuspendState(0, 1, 0)
    if a == 4:
        flag = raw_input('exit?')
        if flag != 'n':
            break
