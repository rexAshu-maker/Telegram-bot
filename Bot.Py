import telebot

TOKEN = '6463820078:AAEya9tZaew9L9Sge0nTvOjQDCGRluOWxkk'
ADMIN_ID = 5618136248  # Replace with your actual numeric Telegram ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_text = (
        "🤖 **Welcome to the Bot!**\n\n"
        "I am your personal assistant. Here is what I can do for you:\n"
        "🔹 /ai - Chat with AI for technical or general questions\n"
        "🔹 /shorts - Generate YouTube Shorts & content ideas\n"
        "🔹 /tech - Get help with DIY electronics, circuits & batteries\n"
        "🔹 /tools - Access useful shortcuts & tools\n"
        "🔹 /help - View all available commands\n\n"
        "Type a command or select it from the menu!"
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "📋 **Available Commands:**\n\n"
        "/start - Initialize the bot\n"
        "/help - View command list\n"
        "/ai - Ask technical/general questions\n"
        "/shorts - YouTube Shorts ideas\n"
        "/tech - DIY electronics & circuit help\n"
        "/tools - Useful links & tools\n"
        "/feedback - Send your feedback"
    )
    bot.reply_to(message, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['ai'])
def ai_command(message):
    bot.reply_to(message, "💬 AI chat mode is ready! Ask me any technical or general question.")

@bot.message_handler(commands=['shorts'])
def shorts_command(message):
    bot.reply_to(message, "🎬 Send me your topic, and I'll generate catchy YouTube Shorts ideas and scripts for you!")

@bot.message_handler(commands=['tech'])
def tech_command(message):
    bot.reply_to(message, "🔧 Send your queries regarding DIY electronics, amplifiers, circuits, or batteries.")

@bot.message_handler(commands=['tools'])
def tools_command(message):
    bot.reply_to(message, "🛠️ Here are your tools and shortcuts list.")

@bot.message_handler(commands=['feedback'])
def feedback_command(message):
    bot.reply_to(message, "✍️ Please write your feedback or suggestions. We'd love to hear from you!")

@bot.message_handler(commands=['admin_stats'])
def stats_command(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "📊 **Bot Stats:**\nTotal Users: 1\nActive: Yes (Admin Only)")
    else:
        bot.reply_to(message, "⚠️ This command is restricted to the admin.")

@bot.message_handler(commands=['broadcast'])
def broadcast_command(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "📢 Broadcast feature ready. (Admin Only)")
    else:
        bot.reply_to(message, "⚠️ This command is restricted to the admin.")

@bot.message_handler(commands=['manage_users'])
def manage_users_command(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "👥 Manage or block/unblock users panel. (Admin Only)")
    else:
        bot.reply_to(message, "⚠️ This command is restricted to the admin.")

@bot.message_handler(commands=['restart'])
def restart_command(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "🔄 Bot script restarted successfully. (Admin Only)")
    else:
        bot.reply_to(message, "⚠️ This command is restricted to the admin.")

print("Bot is running...")
bot.infinity_polling()
