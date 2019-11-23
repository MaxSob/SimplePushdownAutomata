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

    def __init__(self, q, sigma, gamma, delta, q0, f):
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
        chars = 1
        print(self.paths)
        for char in input_string:
            print("*" * 30)
            print("Processing char " + str(chars) + " : " + char)
            new_paths = []
            for p in self.paths:
                cp = p[-1]
                print(cp[1], cp[2], char)
                next_paths = self.moveAutomata(cp[1], cp[2], char)
                pending_process = []
                for n in next_paths:
                    #print(n)
                    #Epsilon input
                    if not n[3]:
                        pending_process.append([n])
                    else:
                        new_paths.append(p + [n])
                while len(pending_process) > 0:
                    #print(pending_process)
                    ap = pending_process.pop()
                    pn = ap[-1]
                    other_paths = self.moveAutomata(pn[1], pn[2], char)
                    for n in other_paths:
                        if not n[3]:
                            pending_process.append([pn, n])
                        else:
                            new_paths.append(p + [pn , n])
            chars += 1
            self.paths = new_paths
        
        for p in self.paths:
            if len(p[-1][2]) > 0:
                next_moves = self.moveAutomata(p[-1][1], p[-1][2], "epsilon")
                for m in next_moves:
                    p.append(m)
                    
        for p in self.paths:
            if p[-1][1] in self.f:
                self.accepted.append(p)
                    
        return self.accepted
       
    def moveAutomata(self, current_state, current_stack, char):
        transitions = []
        current_rules = self.delta[current_state] if current_state in self.delta.keys() else []
        stack_symbol = current_stack.pop() if len(current_stack) > 0 else None
        for r in current_rules:
            processed = True
            input_accepted = r.input == 'epsilon' or r.input == char
            stack_accepted = r.stack == 'epsilon' or r.stack == stack_symbol
            if input_accepted and stack_accepted:
                print("Applying " + str(r))
                if r.stack == "epsilon" and stack_symbol is not None:
                    current_stack.append(stack_symbol)
                stack_copy = current_stack
                if r.push != "epsilon":
                    stack_copy.append(r.push)
                if r.input == "epsilon":
                    processed = False
                transitions.append((r, r.n_state, stack_copy, processed))
        return transitions

    def printPaths(self, paths = None):
        i = 1
        paths = paths if paths is not None else self.paths
        for p in paths:
            print("Printing path: " + str(i))
            for t in p:
                print(t[0])
        i += 1