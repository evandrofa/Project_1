import pandas as pd
import telebot
from telebot import types


abacate_dados = pd.read_csv('data/abacate_data.csv')
abacaxi_dados = pd.read_csv('data/abacaxi_data.csv')
banana_dados = pd.read_csv('data/banana_data.csv')
limao_tahiti_dados = pd.read_csv('data/abacaxi_data.csv')
maca_fuji_dados = pd.read_csv('data/maca_fuji_data.csv')
maca_gala_dados = pd.read_csv('data/maca_gala_data.csv')
mamao_dados = pd.read_csv('data/mamao_data.csv')
maracuja_dados = pd.read_csv('data/maracuja_data.csv')
melancia_dados = pd.read_csv('data/melancia_data.csv')
pera_dados = pd.read_csv('data/pera_data.csv')
tangerina_dados = pd.read_csv('data/tangerina_data.csv')
uva_dados = pd.read_csv('data/uva_data.csv')
bot = telebot.TeleBot('6995053124:AAEmaVvDWBqnJt2GFLRHmRXGm0R69rKRmDM')

@bot.message_handler(commands=['start'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=4)

    abacate = types.InlineKeyboardButton('Abacate', callback_data='abacate')
    abacaxi = types.InlineKeyboardButton('Abacaxi', callback_data='abacaxi')
    mamao = types.InlineKeyboardButton('Mamao', callback_data='mamao')
    maracuja = types.InlineKeyboardButton('Maracuja', callback_data='maracuja')
    pera = types.InlineKeyboardButton('Pera', callback_data='pera')
    tangerina = types.InlineKeyboardButton('Tangerina', callback_data='tangerina')
    uva = types.InlineKeyboardButton('Uva', callback_data='uva')
    melancia = types.InlineKeyboardButton('Melancia', callback_data='melancia')
    banana = types.InlineKeyboardButton('Banana', callback_data='banana')
    limao_tahiti = types.InlineKeyboardButton('Limao_tahiti', callback_data='limao_tahiti')
    maca_fuji = types.InlineKeyboardButton('Maca Fuji', callback_data='maca_fuji')
    maca_gala = types.InlineKeyboardButton('Maca Gala', callback_data='maca_gala')

    markup.add(abacate, abacaxi, mamao, maracuja, pera, tangerina, uva, melancia, banana, limao_tahiti, maca_fuji, maca_gala)
    
    bot.send_message(message.chat.id, 'Qual cotação gostaria de ver hoje? Preço/KG', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.message:
        if callback.data == 'abacate':
            bot.send_message(callback.message.chat.id, 'Cotação do Abacate')
            for i in range(len(abacate_dados)):
                mensagem = f"{abacate_dados['Local'].iloc[i]} : {abacate_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'abacaxi':
            bot.send_message(callback.message.chat.id, 'Cotação do Abacaxi')
            for i in range(len(abacaxi_dados)):
                mensagem = f"{abacaxi_dados['Local'].iloc[i]} : {abacaxi_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
        else:   
            bot.send_message(callback.message.chat.id, 'Think Again...')
    
bot.polling()