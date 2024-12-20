from pyModbusTCP.client import ModbusClient
import time

# Configuration
server_ip = "127.0.0.1"  # Change to your server's IP address
port = 10000              # Port number used by the server
slave_id = 1              # Slave ID

# Create a Modbus client
modbus_client = ModbusClient(host=server_ip, port=port, unit_id=slave_id)

def read_data():
    # Connect to the Modbus server
    if modbus_client.open():
        print("Connected to Modbus server.")
        
        try:
            # Read holding registers for Ampere, Voltage, and Error Code
            registers = modbus_client.read_holding_registers(40001, 3)  # Read 3 registers starting at 40001
            
            if registers:
                ampere, voltage, error_code = registers
                if error_code == 0:
                    error_code = "No Error"
                else:
                    error_code = f"Device Error"
                print(f"Ampere: {ampere} A, Voltage: {voltage} V, Error: {error_code}")
            else:
                print("Failed to read registers.")

        finally:
            # Close the connection
            modbus_client.close()
            print("Disconnected from Modbus server.")
    else:
        print("Unable to connect to Modbus server.")

if __name__ == "__main__":
    while True:
        read_data()
        time.sleep(10)  # Wait for 5 seconds before the next read
