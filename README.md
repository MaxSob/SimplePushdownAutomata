# SimplePushdownAutomata
A simple implementation of a pushdown automata to recognize context free grammars

## Automata definition 
To define the automata we need to define the sets of states, input alphabet, stack alphabet, final states and transition rules
```python
q = ['q1','q2','q3','q4']
sigma = ['0','1']
gamma = ['0',"$"]
delta = {}
f = ['q1','q4']
```

## Rule definition
A simple way to define the rules of the automata is using the method add rule of the pushdown automata, it recieves the current state, the next state, the input character the stack character and the symbol to push to the stack. You can use the `epsilon` special word to define and empty char of the input an empty reading operation of the stack and a empty push operation to the stack
```python
a = PushdownAutomata(q, sigma, gamma, delta, 'q1', f)
a.addRule('q1','q2','epsilon','epsilon','$')
a.addRule('q2','q2','0', 'epsilon', '0')
a.addRule('q2','q3','1', '0', 'epsilon')
a.addRule('q3','q3','1', '0', 'epsilon')
a.addRule('q3','q4','epsilon', '$', 'epsilon')
```

##Word processing
To process a string you cak use the `processInput` method of the automata which returns the transitions used to accept the input string
```python
accepted_paths = a.processInput('0000011111')

#Print accepted paths
i = 1
for p in accepted_paths:
    print("Printing path: " + str(i))
    for t in p:
        print(t[0])
    i += 1
```

