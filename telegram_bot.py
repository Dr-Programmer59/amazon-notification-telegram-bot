
import telebot
from telebot import types
import csv
api_key="ADD-YOUR-API-KEY"
bot=telebot.TeleBot(api_key)




def greet(message):
    print(str(message.from_user.username))
    bot.reply_to(message,"Hi,How are you?")
    
    
@bot.message_handler(commands=['add'])
def greet(message):
            bot.reply_to(message,"Enter the keywords:")
            bot.reply_to(message,"Format of message will be like \n *add nameOfProduct(unique)=ASIN.*",parse_mode= 'Markdown')
@bot.message_handler(commands=['check'])
def greet(message):
            messageTosend="*Name*||*ASIN*"
            details=[]
            with open("links.csv","r",encoding="utf-8") as f:
                for i in csv.reader(f):
                   details.append(i)
            print(details)
               

          
            bot.reply_to(message,messageTosend,parse_mode= 'Markdown')
@bot.message_handler(commands=['remove'])
def remove(message):
    bot.reply_to(message,"Format of message will be like \n *remove nameOfProduct(unique).*",parse_mode= 'Markdown')
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if("remove" in message.text):
        try:
            keyword=message.text.replace("remove","").strip()
            
            details=[]
            with open("links.csv","r") as f:
                for detail in csv.reader(f):
                    details.append(detail)
            for i,value in enumerate(details):
                if keyword in  value:
                    details.pop(i)
                
            with open("links.csv","w",newline='') as f:
                csv.writer(f).writerows(details)
            
            bot.reply_to(message,"Sucessfully Removed")
        except:
            bot.reply_to(message,"Some error occurs")
    elif("add" in message.text):
        try:
            keyword=message.text.replace("add","").strip().split("=")
            print(keyword)
            
                
            with open("links.csv","a+",newline='') as f:
                csv.writer(f).writerows(keyword)            
            bot.reply_to(message,"Sucessfully ADD")
        except:
            bot.reply_to(message,"Some error occurs")  


   
        



bot.polling()
