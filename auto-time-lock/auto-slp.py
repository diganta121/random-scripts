import os
import time

try:
    n = int(eval(input("expressions for number of seconds (-ve to -s): \n>>: ")))
    time.sleep(abs(n))

    if n < 0:
        print("shdwn the system")
        os.system("shutdown /s /t 1")
    else:
        print("sleepy time")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
except:
    print("Invalid input. Please enter a number.")
finally:
    sys.exit(0)
