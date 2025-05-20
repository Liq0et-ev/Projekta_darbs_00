<b><h2>Projekta uzdevums:</h2></b>

Atrast un nosutīt no portāla ss.lv pedējos piedāvājumus par datora komponent, kas tiek izvēlēts no piedāvātā saraksta (cpu,ssd,hdd,ram,video). 

Atrast informāciju par izvelētā komponenta veidu, piemēram -> video -> 3060.

Atsutīt lietotāja pieprasīto informāciju par pēdējiem piedāvājumiem uz tā e-pastu ik pēc 10-30 sekundēm.

<b><h2>Python bibliotēkas un tās nepieciešamība projektā:</h2></b>

<b>import requests</b> - <i>sūta pieprasījumu HTTP lietojot Python</i>.
    Projektā tas tiek izmantots lai: 

        1.Saņemtu saites statusu un parbaudīt vai ar to ir izveidots savienojums

<b>import time </b >- <i>palīdz realizēt laiku</i>, kas ir vajadzīgs lai:
    1.Dot iespeju izvēlēties nejaušu laiku vietnes piekļuvei.

    2.Dot komandu time.sleep, kura palīdz apstāt gmail ziņojumu nosūtīšanu līdz nākošajam ciklam.


<b>from bs4 import BeautifulSoup</b> -</i> saņemt informaciju no saitēm </i>:
    Projektā, tas tiek reālizēts lai:

    1.Sutītu pieprasījumus uz saitēm(CATEGORY_URL), kuras atrodas case1, case2, case3, case4 un case5.

    2.Sūtītu pieprasījumu pēc lietotājā ievadītiem atslegvārdiem(user_words), kas tiek pievienoti izvēlētas saites(CATEGORY_URL) galā.

    3.Analizētu ss.lv lapas HTML strukturu ar "html.parser".

    4.Atrastu visu informāciju par izvelēto produktu meklējot klases ar nosaukumu "msga2-o pp6".

<b>import threading</b> - <i>lai atbalstīt vairāk darbību</i>.
    Izmantošāna kodā:

        1.Dod iespieju pārbaudīt lietotāja tastatūras ievadi ("stop" komandu) darbojoties programmas fonā

        2.Neaptur pārējās programmas darbību kamēr gaida lietotāja ievadi.

<b>import random</b> - <i>izmantots lai nejauši ģenēret skaitli</i>.
    Izmantošāmna koda:
        1. Ģenerē nejaušu skaitli no 10-30, kas tiek izmantots lai "simulētu" lietotāja uzvedību, programmai pārbaudot saiti dotā skaitļa intervālā(sekundēs).

<b>import smtlib</b> -<i> reālizē ziņojumu nosūtīšanu uz e-pastu caur SMTP protokolu</i>.
    Izmatošāna koda:

    1.Izveido savienojumu ar e-pasta SMTP serveri(smtp.gmail.com:587)

    2.Autenficē lietotāju ar gmail konta datiem.

    3.Nosūta e=pastu ar  informciju par atrastiem sludinājumiem.

from email.mime.text <b>import MIMEText</b> and 
from email.mime.multipart <b> import MIMEMultipart</b> - <i> e-pasta ziņojumu formatēšana.</i>
    Izmatošana kodā: 

    MIMEMultipart - izvedo e-pasta zinojumu, kas palīdz tam izskatīties "glītāk".
    MINEText - pievieno teksta daļu e-pastam ar UTF-8 kodējumu.

<b><h2>Projekta definētas datu struktūras</h2></b><br/>
    Projekta darba laikā tiek definētas:.</br>
    1.Klase <b>"ComponentChoose"</b>, kas pilda pārslēgšanas (switch-case) struktūru
    Šī klase uzglabā metodes ar dažādu kategoriju URL saitēm, kas ļauj lietotājam izvēlēties, vienu no piecām komponentēm kuru tas vēlas meklēt(HDD,SSD, RAM, Video kāerti un CPU) </br>
    2.Saraksts <b>"list"</b>, kurā glabajas komponentu nosaukumi.</br>
    3.Funkcija <b>"cleaner"</b>, kas veido strukturētu datu no atrastajiem HTML elemetiem
    4.Funkcija <b>"product_checker"</b>, kas veido savienojumu ar mājaslapu un kas saņem no tās visus nepieciešamos datus
    5.Funkcija <b>"wait"</b>, kas darbojas programmas fonā, uztverot lietotāja tastatūras ievadi, un, apstādinot visas programmas darbību pēc lietotāja ievades

<b><h2>Saite uz video:</h2> <h3><i><a>https://youtu.be/JPYUYuaL6aM</a></i></h3><b>
