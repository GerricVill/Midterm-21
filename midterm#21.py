from flask import Flask, jsonify, request
app = Flask(__name__)
heartinfo = [
    {
        "heart_id" : "2012703",
        "date" : ["November 29, 2023"],
        "heart_rate" : ["70/120"]
    }
]
@app.route('/Heart', methods=['Get'])
def getHeart():
    return jsonify(heartinfo)

@app.route('/Heart', methods=['Post'])
def addHeart():
    heartadd = request.get_json()
    heartinfo.append(heartinfo)
    return{'id': len(heartinfo)},200

@app.route('/Heart/<int:index>', methods=['Delete'])
def deleteHeart():
    heartinfo.pop(index)
    return 'Deleted',200

if __name__ == '__main__':
    app.run()