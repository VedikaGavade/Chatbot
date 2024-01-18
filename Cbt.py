# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:41:47 2023

@author: Admin
"""

while True:
    def Books():
        
        dict1={"Can I get the book called The Alchemist?":"Yess! you can It is available at our store",
               "Can I exchange this book and get the another though i have completed it before time":"Yess! definetly But you first need to register yourself here"}
        dict2={"1":"Yess! you can It is available at our store","2":"Yess! definetly But you first need to register yourself here"}
        dict3={"hii":"hii","hello":"hello","how are you?":"Fine.....Thanks what about you?"}
        user=input("Please tell me your concern: _")
        if user in dict3:
            print("chatbot:",dict3[user])
            
        elif user in dict1:
            print("chatbot:",dict1[user])
            
        else:
            print("\nSorry cant understand:")
            print("1.Can I get the book called The Alchemist?")
            print("2.Can I exchange this book and get the another though i have completed it before time")
            user=input("please select your query! type quit to exit")
            if user in dict2:
                print("chatbot:",dict2[user])
            else:
                print("Thankyou!")
print("Hey!! \nThis is Ved,How can i help you? ")
while True:
    def Music():
        
        dict11={"Which is the most played song on youtube?":"SATRANGA- from ANIMAL[starring Ranbir Kappor & Rashmika Mandana",
                "List the Top 10 songs of 80's Kumar Sanu":"mera dil wo itna pagal hai ,Ashiqui"}
        dict22={"1":"SATRANGA- from ANIMAL[starring Ranbir Kappor & Rashmika Mandana","2":"mera dil wo itna pagal hai ,Ashiqui"}
        dict33={"hii":"hii","hello":"hello","how are you?":"Fine.....Thanks what about you?"}
        user=input("Please tell me your concern: _")
        if user in dict33:
            print("chatbot:",dict33[user])
            
        elif user in dict11:
            print("chatbot:",dict11[user])
        
        else:
            print("\nSorry cant understand:")
            print("1.Which is the most played song on youtube?")
            print("2.List the Top 10 songs of 80's Kumar Sanu")
            user=input("please select your query! type quit to exit")
            if user in dict22:
                print("chatbot:",dict22[user])
            else:
                print("Thankyou!")
print("Hey!! \nThis is Ved,How can i help you? ")
                
                