import telebot as telebot
from telegram import *
from telegram import bot
from telegram.ext import *
from requests import *
import os
import logging
from uuid import uuid4

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
#deserts="Desserts"
orderfood = "Type of food"
rateourservice = "Rate our service"
ratethefood = "Rate the food"
Vegetarian = "Vegetarian"
maincourse="Main course"
southIndian="South Indian"
icecreams="Ice creams"
american="American"
chettinad="Chettinad"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
# def put(update, context):
#     """Usage: /put value"""
#     # Generate ID and separate value from command
#     key = str(uuid4())
#     # We don't use context.args here, because the value may contain whitespaces
#     value = update.message.text.partition(' ')[2]
#
#     # Store value
#     context.user_data[key] = value
#     # Send the key to the user
#     update.message.reply_text(key)
#
# def get(update, context):
#     """Usage: /get uuid"""
#     # Seperate ID from command
#     key = context.args[0]
#
#     # Load value and send it to the user
#     value = context.user_data.get(key, 'Not found')
#     update.message.reply_text(value)
logger = logging.getLogger(__name__)

# soup="Soups"
# starters="Starters"
# maincourse="Main Course"
# deserts="deserts"
# juices="Juices"

def start_handler(update, context):
    # update.message.reply_text("Hello", reply_markup=food())
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome, Please choose any one of the options",
                             reply_markup=ReplyKeyboardMarkup(choice()))


def choice():
    keyboard = [[KeyboardButton(orderfood)], [KeyboardButton(rateourservice)], [KeyboardButton(ratethefood)]]
    return keyboard


def pref():
    buttons = [[KeyboardButton(Vegetarian, callback_data="Vegetarian")],
               [KeyboardButton("Nonveg", callback_data="Nonveg")]]
    return ReplyKeyboardMarkup(buttons)


def food():
    button = [[KeyboardButton(southIndian, callback_data="southIndian")], [KeyboardButton(chettinad, callback_data="chettinad")],[KeyboardButton(icecreams, callback_data="icecreams")],[KeyboardButton(american, callback_data="american")]]
    return button


# def favour():
#
#     keyboard=[[InlineKeyboardButton(soup,callback_data="soup")],[InlineKeyboardButton(starters,callback_data="starters")],[InlineKeyboardButton(maincourse,"maincourse")],[InlineKeyboardButton(deserts,callback_data="deserts")],[InlineKeyboardButton(juices,callback_data="juices")]]
#     return keyboard

def message(update: Update, context: CallbackContext):
    # if orderfood in update.message.text:
    #     #update.message.reply_text(orderfood)
    #     button = [[InlineKeyboardButton("soup", callback_data="soup")],
    #                 [InlineKeyboardButton("starters", callback_data="starters")],
    #                 [InlineKeyboardButton("maincourse", "maincourse")],
    #                 [InlineKeyboardButton("deserts", callback_data="deserts")],
    #                 [InlineKeyboardButton("juices", callback_data="juices")]]
    #
    #     context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(button),text="What would you like to have now??")

    if rateourservice in update.message.text:
        # update.message.reply_text(rateourservice)
        like="👍"
        dislike="👎"
        buttons = [[KeyboardButton(like, callback_data="like")],
                   [KeyboardButton(dislike, callback_data="dislike")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons),
                                 text="Did you like our service?")



    if ratethefood in update.message.text:
        buttons = [[InlineKeyboardButton("👍", callback_data="like")],
                   [InlineKeyboardButton("👎", callback_data="dislike")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                 text="Did you like the food?")

    if orderfood in update.message.text:
        # buttons = [[KeyboardButton(Vegetarian, callback_data="Veg")],[KeyboardButton("Non-Vegetarian", callback_data="Nonveg")]]
        # context.bot.send_message(chat_id=update.effective_chat.id,text="Choose any one?")
        update.message.reply_text("choose any one", reply_markup=pref())
    if Vegetarian in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=ReplyKeyboardMarkup(food()),text="Choose any one?")
    elif "Nonveg" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(food()),text="Choose any one?")
    if southIndian in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,text="https://www.zomato.com/chennai/mami-tiffen-stall-mylapore \n\n https://www.zomato.com/chennai/nithya-amirtham-mylapore \n\n https://www.zomato.com/chennai/prive-restaurant-mylapore \n\n  https://www.zomato.com/chennai/sukha-nivas-mylapore \n\n https://www.zomato.com/chennai/hotel-chaitra-mylapore ")
    elif chettinad in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,text="https://www.zomato.com/chennai/kaaraikudi-mylapore \n\n https://www.zomato.com/chennai/anjappar-mylapore \n\n https://www.zomato.com/chennai/viswanathan-chettinadu-hotel-mylapore \n\n https://www.zomato.com/chennai/hotel-karur-alagar-mylapore \n\n https://www.zomato.com/chennai/madurainaygam-chettinadu-mess-mylapore \n\n https://www.zomato.com/chennai/hotel-select-mylapore")
    elif icecreams in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,text="https://www.zomato.com/chennai/a2b-adyar-ananda-bhavan-mylapore \n\n https://www.zomato.com/chennai/lassi-shop-mylapore \n\n https://www.zomato.com/chennai/ibaco-mylapore \n\n https://www.zomato.com/chennai/keventers-milkshakes-ice-creams-mylapore \n\n https://www.zomato.com/chennai/milkyway-mylapore")
   # elif deserts in update.message.text:
        #context.bot.send_message(chat_id=update.effective_chat.id, text="https://www.zomato.com/chennai/27-culinary-street-mylapore ")#\n\n https://www.zomato.com/chennai/zuka-mylapore \n\n https://www.zomato.com/chennai/southern-street-mylapore \n\n https://www.zomato.com/chennai/cake-affairs-mylapore \n\n https://www.zomato.com/chennai/senthil-softy-zone-mylapore")
    elif american in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="https://www.zomato.com/chennai/tovo-1-mylapore \n\n https://www.zomato.com/chennai/bro-bistro-1986-mylapore \n\n https://www.zomato.com/chennai/pedrenos-mylapore \n\n ")




        # update.message.reply_text("choose any one", reply_markup=food())

    # else:
    #     context.bot.send_message(chat_id=update.effective_chat.id,text="Please Choose the options below")


if __name__ == '__main__':

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # dp.add_handler(CommandHandler('put', put))
    # dp.add_handler(CommandHandler('get', get))
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(MessageHandler(Filters.text, message))
    updater.bot.set_webhook()
    updater.start_polling()
    updater.idle()
