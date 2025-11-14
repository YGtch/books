import threading
import telebot
import json
from collections import defaultdict


with open('config.json', 'r') as cfg:
    data = json.load(cfg) 
  
def run_bot(batch_size):

    bot = telebot.TeleBot(data["token"])
    
    buffers = defaultdict(list)
    buffers_lock = threading.Lock()

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def handle_text(message: telebot.types.Message):
        chat_id = message.chat.id  
        # save messages in a specific chat
        batch = None
        with buffers_lock:
            buffers[chat_id].append(message.text)
            if len(buffers[chat_id]) >= batch_size:
                batch = buffers[chat_id][:batch_size]
                buffers[chat_id] = buffers[chat_id][batch_size:]

        if batch:
            try:
                bot.send_message(chat_id, "\n".join(batch))
            except Exception as e:
                print(f"Failed to send message to {chat_id}: {e}")
    bot.infinity_polling()
