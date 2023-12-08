from sds011lib import SDS011QueryReader
from serial import Serial
import time

# Setup a query-mode reader on /dev/ttyUSB0
sensor = SDS011QueryReader('/dev/ttyUSB0') # TODO this might be some other usb dev
# Wake it back up
sensor.wake()

# Read some data!
while 1:
    aqi = sensor.query()
    print('2.5:', aqi.pm25)
    print('10 :', aqi.pm10)
    # put it in a db
    time.sleep(15)

# Put the device to sleep
#sensor.sleep()

