# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:41:04 2018

@author: Han
"""
print('This is the Password Generator!')
#how difficult od you want your password
#low: only lowercase
#med: lowercase + uppercase
#high: lowercase + uppercase + numbers

import random 

difficulty = input('How difficult do you want your password? (low/med/high/extreme)')
length = int(input('How many characters do you want your password to have?'))

LowLetters = 'abcedfghijklmnopqrstuvwxyz'
UppLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
Numbers = '1234567890'
SpeChara = '!@#$%^&*_+?/><'

password = ''

if difficulty == 'low': 
    for chara in range(length):
        password += random.choice(LowLetters)
if difficulty == 'med':
    for chara in range(length):
        password += random.choice(LowLetters+UppLetters) 
if difficulty == 'high': 
    for chara in range(length):
        password += random.choice(LowLetters+UppLetters+Numbers) 
if difficulty == 'extreme':   
    for chara in range(length):
        password += random.choice(LowLetters+UppLetters+Numbers+SpeChara) 
    
 
print('Here\'s your password: ' + password)


