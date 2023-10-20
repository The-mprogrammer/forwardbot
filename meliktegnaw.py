
#import some classes from the telebot package
from telebot import TeleBot,telebot,types,util
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from telebot.util import user_link

ADMIN_ID= 550518325 
# id during the test [5249435830 ]
bot_token = "6809638781:AAHI3ucRVlZOwJjESxkCc-_9TFwfgmCluWs"
bot=telebot.TeleBot(bot_token,parse_mode="HTML")

#this help us to create an inline button with attached to text
markup=InlineKeyboardMarkup()
channel=InlineKeyboardButton(text="Group", url="t.me/Darbimoi_TeachTech")
markup.add(channel)

#this decorator used to handle the /start command,if we specify the command parameter
@bot.message_handler(commands=["start"])
def greetUSer(msg):
    #this is user object
    user=msg.from_user
    text="Assaymanti bifa suraatini ykn dokumantitin eergi:\n Send the assignment in the form of image or document:"
    if msg.from_user.id != ADMIN_ID:
        bot.send_message(msg.chat.id,f"Hello {user_link(user)} {text}",reply_markup=markup)
        #this method used to register a content sent by user,just it store and we can fetch the data by creating a function like the below code
        bot.register_next_step_handler(msg,toAdmin)
    else:
        bot.reply_to(msg,"Hellow my king,your servent is ready to serve you:)",reply_markup=markup)

#forward to admin *this is the function which works the final step,send the stored data to user
def toAdmin(msg):
    user= msg.from_user
    #for admin only
    bot.copy_message(ADMIN_ID,msg.chat.id,msg.message_id) 
    bot.send_message(ADMIN_ID,f"This message is sent from: {user_link(user)}")
    #notify the user,their msg is sent successfully 
    bot.reply_to(msg,"Ergan ke seene jira!\n irra deebite erguf kana tuqi:> /start\n your message is delivered successfully,to send another file click /start",reply_markup=markup) 

bot.infinity_polling()
