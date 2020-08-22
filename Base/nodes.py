import copy
import numpy as np

class State:
	def __init__ (self,file = None):
		self.p = np.zeros((9,9),dtype=int)
		if(file is not None):
			#file = './instance/tablero.txt'	
			archivo = open(file,'r')
			j = 0
			for linea in archivo:
				linea = linea.strip().split(" ")
				for i in range(0,9):
					self.p[j][i] = int(linea[i])
				j=j+1
		print("State Create")
	
	def get_action(self):
		actions = []
		for i in range(0,9):
			for j in range(0,9):	
				if self.p[i][j] == 0 :
					for n in range(1,10):
						self.p[i][j] = n
						if(self.is_valid()):
							a = action(i,j,n)
							actions.append(a)		
						self.p[i][j] = 0	
					return actions
		return actions

	def transition(self,action):
		s = copy.deepcopy(self)
		i = action.x
		j = action.y
		s.p[i][j] = action.num
		return s	

	def is_valid(self):
		for i in range(0,9):
			checkCol = []
			checkRow = []
			for j in range(0,9):
				if(self.p[i][j] != 0):
					checkCol.append(self.p[i][j])	
					if(checkCol.count(self.p[i][j]) > 1):
						return False

				if(self.p[j][i] != 0):
					checkRow.append(self.p[j][i])	
					if(checkRow.count(self.p[j][i]) > 1):
						return False
	
		for m in range(0,3):
			for n in range (0,3):
				checkMatrix = []
				for i in range(0,3):
					for j in range(0,3):
						x = 3*m+i
						y = 3*n+j
						if(self.p[x][y] != 0):
							checkMatrix.append(self.p[x][y])	
							if(checkMatrix.count(self.p[x][y]) > 1):
								return False
		return True

	def is_final_state(self):
		if(self.is_valid()):
			for i in range(0,9):
				for j in range(0,9):
					if (self.p[i][j] == 0):
						return False
			return True		
		else:
			return False

		
class action:
	def __init__(self,x,y,num):
		self.x = x
		self.y = y
		self.num = num

				




	
