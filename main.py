from flask import *
import time
from Mixer import Mixer
from Tank import Tank
from PHMeter import PHMeter

app = Flask(__name__)

mixer = Mixer()
ph = PHMeter()
water = Tank()
acid = Tank()

sensors_set = {
        "mixer": mixer.set_state,
        "tank": 1,
        "ph": ph.change,
    }

sensors_get = {
        "mixer": mixer.get_state,
        "tank": 1,
        "ph": ph.get_state,
    }

states = {
        "1": 1,
        "0": 0
    }

# Index route
@app.route("/")
def index():
    return render_template('index.html', mixer_state=mixer.get_state(), ph_level=ph.get_state())

# Get response handle:
@app.route("/api/1/monitor", methods=['GET'])
def monitor():
    sensor = request.args.get('sensor', None)
    return jsonify(
        timestamp=time.time(),
        sensor=sensor,
        state=sensors_get[sensor]()
    )

# Get response handle:
@app.route("/api/1/monitor/all", methods=['GET'])
def monitor_all():
    sensors = {
      "mixer": mixer.get_state,
      "tank": 1,
      "ph": ph.get_state,
    }
    return jsonify(
        timestamp=time.time(),
        mixer=mixer.get_state(),
        ph=ph.get_state(),
    )

# Change value by POST request.
@app.route("/api/1/control", methods=['POST'])
def control():
    # Get the data:
    sensor = request.form['sensor']
    state = request.form['state']
    sensors_set[sensor](states[state])
    new_value = sensors_get[sensor]()
    return jsonify({'success': True, 'sensor': sensor, 'state': new_value}), 200, {'ContentType': 'application/json'}

# About route
@app.route("/about")
def about():
    # Render the about.html template
    return render_template('about.html')

# Index route
@app.route("/statistic")
def statistic():
    return jsonify({'Text': "Not ready yet"}), 200, {'ContentType': 'application/json'}

# Index route
@app.route("/secret")
def secret():
    return jsonify({'Text': "Go away! Nothing to do here."}), 200, {'ContentType': 'application/json'}


# Starts the app listening to port 5000 with debug mode
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
