#!pip install wikipedia

import wikipedia
import datetime
import smtplib


ADRESATEN_FILE = "To.txt"
DATE_FILE = "Dates.txt"
TAGE_FILE = "Tage.txt"
MY_EMAIL = "wikipediabotus@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(MY_EMAIL, 'wiki1942')
msg = "Hello!"
Adresaten = []
wikipedia.set_lang("DE")
jetzt = datetime.datetime.now()
CurrentDay = jetzt.strftime("%d.%m.%Y")

WochentagEng = {
    "Monday": "Montag",
    "Tuesday": "Dienstag",
    "Wednesday": "Mittwoch",
    "Thursday": "Donnerstag",
    "Friday": "Freitag",
    "Saturday": "Samstag",
    "Sunday": "Sonntag"
}

Wochentag = WochentagEng[jetzt.strftime("%A")]

def GetAdresaten():
    file = open(ADRESATEN_FILE, "r", encoding='utf-8')
    AdresatenOut = []
    for AD in file.readlines():
        AD = AD.rstrip()
        AdresatenOut.append(AD)
    return (AdresatenOut)

def GetWikipediaArticleAndUrl():
    WochentagIn = Wochentag
    while True:
        Seite = []
        site = wikipedia.random(1)
        if (site[0]) == WochentagIn[0]:
            Seite.append(Wochentag + "-Update") #Seite[0]
            Seite.append(site.split("(")[0]) #Seite[1]
            Seite.append("https://de.wikipedia.org/wiki/" + "_".join(site.split(" "))) #Seite[2]
            # Seite.append(wikipedia.summary(site))
            Seite.append("Frohlocket, es ist " + Seite[1] + "-" + Wochentag + "!\n Wikipedia Link: " + Seite[2]) #Seite[3]
            # print(wikipedia.WikipediaPage.images)
            return (Seite)

def PrepareMSG(Seite):
    SUBJECT = Seite[3]
    TEXT = Seite[3]
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    return msg

def SendEmailToList(Adresaten, msg):
    for Adresat in Adresaten:
        server.sendmail(MY_EMAIL, Adresat, msg)
        print("EMail an ", Adresat, "wurde versand")

def DayAlreadyDone():#
    file = open(DATE_FILE, "r", encoding='utf-8')
    print(CurrentDay)
    DayDone = False
    DoneDates = []
    for Date in file.readlines():
        Date = Date.rstrip()
        DoneDates.append(Date)
    for Date in DoneDates:
        if Date == CurrentDay:
            DayDone = True
            break
    if DayDone == False:
        file = open(DATE_FILE, "a+", encoding='utf-8')
        print("DayNotDone")
        file.write("\n" + CurrentDay)
    else:
        print("Day Already Done")
    return DayDone

Adresaten = GetAdresaten()
DayDone = DayAlreadyDone()
 if DayDone == False:
    #WikipediaSeite = GetWikipediaArticleAndUrl()
    #file = open(TAGE_FILE, "a+", encoding='utf-8')
    #WriteText = CurrentDay + " : " + WikipediaSeite[1] + "-" + Wochentag + "\n"
    #file.write(WriteText)
    #msg = PrepareMSG(WikipediaSeite)
    #SendEmailToList(Adresaten, msg)
else:
    print("Dieser Tag wurde bereits bearbeitet. Konsultiere Tage.txt für genauere Informationen bezüglich des Tages")
