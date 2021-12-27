from __future__ import print_function
import wikipedia
import datetime
import smtplib
from tsg import tagenerator_edit_channel
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import random


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("wikipediabotus@gmail.com", "wiki1942")
wikipedia.set_lang("DE")
jetzt = datetime.datetime.now()
jetztNumeric = jetzt.strftime("%d.%m.%Y")
jetztTag = { "Monday": "Montag", "Tuesday": "Dienstag", "Wednesday": "Mittwoch", "Thursday": "Donnerstag", "Friday": "Freitag", "Saturday": "Samstag", "Sunday": "Sonntag"}[jetzt.strftime("%A")]
specialDays = {
    "24.12" : "Lukas Geburtstag / Weihnachten",
    "21.04" : "Ostern",
    "31.12" : "Sylvester",
    "13.10" : "Geburtstag des Tagenerators",
    "07.01" : "Pождество",
    '13.11' : "Anns Geburtstag",
    '20.08' : "Breinich BDay",
    '16.09' : 'Markus Geburtstag',
    '24.07' : 'Tim Rohrbach Tag',
    '09.06' : "Europatag",
    '22.07' : 'Matthias Mondtag',
    '02.12' : 'Andreas-Tag',
    '11.09' : 'Alex-Tag und anderes',
    '31.10' : 'Halloween',
    '01.11' : 'nichtiger Nusskonsum November',
    '01.03' : 'Tim Tag',
    '21.11' : 'Tag des Davids',
    '01.12' : 'erster Advent',
    '26.01' : 'Feier für Fisel Fest',
    '27.01' : 'Moritz-Tag',
    '08.04' : 'Mamas Geburtstag',
    '24.07' : 'Wahrscheinlich Tims-Geburtstag Tag',
    '30.08' : 'Reise zum Mittelpunkt Hamburgs',
    '27.09' : 'Golf II-Tag' ,
    '01.01' : 'Neues Jahr Tag'
}

def SpecialDayCheck():
    jetztTag = "None"
    print(jetztNumeric)
    if jetztNumeric[0:-5] in specialDays.keys():
        print("Special Day Found!" + jetztNumeric + " is " + specialDays[jetztNumeric[0:-5]] + "!")
        jetztTag = specialDays[jetztNumeric[0:-5]]
    file = open("To.txt", "r", encoding="utf-8")
    for line in file.readlines():
        if line.split(";")[1] == jetztNumeric:
            print("Es ist " + line.split(";")[2] + "s Geburtstag!")
            jetztTag = line.split(";")[2] + "s Geburtstag"
            break
    return jetztTag

def DayDoneCheck():
    file = open("Tage.txt", "r", encoding="utf-8")
    for Day in file.readlines():
        if jetztNumeric == Day.split(" : ")[0]:
            print("Day Already Done!")
            return(True)
    print("Day Not Done")
    return(False)

def WikipediaArcticle():
    Seite = []
    while True:
        site = wikipedia.random(1)
        if (site[0] == jetztTag[0].upper()):
            Seite.append(site.split("(")[0]) #[0]
            Seite.append("https://de.wikipedia.org/wiki/" + "_".join(site.split(" "))) #[1]
            Seite.append(site) #[2]
            return(Seite)

def SendEmailsToAdresssssaten(Seite):
    SUBJECT = "Der heutige Tag ist " + Seite[0].rstrip() + "-" + jetztTag
    TEXT = "Seiet begeistert, denn es handelt sich bei dem Tag der Heute ist um den " + Seite[0].rstrip() + "-" + jetztTag +"!\n Recherchiere mehr darueber auf der Wikipedia Seite: " + Seite[1]
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    print(msg)
    file = open("To.txt","r", encoding="utf-8")
    for AD in file.readlines():
        send_mail(AD.split(";")[0].rstrip(), AD.split(";")[-1].rstrip(), SUBJECT, TEXT)
        print("Email an " + AD.split(";")[0].rstrip() + " wurde versandt")

def send_mail(to, name,  subject, text):
   msg = MIMEMultipart()
   msg['From'] = "Wikipedia Bot"
   msg['To'] = name
   msg['Date'] = formatdate(localtime=True)
   msg['Subject'] = subject
   msg.attach(MIMEText(text, _charset='utf-8'))
   server.sendmail("wikipediabotus@gmail.com", to, msg.as_string())

def ts3channelset(Seite):
    tagenerator_edit_channel(Seite[0].rstrip() + "-" + jetztTag)

if(DayDoneCheck()==False):
    SpezialTag = SpecialDayCheck()
    if (SpezialTag != "None"):  #verändert den Wochentag auf z.b. Weihnachten
        jetztTag = SpezialTag
    print(jetztTag)
    HeutigeSeite = WikipediaArcticle()
    print(HeutigeSeite)
    ts3channelset(HeutigeSeite)
    SendEmailsToAdresssssaten(HeutigeSeite)
    file = open("Tage.txt", "a+", encoding="utf-8")
    file.write("\n" + jetztNumeric + " : " + HeutigeSeite[2] + "-" + jetztTag)
