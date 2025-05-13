import requests
import time
import os
import json
from bs4 import BeautifulSoup
import random
from datetime import datetime
SEEN_FILE = "seen_ads.json"

class ComponentChoose:
    def day(self, component_number):
        default = None
        return getattr(self, f'case_{component_number}', lambda: default)()

    def case_1(self):
        return "https://www.ss.lv/ru/electronics/computers/completing-pc/cpu/"

    def case_2(self):
        return "https://www.ss.lv/ru/electronics/computers/completing-pc/hdd/"

    def case_3(self):
        return "https://www.ss.lv/ru/electronics/computers/completing-pc/hdd/"

    def case_4(self):
        return "https://www.ss.lv/ru/electronics/computers/completing-pc/ram/"
    
    def case_5(self):
        return "https://www.ss.lv/ru/electronics/computers/completing-pc/video/"
    
    def case_6(self):
        return "https://www.ss.lv/ru/electronics/computers/completing-pc/network-cards/"

print("Izvēlies komponentes kategoriju:")
print("1 - CPU")
print("2 - HDD")
print("3 - SSD")
print("4 - RAM")
print("5 - Videokartes")
print("6 - Tīkla kartes")

my_switch = ComponentChoose()
try:
    user_choice = int(input("Ievadi komponentes numuru (1-6): "))
    CATEGORY_URL = my_switch.day(user_choice)
    if not CATEGORY_URL:
        print("Kļūda: neatpazīts numurs.")
        exit()
    print("Izvēlēta saite:", CATEGORY_URL)
except ValueError:
    print("Lūdzu ievadi derīgu numuru.")
    exit()

user_keywords = input("Ievadi atslēgvārdus meklēšanai (atdalīt ar komatu): ")
KEYWORDS = [kw.strip().lower() for kw in user_keywords.split(",") if kw.strip()]

if not KEYWORDS:
    print("Nav ievadīts neviens atslēgvārds. Programma beidzas.")
    exit()

print("Meklēsim pēc atslēgvārdiem:", KEYWORDS)

if os.path.exists(SEEN_FILE):
    with open(SEEN_FILE, "r") as f:
        seen_ads = set(json.load(f))
else:
    seen_ads = set()

def fetch_ads():
    resp = requests.get(CATEGORY_URL, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    rows = soup.select("table.list tr[id]")

    new_matches = []

    for row in rows:
        ad_id = row.get("id")
        if ad_id in seen_ads:
            continue
        seen_ads.add(ad_id)

        title_cell = row.select_one("td.msg2")
        if not title_cell:
            continue

        title_text = title_cell.get_text(strip=True).lower()
        if any(kw in title_text for kw in KEYWORDS):
            link = "https://www.ss.lv" + title_cell.find("a")["href"]
            new_matches.append((title_text, link))

    return new_matches

def save_seen():
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen_ads), f)

print("Sāk meklēšanu izvēlētajā kategorijā. Jauni sludinājumi tiks pārbaudīti ik pēc 14-54 sekundēm.")

while True:
    try:
        matches = fetch_ads()
        if matches:
            for title, link in matches:
                if link == matches:
                    current_time = datetime.now()
                    file1 = open("New_offers.txt","w")
                    L = ["Jauns sludinājums:"]
                    file1.write(L)
                    file1.write(title)
                    file1.write(link)
                    file1.write(current_time)
                    print("\nJauns sludinājums:")
                    print(title)
                    print(link)
                    print(current_time)
                
                save_seen()
        else:
            print("Jaunu sludinājumu nav.")
            time_sleep = random.randint(15,54)
        time.sleep(time_sleep)
        
        print(current_time)
    except Exception as e:
        print("Kļūda:", e)
        time.sleep(60)
        
