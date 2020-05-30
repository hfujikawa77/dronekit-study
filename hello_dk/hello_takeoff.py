from dronekit import connect, VehicleMode
import time

vehicle = connect('tcp:127.0.0.1:5763', wait_ready=True)

print('connected')
print(vehicle)

while not vehicle.is_armable:
    print("Waiting for ...")
    time.sleep(1)

print("Arming motors")
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

while not vehicle.armed:
    print("Waiting for ...")
    time.sleep(1)

targetAltitude = 20

print("Takeoff")
vehicle.simple_takeoff(targetAltitude)

while True:
    print("Altitude:", vehicle.location.global_relative_frame.alt)

    if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95:
        print("Reached target altitude")
        break
    time.sleep(1)

vehicle.close