"""A module to return the major health details of a system."""
# import click
import psutil
from datetime import datetime

# @click.command()
# @click.option("-s", "--sensor", help="Absolute location of the CPU temperature file.", default="rpi_health/Tests/example_cpu_temp")

def run() -> dict:
    """Main method of rpi_Health. Returns a dict containing all major health details of the system.

    Returns:
        dict: A dict containing the uptime, CPU usage, temperature, memory used, etc.
    """

    # Rpi location: sys/devices/virtual/thermal/thermal_zone0/temp


    cpu_percent = psutil.cpu_percent(interval=1)  # The percentage of CPU in use.


    mem = psutil.virtual_memory()
    memory_percent = mem.percent  # The percentage of memory in use.
    memory_total = round((mem.total / 1000000000), 1)  # Total memory in the system in GB.
    memory_used = round((mem.used / 1000000000), 1)  # Memory in use in the system in GB.


    temperature = psutil.sensors_temperatures()  # Returns a dict of all temperatures.
    temp_keys = list(temperature.keys())[0]  # Returns the first key of all temperatures.
    temp = temperature[temp_keys][0].current   # Sets temp to the current temperature of the first temperature reading.
    temp = round(temp, 1)


    boot_time = psutil.boot_time()  # Returns the time that the computer was booted up.
    cur_time = datetime.now()  # Returns the current time.
    uptime = cur_time - datetime.fromtimestamp(boot_time)


    health = {
        "datetime": cur_time,
        "success": True,
        "temp": temp,
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "memory_total": memory_total,
        "memory_used": memory_used,
        "uptime": str(uptime)
    }

    print("\nCPU Usage:        " + str(cpu_percent) + "%")
    print("Temperature:      " + str(temp) + "°c")
    print("Memory Usage:     " + str(memory_percent) + "%")
    print("Used Memory:      " + str(memory_used) + "%")
    print("Total Memory:     " + str(memory_total) + "%")
    print("Uptime:           " + str(uptime) + "\n")


    return health




if __name__ == '__main__':
    run()
