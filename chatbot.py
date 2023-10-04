#question:answer

import time

tm = time.ctime()

qna ={
    "hi":"Hello,How can I assist you.",
    "hey":"Hello,How can I assist you.",
    "hlo":"Hello,How can I assist you.",
    "hello":"Hello,How can I assist you.",
    "who has created you":"Abhay created me using python.",
    "your name":"My name is AI chatbot, but you can call me just chatbot.",
    "chatbot":"Yes, How can i help you",
    "hor are you":"I am doing well. What's about you.",
    "how old are you":"I am 2 years old",
    "i am well":"Nice to hear that.",
    "tell me something about you":"Sure, I am a rule based chatbot created by Mr. Abhay.",
    "what is the time now": tm,
    "time":tm,
    "help":"I can help you.",
    "quit":"Bye for now. See you soon :)",
    "are you human":"No, i am simple rule based chatbot.",
    "sorry":"Its alright.",

}

while True: #infinite loop created
    question=input()
    
    if(question =="exit()"):
        break
    
    else:
        print(qna[question])
    
