#!/usr/bin env python3.4
from  OpenFile  import  *
import  re

class   Team:
	def __init__(self, rcg):
		self.rcg=rcg
	def get_team_name(self):
		team_expr = "^\(team[ ][1]*[ ][a-zA-Z0-9]*([-]*[_]*[a-zA-Z0-9]*)*" + \
		            "[ ][a-zA-Z0-9]*([-]*[_]*[a-zA-Z0-9]*)*"
		
		for elt in self.rcg:
			if re.search(team_expr, elt) is not None:
				tmp = re.search(team_expr, elt).group()
				tmp = tmp.split(" ")
				return (tmp[2], tmp[3])  # team_left, team_right
		
		return ("not found", "not found")
	
	
	

if  __name__=="__main__":
	path="../log/201704040927-Miracle_2D_4_2-vs-YuShan2017_4_3"
	rcg=OpenFile(path).read_rcg()
	team1,team2=Team(rcg).get_team_name()
	
	print(team1)
	print(team2)