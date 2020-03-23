import time

while(True):
    segundo = time.strftime("%S")
    if(int(segundo) % 5 == 0):
        print(segundo + " Es multiplo de 5")
    else:
        print(segundo + " No es multiplo de 5")
    time.sleep(1)
