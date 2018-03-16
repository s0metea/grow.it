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


# Index route
@app.route("/")
def index():
    # Read the value of the sensor
    # value = raspi.read_sensor()
    # Render the index.html template passing the value of the sensor
    return render_template('index.html', mixer_state=mixer.get_state(), ph_level=ph.get_state())

# Get response handle:
@app.route("/api/1/monitor", methods=['GET'])
def monitor():
    sensor = request.args.get('sensor', None)
    sensors = {
      "mixer": mixer.get_state,
      "tank": 1,
      "ph": ph.get_state,
    }
    return jsonify(
        timestamp=time.time(),
        sensor=sensor,
        state=sensors[sensor]()
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
    # Get the parameters:
    sensor = request.form['sensor']
    state = request.form['state']
    states = {
        "1": 1,
        "0": 0
    }
    sensors = {
        "mixer": mixer.set_state,
        "tank": 1,
        "ph": ph.change,
    }
    sensors[sensor](states[state])
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# About route
@app.route("/about")
def about():
    # Render the about.html template
    return render_template('about.html')

# Starts the app listening to port 5000 with debug mode
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
