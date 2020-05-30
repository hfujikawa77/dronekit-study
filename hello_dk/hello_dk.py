from dronekit import connect, VehicleMode

vehicle = connect('tcp:127.0.0.1:5763', wait_ready=True)

print('connected')
print(vehicle)
# print(vehicle.mode)
# print(vehicle.arm)
# print(vehicle.battery)
# print(vehicle.parameters.values)

for key, value in vehicle.parameters.items:
    print(kye+"="+value)

# GUIDEDモードを設定
vehicle.mode = VehicleMode("GUIDED")

# Arming
# vehicle.armed = False

def location_callback(self, attr, val):
    print(attr)
    print(val)

vehicle.add_attribute_listener('location.grobal_frame', location_callback)
# time.sleep(10)

vehicle.remove_attribute_listener('location.grobal_frame', location_callback)

vehicle.close()
