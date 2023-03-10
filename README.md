# rpi_health

Last update: 2023/03/10 00:29
<br><br>

## rpi_health

**Title**: rpi_health

**Date Started**: 2023-03-04

**Date Completed**: 2023-04-10

**Language**: Python

**Overview**: Add a dashboard which reads the resource usage of the Raspberry Pi and outputs it into the flask website. This link may be useful. The page could output the temperature, CPU/System load, memory usage and up-time of the Raspberry Pi using something as simple as os.system("armbianmonitor -M") inside python. This runs that command as if it were command line. You could also output it to a text file for python to read the exact values. You could add to this to ping an alert to all computers on the network if the temperature is too high.

**Result**: My rpi_health project is complete. It heavily makes use of the psutil library (installable from Pip). The script outputs the system's: CPU usage (%), temperature (°c), memory usage (%), used memory (GB), total memory (GB) and uptime ([int]) alongside the current datetime ([int]).

---

### Running the Project

To run the project, simply run the following commands:

```bash
cd rpi_health

pip install -r requirements.txt

python3 rpi_health/rpi_health.py
```

If the project fails, make sure that the "assets/*records.json*" file contains:

```json
{
    "data": []
}
```
