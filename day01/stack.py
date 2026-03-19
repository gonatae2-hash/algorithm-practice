stack = [] # stack = LIFO(마지막에 넣은게 먼저 나옴) 사용
stack.append('A') # push A -> ['A']
stack.append('B') # push B -> ['A','B']
stack.append('C') # push C -> ['A', 'B', 'C']
print(stack.pop()) # -> 'C'
print(stack.pop()) # -> 'B'