import paho.mqtt.client as mqtt

# MQTT Broker configuration
broker = "mqtt.fuvitech.vn"
port = 1883
topic = "phuongle_iot/sensor"

# Callback when the client receives a message
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the message callback
client.on_message = on_message

# Connect to the broker
client.connect(broker, port, 60)

# Subscribe to the topic
client.subscribe(topic)

# Start the loop to process network events
client.loop_start()

try:
    print("Waiting for messages...")
    while True:
        pass  # Keep the script running

except KeyboardInterrupt:
    print("Exiting...")

finally:
    client.loop_stop()
    client.disconnect()
