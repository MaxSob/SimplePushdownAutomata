#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:48:15 2019

@author: mcampos
"""
class PushdownAutomataRule:
    
    def __init__(self, current_state, next_state, input_string, stack_string, push):
        self.c_state = current_state
        self.n_state = next_state
        self.input = input_string
        self.stack = stack_string
        self.push = push
    
    def __str__(self):
        return self.c_state + ": (" + self.input + "," + self.stack + ")-->" + self.push + " : " + self.n_state 
    
    
class PushdownAutomata:
    
    def __init__(self, q, sigma, gamma, delta, q0, f, stack=[]):
        self.q = q
        self.sigma = sigma
        self.gamma = gamma
        self.delta = delta
        self.q0 = q0
        self.f = f
        self.paths = [[(None, self.q0, [])]]
        self.accepted = []
    
    def addRule(self, current_state, next_state, input_char, stack, push):
        rule = PushdownAutomataRule(current_state, next_state, input_char, stack, push)
        if current_state in self.delta.keys():
            self.delta[current_state].append(rule)
        else:
            self.delta[current_state] = [rule]
        
    def processInput(self, input_string):
        print(self.paths)
        for char in input_string:
            print("*" * 30)
            print("Processing " + char)
            new_paths = []
            for p in self.paths:
                cp = p[-1]
                print(cp[1], cp[2], char)
                next_paths = self.moveAutomata(cp[1], cp[2], char)
                for n in next_paths:
                    new_paths.append(p + [n])
            self.paths = new_paths
            
        for p in self.paths:
            if p[-1][1] in self.f:
                self.accepted.append(p)
        return self.accepted
            
    def moveAutomata(self, current_state, current_stack, char):
        candidates = []
        current_rules = self.delta[current_state]
        stack_symbol = current_stack.pop() if len(current_stack) > 0 else None
        for r in current_rules:
            input_accepted = r.input == 'epsilon' or r.input == char
            stack_accepted = r.stack == 'epsilon' or r.stack == stack_symbol
            if input_accepted and stack_accepted:
                print("Applying " + str(r))
                if r.stack == "epsilon" and stack_symbol is not None:
                    current_stack.append(stack_symbol)
                stack_copy = current_stack
                if r.push != "epsilon":
                    stack_copy.append(r.push)
                candidates.append((r, r.n_state, stack_copy))
        return candidates

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
accepted_paths = a.processInput('0000011111')

#Print accepted paths
i = 1
for p in accepted_paths:
    print("Printing path: " + str(i))
    for t in p:
        print(t[0])
    i += 1