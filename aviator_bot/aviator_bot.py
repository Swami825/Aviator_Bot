



# In[1]:


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# In[2]:


import telegram
print(telegram.__version__)



# In[3]:


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime, timedelta
import random

TELEGRAM_BOT_TOKEN = '7821961986:AAEI8VGaCl5Dwo0YgkPBzZ4Pkg3XIts5sVI'

def generate_fake_signal(for_time):
    minute = for_time.minute
    second = for_time.second
    seed = minute * second + for_time.hour + random.randint(0, 999)
    random.seed(seed)
    predicted_multiplier = round(random.uniform(1.01, 5.0), 2)
    if minute % 5 == 0 and predicted_multiplier < 2:
        predicted_multiplier += random.uniform(1.0, 1.5)
    return round(predicted_multiplier, 2)

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time_gaps = [2, 4, 5, 6, 8]
    chosen_gap = random.choice(time_gaps)
    future_time = datetime.now() + timedelta(minutes=chosen_gap)
    predicted_multiplier = generate_fake_signal(future_time)
    
    message = (
        f"🛩️ *Aviator Signal*\n"
        f"⏰ Signal Time: *{future_time.strftime('%H:%M:%S')}*\n"
        f"💥 Predicted Crash Multiplier: *{predicted_multiplier}x*"
    )
    await update.message.reply_markdown(message)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("signal", signal))
    print("✅ Bot is running. Send /signal to your bot.")
    app.run_polling()

if __name__ == '__main__':
    main()


# In[ ]:




