import telebot
import requests
import time
from telebot import types
from time import sleep
from bs4 import BeautifulSoup as Bs

bot = telebot.TeleBot('5847056954:AAEqO3QgPiVibkI2IGCXj4JwJ1TThZJQUkM')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Проект розробив ' + 'https://t.me/Bishopchick')
    msg = bot.send_message(message.chat.id, "Введите логин: ")
    bot.register_next_step_handler(msg, send_password)


def send_password(message):
    name = (message.text)
    f = open('regdata.txt', 'w')
    f.write(str(name))
    f.close
    f = open('data.txt', 'a')
    f.write('\n' + str(name))
    f.close
    msg = bot.send_message(message.chat.id, "Введите пароль: ")
    bot.register_next_step_handler(msg, last)

def last(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Статистика")
    item2=types.KeyboardButton("Колизей")
    item3=types.KeyboardButton("Казна")
    item4=types.KeyboardButton("Арена")
    item5=types.KeyboardButton("Забрати золото")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    password = (message.text)
    f = open('regdatapass.txt', 'w')
    f.write(str(password))
    f = open('data.txt', 'a')
    f.write('\n' + str(password))
    f.close
    msg = bot.send_message(message.from_user.id, 'Виберіть дію',  reply_markup=markup)
    bot.register_next_step_handler(msg, register)

    

@bot.message_handler(commands=['info'])
def info(message):  
    f = open("data.txt","rb")
    bot.send_document(message.chat.id,f)


@bot.message_handler(commands=['a'])
def login(message):  
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Статистика")
    item2=types.KeyboardButton("Колизей")
    item3=types.KeyboardButton("Казна")
    item4=types.KeyboardButton("Арена")
    item5=types.KeyboardButton("Забрати золото")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    bot.send_message(message.from_user.id, 'Виберіть дію',  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def register (message):
    with open('regdata.txt') as f:
        name = list(f)
        password = list(f)
        f.close
    with open('regdatapass.txt') as f:
        password = list(f)
        f.close
    session = requests.Session()
    url = 'https://mrush.mobi'
    r = session.get(url)
    soup = Bs(r.content, 'lxml')
    soup, styles = Bs(r.content, 'lxml'), []
    for style in soup.find_all('style'):
        style = style.decode_contents()
        if 'float: left;' not in style \
        and 'overflow: hidden;' not in style \
        and 'display: none;' not in style:
            styles.append(style[style.find('.')+1:style.find('{')])
    checkbox = soup.find('div', {'class': styles[1]}).find('input')['class'][0]+''
    post_request = session.post('https://mrush.mobi/login', data= {
        'name': name,
        'password': password,
         checkbox : ''
    },headers=headers)
    print('work')

    msg = bot.send_message(message.from_user.id,'Завантаження...')
    if message.text == 'Статистика':
        quests(session,message)
    elif message.text == 'Колизей':
        kolizei(session)
    elif message.text == 'Казна':
        money(session,message)
    elif message.text == 'Арена':
        arena(session,message)
    elif message.text == 'Забрати золото':
        gold(session,message)

def quests(session,message):
    g = session.get("https://mrush.mobi/christmasCollection?r=815")
    soup = Bs(g.text, 'html.parser') 
    quest_status = soup.find_all('div', class_='wr8')
    for status in quest_status:
        bot.send_message(message.from_user.id,status.text)

def money(session,message):
    g = session.get("https://mrush.mobi")
    soup = Bs(g.text, 'html.parser') 
    gold_status = soup.find_all('div', class_='cntr lorange small')
    for money in gold_status:
        print("Ваші кошти \nЗолота|Срібла\n" + "     " + money.text)
        bot.send_message(message.from_user.id,"Ваші кошти \nЗолота|Срібла\n" + "       " + money.text)

def gold(session,message):
    while  True:
        get_lair_gold = session.get("https://mrush.mobi/lair_gold_get")
        bot.send_message(message.from_user.id,"Забрано")
        print("Забрано")
        time.sleep(86400)
 
def kolizei(session):
    while True:
        g = session.get("https://mrush.mobi/pvp")
        soup = Bs(g.text, 'html.parser') 
        arena_href= soup.find_all('div', class_='cntr mb10')
        for href in arena_href:
            arena_final = href.find('a', {"class": "ubtn inbl mt-15 green mb2"})
            href = arena_final.get("href")
            silk = ("https://mrush.mobi" + href)

        Kolizui = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        # Kolizui = [1]
        iter = 0
        for i in (Kolizui):
            session.get("https://mrush.mobi/christmasCollection/completeQuest?type=FIGHT_COLISEUM")
            figt_monstr= session.post(silk, {
                "in": '1',
                "r": '16',
                })
            iter  += 1
            # bot.send_message(message.from_user.id, ('{} Гру в колізеї зіграно.').format(iter))
            print(('{} Гру в колізеї зіграно.').format(iter))
            time.sleep(140)

def arena(session,message):
    while True:
        Arena = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        for i in (Arena):
            arena = session.get("https://mrush.mobi/arena")
            text = Bs(arena.content, 'html.parser')
            fresh = text.find("a", class_='ubtn inbl mt-15 red mb5')
            url = ('https://mrush.mobi' + fresh['href'])
            print(url)
            r = (url[32:35])
            hash = (url[41:46])
            figt_url_arena = (url)
            figt_arena= session.post(figt_url_arena, {
                "id": '1',
                "r": r ,
                "hash": hash
                })
            print("Бій завершено")
            time.sleep(3)
        time.sleep(10)
        bot.send_message(message.from_user.id,"Good job")



if __name__ == '__main__':  
    print('Початок програми')
    bot.polling(none_stop=True)