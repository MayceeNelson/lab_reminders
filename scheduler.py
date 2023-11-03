import schedule 
import time
import requests

def job():
    print("working")
    requests.get("http://localhost:5000/check-message")
    return ""
schedule.every().day.at("08:00", "US/Mountain").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)
    