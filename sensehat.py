from sense_hat import SenseHat  
import time  
import sys  
from ISStreamer.Streamer import Streamer  
  
# --------- User Settings ---------
CITY = "Elst"
BUCKET_NAME = ":partly_sunny: " + CITY + " Weather"
BUCKET_KEY = "sensehat"
ACCESS_KEY = "Your_Access_Key"
SENSOR_LOCATION_NAME = "Office"
MINUTES_BETWEEN_SENSEHAT_READS = 0.1
# ---------------------------------

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
  
sense = SenseHat()  
  
while True:
  # Read the sensors
  temp = sense.get_temperature()
  humidity = sense.get_humidity() 
  pressure = sense.get_pressure() 

  # Format the data
  temp = float("{0:.2f}".format(temp))
  humidity = float("{0:.2f}".format(humidity))
  pressure = float("{0:.2f}".format(pressure))

  # Print and stream 
  print SENSOR_LOCATION_NAME + " Temperature: " + str(temp)
  print SENSOR_LOCATION_NAME + " Humidity(%): " + str(humidity)
  print SENSOR_LOCATION_NAME + " Pressure: " + str(pressure)
  streamer.log(":sunny: " + SENSOR_LOCATION_NAME + " Temperature", temp)
  streamer.log(":sweat_drops: " + SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
  streamer.log(":cloud: " + SENSOR_LOCATION_NAME + " Pressure", pressure)

  streamer.flush()
  time.sleep(60*MINUTES_BETWEEN_SENSEHAT_READS)
