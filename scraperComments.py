import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5N1WBH/ref=sr_1_1?crid=L4QWKYMV51PV&keywords=macbook%2Bair%2Bm1&qid=1655923623&sprefix=macbook%2Bair%2Bm1%2Caps%2C78&sr=8-1&th=1'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(class_="a-price-whole").get_text()
    converted_price = int(price[0:3])

    print(title.strip())
    print(converted_price)

    if(converted_price < 950):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', '') #gmail account and app password
    
    subject = 'Get your skates on...'
    body = 'Your MacBook Air is down in price! Christmas present for mum, sorted!\n\nhttps://www.amazon.co.uk/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5N1WBH/ref=sr_1_1?crid=L4QWKYMV51PV&keywords=macbook%2Bair%2Bm1&qid=1655923623&sprefix=macbook%2Bair%2Bm1%2Caps%2C78&sr=8-1&th=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '', #sender gmail account
        '', #recipient email address
        msg
    )
    print('The order has been given')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 240)


