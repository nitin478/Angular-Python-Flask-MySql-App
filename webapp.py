import json
from flask import Flask,request, send_from_directory
import model
import random

app = Flask(__name__, static_url_path='')

def AsDict(guest):
  return {'id': guest.id, 'first': guest.first, 'last': guest.last}





@app.route('/')
def index():
    return send_from_directory('app', 'index.html')


@app.route('/js/<path:path>')
def send_js(path):
    print path
    return send_from_directory('app/js', path)


@app.route('/partials/<path:path>')
def send_partials(path):
    print path
    return send_from_directory('app/partials', path)


@app.route('/css/<path:path>')
def send_css(path):
    print path
    return send_from_directory('app/css', path)


@app.route('/rest/query')
def get_all():
    print '111'
    guests = model.AllGuests()
    print '2222'
    r = [ AsDict(guest) for guest in guests ]
    return json.dumps(r)



@app.route('/rest/update', methods=['POST'])
def update():
    r = json.loads(request.get_data())
    guest = model.UpdateGuest(r['id'], r['first'], r['last'])
    r = AsDict(guest)
    return json.dumps(r)



@app.route('/rest/insert', methods=['POST'])
def insert():
    r = json.loads(request.get_data())
    rand = random.randint(10000, 9999999)
    guest = model.InsertGuest(rand, r['first'], r['last'])
    r = AsDict(guest)
    return json.dumps(r)

@app.route('/rest/delete', methods=['POST'])
def delete():
    r = json.loads(request.get_data())
    model.DeleteGuest(r['id'])
    return json.dumps(r)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
