# rpi_health

Last update: 2023/03/04 21:21
<br><br>

## rpi_health

**Title**: rpi_health

**Language**: Python

**Overview**: Add a dashboard which reads the resource usage of the Raspberry Pi and outputs it into the flask website. This link may be useful. The page could output the temperature, CPU/System load, memory usage and up-time of the Raspberry Pi using something as simple as os.system("armbianmonitor -M") inside python. This runs that command as if it were command line. You could also output it to a text file for python to read the exact values. You could add to this to ping an alert to all computers on the network if the temperature is too high.
