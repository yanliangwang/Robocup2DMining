#!/usr/bin eny python3.4
import sys
import  os
sys.path.append("lib")
from  lib.Kick import  *
from lib.OpenFile import  *
import  numpy  as np
import  matplotlib.pyplot  as plt


plt.title("Yushan2017 all shoot position  data from log 2017")

plt.plot([-52.5,-52.5],[-34,34],color="k" ,linestyle="-", linewidth=0.5)
plt.plot([52.5,52.5],[-34,34],color="k",linestyle="-", linewidth=0.5)
plt.plot([52.5,-52.5],[-34,-34],color="k",linestyle="-", linewidth=0.5)
plt.plot([52.5,-52.5],[34,34],color="k",linestyle="-", linewidth=0.5)


# opp penalty
# Draws penalty area
plt.plot([36, 52.5], [-20, -20], color="k", linestyle="-", linewidth=0.5)
plt.plot([36, 52.5], [20, 20], color="k", linestyle="-", linewidth=0.5)
plt.plot([36, 36], [-20, 20], color="k", linestyle="-", linewidth=0.5)
plt.plot([52.5,52.5],[7,-7], color='r',linewidth=1.0)
plt.plot([50.5,52.5],[7,7],color='r',linewidth=1.0)
plt.plot([50.5,52.5],[-7,-7],color='r',linewidth=1.0)
plt.plot([50.5,50.5],[7,-7],color='r',linewidth=1.0)


plt.plot([-36, -52.5], [-20, -20], color="k", linestyle="-", linewidth=0.5)
plt.plot([-36, -52.5], [20, 20], color="k", linestyle="-", linewidth=0.5)
plt.plot([-36, -36], [-20, 20], color="k", linestyle="-", linewidth=0.5)
plt.plot([-52.5,-52.5],[7,-7], color='r',linewidth=1.0)
plt.plot([-50.5,-52.5],[7,7],color='r',linewidth=1.0)
plt.plot([-50.5,-52.5],[-7,-7],color='r',linewidth=1.0)
plt.plot([-50.5,-50.5],[7,-7],color='r',linewidth=1.0)

ALL_PATH=list()
for file_name in  os.listdir("./log/Yushan"):
	if file_name.__contains__("rcl"):
		temp="./log/Yushan/"+file_name[:-4]
		ALL_PATH.append(temp)


All_shoot_data=list();

for   path  in   ALL_PATH:
	rcl=OpenFile(path).read_rcl()
	rcg=OpenFile(path).read_rcg()
	shoot_data=Kick(rcl=rcl,rcg=rcg,team_name="YuShan2017").get_shoot_data()
	for  i  in shoot_data :
		plt.scatter([abs(i[3])],[i[4]], color="r")
	
	
	
plt.savefig("./yushan_shoot.png")

plt.show()
