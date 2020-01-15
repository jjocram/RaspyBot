# RaspyBot
A telegram bot to manage a RaspberryPi

# How to setup
Follow this steps to setup RaspyBot

## 1. Create a new bot on telegram
Go to [telegram official guide](https://core.telegram.org/bots#3-how-do-i-create-a-bot) to create a new bot

## 2. Clone this repository on your raspberry
```git clone https://github.com/jjocram/RaspyBot```

## 3. Create a new systemd serivce.
Create new file: /lib/systemd/system/raspy_bot.service
**Remeber to:** 
  - change YOUR_BOT_TOKEN_GOES_HERE with your bot's token. Otherwise -2 will be return on start;
  - change YOUR_USER with your username;
  - change PATH_TO_RASPYBOT_DIR with the absolute path to reach the directory created when your cloned this repository;
  - install python-telegram-bot with ```pip install python-telegram-bot```
  
```
[Unit]
Description=Run RaspyBot on startup
Wants=network.target
After=network.target
After=multi-user.target

[Service]
WorkingDirectory=/home/pi/
User=YOUR_USER
Environment=BOT_TOKEN=YOUR_BOT_TOKEN_GOES_HERE
ExecStart=/usr/bin/python3 PATH_TO_RASPYBOT_DIR/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## 4. Enable the service to run at startup
```sudo systemctl enable raspy_bot.service```

## 5. Start your bot
```sudo systemctl start raspby_bot.service```
