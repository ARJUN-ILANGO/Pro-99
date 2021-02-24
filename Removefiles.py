import time
import os
import shutil

class RemoveFiles:
    path = input('Enter Your Path To The File')
    Days = 200
    time.time()
    os.path.exists(path)

    if(path.exists):
        os.walk(path)
        os.path.join()
        ctime= os.stat(path).st_ctime
        if(ctime>time):
            os.remove(path)
        else:
            shutil.rmtree()
    else:
        print('Path Not Exist')