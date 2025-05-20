import requests
import time
from bs4 import BeautifulSoup
import threading
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ComponentChoose:
    def component(self, component_number):
        return getattr(self, f'case_{component_number}')()

    def case_1(self):
        return "https://www.ss.lv/lv/electronics/computers/completing-pc/cpu/search-result/?q="

    def case_2(self):
        return "https://www.ss.lv/lv/electronics/computers/completing-pc/hdd/search-result/?q="

    def case_3(self):
        return "https://www.ss.lv/lv/electronics/computers/completing-pc/ssd/search-result/?q="

    def case_4(self):
        return "https://www.ss.lv/lv/electronics/computers/completing-pc/ram/search-result/?q="
    
    def case_5(self):
        return "https://www.ss.com/lv/electronics/computers/completing-pc/video/search-result/?q="

print("Izvēlies komponentes kategoriju:")
print("1 - CPU")
print("2 - HDD")
print("3 - SSD")
print("4 - RAM")
print("5 - Videokartes")

a = ["CPU", "HDD", "SSD", "RAM", "Videokartes"]

my_switch = ComponentChoose()
try:
    user_choice = int(input("Ievadi komponentes numuru (1-5): "))
    CATEGORY_URL = my_switch.component(user_choice)
    if not CATEGORY_URL:
        print("Kļūda: neatpazīts numurs.")
        exit()
    
    print("Izvēlēta kategorija:", a[user_choice-1])
except ValueError:
    print("Lūdzu ievadi derīgu numuru.")
    exit()

user_keywords = input("Ievadi atslēgvārdus meklēšanai (atdalīt ar komatu): ")

print("Meklēsim pēc atslēgvārdiem:", user_keywords)
CATEGORY_URL = CATEGORY_URL + user_keywords

def product_checker():
    page = requests.get(CATEGORY_URL)
    if page.status_code != 200:
        print ("Error unexpected status", {page.status_code})
        return[]
    
    
    page_content = BeautifulSoup(page.content, "html.parser")
    found_products = page_content.find_all(class_= "msga2-o pp6")
    return found_products

print("Sāk meklēšanu izvēlētajā kategorijā. Jauni sludinājumi tiks pārbaudīti ik pēc 10-30 sekundēm.")

def cleaner(matches):
    ans = []
    c = 0
    if (user_choice == 4): maxi = 6
    elif(user_choice == 5): maxi = 5
    else: maxi = 4
    for i in matches:
        text = list(i.stripped_strings)
        if (c == 0): ans.append("")
        if (len(text) > 1):
            for j in text:
                ans[len(ans)-1] = ans[len(ans)-1] + j + " "
        else:
            for j in text:
                ans[len(ans)-1] = ans[len(ans)-1] + j + " "
        c = c+1
        if (c == maxi): c = 0
    return ans


stop = False
r = random.randint(10,30)

def wait():
    global stop
    while True:
        user_input = input()
        if user_input.strip().lower() == 'stop':
            stop = True
            break

threading.Thread(target=wait, daemon=True).start()

while not stop:
    matches = product_checker()
    matches = cleaner(matches)

    ans = '\n'.join(matches)
    ans1 = MIMEMultipart()
    ans1.attach(MIMEText(ans, 'plain', 'utf-8'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('testovicstest@gmail.com', 'oxcu zlbt rvlq cgqd')
    server.sendmail('testovicstest@gmail.com', 'testovicstest@gmail.com', ans1.as_string())
    time.sleep(r)

server.quit()
