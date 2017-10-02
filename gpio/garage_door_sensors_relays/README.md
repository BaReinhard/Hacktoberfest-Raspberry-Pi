The door open/close state is determined through the use of the magnetic reed sensors.

The sensors being used with this project are the GE 2315 series.
These get connected directly back to the RaspberyPi on GPIO 12 + Gnd and GPIO 16 + Gnd

You will need to force GPIO 12 and 16 to be "high" so that when the sensors are together,
they are shorting the connection to ground, bringing the pins to a "low" state when the
garage doors are closed. This is how we determine that 0 = closed and 1 = open.

The following code example is what I'm using:

Save it to a file and include it in [SCRIPTS] section of /etc/webiopi/config
ie: GarageSensors = /etc/webiopi/garagesensors

```### Code Begin ###
# GarageDoor GPIO Config
import webiopi
GPIO = webiopi.GPIO

def setup():
    GPIO.setFunction(12, GPIO.IN, GPIO.PUD_UP)
    GPIO.setFunction(16, GPIO.IN, GPIO.PUD_UP)
    return

def loop():
    return

def destroy():
    GPIO.setFunction(12, GPIO.IN, GPIO.PUD_UP)
    GPIO.setFunction(16, GPIO.IN, GPIO.PUD_UP)
### Code End ###
```
Add these 2 lines to both the the [GPIO] and [~GPIO] sections of /etc/webiopi/config:

``` 12 = IN 
16 = IN 
```

In order to control the garage doors, an external relay board is used, connected to GPIO pins 5 and 6. 
It's a small, inexpensive 4-Channel relay board, readily found on popular auction sites for less than $10.
It can be run directly off the RaspPi if you make sure you get one that can be driven with a 
Low Trigger 3.3v or 5v signal. Tip: Search for: Relay Module Low Trigger 3.3V/5V

Add these 2 lines to both the the [GPIO] and [~GPIO] sections of /etc/webiopi/config:

```5 = OUT 1
6 = OUT 1
```

Add these 4 lines to the [ROUTES] section of /etc/webiopi/config:

``` /garage/north/status = /GPIO/12/value
/garage/north/button = /GPIO/5/sequence/500,01
/garage/south/status = /GPIO/16/value
/garage/south/button = /GPIO/6/sequence/500,01
```
