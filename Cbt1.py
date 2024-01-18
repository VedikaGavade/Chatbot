# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:34:55 2023

@author: Admin
"""

while True:
    print("Welcome! I'm your chat helper")
    
    print("1.Related to Books")
    print("2.Related to Music")
    print("3.Related to News")
    
    option=int(input("please choose above options to get your queries done: _"))
    import Cbt
    
    
    if option==1:
        Cbt.Books()
    if option==2:
        Cbt.Music()
    if option==3:
        Cbt.News()
        
    