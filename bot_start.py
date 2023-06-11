import telebot;
import numpy as np
import pandas as pd
import matplotlib as mpl
from telebot import types
bot=telebot.TeleBot('5836703328:AAGNXDvkH7K1hSe0bH6Dvl5L01GZAYJ4o0c');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, напиши /help для получения списка доступных команд")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /reg для регистрации или /start для решения задач")
    elif message.text == "/reg":
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    elif message.text =="/start":
        bot.send_message(message.from_user.id,"Начинаем решать задачи?")
        bot.register_next_step_handler(message,education)
    elif message.text == "/stats123":
        for i  in range(user_number):
            bot.send_message(message.from_user.id,users[i])
            bot.send_message(message.from_user.id,amount[i])
    else:
        bot.send_message(message.from_user.id,"Я не могу тебя понять, напиши /help для получения доступных комманд")

name = '';
surname = '';
age = 0;
global k;
k=0;
global user_number;
users=[""]*100;
amount=[""]*100;
tasks=[""]*100;
ans=[""]*100;
user_number=0;
task_number=[0]*100;

with open(r'C:\Users\t7623\Desktop\tasks.txt') as text:
    for line in text.readlines():
        tasks[k]=line;
        k=k+1;

k=0;
with open(r'C:\Users\t7623\Desktop\ans.txt') as text:
    for line in text.readlines():
        ans[k]=line
        k=k+1
k=0;

def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id,'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    age = int(message.text) #проверяем, что возраст введен корректно
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?');
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id,"Всё верно?", reply_markup=markup);
    bot.register_next_step_handler(message,check_registration);

def check_registration(message):
    global user_number
    if message.text == "Да":
        bot.send_message(message.from_user.id,"Регистрация Завершена")
        users[user_number]=surname+' '+name;
        user_number=user_number+1;
        bot.send_message(message.from_user.id,"Введите /start для решения задач")

    elif message.text == "Нет":
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name)

def education(message):
    if message.text=="Да":
        if tasks[task_number[user_number]]=="END":
            bot.send_message(message.from_user.id,"Задачи кончились")
            amount[user_number-1]=task_number[user_number];
        else:
            bot.send_message(message.from_user.id,tasks[task_number[user_number]]);
            bot.send_message(message.from_user.id,"Введите ответ");
            bot.register_next_step_handler(message,check_task);
    elif message.text=="Нет":
        amount[user_number-1]=task_number[user_number];
def check_task(message):
    if int(message.text) == int(ans[task_number[user_number]]):
        bot.send_message(message.from_user.id,"Верно");
        task_number[user_number]=task_number[user_number]+1;
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Продолжаем решать задачи?", reply_markup=markup);
        bot.register_next_step_handler(message,education);
    else:
        bot.send_message(message.from_user.id,"Неверно,попробуйте ввести ответ снова");
        bot.register_next_step_handler(message, check_task);

bot.polling(none_stop=True, interval=0)