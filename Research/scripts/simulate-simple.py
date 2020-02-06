'''
Simple program to simulate Infector in env.
github.com/ginchung/2020Wuhan
Created on Feb 5, 2020
'''

import numpy as np

# Original Number: Normal people, Infected persons
Normal=10000 
Infect=5
Normal-=Infect

# Env setting, making it Square
x=80
y=80
l_inf=0.01 #km

#agent data: i in front of var means Infected
x=np.random.rand

