import sqlite3
import os.path



def main():
    try:
        # Check Storage Location
        storageLocation = '/home/pi/CameraCaptures/'
        if os.path.exists(storageLocation) != True:
            raise

        # Check Database
        databaseName = 'CapturedImages.db'
        database = sqlite3.connect(storageLocation + databaseName)
        cursor = database.cursor()
        cursor.execute('''Select * From Images''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
    except Exception as e:
        database.rollback()
        print(e)
        raise e
    finally:
        database.close()

#start process here
if __name__ == '__main__':
    main()
