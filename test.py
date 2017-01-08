
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

from picontrol import PiControl


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/picontrol/drawer/open/<string:device_path>')
def drawer_opener(device_path):
    drawer = PiControl(device=device_path.replace("_","/"))
    return str(drawer.open_drawer())

@app.route('/picontrol/door/open/<int:pin>/<int:duration>')
def door_opener(pin, duration_secs):
    door = PiControlx()
    door.GPIO_pin=pin
    door.open_door(duration=int(duration_secs))
    return "Requesting door opening on {} during {}".format(str(pin), str(duration))

if __name__ == "__main__":
    app.run(debug=True)
