# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os

from toolsEvent import *
import datetime


def todayEvent():
    "Fonction de recherche des événement du jour"
    reply = ""

    # Parametrage de l'aplication
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId=CALENDAR_ID, timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    # Récupération des événements
    i = 0
    evenements = ""
    for event in events:
        date = ""
        debut= event['start'].get('dateTime')
        if debut == None :
            debut = event['start'].get('date')
                
            # Formatage de la date
            if int(debut[8:10]) == int(now[8:10]) :
                i += 1
                date = "Aujourd'hui "
                heure = ""
                
        else :
            # Formatage de la date
            if debut[0:10] == now[0:10] :
                i += 1
                date = "Aujourd'hui "
                # Formatage de l'heure
                heure = u"à " + debut[11:13] + " heure"
                if debut[14:16] != "00" :
                    heure = heure + " " + debut[14:16]

        try :
            summary = event['summary']
        except :
            summary = "Sans titre"

        try :
            location = event['location']
        except :
            location = "Aucun lieu défini"

        try :
            description = event['description']
        except :
            description = "Pas de description"

        if date == "Aujourd'hui " :
            evenements += date + heure + u", vous avez l'événement : " + summary + ".\n"
            date = ""
            
    if i ==  0:
        reply += u"Aucun événements de prévus pour aujourd'hui.\n"
    elif i == 1 :
        reply += u"Vous avez 1 événement prévus aujourd'hui\n" + evenements
    else :
        reply += "Vous avez " + str(i) + u" événements de prévus aujourd'hui\n" + evenements
        
    fichier = open(EVENT_PATH, "w")
    fichier.write(reply.encode("utf-8"))
    fichier.close


todayEvent()
