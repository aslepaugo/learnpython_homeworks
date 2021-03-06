"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings 

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME, 
        'password': settings.PROXY_PASSWORD
    }
}

LIST_OF_PLANETS = [
    'Mercury',
    'Venus',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
]


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def show_planet_constellation(bot, update):
    planet_name = update.message.text.split()[1].capitalize()

    if planet_name in LIST_OF_PLANETS:      
        planet = getattr(ephem, planet_name)()
        planet.compute(datetime.now())
        update.message.reply_text("{} is in {} constellation now".format(planet_name, ephem.constellation(planet)[1]))  
    else:
        update.message.reply_text("I cannot identify constellation for {}".format(planet_name)) 


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", show_planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
