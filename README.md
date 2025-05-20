<b><h2>Projekta uzdevums:</h2></b>

Atradit un nosutit no portāla ss.lv pedējos piedavajumus par datora komponent daļu, kura tiek izvlēta no saraksta (cpu,ssd,hdd,ram,video). 

Atrast informaciju par izvelētu komponenta veidu, piemēram -> video -> 3060.

Atsutīt katras 10-30 lietotāja gmail informaciju par pedējiem piedavajumiem, kuri lietotājs bijis prasīts.

<b><h2>Python bibliotekas un tas nepieciešamība projekta:</h2></b>

<b>import requests</b> - <i>suta pieprasījumu HTTP lietojot Python</i>.
    Projekta tas tiek izmantots lai: 

        1.Saņemt lapaspuses statusu un parbaudīt vai tā nav vienāda ar 200

<b>import time </b >- <i>palīdz realizēt laiku</i>, kas ir vajadzīgs lai:
    1.Dot randomu iespeju strādat ar laiku .

    2.Dot komandu time.sleep, kura palīdz apstat gmail zinojumu atsutīšanu lidz jaunam ciklam.


<b>from bs4 import BeautifulSoup</b> -</i> noņemt informaciju no saitem </i>pēc kaut kada klases:
    Projektā, tas tiek reālizēts lai:

    1.Sutīt pieprasījumu izvēlne case1, case2, case3, case4. case5, kur tiek izmantots katram sava saite(CATEGORY_URL).

    2.Nosutīt pieprasījumu jau pēc atslegvārdiem(user_words), kurus pievienojam beigas0 pie izvēlētas saites(CATEGORY_URL) .

    3.Analizē ss.lv lapas HTML strukturu ar "html.parser"'.

    4.Atrast visu informāciju par izvelēto productu izmantojot klasu "msga2-o pp6".

<b>import threading</b> - <i>lai atbalstīt vairāku pavedienu</i>.
    Izmantošāna kodā:

        1.Dod iespieju vienlaicīgi pārbadīt lietotāja ievadi ("stop" komanda)

        2.Neaptur galvenas programmas darbību, kamēr gaida lietotāja ievadi.

<b>import random</b> - <i>izmantots lai nejauši ģenēret skaitli</i>.
    Izmantošāmna koda:
        1. Ģenerē nejaušu skaitli laika intervāla (10-30 sek).random.randint(10,30).Tiek izdarīts lai "simulētu" lietotāja uzvedību.

<b>import smtlib</b> -<i> reālizē zinojumu sūtīšanu uz gamil caur SMTP protokolu</i>.
    Izmatošāna koda:

    1.Izveido savienojumu ar gmail SMTP serveri(smtp.gmail.com:587)

    2.Autenficē lietotāju ar gmail konta datiem.

    3.Nosūta zinojumu pastā ar atrastiem sludinājumiem.

from email.mime.text <b>import MIMEText</b> and 
from email.mime.multipart <b> import MIMEMultipart</b> - <i> e-pasta zinojumu formatēšana.</i>
    Izmatošana kodā: 

    MIMEMultipart - izvedo daudzdalīgu e-pasta zinojumu, kas palīdz tam izskatīties "glītāk".
    MINEText - pievieno teksta daļu e-pastam ar UTF-8 kodējumu.

<b><h2>Projekta definētas datu struktūras</h2></b><br/>
    Projekta darba laikā tiek definētas:.</br>
    1.Klase <b>"ComponentChoose"</b>, kas pilda pārslēgšanas (switch-case) struktūru.
    Tā klase uzglabā metode sar dažādu kategoriju URL saitēm, kas ļauj lietotājam izvēlēties, kādu vienu no piecam komponenti (HDD,SSD, RAM, Video kāerti un CPU) </br>
    2.Saraksts <b>"list"</b>, kurā glabajas komponentu nosaukumi.</br>
    3.Funkcija <b>"cleaner"</b>, kas veido strukturētu datu no atrastajiem HTML  elemetiem 


https://mailtrap.io/blog/python-send-email-gmail/
