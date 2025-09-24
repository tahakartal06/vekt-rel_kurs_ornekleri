# import time
# print ("3 saniye bekle.")
# time.sleep(3)
# print("Bekledim.", )
# time.sleep(3)
# print ("Bekledim.",)

import time, sys
# for a in range(10,0,-1):
#     # print(a)
#     time.sleep(1)
#     sys.stdout.write(u"\u001b[1000D") #gerisayım
#     sys.stdout.write(f"{str(a)}   ")
#     sys.stdout.flush()

# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

# import datetime, sys
# while True:
#     simdi = datetime.datetime.now()
#     saat = simdi.strftime("%H:%M:%S")
#     sys.stdout.write(u"\u001b[1000D" + str(saat))
#     sys.stdout.flush()


import datetime, sys
gunler = ["Pz","Pt","Sl","Çarşamba","Pr","Cu","Ct"]


simdi = datetime.datetime.now()
gun = int(simdi.strftime("%w"))
#print(type(gun))
print(gun, gunler[gun])
