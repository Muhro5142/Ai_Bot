import telebot
from logic import Text2ImageAPI
from config import TOKEN , api_key , api_secret

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['gen'])
def gen(message):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', api_key, api_secret)

    if len(message.text.split()) > 1 :

        model_id = api.get_model()
        promt = ''.join(message.text.split()[1:])
        uuid = api.generate(promt, model_id)

        base64_img = api.check_generation(uuid)

        api.decode64(base64_img)

        with open('output0.png' , 'rb') as photo:
            bot.send_photo(message.chat.id,photo)
    else:
        bot.send_message(message.chat.id,"No text NO PIC")


if __name__ == "__main__":
    bot.polling(none_stop = True)