from rivescript import RiveScript

# initializing rivescript object + Arabic Language support
bot = RiveScript(utf8=True)

# load directory of the brain file
bot.load_directory("brain")
bot.sort_replies()


'''
# bot reply validation function
def chat(message):
    if message == "":
        return -1, "No message found!"
    else:
        response = bot.reply("user", message)
        if response:
            return 0, response
        else:
            return -1, "No Response found!!"

'''


while True: 
    msg = str(input("User: "))
    reply = str(bot.reply('localuser', msg))
    if msg == "quit":
        break
    else:
        print("Bot: " + reply)