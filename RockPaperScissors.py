# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:02:22 2018

@author: Han
"""
print('This is the Rock, Paper, Scissors Game! Play with a friend!')
Ply1 = input("What is Player 1's name?")
Ply2 = input('What is Player 2\'s name?')


guessPly1 = input(Ply1 + ', choose between rock, paper, or scissors.')

guessesDone1 = 0 
guessesDone2 = 0
 
import sys 

for guessesDone1 in range(3):
    # Put logic to check if the input equals to 'rock' or equals to 'paper' or equals to 'scissors'
    # logical comparison 
    # 'and'
    # 'or'
     if guessPly1 == 'rock' or guessPly1 == 'paper' or guessPly1 == 'scissors':
        break
     if guessPly1 != 'rock' or guessPly1 != 'paper' or guessPly1 != 'scissors':
        guessPly1 = input('Invalid answer, ' + Ply1 + '. Please input again.')
for guessesDone1 in range(3,4):
    sys.exit('You did not input a valid answer.')

guessPly2= input(Ply2 + ', choose between rock, paper, or scissors.')

for guessesDone2 in range(3):
    if guessPly2 == 'rock' or guessPly2 == 'paper' or guessPly2 == 'scissors': 
        break
    if guessPly2 != 'rock' or guessPly2 != 'paper' or guessPly2 != 'scissors': 
        guessPly2= input('Invalid answer, ' + Ply2 + '. Please input again.')
        exit

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

