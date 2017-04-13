#!/usr/bin eny python3.4
import sys
sys.path.append("lib")
from  lib.Kick import  *
from lib.OpenFile import  *
import  numpy  as np
import  matplotlib.pyplot  as plt


plt.title("Miracle_2d vs Yushan2017")

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


path = "./log/201704040927-Miracle_2D_4_2-vs-YuShan2017_4_3"
rcl = OpenFile(path).read_rcl()
rcg = OpenFile(path).read_rcg()
# afert=Kick(rcl,rcg).get_after_goal_data()
shoot_data = Kick(rcl, rcg, "YuShan2017").get_shoot_data()

for elt  in  shoot_data:
	plt.scatter([elt[3]],[elt[4]],color="r")


shoot_data_r= Kick(rcl, rcg, "Miracle_2D").get_shoot_data()

for elt  in  shoot_data_r:
	plt.scatter([elt[3]],[elt[4]],color="r")
plt.show()