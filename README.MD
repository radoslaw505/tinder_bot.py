Before running script you need to:
 - download chromedriver, unzip, and move to `/usr/local/bin` (linux)
 - `pip install selenium`

create a properties.py file with variables for facebook login:
``` 
 username = 'your_username'
 password = 'your_password'
```

Running script:
```
python3 -i tinder_bot.py
```

Script will run interactive. He is creating a class `bot` and executing a `login()` function.
To run functions:
```
bot.login()         # fb authentication, accepting localization popup, reject notifications
bot.like()          # swipe right
bot.dislike()       # swipe left
bot.next_photo()    # show next photo
bot.autoswipe()     # run auto swipe (likes), execute close_popups(), close_match() and out_of_likes() if nessesary
bot.close_popup()   # close popups
bot.close_match()   # close match popup (to be added)
bot.out_of_likes()  # when out of like, closing popup and exit()
```