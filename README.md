# telegram-bot
Little implementation to read changes on git repo and send messages on telegram group

# export to the internet
* download [Ngrok](https://ngrok.com/download)
* run:
    > ./ngrok http 5000
* get temp url

# config webhook
* in your git repo
* settings > webhooks > add webhook
* on field "Payload URL" add Ngrok temp url "<ngrok_url/webhook>"
* change to "application/json"
* and confirm

# how to init the project
* on the "app.py" replace values:
    > <TELEGRAM_BOT_TOKEN>

    > <TELEGRAM_GROUP_ID>
* install dependencies run:
    > pip install Flask python-telegram-bot
* to start server run:
    > python app.py

# example message from terminal
* on windows power shell
```
	Invoke-RestMethod -Uri "https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/sendMessage" -Method POST -Body @{
	    chat_id = "<TELEGRAM_GROUP_ID>"
	    text = "teste bot :D"
	}
```

* on linux/mac

```
curl -X POST "https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/sendMessage" -d "chat_id=<TELEGRAM_GROUP_ID>&text=teste bot :D"
```

# tips
* to get the group id, add your bot on the group and see the update log on
    > https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/getUpdates

* telegram docs
    > https://core.telegram.org/bots
