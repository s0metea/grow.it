Fertigation system

API:
You can monitor any aspect of the system with GET request:
http://website/api/1/monitor?sensor=<sensor>
GET request example:
http://website/api/1/monitor?sensor=ph
It will return JSON like this:
{
  "sensor": "ph",
  "state": 6.0,
  "timestamp": 1521172699.513489
}
It is possible to get all sensors at once:
http://website/api/1/monitor/all will return JSON:
{
  "mixer": false,
  "ph": 6.0,
  "timestamp": 1521173862.833971
}

Available sensors:
1) mixer: We use it to mix water. It has 2 states: 0 and 1
2) pump: <Under development>
3) ph: PH control and measurement. Pass 1 to increase PH by 0.1 and 0 to decrease by 0.1
4) tank <Under development>

To control the system you should send POST request:
POST request: http://website/api/1/control
Provide the sensor type and the desirable state:
For example: {sensor: "mixer", state: "0"}
