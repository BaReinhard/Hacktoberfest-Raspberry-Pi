#!/bin/sh
TEMP=$(sudo /opt/vc/bin/vcgencmd measure_temp)
echo "$(date) $TEMP"
