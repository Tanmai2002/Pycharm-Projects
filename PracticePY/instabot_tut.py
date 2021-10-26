import instabot
def postpic(pic_path): 
    bot=instabot.Bot()
    bot.login()
    l=bot.upload_photo(pic_path)
def downloadImg(url,name="test.jpg"):
    import requests
    r = requests.get(url, allow_redirects=True)

    open(name, 'wb').write(r.content)

