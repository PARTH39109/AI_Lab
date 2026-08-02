from collections import deque 
 
a_cap = 4 
b_cap = 3 
 
goal = 2 
 
start = (0, 0) 
 
q = deque() 
 
visited = set() 
 
q.append((start, [start])) 
visited.add(start) 
 
while q: 
    (a, b), path = q.popleft() 
 
    if a == goal: 
        print("Solution Found!\n") 
        for i, state in enumerate(path): 
            print("Step", i, ":", state) 
        break 
 
    next_states = [(a_cap, b), (a, b_cap), (0, b), (a, 0)] 
 
    t = min(a, b_cap - b) 
    next_states.append((a - t, b + t)) 
 
    t = min(b, a_cap - a) 
    next_states.append((a + t, b - t)) 
 
    for state in next_states: 
        if state not in visited: 
            visited.add(state) 
            q.append((state, path + [state])) 

 
