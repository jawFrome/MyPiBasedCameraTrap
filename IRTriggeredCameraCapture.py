import datetime
from picamera import PiCamera
import os.path
from time import sleep

from gpiozero import LED
from gpiozero import DigitalInputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

import sqlite3

# Only need remotely
#factory = PiGPIOFactory(host='192.168.1.87')
#led = LED(24, pin_factory=factory)
#IRSensor = DigitalInputDevice(17, pin_factory=factory)

led = LED(24)
IRSensor = DigitalInputDevice(17)
camera = PiCamera()

# Check Storage Location
storageLocation = '/home/pi/CameraCaptures/'
if os.path.exists(storageLocation) != True:
    mkdir(storageLocation)

# Check Database
databaseName = 'CapturedImages.db'
database = sqlite3.connect(storageLocation + databaseName)
cursor = database.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
                      images(id INTEGER PRIMARY KEY, CaptureTime DATETIME, filePath TEXT)''') 
database.commit()

while True:
    value = IRSensor.value
    print("Value is ", value)
    if value==1:
        led.on()
        sleep(1)

        # Take the picture
        captureTime = datetime.datetime.now()
        nextPicture = storageLocation + 'Capture' + captureTime.strftime("%m%d%Y%H%M%S") + '.jpg'
        camera.rotation = 180
        camera.capture(nextPicture)

        #Reference it in the database
        cursor.execute('''INSERT INTO images(CaptureTime, filePath) VALUES(?,?)''', (captureTime, nextPicture))
        database.commit()

        # Display how many captures we have
        count = cursor.execute('SELECT Count(id) FROM images').fetchone()[0]
        print('We have ' + str(count) + ' images')
    
        led.off()
        sleep(1)
    elif value==0:
        sleep(1)
 
