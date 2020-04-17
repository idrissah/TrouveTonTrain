# Récupérer la liste des gares d'une ville
# Gare de départ
import json, requests
from http.cookiejar import request_host

url = "https://api.sncf.com/v1/coverage/sncf/places?q="
user = "09d6b8b7-ac2c-4bf7-9985-3d4d8ce028e3"
pwd = ""
PARAMS = {user, pwd}


def afficherNomGareD(gareD):
    # listeD = requests.get("https://data.sncf.com/api/records/1.0/search/?dataset=liste-des-gares&q=" + gareD)
    listeD = requests.get("https://api.sncf.com/v1/coverage/sncf/places?q=" + gareD, auth=(user, pwd))
    response_ld = json.loads(listeD.text)
    listeNomGD = []
    print(response_ld)
    for element in response_ld['places']:
        type = element['embedded_type']
        if type == "stop_area":
            listeNomGD.append(element['name'])
    return listeNomGD


def afficherNomGareA(gareA):
    listeA = requests.get("https://api.sncf.com/v1/coverage/sncf/places?q=" + gareA, auth=(user, pwd))
    response_la = json.loads(listeA.text)
    listeNomGA = []
    # print(response_ld)
    for element in response_la['places']:
        type = element['embedded_type']
        if type == "stop_area":
            listeNomGA.append(element['name'])
    return listeNomGA
