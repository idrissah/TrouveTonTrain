import json

import requests

url = "https://api.sncf.com/v1/coverage/sncf/places?q="
user = "09d6b8b7-ac2c-4bf7-9985-3d4d8ce028e3"
pwd = ""


def coordonneeGare(gareD, gareA):
    # URl pour demander les coordonées de la gare de départ
    responseD = requests.get("https://api.sncf.com/v1/coverage/sncf/places?q=" + gareD, auth=(user, pwd))
    response_d = json.loads(responseD.text)
    coordGareD = []
    # Ajouter dans le tableau les coordonées récupérer pour la gare de départ

    for element in response_d['places']:
        type = element['embedded_type']
        if type == "stop_area":
            coord = element['stop_area']['coord']
            lat = coord['lat']
            lon = coord['lon']
            coordGareD.append(lat)
            coordGareD.append(lon)

    # URl pour demander les coordonées de la gare de arrivé
    responseA = requests.get("https://api.sncf.com/v1/coverage/sncf/places?q=" + gareA, auth=(user, pwd))
    response_a = json.loads(responseA.text)
    coordGareA = []

    # Ajouter dans le tableau les coordonées récupérer la gare d'Arrivé
    for element in response_a['places']:
        type = element['embedded_type']
        if type == "stop_area":
            coordinate = element['stop_area']['coord']
            lat = coordinate['lat']
            lon = coordinate['lon']
            coordGareA.append(lat)
            coordGareA.append(lon)
    # return coordGareA

    # Pour afficher les coordonée de la gare de départ
    # Par exemple pour la gare de grenoble latitude est de : 45.1667 et longitude est de 5.167
    # Les coordonnées récupérer sont de la gare principale

    print(coordGareA)
    print(coordGareD)
    distance = requests.get(
        "https://fast3t.azurewebsites.net/TD2_ETRS804_war_exploded/Billing?latitude1=" + coordGareA[0] + "&longitude1=" + coordGareA[1] + "&latitude2=" + coordGareD[0] + "&longitude2=" + coordGareD[1])
    # Exemple de l'url http://localhost:8080/TD2_ETRS804_war_exploded/Billing?latitude1=5.714584&longitude1=45.191493&latitude2=2.275149&longitude2=48.85645
    print(distance.text)
    dis = distance.text.rstrip()
    # floDis = float(dis)
    # print(floDis)

    return {
        "coords": {
            "from": "{};{}".format(coordGareA[1], coordGareA[0]),
            "to": "{};{}".format(coordGareD[1], coordGareD[0])
        },
        "distance": dis
    }
