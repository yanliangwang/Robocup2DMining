#!/usr/bin env python3.4
import re
from  OpenFile  import *
from  Team      import *
from  Kick      import *
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
	
	def get_team_ball_possion_exchage_count(self):
		best_tackle = 0
		n = 0
		all_kick_data = Kick(self.rcl, self.rcg).get_all_kick_data()
		for i in team_l_tackle_cycle:
			while n < len(all_kick_data):
				if all_kick_data[n][0] > i and all_kick_data[n][1] == self.team_name and all_kick_data[n - 1][0] < i:
					best_tackle += 1
					break
				n += 1
		return  best_tackle
		#print(self.team_name + "铲球以后球权转换次数:" + str(best_tackle))
		
	
	

if __name__=="__main__":
	path="../log/201704040927-Miracle_2D_4_2-vs-YuShan2017_4_3"
	rcl=OpenFile(path).read_rcl()
	rcg=OpenFile(path).read_rcg()
	team_l,team_r=Team(rcg).get_team_name()
	team_l_tackle_cycle=Tackle(rcl,rcg,team_l).get_team_tackle_cycle()
	#print(team_l+" Tackle count:"+str(len(team_l_tackle_cycle)))
	
	l_best_tackle=0
	n=0
	

	
	
	all_kick_data=Kick(rcl,rcg).get_all_kick_data()
	n=0
	for  i in  team_l_tackle_cycle:
		while n<len(all_kick_data):
			if  all_kick_data[n][0]>i and  all_kick_data[n-1][0]<i :
				print(all_kick_data[n][0])
				print(i)
				break
			n+=1
		

	
	
	
	
	
	
	team_r_tackle_cycle=Tackle(rcl,rcg,team_r).get_team_tackle_cycle()
	#print(team_r+" Tackle count:"+str(len(team_r_tackle_cycle)))
	
	
	
	
