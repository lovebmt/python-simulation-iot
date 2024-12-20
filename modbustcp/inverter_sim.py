#!/bin/python

from pyModbusTCP.server import ModbusServer, DeviceIdentification
from time import sleep
from random import uniform
import threading

class SimpleModbusServer(threading.Thread):
    def __init__(self, host, port, slave_id):
        super().__init__()
        self.server = ModbusServer(host, port, no_block=True,
                                   device_id=DeviceIdentification(objects_id=slave_id))
        # Initialize registers: Ampere, Voltage, Error Code
        self.server.data_bank.set_holding_registers(40001, [0, 0, 0])  # [Ampere, Voltage, Error Code]

    def run(self):
        print(f"Server for Slave {self.server.device_id} starting...")
        self.server.start()
        print("Server is online.")
        
        while True:
            # Generate random values for Ampere, Voltage, and Error Code
            ampere = int(uniform(0, 100))  # Ampere: 0-100 A
            voltage = int(uniform(220, 480))  # Voltage: 220-480 V
            error_code = int(uniform(0, 5))  # Error Code: 0-4 (0 = no error)

            # Update the registers
            self.server.data_bank.set_holding_registers(40001, [ampere, voltage, error_code])
            print(f"Updated Registers - Ampere: {ampere}, Voltage: {voltage}, Error Code: {error_code}")
            
            sleep(10)

    def stop(self):
        print(f"Shutting down server for Slave {self.server.device_id}...")
        self.server.stop()
        print("Server is offline.")

# Create and start a single server instance
server = SimpleModbusServer("127.0.0.1", 10000, 1)

try:
    server.start()
    while True:
        sleep(1)

except KeyboardInterrupt:
    server.stop()
    print("Server is offline.")
