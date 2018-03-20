from flask import *
import time

from Ferigator import Fertigator

app = Flask(__name__)

fertigator = Fertigator()

sensors_set = {
        "plant": fertigator.plant.set_strain,
        "plant_ph": fertigator.plant.set_ph,
        "mixer": fertigator.mixer.set_state,
        "tank_pump_in": fertigator.main_container_pump_in.set_state,
        "tank_pump_out": fertigator.main_container_pump_out.set_state,
        "water_pump": fertigator.water_pump.set_state,
        "acid_pump": fertigator.acid_pump.set_state,
        "alkali_pump": fertigator.alkali_pump.set_state,
        "fertilizer_pump": fertigator.fertilizer_pump.set_state,
        "fertigator_state": fertigator.get_state,
    }

sensors_get = {
        "plant": fertigator.plant.get_strain,
        "plant_ph": fertigator.plant.get_ph,
        "mixer": fertigator.mixer.get_state,
        "ph": fertigator.ph.get_state,
        "water_level": fertigator.water_level.get_state,
        "tank_pump_in": fertigator.main_container_pump_in.get_state,
        "tank_pump_out": fertigator.main_container_pump_out.get_state,
        "water_pump": fertigator.water_pump.get_state,
        "acid_pump": fertigator.acid_pump.get_state,
        "alkali_pump": fertigator.alkali_pump.get_state,
        "fertilizer_pump": fertigator.fertilizer_pump.get_state,
        "fertigator_state": fertigator.set_state,

}

# Index route
@app.route("/")
def index():
    return render_template('index.html', mixer_state=fertigator.mixer.get_state(), ph_level=fertigator.plant.get_ph())

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
    return jsonify(
        timestamp=time.time(),
        plant=fertigator.plant.get_strain(),
        plant_ph=fertigator.plant.get_ph(),
        mixer=fertigator.mixer.get_state(),
        water=fertigator.water_pump.get_level(),
        alkali=fertigator.alkali_pump.get_level(),
        acid=fertigator.acid_pump.get_level(),
        fertilizer=fertigator.fertilizer_pump.get_level(),
        tank_pump_in=fertigator.main_container_pump_in.get_state,
        tank_pump_out=fertigator.main_container_pump_out.get_state,
        ph=fertigator.ph.get_state(),
    )


# Change value by POST request.
@app.route("/api/1/control", methods=['POST'])
def control():
    # Get the data:
    sensor = request.form['sensor']
    state = request.form['state']
    sensors_set[sensor](state)
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
