import requests
from bs4 import BeautifulSoup
import smtplib
import datetime
import time


url = 'https://www.bestbuy.com/site/asus-rog-zephyrus-g14-14-gaming-laptop-amd-ryzen-9-16gb-memory-nvidia-geforce-rtx-2060-1tb-ssd-moonlight-white/6403816.p?skuId=6403816'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


def check_price():
    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    #soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    # title = soup1.find(class="heading-5 v-fw-regular").get_text()
    pre_order = soup1.find(type="button").get_text()

    #converted_price = float(price[1:7])
    add_to_cart = "Add to Cart"

    #global titles
    #titles = title[0:12]

    if (pre_order == add_to_cart):
        send_mail()
    else:
        today = datetime.date.today()
        print(f'The item is still not ready for purchase {today: %Y-%m-%d}. ')
        send_mail()

    # print(converted_price)

    # print("The price right now is {0}".format(
    #    converted_price), title.strip())


# title_short = title[0:12]


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('<email>', '<auth_token>')

    subject = f'The item is ready to purchase & ship!'
    body = f"\nThe laptop isn't for sale yet but this robot is sending you an email of the item to pre order for me or buy when on sale..\nCheck the link before price goes up! \n{url}"
    body1 = f"\nYou are now apart of this...\nThe laptop isn't for sale yet but this robot is sending you an email of the item to pre order for me or buy when on sale..\nCheck the link before price goes up! \n{url}"

    msg = f"Subject: {subject}\n\n{body}"
    msg1 = f'Subject: {subject}\n\n{body1}'

    server.sendmail(
        '<sender_email>',
        '<reciever_emmail>',
        msg
    )
    server.sendmail(
        '<sender_email>',
        '<reciever_emmail>',
        msg1
    )
    print("An email has been sent.")


# def no_email():
#     dates = datetime.now()
#     # now = datetime.timestamp(date)
#     print(f'Sorry. The price seems to be the same or higher. As of {dates}')
    server.quit()


while True:
    time.sleep(10)
    check_price()

check_price()
