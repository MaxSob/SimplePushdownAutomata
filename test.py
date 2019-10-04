from PushdownAutomata import PushdownAutomata

#Automata definition
q = ['q1','q2','q3','q4']
sigma = ['0','1']
gamma = ['0',"$"]
delta = {}
f = ['q1','q4']

#Rule definition
a = PushdownAutomata(q, sigma, gamma, delta, 'q1', f)
a.addRule('q1','q2','epsilon','epsilon','$')
a.addRule('q2','q2','0', 'epsilon', '0')
a.addRule('q2','q3','1', '0', 'epsilon')
a.addRule('q3','q3','1', '0', 'epsilon')
a.addRule('q3','q4','epsilon', '$', 'epsilon')

#Process a String
accepted_paths = a.processInput('000111')
a.printPaths(accepted_paths)
