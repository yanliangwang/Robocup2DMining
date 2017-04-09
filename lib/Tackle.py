#!/usr/bin env python3.4
import re
from  OpenFile  import *
from  Team      import *
class  Tackle:
	def __init__(self,rcl,rcg,team_name):
		self.rcl=rcl
		self.rcg=rcg
		self.team_name=team_name
	def get_team_tackle_cycle(self):
		Tackle_Cycle=list()
		Tackle_expr = "^([0-9]*)?,\d\sRecv\s"+self.team_name+".*?tackle"
		for elt in self.rcl:
			if  re.search(Tackle_expr,elt) is not None:
				temp=re.search(Tackle_expr,elt).group(1)
				Tackle_Cycle.append(temp)
		return Tackle_Cycle
	
	

if __name__=="__main__":
	path="../log/201704040927-Miracle_2D_4_2-vs-YuShan2017_4_3"
	rcl=OpenFile(path).read_rcl()
	rcg=OpenFile(path).read_rcg()
	team_l,team_r=Team(rcg).get_team_name()
	team_l_tackle_cycle=Tackle(rcl,rcg,team_l).get_team_tackle_cycle()
	print(team_l+" Tackle count:"+str(len(team_l_tackle_cycle)))
	team_r_tackle_cycle=Tackle(rcl,rcg,team_r).get_team_tackle_cycle()
	print(team_r+" Tackle count:"+str(len(team_r_tackle_cycle)))


	
