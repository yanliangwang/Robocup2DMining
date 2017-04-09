#!/usr/bin env python3.4

class   OpenFile:
	def __init__(self, file_path):
		self.file_path=file_path
	def read_rcg(self):
		rcg=open(self.file_path+".rcg").read()
		rcg=rcg.split("\n")
		return  rcg
	def read_rcl(self):
		rcl=open(self.file_path+".rcl").read()
		rcl=rcl.split("\n")
		return  rcl
	
#  test
if __name__=="__main__":
	path="../log/201704040927-Miracle_2D_4_2-vs-YuShan2017_4_3"
	rcl=OpenFile(path).read_rcg()
	for  elt  in  rcl:
		print(elt)
	
	
	
		














		
