from flask import Flask, jsonify

app = Flask(__name__)

samples = { "39dcda76-a9f9-11e9-b1a9-12009e28c71e" : 0.1, "49ac0c60-a9f9-11e9-b1a9-12009e28c71e" : 0.2 }

@app.route("/samples", methods=["GET"])
def getSamples():
    return jsonify(samples)


@app.route("/samples/<id>", methods=["GET"])
def getScore(id):
    return jsonify (samples[id])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
