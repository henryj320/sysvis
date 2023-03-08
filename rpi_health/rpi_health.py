"""A module to return the major health details of a system."""
# import click
import psutil
from datetime import datetime
import sys

import json

JSON_PATH = "rpi_health/assets/records.json"

# @click.command()
# @click.option("-s", "--sensor", help="Absolute location of the CPU temperature file.", default="rpi_health/Tests/example_cpu_temp")

def run() -> dict:
    """Main method of rpi_Health.
    Returns:
        dict: A dict containing the uptime, CPU usage, temperature, memory used, etc.
    """
    
    health = get_health()  # A dict containing the health characteristics.

    updateJSON(JSON_PATH, health)


    return health


def get_health() -> dict:
    """Returns a dict containing the main health characteristics of the system using the psutil library.
    Returns:
        dict: A dict containing the health characteristics of the system.
    """


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
        "datetime": convert_datetime(str(cur_time)),
        "success": True,
        "temp": str(temp),
        "cpu_percent": str(cpu_percent),
        "memory_percent": str(memory_percent),
        "memory_total": str(memory_total),
        "memory_used": str(memory_used),
        "uptime": convert_uptime(str(uptime))
    }

    print("\nCPU Usage:        " + str(cpu_percent) + "%")
    print("Temperature:      " + str(temp) + "°c")
    print("Memory Usage:     " + str(memory_percent) + "%")
    print("Used Memory:      " + str(memory_used) + "%")
    print("Total Memory:     " + str(memory_total) + "%")
    print("Uptime:           " + str(uptime) + "\n")

    return health


def updateJSON(JSON_PATH: str, health: dict) -> bool:
    """Updates the JSON file with the new health metrics.
    Args:
        JSON_PATH (str): The path to the JSON file.
        health (dict): The dict containing the system's health metrics.

    Returns:
        bool: True if the update succeeded.
    """

    try:
        f = open(JSON_PATH)
        json_file = json.load(f)  # Converts the file into a JSON object.
        f.close()

        max_metrics = 1000

        # Checks if the oldest metrics need to be removed or not.
        while len(json_file["data"]) > max_metrics:

            fifo_oldest = json_file["data"].pop(0)  # Removes the oldest RPI Health entry.

            # Prints the removed metrics
            print("\nOldest health metrics being deleted because number of metrics saved in " + str(JSON_PATH) + "is greater than " + str(max_metrics) + ":")
            print(fifo_oldest)
            print()

        json_file["data"].append(health)  # Adds the latest metrics to the end of the file.

        with open(JSON_PATH, "w") as f:
            json.dump(json_file, f, indent=4)  # Converts the JSON object back into the file.

        print("JSON file updated.\n")
    
    except FileExistsError as e:
        print("Failed to update JSON file. Exiting...\n")
        sys.exit()

    return True


def convert_datetime(datetime: str) -> list:
    """Converts a stringified datetime into an array.
    Args:
        datetime (str): A datetime string in the format of '2023-03-08 22:38:37.113266'.

    Returns:
        list: An array containing each of the datetime fields separated.
    """

    date_full = datetime.split(" ")
    time_fullstring = date_full[1]  # Contains HH:MM:SS.123456
    date_fullstring = date_full[0]  # Contains YYYY-MM-DD

    date_split = date_fullstring.split("-")

    years = date_split[0]
    months = date_split[1]
    days = date_split[2]



    time_split = time_fullstring.split(".")[0] # Removes the nanoseconds.
    time_split = time_split.split(":")

    hours = time_split[0]
    minutes = time_split[1]
    seconds = time_split[2]

    return [years, months, days, hours, minutes, seconds]


def convert_uptime(uptime: str) -> list:
    # "1 day, 14:18:25.435976"
    # Input is always x days, even at "1390 days, 16:19:28.533798"

    print(uptime)

    days = uptime.split(" ")
    time = days[2]  # Contains HH:MM:SS.123456
    days = days[0]

    time_split = time.split(".")[0]
    time_split = time_split.split(":")
    hours = time_split[0]
    minutes = time_split[1]
    seconds = time_split[2]

    print(days)



    return [days, hours, minutes, seconds]


if __name__ == '__main__':
    run()
