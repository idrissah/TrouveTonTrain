from flask import Flask, render_template, request

from script import response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/response', methods=['GET'])
def exec():
    gareA = request.args.get('gareA')
    gareD = request.args.get('gareD')

    dist = response.execution(gareA, gareD)
    stop_arrays = response.listTrajet(gareA, gareD)

    location = {
        "start": gareD,
        "end": gareA
    }

    price = round(float(dist['distance']) * 0.25, 2)
    print(gareD)
    print(dist)
    print(stop_arrays)
    return render_template('trajet.html', stop_arrays=stop_arrays, location=location, price=price), 200


@app.route('/afficheRouteA', methods=['GET'])
def afficheRouteA():
    respGares = {"success": "true", "results": []}
    # gare_depart = request.json_module
    gareA = request.args.get('gareA')
    gares = response.afficherNomGareA(gareA)
    for gare in gares:
        respGares["results"].append({"name": gare, "value": gare})

    print("=== Liste des gares ===")
    print(respGares)

    return respGares, 200


@app.route('/afficheRouteD', methods=['GET'])
def afficheRouteD():
    respGares = {"success": "true", "results": []}
    gareD = request.args.get('gareD')
    gares = response.afficherNomGareD(gareD)
    for gare in gares:
        respGares["results"].append({"name": gare, "value": gare})

    print("=== Liste des gares ===")
    print(respGares)

    return respGares, 200


@app.route('/test')
def test():
    return render_template('demo/three.html'), 200
