# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os
from toolsEvent import *

import datetime

def nextEvent():
    "Fonction qui retourne les 10 prochains événements" 
    reply = ""
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        reply += u"vous n'avez aucun événements de prévus.\n"
    elif len(events) == 1:
        reply += "Votre avez 1 événement de prévu :\n"
    else:      
        reply += 'Vos ' + str(len(events)) + u" prochains événements sont :\n"
        
    for event in events:
        debut= event['start'].get('dateTime')

        # Formatage de la date
        if debut[8:10] == now[8:10] :
            date = "Aujourd'hui"
        elif int(debut[8:10])-1 == int(now[8:10]) :
            date = "Demain"
        else :
            date = "Le " + debut[8:10] + " " + get_strMonth(debut[5:7]) + " " + debut[0:4]
            
        # Formatage de l'heure
        heure = debut[11:13] + " heure"
        if debut[14:16] != "00" :
            heure = heure + " " + debut[14:16]

        
        fin = event['end'].get('dateTime')
        summary = event['summary']
        location = event['location']
        description = event['description']

        reply += date + u" à " + heure + ", " + summary + ".\n"
        
    
    file = open(EVENT_PATH, "w")
    file.write(reply.encode("utf-8"))
    file.close()



nextEvent()