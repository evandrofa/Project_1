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
    limao_tahiti = types.InlineKeyboardButton('Limao Tahiti', callback_data='limao_tahiti')
    maca_fuji = types.InlineKeyboardButton('Maca Fuji', callback_data='maca_fuji')
    maca_gala = types.InlineKeyboardButton('Maca Gala', callback_data='maca_gala')

    markup.add(abacate, abacaxi, mamao, maracuja, pera, tangerina, uva, melancia, banana, limao_tahiti, maca_fuji, maca_gala)
    
    bot.send_message(message.chat.id, 'Qual cotação gostaria de ver hoje? Preço/KG', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.message:
        if callback.data == 'abacate':
            bot.send_message(callback.message.chat.id, "🥑Cotação do Abacate🥑")
            for i in range(len(abacate_dados)):
                mensagem = f"{abacate_dados['Local'].iloc[i]} : {abacate_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'abacaxi':
            bot.send_message(callback.message.chat.id, '🍍Cotação do Abacaxi🍍')
            for i in range(len(abacaxi_dados)):
                mensagem = f"{abacaxi_dados['Local'].iloc[i]} : {abacaxi_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)


        elif callback.data == 'banana':
            bot.send_message(callback.message.chat.id, '🍌Cotação da Banana🍌')
            for i in range(len(banana_dados)):
                mensagem = f"{banana_dados['Local'].iloc[i]} : {banana_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'limao_tahiti':
            bot.send_message(callback.message.chat.id, '🍋Cotação do Limao Tahiti🍋')
            for i in range(len(limao_tahiti_dados)):
                mensagem = f"{limao_tahiti_dados['Local'].iloc[i]} : {limao_tahiti_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'maca_fuji':
            bot.send_message(callback.message.chat.id, '🍎Cotação da Maça Fuji🍎')
            for i in range(len(maca_fuji_dados)):
                mensagem = f"{maca_fuji_dados['Local'].iloc[i]} : {maca_fuji_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'maca_gala':
            bot.send_message(callback.message.chat.id, '🍎Cotação da Maça🍎')
            for i in range(len(maca_gala_dados)):
                mensagem = f"{maca_gala_dados['Local'].iloc[i]} : {maca_gala_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'mamao':
            bot.send_message(callback.message.chat.id, '🥭Cotação do Mamão🥭')
            for i in range(len(mamao_dados)):
                mensagem = f"{mamao_dados['Local'].iloc[i]} : {mamao_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'maracuja':
            bot.send_message(callback.message.chat.id, 'Cotação do Maracuja')
            for i in range(len(maracuja_dados)):
                mensagem = f"{maracuja_dados['Local'].iloc[i]} : {maracuja_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'melancia':
            bot.send_message(callback.message.chat.id, '🍉Cotação da melancia🍉')
            for i in range(len(melancia_dados)):
                mensagem = f"{melancia_dados['Local'].iloc[i]} : {melancia_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'pera':
            bot.send_message(callback.message.chat.id, '🍐 Cotação da pera 🍐')
            for i in range(len(pera_dados)):
                mensagem = f"{pera_dados['Local'].iloc[i]} : {pera_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'tangerina':
            bot.send_message(callback.message.chat.id, '🍊Cotação da Tangerina🍊')
            for i in range(len(tangerina_dados)):
                mensagem = f"{tangerina_dados['Local'].iloc[i]} : {tangerina_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'uva':
            bot.send_message(callback.message.chat.id, '🍇Cotação da uva🍇')
            for i in range(len(uva_dados)):
                mensagem = f"{uva_dados['Local'].iloc[i]} : {uva_dados['Preço'].iloc[i]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        else:   
            bot.send_message(callback.message.chat.id, 'ERROR')
    
bot.polling()