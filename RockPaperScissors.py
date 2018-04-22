# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:02:22 2018

@author: Han
"""

Ply1 = input("What is Player 1's name?")
Ply2 = input('What is Player 2\'s name?')

guessPly1= input(Ply1 + ', choose between rock, paper, or scissors.')
guessPly2= input(Ply2 + ', choose between rock, paper, or scissors.')

if guessPly1 == 'rock':
    if guessPly2 == 'paper':
        print(Ply2 + ' WINS! Paper beats rock!') 
    if guessPly2 == 'rock': 
        print('It\'s a tie, play again!')
    if guessPly2 == 'scissors': 
        print(Ply1 + ' WINS! Rock beats scissors!')
    
if guessPly1 == 'paper':
    if guessPly2 == 'paper':
        print('It\'s a tie, play again!') 
    if guessPly2 == 'rock': 
        print(Ply1 + ' WINS! Paper beats rock!')
    if guessPly2 == 'scissors': 
        print(Ply2 + ' WINS! Scissors beats paper!')
        
if guessPly1 == 'scissors': 
    if guessPly2 == 'paper':
        print(Ply1 + ' WINS! Scissors beats paper!') 
    if guessPly2 == 'rock': 
        print(Ply2 + ' WINS! Rock beats scissors!')
    if guessPly2 == 'scissors': 
        print('It\'s a tie, play again!')

for guessPly1 in range(3):
    if guessPly1 != 'rock': 
         print('Invalid answer, ' + Ply1 + ' please input again.')
    if guessPly1 != 'paper':  
         print('Invalid answer, ' + Ply1 + ' please input again.')
    if guessPly1 != 'scissors':
         print('Invalid answer, ' + Ply1 + ' please input again.')
        
for guessPly2 in range(3):
    if guessPly2 != 'rock': 
         print('Invalid answer, ' + Ply2 + ' please input again.')
    if guessPly2 != 'paper':  
         print('Invalid answer, ' + Ply2 + ' please input again.')
    if guessPly2 != 'scissors':
         print('Invalid answer, ' + Ply2 + ' please input again.')