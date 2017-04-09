#!/usr/bin env python3.4
import re

class  Kick:
	def __init__(self,rcl,rcg,M_team_name=team_name):
		self.rcl=rcl
		self.rcg=rcg
		self.M_team_name=M_team_name
	
	def get_team_kick_cycle(self):
		Kick_Cycle=list()
		for elt in rcl:
			kick_expr="(^d),d\sRecv\s"+self.M_team_name+"\wd\(kick"
			if  re.search(kick_expr,elt).is not None:
				temp=re.search(kick_expr,elt).group()
				Kick_Cycle.append(temp)
		return Kick_Cycle
