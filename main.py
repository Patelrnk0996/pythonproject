# Show the IPL Score
import requests
from bs4 import BeautifulSoup
import time
from plyer import notification

while True:
    # Open the site
    url = "https://www.scorespro.com/rss2/live-cricket.xml"
    r = requests.get(url)
    # Find the text from site
    sp = BeautifulSoup(r.text,'html.parser')
    # Find the Score related to IPL
    data = sp.find_all('title')
    # print(data)
    d = data[1].text
    # print(d)         # It the print title of all but it ignore then print length 32 after all print
    d = d[32:]
    print(d)
    # Set the NOtification for Windows.
    notification.notify(
    title = "IPL Score Notifier",
    message = str(d),
    app_name = "IPL 2020",
    app_icon = "ipl.ico",
    timeout = 15
    )
    time.sleep(20)