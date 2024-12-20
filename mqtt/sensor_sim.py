import paho.mqtt.client as mqtt
import random
import time

# MQTT Broker configuration
broker = "mqtt.fuvitech.vn"
port = 1883
topic = "phuongle_iot/sensor"

# Callback when the client receives a response from the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

# Create an MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect

# Connect to the broker
client.connect(broker, port, 60)

# Start the loop to process network events
client.loop_start()

try:
    while True:
        # Generate random sensor data
        ampere = random.randint(0, 100)  # Ampere: 0-100 A
        voltage = random.randint(220, 480)  # Voltage: 220-480 V
        error_code = random.randint(0, 4)  # Error Code: 0-4 (0 = no error)
        
        # Create a message
        payload = f"Ampere: {ampere}, Voltage: {voltage}, Error Code: {error_code}"
        
        # Publish the message to the topic
        client.publish(topic, payload)
        print(f"Published: {payload} to topic: {topic}")
        
        time.sleep(5)  # Publish every 5 seconds

except KeyboardInterrupt:
    print("Exiting...")

finally:
    client.loop_stop()
    client.disconnect()
