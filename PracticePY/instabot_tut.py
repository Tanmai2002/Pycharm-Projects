import instabot
def postpic(pic_path): 
    bot=instabot.Bot()
    bot.login()
    l=bot.upload_photo(pic_path)


