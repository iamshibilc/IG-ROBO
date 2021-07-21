#import modules
import os
import time
import sys
import random
import requests
from tqdm import tqdm
from instabot import Bot
from bullet import Password
# Bot Parameters
bot = Bot(
    max_likes_per_day=450,
    max_follows_per_day=300,
    max_unfollows_per_day=200,
    max_comments_per_day=100,
    max_messages_per_day=50,

    max_likes_to_like=10000000000,
    min_likes_to_like=10,

    max_followers_to_follow=500,
    min_followers_to_follow=100,
    max_following_to_follow=10,
    min_following_to_follow=2,
    min_media_count_to_follow=2,

    like_delay=random.randint(15, 30),
    follow_delay=30,
    unfollow_delay=35,
    comment_delay=20,
    message_delay=20,

    filter_users=False,
)

#Creating Clear Console Funcation...
def console_clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')


#Target Can Edit...
INSHACKE_TARGETS = [
    'adnaan_07dz',
    'ask_attractive',
    'virat.kohli',
    'riyaz.14',
    'mr_faisu_07',
    'pappya_gaikwad_official',
    'dqsalmaan',
    'hasnaink07'
    ]
def Igrobo():
 os.system("clear")
 print ('  ')
 print (""" \033[36m  ▄▄▄▄▄▄     ▄▄▄▄   \033[31m   ▄▄▄▄▄▄      ▄▄▄▄    ▄▄▄▄▄▄      ▄▄▄▄""") 
 print (""" \033[36m  ▀▀██▀▀   ██▀▀▀▀█  \033[31m   ██▀▀▀▀██   ██▀▀██   ██▀▀▀▀██   ██▀▀██""")
 print (""" \033[36m    ██    ██        \033[31m   ██    ██  ██    ██  ██    ██  ██    ██""")
 print (""" \033[36m    ██    ██  ▄▄▄▄  \033[31m   ███████   ██    ██  ███████   ██    ██""")
 print (""" \033[36m    ██    ██  ▀▀██  \033[31m   ██  ▀██▄  ██    ██  ██    ██  ██    ██""")
 print (""" \033[36m  ▄▄██▄▄   ██▄▄▄██  \033[31m   ██    ██   ██▄▄██   ██▄▄▄▄██   ██▄▄██""")
 print (""" \033[36m  ▀▀▀▀▀▀     ▀▀▀▀   \033[31m   ▀▀    ▀▀▀   ▀▀▀▀    ▀▀▀▀▀▀▀     ▀▀▀▀""")
 print ("""          """), time.sleep(.1)
 print (""" \033[31m [\033[36m +\033[31m ]\033[36m  TOOL CREATED BY SIMZEOVER  V.2.0 """)
 print ("    ")

def Login():
 f = open("/data/data/com.termux/files/home/.bash_profile","w")
 f.write("alias igrobo='cd $HOME/IG-ROBO && rm -rf config && python igrobo.py'")
 f.close()
 Igrobo() 
 print('\033[36m')
 variable = requests.get('https://docs.google.com/spreadsheets/d/1Ij4ARxsQAyhlXt0eLnZ8d6MwXxOue5W96Cm3xJP3O90/edit?usp=drivesdk')
 time.sleep(.1)
 print("  \033[36m[R] LOGIN PAGE  ")
 USERNAME = input ("  \033[36m[R] USERNAME [\033[37m ")
 if USERNAME in variable.text:
  cli= Password(prompt="  \033[36m[R] PASSWORD [\033[37m ", hidden="•")
  result = cli.launch()
  print ('\033[36m')
  bot.login(username=USERNAME,password=result),
  igrobo()
 else:
  print (" \033[36m")
  print ("    \033[36m [x] YOUR USERNAME IS NOT IN OUR DATABASE!!")
  print ("    \033[36m [x] KINDLY CONTACT OUR ADMINISTRATORS!! \033[37m")
  print ("			")
def igrobo():
    while True:
        i = 1  # Number of Loop
        try:
            while i < 10:
                i += 1
                bot.unfollow_users(user_ids=INSHACKE_TARGETS)
                print('     \033[36m[->] UNFOLLOWING IN PROGRESS PLEASE WAIT!![<-]')
                print('     \033[36m[✓] USERS UNFOLLOWED SUCCESSFULLY [✓]')
                print('     \033[36m[->] SLEEPING 960 SEC [<-]')
                time.sleep(960)  # 16 min...
                bot.follow_users(user_ids=INSHACKE_TARGETS, nfollows=10)
                print('     \033[36m[->] FOLLOWING IN PROGRESS PLEASE WAIT!![<-]')
                print('     \033[36m[✓] USERS FOLLOWED SUCCESSFULLY [✓]')
                print('     \033[36m[->] SLEEPING 960 SEC [<-]')
                time.sleep(960)  # 16 min
        except KeyboardInterrupt:
            break
        time.sleep(1800)
    console_clear()
Login()
