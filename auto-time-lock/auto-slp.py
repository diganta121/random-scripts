import os
import time
import datetime

prev = datetime.datetime.now()

try:
    n = int(eval(input("expressions for number of seconds (-ve to -s): \n>>: ")))
    time.sleep(abs(n))

    if n < 0:
        # shdn the system
        os.system("shutdown /s /t 1")
    else:
        # to sleep
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
except:
    print("Invalid input. Please enter a number.")
finally:
    sys.exit(0)
