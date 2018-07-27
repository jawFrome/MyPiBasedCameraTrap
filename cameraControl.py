import datetime
import os.path
import sqlite3
from os import mkdir
from picamera import PiCamera
from time import sleep

# Check Storage Location
storageLocation = '/home/pi/CameraCaptures/'
if os.path.exists(storageLocation) != True:
    mkdir(storageLocation)

# Check Database
databaseName = 'CapturedImages.db'

try:    
    database = sqlite3.connect(storageLocation + databaseName)
    cursor = database.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      images(id INTEGER PRIMARY KEY, CaptureTime DATETIME, filePath TEXT)''') 

    database.commit()
    
    # Instantiate a camera instance
    nextPicture = storageLocation + 'test.jpg'
    camera = PiCamera()
    camera.rotation = 180
    sleep(5)
    camera.capture(nextPicture)

    #Reference it in the database
    cursor.execute('''INSERT INTO images(CaptureTime, filePath)
                    VALUES(?,?)''', (datetime.datetime.now(), nextPicture))
    database.commit()

    # Display how many captures we have
    count = cursor.execute('SELECT Count(id) FROM images').fetchone()[0]
    print('We have {0} images', count)    
    
except Exception as e:
    database.rollback()
    raise e
finally:
    database.close()
