import temperature
import time
while(1):
    time.sleep(1)  
    dict_tmp = temperature.get_temperature()
    if(dict_tmp["result"] ==1):
        print(dict_tmp["temperature"])
        print(dict_tmp["humidity"])
    else:
        print("wrong temperature")
