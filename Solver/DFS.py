import sys
sys.path.append("..")

from Base.nodes import State
from Base.nodes import action

def dfs(state):
    itex = 0
    S =[]
    S.append(state)
    
    while(len(S) != 0):
        actual = S.pop()
        actions = actual.get_action()
        
        if(actual.is_final_state()):
            print(itex)
            print(actual.p)
            break
        
        for a in actions:
            ss = actual.transition(a)
            S.append(ss)
            
        if(itex%10000 == 0):
            print(itex)
            print(actual.p)
        itex += 1
        
            