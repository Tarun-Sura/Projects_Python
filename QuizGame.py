# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:56:52 2020

@author: Tarun
"""

import requests

r =requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple")
r.status_code
r.text
#for parsing the string to dict
import json
#question =json.loads(r.text)
import html
import pprint

#pprint.pprint(question)

#qn=question['results'][0]['question']

#ans = question['results'][0]['correct_answer']

#print(qn)

#print(ans)

input("WELCOME TO VIDEO GAME QUIZZING!! PRESS ENTER TO START")
con=-1
score=0
rnd=0
while con < 0:
    r =requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple")
    r.status_code
    r.text
    question =json.loads(r.text)
    qn=question['results'][0]['question']
    ans = question['results'][0]['correct_answer']
    print("Qn: ",html.unescape(qn))
    users_ans=input("Type your answer: ").lower()
    rnd=rnd+1
#Checking if the answer matches or not       
    if users_ans.lower() == ans.lower():
        print("Right answer!!")
        score = score+1
#To know the Correct answer        
    elif users_ans.lower() == "idk":
        print("The right answer is :",html.unescape(ans))
#To exit the game        
    elif users_ans.lower() == "quit":
        print("Thanks for playing !!")
        break;
    else:
        print("Wrong answer!! Try again!!")
        score = score -1
    
        
    print("Your Current Score is",score)
    print("You played ",rnd,"round(s)") 
    play_again =input("press enter to play again!!")
    if play_again.lower() == "quit":
        print("Thanks for playing !!")
        break;
    
    
    
    