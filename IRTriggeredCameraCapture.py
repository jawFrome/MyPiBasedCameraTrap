from picamera import PiCamera
import os.path
from time import sleep

from gpiozero import LED
from gpiozero import DigitalInputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

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

count = 0  
while True:
    value = IRSensor.value
    print("Value is ", value)
    if value==1:
        count = count +1
        led.on()
        sleep(1)

        # Take the picture
        nextPicture = storageLocation + 'test' + count + '.jpg'
        camera.rotation = 180
        sleep(5)
        camera.capture(nextPicture)
    
        led.off()
        sleep(1)
    elif value==0:
        sleep(1)
 
