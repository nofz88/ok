import requests
from config import *

def telegram_bot2(hello2 + message2):
    send_text2 = 'https://api.telegram.org/bot' + bot_token2 + '/sendMessage?chat_id=' + bot_chatID2 + '&parse_mode=Markdown&text=' + message2
    response2 = requests.get(send_text2)
    return response2.json()
    
def telegram_bot1(hello1 + message1):
    send_text1 = 'https://api.telegram.org/bot' + bot_token1 + '/sendMessage?chat_id=' + bot_chatID1 + '&parse_mode=Markdown&text=' + message1
    response1 = requests.get(send_text1)
    return response1.json()
    
#print(telegram_bot("HI"))