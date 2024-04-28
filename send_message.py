import requests
import schedule
import time
def send_message():
   
    resp = requests.post('https://textbelt.com/text', {
    'phone': '9945886311',
    'message': 'good morning',
    'key': 'textbelt',
    })
    print(resp.json())
    
# schedule.every().day.at("10:30").do(send_message)
schedule.every(10).seconds.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)