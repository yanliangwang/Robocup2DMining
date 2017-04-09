#!/usr/bin env python3.4
import re
from  OpenFile  import *
from  Team      import *


class  Kick:
	def __init__(self,rcl,rcg,team_name):
		self.rcl=rcl
		self.rcg=rcg
		self.team_name=team_name
	
	def get_team_kick_cycle(self):
		Kick_Cycle=list()
		kick_expr = "^([0-9]*)?,\d\sRecv\s"+self.team_name+".*?kick"
		for elt in rcl:
			if  re.search(kick_expr,elt) is not None:
				temp=re.search(kick_expr,elt).group(1)
				Kick_Cycle.append(temp)
		return Kick_Cycle



if __name__=="__main__":
	path="../log/201704040927-Miracle_2D_4_2-vs-YuShan2017_4_3"
	rcl=OpenFile(path).read_rcl()
	rcg=OpenFile(path).read_rcg()
	team_l,team_r=Team(rcg).get_team_name()
	team_l_kick_cycle=Kick(rcl,rcg,team_l).get_team_kick_cycle()
	print(team_l+" kick count:"+str(len(team_l_kick_cycle)))
	team_r_kick_cycle=Kick(rcl,rcg,team_r).get_team_kick_cycle()
	print(team_r+" kick count:"+str(len(team_r_kick_cycle)))

