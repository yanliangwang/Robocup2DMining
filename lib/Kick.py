#!/usr/bin env python3.4
import re

import  OpenFile  as op
import  Team      as tm


class  Kick:
	def __init__(self,rcl,rcg,team_name="NULL"):
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
	
	def get_ball_data(self):
		
		ball_data_expr = "[0-9]*[ ]\(\(b\)([ ][-]?[0-9]*(\.[0-9]*)?){4}\)"
		ball_data = list()
		
		for elt in self.rcg:
			ball = list()
			line = elt.split(" ")
			if re.search(ball_data_expr, elt) is not None:
				tmp = re.search(ball_data_expr, elt).group()
				tmp = tmp.split(" ")
				ball.append(int(tmp[0]))
				ball.append(float(tmp[2]))
				ball.append(float(tmp[3]))
				ball_data.append(ball)  # cycle, x, y
		
		return ball_data
	
	def get_kick_data(self):
		ball_data=self.get_ball_data()
		
		kick_data_expr = "^(\d*),.*?Recv ([a-z0-9A-Z_]*)_(\d*): \(kick"
		kick_data = list()
		for elt in self.rcl:
			result=re.search(kick_data_expr,elt)
			if result is not None:
				cycle=int(result.group(1))
				team=result.group(2)
				n_player=int (result.group(3))
				tmp=[cycle,team,n_player]
				kick_data.append(tmp)  #
				#print(tmp)
		
		for elt in kick_data:
			for p in ball_data:
				
				if elt[0]==p[0]:
					elt.insert(3,p[1])
					elt.insert(4,p[2])
					#print(elt)
		return  kick_data
		
	
	def get_after_goal_data(self):
			after_goal_expr="^(\d*)?,.*\(referee goal_([l-r])"
			after_goal_data=list()
			for elt in self.rcl:
				result=re.search(after_goal_expr,elt)
				if result is not None:
					cycle=int(result.group(1))
					side=result.group(2)
					tmp=[cycle,side]
					after_goal_data.append(tmp)
			
			return  after_goal_data
	
	
	def get_shoot_data(self):
		shoot_data=list()
		kick_data=self.get_kick_data()
		after_goal_data=self.get_after_goal_data()
		team_l,team_r=tm.Team(self.rcg).get_team_name()
		
		team_side="l"
		
		
		
		if team_l==self.team_name:
			team_side="l"
		else:
			team_side="r"
			
	
		team_kick_data=list()
		
		for i  in kick_data:
			if i[1]==self.team_name:
				team_kick_data.append(i)

		
		
		team_after_goal_data=list()
		
		for i in after_goal_data:
			if i[1]==team_side:
				team_after_goal_data.append(i)
				
	   
				
				
		print(self.team_name+"  shoot data")
		for i in  team_after_goal_data:
			for j in team_kick_data:
				j_index=team_kick_data.index(j)
				if j[0]<=i[0]  and  j_index+1<len(team_kick_data) and  team_kick_data[j_index+1][0]>=i[0]:
					print(j)
					shoot_data.append(j)
					break

				
		return  shoot_data
				
				
				
		
	
		
		
					
			

	
	
if __name__=="__main__":
	path = "../log/201704040927-Miracle_2D_4_2-vs-YuShan2017_4_3"
	rcl = op.OpenFile(path).read_rcl()
	rcg = op.OpenFile(path).read_rcg()
	#afert=Kick(rcl,rcg).get_after_goal_data()
	shoot_data=Kick(rcl,rcg,"YuShan2017").get_shoot_data()
	shoot_data_2=Kick(rcl,rcg,"Miracle_2D").get_shoot_data()


	

	
