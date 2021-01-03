from Bot import Bot

# your location to chromedriver executable
bot = Bot('/Users/**/Downloads/chromedriver')

bot.goto_youtube() \
    .login(email='andilexmchunu@gmail.com', password='A78512345') \
    .subscribe(channelId='uisdg22g') \
    .end()
