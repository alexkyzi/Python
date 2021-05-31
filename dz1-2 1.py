secUser=int(input('введи время в секундах: '))
hour=secUser//3600
minZ=(secUser-3600*hour)//60
secZ=secUser-3600*hour-60*minZ
print(f"{hour:02d}"':'f"{minZ:02d}"':'f"{secZ:02d}")
