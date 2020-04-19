# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:16:04 2020

@author: hidrissa
"""
import json
from datetime import datetime

import requests

from script.afficherNomGare import afficherNomGareA, afficherNomGareD
from script.coordonneeGare import coordonneeGare

url = "https://api.sncf.com/v1/coverage/sncf/journeys?count=10&"
user = "09d6b8b7-ac2c-4bf7-9985-3d4d8ce028e3"
pwd = ""


def execution(gare_a, gare_d):
    afficherNomGareA(gare_a)
    afficherNomGareD(gare_d)
    return coordonneeGare(gare_a, gare_d)


def listTrajet(gare_a, gare_d):
    listeGare = coordonneeGare(gare_a, gare_d)
    s_from = listeGare['coords']['from']
    s_to = listeGare['coords']['to']

    request_url = "{}from={}&to={}&".format(url, s_from, s_to)
    listes = requests.get(request_url, auth=(user, pwd))

    response = json.loads(listes.text)

    api_format = "%Y%m%dT%H%M%S"
    date_format = "%d/%m/%Y"
    time_format = "%H:%M"
    result = []
    print(request_url)
    if 'journeys' in response:
        for element in response['journeys']:
            depart = datetime.strptime(element['departure_date_time'], api_format)
            arrival = datetime.strptime(element['arrival_date_time'], api_format)

            result.append({
                "depart_date": depart.strftime(date_format),
                "depart_time": depart.strftime(time_format),
                "arrival_time": arrival.strftime(time_format)
            })
    return result
