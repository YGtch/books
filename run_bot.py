import threading
import telebot

def run_bot(batch_size):

    bot = telebot.TeleBot("8582026537:AAFYozpkEBEX1OdS50Vu8lLjCEKHkZPv2GI")
    
    buffers = {}
    buffers_lock = threading.Lock()

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def handle_text(message: telebot.types.Message):
        chat_id = message.chat.id 
        
        # сохраняем сообщение в буфере конкретного чата
        with buffers_lock:
            if chat_id not in buffers:
                buffers[chat_id] = []
            buffers[chat_id].append(message.text)

            # Если накопилось достаточно сообщений — отправляем их назад
            if len(buffers[chat_id]) >= batch_size:
                batch = buffers[chat_id][:batch_size]
                buffers[chat_id] = buffers[chat_id][batch_size:]
            else:
                batch = None

        if batch:
            reply_text = "\n".join(t for t in batch)
            try:
                bot.send_message(chat_id, reply_text)
            except Exception as e:
                print(f"Не удалось отправить сообщение в чат {chat_id}: {e}")
    bot.infinity_polling()
