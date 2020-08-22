from Solver.DFS import dfs 
from Solver.BFS import bfs
from Base.nodes import State
import os
import sys


def main():
	
	s = 0
	if len(sys.argv) <= 1:
		s = State()
	else:
		file = sys.argv[1]
		THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
		my_file = os.path.join(THIS_FOLDER, 'instance\\'+file)
		s = State(my_file)
	dfs(s)	

if __name__ == "__main__":
   main()