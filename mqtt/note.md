pip install paho-mqtt==1.6.1


# 1 device
python server.py
python sensor_sim.py

# 2 device
create second file
sensor_sim2.py
Edit:
topic = "phuongle_iot/sensor2" 
Run:
python sensor_sim.py
python sensor_sim2.py
