from wsntk.sensor import SensorNode

#create two sensors with different radio configurations
Sensor1 = SensorNode()
Sensor2 = SensorNode(radio = "ESP32-WROOM-32U")

#get current radio configuration
print("Sensor1: tx power =  %s, rx_sensitivity = %s " %(Sensor1.get_txpower(), Sensor1.get_rxsensitivity()))
print("Sensor2: tx power =  %s, rx_sensitivity = %s " %(Sensor2.get_txpower(), Sensor2.get_rxsensitivity()))
