from flask import render_template
from flask import Flask as _Flask, jsonify
from gevent import pywsgi
from flask.json import JSONEncoder as _JSONEncoder
import decimal
import utils


class JSONEncoder(_JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                return float(o)
            super(_JSONEncoder, self).default(o)

class Flask(_Flask):
    json_encoder = JSONEncoder

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/time')
def get_time():
    return utils.get_time()

@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})

@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        res.append({"name":tup[0], "value":int(tup[1])})
    return jsonify({"data":res})

@app.route('/l1')
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

@app.route('/l2')
def get_l2_data():
    data = utils.get_l2_data()
    day,confirm_add,suspect_add = [],[],[]
    for a,b,c in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day":day,"confirm_add":confirm_add,"suspect_add":suspect_add})

@app.route('/r1')
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for j,k,v in data:
        city.append(j+"("+k+")")
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})

@app.route('/r2')
def get_r2_data():
    res = []
    for tup in utils.get_r2_data():
        res.append({"name":tup[0], "value":int(tup[1]) })
    return jsonify({"data":res})


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()

